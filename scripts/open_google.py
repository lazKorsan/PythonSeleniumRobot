"""open_google.py

Basit bir betik — varsayılan tarayıcıda https://www.google.com açar.
Opsiyonel olarak Selenium ile otomasyon yapma seçeneği de vardır.
"""

import webbrowser
import argparse
import sys


def open_with_webbrowser():
    webbrowser.open("https://www.google.com", new=2)


def open_with_selenium():
    try:
        from utils.driver_manager import DriverManager
    except Exception as e:
        print("DriverManager import edilemedi:", e)
        print("requirements.txt içindeki paketleri yükleyip tekrar deneyin.")
        return

    dm = DriverManager(use_temp_profile=True)
    with dm.driver_context() as driver:
        driver.get("https://www.google.com")


def main():
    parser = argparse.ArgumentParser(description="Open google.com (webbrowser or selenium)")
    parser.add_argument("--selenium", action="store_true", help="Use Selenium + webdriver-manager to open the browser")
    args = parser.parse_args()

    if args.selenium:
        open_with_selenium()
    else:
        open_with_webbrowser()


if __name__ == "__main__":
    main()
