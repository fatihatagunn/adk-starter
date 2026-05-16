# Adım 5: Alt Ajan Yönlendirme (Sub-Agent Delegation)

Bu adımda ana agent'ın kullanıcı talebini analiz ederek uygun alt ajana yönlendirmesini öğreniyoruz. Bu desen, karmaşık sistemlerde uzmanlık alanlarını birbirinden ayırmak için kullanılır.

## Bu adımda ne öğreneceksiniz?

- `sub_agents` parametresiyle agent hiyerarşisi kurmak
- Ana agent'ın yönlendirme (routing) mantığını instruction ile tasarlamak
- Agent as Tool ile Sub-Agent arasındaki farkı anlamak

## Temel Kavramlar

### Sub-Agent Delegation

`sub_agents` parametresi, ana agent'a hangi uzman ajanlara delege edebileceğini bildirir. Ana agent bir talebi aldığında instruction'ındaki kurallara göre ilgili alt ajana yönlendirir.

```python
root_agent = Agent(
    name="support_agent",
    ...
    sub_agents=[order_agent, after_sale_agent],
)
```

### Agent as Tool vs Sub-Agent

| Agent as Tool | Sub-Agent |
|---------------|-----------|
| Ana agent aracı açıkça çağırır | Ana agent yönlendirme kararı verir |
| Ana agent kontrolü elinde tutar | Alt agent konuşmayı devralır |
| Sonuç ana agent'a döner | Kullanıcıyla alt agent konuşur |
| Birden fazla kez çağrılabilir | Bir kez yönlendirilir |

### Bu Örnekteki Yapı

```
Kullanıcı mesajı
      ↓
support_agent (talebi analiz eder)
      ├──→ order_agent     (sipariş/teslimat/iade soruları)
      └──→ after_sale_agent (arıza/garanti/teknik sorunlar)
```

## Test Edin

```
ORD-12345 numaralı siparişim nerede?
```

```
Aldığım laptopun ekranı çalışmıyor, garanti kapsamında mı?
```

```
İade yapmak istiyorum
```

```
Ürünümün seri numarasına bakarak teknik destek alabilir miyim?
```

ADK arayüzünde `support_agent`'ın hangi alt ajana yönlendirdiğini ve o ajanın yanıtını gözlemleyebilirsin.

## Sonraki Adım

[Adım 6 → Sıralı İş Akışı (Sequential Workflow)](../s06_sequential/README.md)
