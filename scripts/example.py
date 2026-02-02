"""Örnek Python dosyası — Outline / Symbols testi için.

Bu dosyayı VS Code'da açtığınızda Outline/Explorer'da
`Planet`, `create_planet` ve `main` sembollerini görmelisiniz.
"""

class Planet:
	def __init__(self, name: str, radius_km: float):
		self.name = name
		self.radius_km = radius_km

	def surface_area(self) -> float:
		from math import pi
		return 4 * pi * (self.radius_km ** 2)


def create_planet(name: str, radius_km: float) -> Planet:
	"""Yeni bir Planet nesnesi oluşturur."""
	return Planet(name, radius_km)


def main() -> None:
	earth = create_planet("Earth", 6371)
	print(f"{earth.name} radius: {earth.radius_km} km")
	print(f"Surface area: {earth.surface_area():.1f} km^2")


if __name__ == "__main__":
	main()

