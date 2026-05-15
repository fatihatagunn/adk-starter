from datetime import datetime
from zoneinfo import ZoneInfo


def get_current_time(timezone: str = "Europe/Istanbul") -> dict:
    """Returns the current date and time for a given timezone.

    Args:
        timezone: IANA timezone name (e.g. 'Europe/Istanbul', 'UTC', 'America/New_York').

    Returns:
        A dict with date, time, day_of_week, and timezone info.
    """
    try:
        tz = ZoneInfo(timezone)
        now = datetime.now(tz)
        return {
            "status": "success",
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "timezone": timezone,
            "day_of_week": now.strftime("%A"),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
