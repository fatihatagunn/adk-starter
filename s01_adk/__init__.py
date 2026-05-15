from google.adk.agents import Agent

from tools.time import get_current_time

root_agent = Agent(
    name="adk_agent",
    model="gemini-flash-latest",
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
