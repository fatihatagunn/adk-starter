# Adım 4: Agent'ı Araç Olarak Kullanmak (Agent as Tool)

Bu adımda bir agent'ın başka bir agent'ı araç olarak çağırmasını öğreniyoruz. Bu desen, karmaşık görevleri uzmanlaşmış alt ajanlara delege etmek için kullanılır.

## Bu adımda ne öğreneceksiniz?

- `AgentTool` ile bir agent'ı tool olarak sarmalamak
- Ana agent ile uzman agent arasındaki sorumluluk ayrımını anlamak
- Agent kompozisyonunun ne zaman kullanışlı olduğunu kavramak

## Temel Kavramlar

### `AgentTool` Nedir?

`AgentTool`, bir agent'ı başka bir agent için araç haline getirir. Ana agent bu aracı çağırdığında, ADK uzman agent'ı çalıştırır ve yanıtını döndürür.

```python
from google.adk.tools.agent_tool import AgentTool

root_agent = Agent(
    ...
    tools=[AgentTool(agent=search_specialist)],
)
```

### Doğrudan Tool vs Agent as Tool

| Doğrudan Tool | Agent as Tool |
|---------------|---------------|
| Python fonksiyonu | Tam bir LLM agent |
| Deterministik çıktı | Model tabanlı çıktı |
| Basit veri dönüşümü | Karmaşık akıl yürütme |
| Hızlı ve öngörülebilir | Esnek ve akıllı |

### Bu Örnekteki Akış

```
Kullanıcı sorusu
      ↓
main_researcher (yorumlama + sentez)
      ↓ AgentTool çağrısı
search_specialist (arama + ham özet)
      ↓ google_search
Web sonuçları
```

`search_specialist` kullanıcıyla doğrudan konuşmaz; sadece `main_researcher`'a hizmet eder.

## Test Edin

```
Kuantum bilgisayarların günümüzdeki pratik kullanım alanları nelerdir?
```

```
Google ADK ile LangChain arasındaki temel farklar neler?
```

```
2025 yılında en çok kullanılan programlama dilleri hangileri?
```

ADK arayüzünde `main_researcher`'ın `search_specialist`'i araç olarak nasıl çağırdığını adım adım gözlemleyebilirsin.

## Sonraki Adım

[Adım 5 → Alt Ajan Yönlendirme (Sub-Agent Delegation)](../s05_sub_agents/README.md)
