class Clock:
    _minutes_in_day = 60 * 24

    def __init__(self, hour, minute):
        self.minutes = (60 * hour + minute) % self._minutes_in_day

    def __repr__(self):
        return f"{self.minutes // 60 :02d}:{self.minutes % 60:02d}"

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
