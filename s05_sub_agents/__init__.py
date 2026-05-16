from google.adk.agents import Agent

order_agent = Agent(
    name="order_agent",
    model="gemini-2.5-flash",
    description="Sipariş durumu, teslimat takibi ve iade işlemleri uzmanı",
    instruction=(
        "Sen bir sipariş destek uzmanısın. Kullanıcının sipariş durumu, "
        "teslimat takibi, kargo bilgisi ve iade talepleri hakkındaki "
        "sorularını yanıtla.\n\n"
        "Örnek senaryolar:\n"
        "- ORD-12345 siparişi kargoya verildi, tahmini teslimat yarın.\n"
        "- ORD-67890 için iade talebi açıldı, 3-5 iş günü içinde işleme alınacak.\n\n"
        "Türkçe ve İngilizce iletişim kurabilirsin."
    ),
)

after_sale_agent = Agent(
    name="after_sale_agent",
    model="gemini-2.5-flash",
    description="Ürün arızaları, garanti talepleri ve teknik destek uzmanı",
    instruction=(
        "Sen bir satış sonrası teknik destek uzmanısın. Ürün arızaları, "
        "garanti kapsamı, servis randevusu ve teknik sorunlar hakkında "
        "kullanıcıya yardım et.\n\n"
        "Örnek senaryolar:\n"
        "- Ürün 2 yıl garantili; garanti kapsamında ücretsiz onarım sağlanır.\n"
        "- Teknik sorun için lütfen seri numarasını paylaşın.\n\n"
        "Türkçe ve İngilizce iletişim kurabilirsin."
    ),
)

root_agent = Agent(
    name="support_agent",
    model="gemini-2.5-flash",
    description="Kullanıcıyı doğru destek ajanına yönlendiren müşteri hizmetleri koordinatörü",
    instruction=(
        "Sen bir müşteri hizmetleri koordinatörüsün. Kullanıcının talebini "
        "anlayarak doğru uzman ajana yönlendir:\n\n"
        "- Sipariş durumu, teslimat, kargo veya iade → order_agent\n"
        "- Ürün arızası, garanti, teknik sorun → after_sale_agent\n\n"
        "Kullanıcıya hangi uzman ajana yönlendirdiğini belirt. "
        "Türkçe ve İngilizce iletişim kurabilirsin."
    ),
    sub_agents=[order_agent, after_sale_agent],
)
