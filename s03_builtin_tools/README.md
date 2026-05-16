# Adım 3: Yerleşik Araçlar (Built-in Tools)

Bu adımda ADK'nın sunduğu hazır araçları kullanmayı öğreniyoruz. `google_search`, modelin internette gerçek zamanlı arama yapmasını sağlar; kendi kodunu yazman gerekmez.

## Bu adımda ne öğreneceksiniz?

- ADK'nın yerleşik araçlarını (`google.adk.tools`) kullanmak
- `google_search` ile gerçek zamanlı web araması yapmak
- Özel fonksiyon yazmadan hazır yetenekler eklemek

## Temel Kavramlar

### Yerleşik Araçlar Nedir?

ADK bazı araçları hazır olarak sunar. Bunları içe aktarıp `tools` listesine eklemek yeterlidir:

```python
from google.adk.tools import google_search

root_agent = Agent(
    ...
    tools=[google_search],
)
```

### `google_search` Nasıl Çalışır?

Gemini modeli, `google_search` aracını şu durumlarda çağırır:

- Güncel bilgi gerektiren sorular ("bugün hava nasıl?", "son haberler neler?")
- Modelin eğitim verisinde bulunmayan konular
- Doğrulama gerektiren olgusal sorular

Arama sonuçları modele geri döner; model bu bilgileri işleyerek kullanıcıya sunar.

> **Not:** `google_search` aracı Gemini'nin Grounding özelliğini kullanır. `GOOGLE_API_KEY` ile çalışır, ek yapılandırma gerekmez.

## Test Edin

```
Bu hafta yapay zeka alanında önemli gelişmeler neler?
```

```
Google ADK'nın en son sürümü hangisi?
```

```
Python 3.13'te ne gibi yenilikler var?
```

```
Bugün dolar/TL kuru nedir?
```

ADK arayüzünde araç çağrısını ve dönen arama sonuçlarını adım adım izleyebilirsin.

## Sonraki Adım

[Adım 4 → Agent'ı Araç Olarak Kullanmak](../s04_agent_as_tool/README.md)
