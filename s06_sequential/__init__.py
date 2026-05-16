from google.adk.agents import Agent, SequentialAgent

poet = Agent(
    name="poet",
    model="gemini-3-flash-preview",
    description="Verilen konu hakkında kısa şiir yazan ajan",
    instruction=(
        "Sen yaratıcı bir şairsin. Kullanıcının verdiği konu hakkında "
        "kısa, etkileyici ve özgün bir şiir yaz.\n\n"
        "Sadece şiiri döndür; başlık, açıklama veya yorum ekleme."
    ),
    output_key="poem",
)

translator = Agent(
    name="translator",
    model="gemini-3-flash-preview",
    description="İngilizce şiiri Türkçeye çeviren ajan",
    instruction=(
        "Sen yetenekli bir şiir çevirmenisin. Aşağıdaki şiiri Türkçeye çevir. "
        "Şiirin ritmi ve duygusunu korumaya özen göster:\n\n"
        "{poem}\n\n"
        "Sadece çeviriyi döndür; açıklama veya yorum ekleme."
    ),
    output_key="translated_poem",
)

root_agent = SequentialAgent(
    name="poet_and_translator",
    description="Önce şiir yazar, ardından Türkçeye çevirir",
    sub_agents=[poet, translator],
)
