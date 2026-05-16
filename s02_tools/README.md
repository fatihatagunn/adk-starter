# Adım 2: Özel Araçlar (Custom Tools)

Bu adımda agent'a özel Python fonksiyonlarını araç (tool) olarak eklemeyi öğreniyoruz. ADK, fonksiyonun imzasını ve docstring'ini okuyarak modele otomatik olarak bir araç şeması gönderir.

## Bu adımda ne öğreneceksiniz?

- Python fonksiyonunu tool olarak tanımlamak
- Docstring ile ADK'ya araç açıklaması sağlamak
- Type hint'lerin araç şemasındaki rolünü anlamak
- Tool'un döndürdüğü `dict` yapısını tasarlamak

## Temel Kavramlar

### Tool Nasıl Çalışır?

ADK bir Python fonksiyonunu tool olarak kaydettiğinde şu bilgileri çıkarır:

1. **Fonksiyon adı** → tool adı
2. **Parametreler + type hint'ler** → model hangi argümanları göndereceğini bilir
3. **Docstring** → modele aracın ne yaptığını anlatır
4. **Return değeri** → `dict` döndürmek standarttır; `status` anahtarı başarı/hata durumunu belirtir

### İmza Örneği

```python
def lookup_stock_ticker(company_name: str) -> dict:
    """Verilen şirket adına karşılık gelen borsa sembolünü döndürür.

    Args:
        company_name: Aranacak şirket adı (örn. "Apple", "Google", "Tesla").

    Returns:
        Borsa sembolü ve işlem durumunu içeren dict.
    """
```

Model bu fonksiyon için şu şemayı görür:

```json
{
  "name": "lookup_stock_ticker",
  "description": "Verilen şirket adına karşılık gelen borsa sembolünü döndürür.",
  "parameters": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "Aranacak şirket adı (örn. 'Apple', 'Google', 'Tesla')."
      }
    },
    "required": ["company_name"]
  }
}
```

## Test Edin

```
Apple'ın borsa sembolü nedir?
```

```
Tesla ve NVIDIA'nın ticker sembollerini öğrenebilir miyim?
```

```
Samsung'u ara
```

```
SpaceX'in sembolü nedir?   ← bulunamayan şirket davranışını gözlemle
```

ADK arayüzünde her konuşma adımını açarak modelin hangi tool'u hangi argümanla çağırdığını görebilirsin.

## Sonraki Adım

[Adım 3 → Yerleşik Araçlar (Built-in Tools)](../s03_builtin_tools/README.md)
