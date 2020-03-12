class SpaceAge:
    def __init__(self, seconds: int):
        self.year_seconds: int = 31557600
        self.seconds_passed: int = seconds

    def on_earth(self) -> float:
        return round(self.seconds_passed /
                     self.year_seconds, 2)

    def on_mercury(self) -> float:
        periodo_mercurio: float = 0.2408467
        return round(self.seconds_passed /
                     (periodo_mercurio * self.year_seconds), 2)

    def on_venus(self) -> float:
        periodo_venus: float = 0.61519726
        return round(self.seconds_passed /
                     (periodo_venus * self.year_seconds), 2)

    def on_mars(self) -> float:
        periodo_venus: float = 1.8808158
        return round(self.seconds_passed /
                     (periodo_venus * self.year_seconds), 2)

    def on_jupiter(self) -> float:
        periodo_jupiter: float = 11.862615
        return round(self.seconds_passed /
                     (periodo_jupiter * self.year_seconds), 2)

    def on_saturn(self) -> float:
        periodo_saturno: float = 29.447498
        return round(self.seconds_passed /
                     (periodo_saturno * self.year_seconds), 2)

    def on_uranus(self) -> float:
        periodo_urano: float = 84.016846
        return round(self.seconds_passed /
                     (periodo_urano * self.year_seconds), 2)

    def on_neptune(self) -> float:
        periodo_neptuno: float = 164.79132
        return round(self.seconds_passed /
                     (periodo_neptuno * self.year_seconds), 2)
