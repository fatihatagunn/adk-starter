from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

search_specialist = Agent(
    name="search_specialist",
    model="gemini-3-flash-preview",
    description="Google Arama yapan uzman ajan — doğrudan kullanıcıyla konuşmaz",
    instruction=(
        "Sen bir arama uzmanısın. Verilen konu hakkında google_search aracını kullanarak "
        "kapsamlı bilgi topla ve derli toplu bir özet döndür. "
        "Sadece bulduğun bilgileri yaz, yorum ekleme."
    ),
    tools=[google_search],
)

root_agent = Agent(
    name="main_researcher",
    model="gemini-3-flash-preview",
    description="Araştırmacı ajan — arama ajanını araç olarak çağırır ve sonuçları yorumlar",
    instruction=(
        "Sen bir araştırmacısın. Kullanıcının sorusunu yanıtlamak için "
        "search_specialist aracını kullan.\n\n"
        "Arama sonuçlarını alıp kullanıcıya anlamlı, düzenli ve yorumlanmış "
        "bir biçimde sun. Gerektiğinde birden fazla arama yapabilirsin.\n\n"
        "Türkçe ve İngilizce iletişim kurabilirsin."
    ),
    tools=[AgentTool(agent=search_specialist)],
)
