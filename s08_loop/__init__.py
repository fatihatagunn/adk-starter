from google.adk.agents import Agent, LoopAgent
from google.adk.tools import exit_loop

code_generator = Agent(
    name="code_generator",
    model="gemini-3-flash-preview",
    description="Kullanıcı isteğine göre Python kodu yazan ve geri bildirimleri dahil eden ajan",
    instruction=(
        "Sen deneyimli bir Python geliştiricisisin. "
        "Kullanıcının isteğine göre temiz ve çalışır Python kodu yaz.\n\n"
        "Eğer konuşma geçmişinde bir kod inceleme geri bildirimi varsa mutlaka dahil et.\n\n"
        "Sadece kodu döndür; açıklama veya yorum ekleme."
    ),
    output_key="generated_code",
)

code_reviewer = Agent(
    name="code_reviewer",
    model="gemini-3-flash-preview",
    description="Kodu inceleyen, geri bildirim veren ve yeterince iyiyse döngüyü sonlandıran ajan",
    instruction=(
        "Sen kıdemli bir yazılım mühendisisin. Aşağıdaki kodu incele:\n\n"
        "```python\n{generated_code}\n```\n\n"
        "Eğer kod doğru, temiz ve yeterince iyiyse exit_loop aracını çağır.\n\n"
        "Aksi halde yapılması gereken somut iyileştirmeleri belirt. "
        "Geri bildirimini kısa ve net tut."
    ),
    output_key="feedback",
    tools=[exit_loop],
)

root_agent = LoopAgent(
    name="code_refiner",
    description="Kod yazar ve inceleme döngüsüyle kaliteyi artırır; en fazla 3 iterasyon",
    sub_agents=[code_generator, code_reviewer],
    max_iterations=3,
)
