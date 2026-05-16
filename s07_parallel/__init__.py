from google.adk.agents import Agent, ParallelAgent, SequentialAgent

company_profiler = Agent(
    name="company_profiler",
    model="gemini-2.5-flash",
    description="Şirketin genel profilini çıkaran ajan",
    instruction=(
        "Kullanıcının belirttiği şirket hakkında kısa bir profil hazırla: "
        "kuruluş yılı, merkez, sektör, ana ürün veya hizmetler ve "
        "çalışan sayısı gibi temel bilgileri içersin. "
        "Sadece profil bilgisini döndür."
    ),
    output_key="profile",
)

news_finder = Agent(
    name="news_finder",
    model="gemini-2.5-flash",
    description="Şirketin son dönem haberlerini özetleyen ajan",
    instruction=(
        "Kullanıcının belirttiği şirketle ilgili son dönemde öne çıkan "
        "3-5 önemli gelişmeyi madde madde listele. "
        "Sadece haberleri döndür."
    ),
    output_key="news",
)

financial_analyst = Agent(
    name="financial_analyst",
    model="gemini-2.5-flash",
    description="Şirketin finansal durumunu analiz eden ajan",
    instruction=(
        "Kullanıcının belirttiği şirketin finansal durumunu analiz et: "
        "piyasa değeri, gelir trendi, karlılık durumu ile güçlü ve "
        "zayıf yönlerini belirt. "
        "Sadece finansal analizi döndür."
    ),
    output_key="financials",
)

market_researcher = ParallelAgent(
    name="market_researcher",
    description="Şirket profili, haberler ve finansal analizi eş zamanlı toplar",
    sub_agents=[company_profiler, news_finder, financial_analyst],
)

report_compiler = Agent(
    name="report_compiler",
    model="gemini-2.5-flash",
    description="Toplanan verileri kapsamlı bir şirket raporuna dönüştüren ajan",
    instruction=(
        "Aşağıdaki bilgileri kullanarak kapsamlı ve okunabilir bir şirket "
        "analiz raporu hazırla:\n\n"
        "**Şirket Profili:**\n{profile}\n\n"
        "**Güncel Haberler:**\n{news}\n\n"
        "**Finansal Analiz:**\n{financials}\n\n"
        "Raporu başlıklar ve maddeler kullanarak düzenli bir formatta sun."
    ),
)

root_agent = SequentialAgent(
    name="company_detective",
    description="Paralel araştırma yaparak kapsamlı şirket raporu oluşturur",
    sub_agents=[market_researcher, report_compiler],
)
