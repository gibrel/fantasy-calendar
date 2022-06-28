from enum import Enum, auto


class WeekHandle(Enum):
    REPEATS = auto(),    # weeks loops throw year (every day have same week days independent of year)
    CONTINUES = auto(),  # weeks continues its own count (days may have different week days on next years)
    BREAKS = auto(),     # weeks restart with the incident of a holiday
    FIXED = auto()       # weeks respect month boundaries, so it restarts at months end
