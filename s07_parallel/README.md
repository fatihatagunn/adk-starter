# Adım 7: Paralel İş Akışı (Parallel Workflow)

Bu adımda birden fazla agent'ı eş zamanlı çalıştırmayı ve sonuçları birleştirmeyi öğreniyoruz. `ParallelAgent` birbirinden bağımsız görevleri aynı anda yürütür; bu da toplam süreyi önemli ölçüde kısaltır.

## Bu adımda ne öğreneceksiniz?

- `ParallelAgent` ile eş zamanlı ajan çalıştırmak
- Paralel fazı sıralı faz ile birleştirmek
- Birden fazla `output_key`'i tek bir raporda toplamak

## Temel Kavramlar

### `ParallelAgent`

Alt ajanlarını eş zamanlı çalıştırır. Birbirinden bağımsız araştırma veya veri toplama görevleri için idealdir.

```python
market_researcher = ParallelAgent(
    name="market_researcher",
    sub_agents=[company_profiler, news_finder, financial_analyst],
)
```

### Paralel + Sıralı Birleştirme

`ParallelAgent` tek başına yeterli değil; sonuçları sentezlemek için sıralı bir adım gerekir:

```
ParallelAgent (eş zamanlı araştırma)
      ↓
SequentialAgent (önce paralel, sonra rapor)
```

### Bu Örnekteki Akış

```
Kullanıcı → şirket adı girer
      ↓
market_researcher (ParallelAgent)
  ├── company_profiler  → {profile}    ┐
  ├── news_finder       → {news}       ├── eş zamanlı
  └── financial_analyst → {financials} ┘
      ↓
report_compiler → {profile} + {news} + {financials} → kapsamlı rapor
      ↓
Kullanıcıya rapor sunulur
```

Üç ajan paralel çalıştığı için toplam süre, en uzun süren tek bir ajanın süresi kadardır.

## Test Edin

```
Apple hakkında kapsamlı bir rapor hazırla
```

```
Tesla şirketini analiz et
```

```
Google hakkında ne biliyorsun?
```

ADK arayüzünde `market_researcher` altındaki üç ajanın eş zamanlı çalıştığını ve `report_compiler`'ın tüm sonuçları birleştirdiğini gözlemleyebilirsin.

## Sonraki Adım

[Adım 8 → Döngüsel İyileştirme (Loop Workflow)](../s08_loop/README.md)
