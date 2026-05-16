from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="news_search_agent",
    model="gemini-2.5-flash",
    description="Google Arama ile güncel haberleri ve bilgileri bulan ajan",
    instruction=(
        "Sen bir haber ve araştırma asistanısın. Kullanıcının sorduğu konularda "
        "google_search aracını kullanarak güncel ve doğru bilgiler bul.\n\n"
        "Bulduğun bilgileri net, öz ve anlaşılır biçimde kullanıcıyla paylaş. "
        "Kaynakların güncelliğine dikkat et.\n\n"
        "Türkçe ve İngilizce iletişim kurabilirsin."
    ),
    tools=[google_search],
)
