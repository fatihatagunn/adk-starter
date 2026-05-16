# Adım 1: İlk Agent

Bu adımda Google ADK ile temel bir agent oluşturmayı öğreniyoruz. Agent, kullanıcı sorularına yanıt veren ve isteğe bağlı olarak araçlar (tools) kullanabilen bir yapıdır.

## Bu adımda ne öğreneceksiniz?

- `Agent` sınıfıyla temel bir agent tanımlamak
- `name`, `description`, `instruction` ve `model` parametrelerini yapılandırmak
- ADK'nın `root_agent` değişkenini nasıl keşfettiğini anlamak
- İsteğe bağlı olarak özel araçları (tools) agent'a bağlamak

## Temel Kavramlar

### `root_agent`

ADK, her pakette `root_agent` adlı değişkeni arar. Bu isim sabittir ve değiştirilemez. `adk web` komutu projedeki tüm paketleri tarayarak bu değişkeni bulunanları arayüze listeler.

### `instruction` (Sistem Promptu)

Agent'ın nasıl davranacağını belirler. Ne yapabileceğini, nasıl yanıt vereceğini ve hangi dili kullanacağını burada tanımlarsınız.

### `tools`

Agent'a verilen Python fonksiyonlarıdır. ADK, fonksiyonun imzasını ve docstring'ini okuyarak modele bir araç şeması (JSON Schema) gönderir. Model gerektiğinde bu araçları çağırır.

## Kodu İnceleyin

```python
root_agent = Agent(
    name="adk_agent",
    model="gemini-3-flash-preview",
    description="Google ADK Workshop için eğitim amaçlı asistan",
    instruction="...",
    tools=[get_current_time],  # Araç bağlantısı
)
```

`get_current_time` fonksiyonu `__init__.py` içinde tanımlıdır. Şu an `tools` listesinde yorum satırına alınmıştır — aktif hale getirmek için yorumu kaldırın.

## Test Edin

```
Google ADK nedir?
```

```
Şu an İstanbul'da saat kaç?   ← get_current_time aktifse çalışır
```

```
New York ile Tokyo arasındaki saat farkı nedir?
```

## Sonraki Adım

[Adım 2 → Özel Araçlar (Custom Tools)](../s02_tools/README.md)
