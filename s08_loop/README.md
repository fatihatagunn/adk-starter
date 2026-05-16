# Adım 8: Döngüsel İyileştirme (Loop Workflow)

Bu adımda bir agent'ın belirli bir kalite eşiğine ulaşana kadar çalışmaya devam eden döngüsel bir iş akışı öğreniyoruz. `LoopAgent`, yazar-inceleyici döngüsü gibi iteratif iyileştirme senaryoları için tasarlanmıştır.

## Bu adımda ne öğreneceksiniz?

- `LoopAgent` ile yinelemeli (iteratif) iş akışı oluşturmak
- `exit_loop` aracıyla döngüyü programatik olarak sonlandırmak
- `max_iterations` ile sonsuz döngüye karşı güvenlik sınırı koymak
- `{key}` ile iterasyonlar arasında durum aktarmak

## Temel Kavramlar

### `LoopAgent`

Alt ajanlarını tekrar tekrar çalıştırır. Döngü iki şekilde sona erer:

1. Bir ajan `exit_loop` aracını çağırır.
2. `max_iterations` sayısına ulaşılır.

```python
root_agent = LoopAgent(
    name="code_refiner",
    sub_agents=[code_generator, code_reviewer],
    max_iterations=3,
)
```

### `exit_loop` Aracı

`google.adk.tools` içinde hazır gelir. Bir ajan bu aracı çağırdığında döngü hemen durur.

```python
from google.adk.tools import exit_loop

code_reviewer = Agent(
    ...
    tools=[exit_loop],
)
```

### İterasyon Akışı

```
İterasyon 1:
  code_generator → kullanıcı isteğine göre ilk kodu yazar → {generated_code}
  code_reviewer  → kodu inceler → iyileştirme gerekiyorsa {feedback} yazar
                                → yeterliyse exit_loop çağırır ✓

İterasyon 2 (feedback varsa):
  code_generator → {feedback}'i okuyarak kodu düzeltir → {generated_code}
  code_reviewer  → yeniden inceler → exit_loop veya yeni {feedback}

İterasyon 3 (max_iterations):
  Döngü otomatik sona erer.
```

### İlk İterasyon ve `{feedback}`

İlk iterasyonda `{feedback}` henüz tanımlı değildir; `code_generator` bunu boş olarak görür ve direkt kullanıcı isteğine göre kod üretir. Bu beklenen davranıştır.

## Test Edin

```
Fibonacci dizisini hesaplayan bir Python fonksiyonu yaz
```

```
Bir listeyi bubble sort ile sıralayan fonksiyon yaz
```

```
Verilen metnin kelime sayısını döndüren bir fonksiyon yaz
```

ADK arayüzünde her iterasyonu genişleterek `code_generator`'ın kodu nasıl geliştirdiğini ve `code_reviewer`'ın ne zaman `exit_loop` çağırdığını gözlemleyebilirsin.

---

Tebrikler! Tüm adımları tamamladınız. [Ana sayfaya dön →](../README.md)
