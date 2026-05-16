from datetime import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent


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


root_agent = Agent(
    name="adk_agent",
    model="gemini-3-flash-preview",
    description="Google ADK Workshop için eğitim amaçlı asistan",
    instruction=(
        "Sen Google ADK (Agent Development Kit) workshop'u için hazırlanmış "
        "yardımcı bir asistansın.\n\n"
        "Yapabileceklerin:\n"
        "- ADK ve Google Gemini hakkında soruları yanıtlamak\n"
        # "- Güncel tarih/saat bilgisi vermek → get_current_time aracını kullan\n"
        "Araçları kullanırken sonucu kullanıcıya açık ve anlaşılır biçimde aktar. "
        "Türkçe ve İngilizce olarak iletişim kurabilirsin."
    ),
    tools=[
        # get_current_time,
    ],
)
