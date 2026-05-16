# Adım 6: Sıralı İş Akışı (Sequential Workflow)

Bu adımda birden fazla agent'ı belirli bir sırayla çalıştırmayı öğreniyoruz. `SequentialAgent`, alt ajanlarını sırayla çalıştırır ve her adımın çıktısını bir sonraki adıma aktarır.

## Bu adımda ne öğreneceksiniz?

- `SequentialAgent` ile adım adım iş akışı oluşturmak
- `output_key` ile ajan çıktısını oturum durumuna (session state) kaydetmek
- `{key}` sözdizimi ile önceki adımların çıktısını instruction'da kullanmak

## Temel Kavramlar

### `SequentialAgent`

Alt ajanlarını verilen sırayla çalıştırır. Bir önceki ajan tamamlanmadan sonraki başlamaz.

```python
root_agent = SequentialAgent(
    name="poet_and_translator",
    sub_agents=[poet, translator],  # Bu sırayla çalışır
)
```

### `output_key`

Bir agent'ın son yanıtını oturum durumuna (session state) kaydeder.

```python
poet = Agent(
    ...
    output_key="poem",  # Yanıt "poem" anahtarıyla kaydedilir
)
```

### `{key}` ile State Okuma

Bir sonraki agent, instruction içinde `{key}` kullanarak önceki adımın çıktısına erişebilir:

```python
translator = Agent(
    instruction=(
        "Aşağıdaki şiiri Türkçeye çevir:\n\n{poem}"
        #                                    ↑
        #                          poet'un output_key'i
    ),
)
```

### Bu Örnekteki Akış

```
Kullanıcı → konu girer
      ↓
poet        → şiir yazar → output_key="poem" ile kaydeder
      ↓
translator  → {poem} okur → Türkçeye çevirir
      ↓
Kullanıcıya çeviri sunulur
```

## Test Edin

```
Deniz hakkında bir şiir yaz
```

```
Write a poem about mountains in English and translate to Turkish.
```

```
Yapay zeka temalı bir şiir istiyorum
```

ADK arayüzünde her adımı açarak `poet`'un yazdığı şiiri ve `translator`'ın çeviriyi nasıl aldığını gözlemleyebilirsin.

## Sonraki Adım

[Adım 7 → Paralel İş Akışı (Parallel Workflow)](../s07_parallel/README.md)
