from google.adk.agents import Agent


def lookup_stock_ticker(company_name: str) -> dict:
    """Verilen şirket adına karşılık gelen borsa sembolünü döndürür.

    Args:
        company_name: Aranacak şirket adı (örn. "Apple", "Google", "Tesla").

    Returns:
        Borsa sembolü ve işlem durumunu içeren dict.
    """
    tickers = {
        "apple": "AAPL",
        "google": "GOOGL",
        "alphabet": "GOOGL",
        "microsoft": "MSFT",
        "tesla": "TSLA",
        "amazon": "AMZN",
        "meta": "META",
        "facebook": "META",
        "netflix": "NFLX",
        "nvidia": "NVDA",
        "samsung": "005930.KS",
        "toyota": "TM",
    }

    symbol = tickers.get(company_name.lower().strip())

    if symbol:
        return {"status": "success", "company": company_name, "ticker": symbol}
    return {"status": "error", "message": f"'{company_name}' için sembol bulunamadı."}


root_agent = Agent(
    name="stock_agent",
    model="gemini-3-flash-preview",
    description="Şirket adından borsa sembolünü bulan ajan",
    instruction=(
        "Sen bir borsa uzmanısın. Kullanıcı bir şirket adı verdiğinde "
        "lookup_stock_ticker aracını kullanarak hisse senedi sembolünü bul "
        "ve kullanıcıya açıkça bildir.\n\n"
        "Sembol bulunamazsa kullanıcıya nazikçe bildir ve desteklenen "
        "şirketlerin bir listesini sun.\n\n"
        "Türkçe ve İngilizce iletişim kurabilirsin."
    ),
    tools=[lookup_stock_ticker],
)
