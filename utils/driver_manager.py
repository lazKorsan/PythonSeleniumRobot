"""DriverManager: Selenium WebDriver yapılandırma yardımı.

Bu modül minimal bağımlılıkla yazıldı: `selenium` yüklü değilse
Selenium ile ilgili kodlar çağrılana kadar import edilmez — böylece
başlangıçta paket zorunluluğu olmaz.

Kullanım örneği:
```py
from utils.driver_manager import DriverManager

dm = DriverManager(browser="chrome", headless=False)
with dm.driver_context() as driver:
    driver.get("https://www.google.com")
```
"""
from typing import Optional, Generator
import contextlib
import tempfile
import shutil


class DriverManager:
    def __init__(
        self,
        browser: str = "chrome",
        headless: bool = False,
        maximize: bool = True,
        implicit_wait: int = 10,
        use_webdriver_manager: bool = True,
        driver_path: Optional[str] = None,
        use_temp_profile: bool = True,
        profile_dir: Optional[str] = None,
    ) -> None:
        self.browser = browser.lower()
        self.headless = headless
        self.maximize = maximize
        self.implicit_wait = implicit_wait
        self.use_webdriver_manager = use_webdriver_manager
        self.driver_path = driver_path
        # profile isolation options
        self.use_temp_profile = use_temp_profile
        self.profile_dir = profile_dir
        self._temp_profile_dir: Optional[str] = None

    def _ensure_selenium(self):
        try:
            import selenium  # type: ignore
        except Exception:
            raise RuntimeError(
                "Selenium yüklü değil. `pip install selenium webdriver-manager` ile yükleyin."
            )

    def create_driver(self):
        """Selenium WebDriver örneği oluşturur.

        Not: Bu metot sadece çağrıldığında Selenium import eder.
        """
        self._ensure_selenium()

        if self.browser == "chrome":
            return self._create_chrome()
        if self.browser == "firefox":
            return self._create_firefox()
        raise ValueError(f"Desteklenmeyen tarayıcı: {self.browser}")

    def _create_chrome(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options

        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        if self.maximize:
            options.add_argument("--start-maximized")

        # profile isolation: prefer explicit profile_dir, otherwise create a temp profile
        if self.profile_dir:
            options.add_argument(f"--user-data-dir={self.profile_dir}")
        elif self.use_temp_profile:
            # create a temporary profile directory so the automation browser is isolated
            self._temp_profile_dir = tempfile.mkdtemp(prefix="dm_profile_")
            options.add_argument(f"--user-data-dir={self._temp_profile_dir}")

        if self.use_webdriver_manager and self.driver_path is None:
            try:
                from webdriver_manager.chrome import ChromeDriverManager

                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=options)
            except Exception as e:
                raise RuntimeError("webdriver-manager ile Chrome sürücüsü kurulamadı: " + str(e))
        else:
            if not self.driver_path:
                raise RuntimeError("driver_path belirtilmeli veya webdriver-manager kullanmalısınız.")
            service = Service(self.driver_path)
            driver = webdriver.Chrome(service=service, options=options)

        driver.implicitly_wait(self.implicit_wait)
        return driver

    def _create_firefox(self):
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.options import Options

        options = Options()
        if self.headless:
            options.add_argument("-headless")

        if self.use_webdriver_manager and self.driver_path is None:
            try:
                from webdriver_manager.firefox import GeckoDriverManager

                service = Service(GeckoDriverManager().install())
                driver = webdriver.Firefox(service=service, options=options)
            except Exception as e:
                raise RuntimeError("webdriver-manager ile Firefox sürücüsü kurulamadı: " + str(e))
        else:
            if not self.driver_path:
                raise RuntimeError("driver_path belirtilmeli veya webdriver-manager kullanmalısınız.")
            service = Service(self.driver_path)
            driver = webdriver.Firefox(service=service, options=options)

        driver.implicitly_wait(self.implicit_wait)
        return driver

    @contextlib.contextmanager
    def driver_context(self) -> Generator[object, None, None]:
        """Context manager olarak kullanmak için: `with dm.driver_context() as driver:`"""
        driver = None
        try:
            driver = self.create_driver()
            yield driver
        finally:
            try:
                if driver:
                    driver.quit()
            except Exception:
                pass
            # cleanup temporary profile directory if we created one
            try:
                if self._temp_profile_dir:
                    shutil.rmtree(self._temp_profile_dir, ignore_errors=True)
                    self._temp_profile_dir = None
            except Exception:
                pass
