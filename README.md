# Google ADK Workshop

Bu workshop, **Google Agent Development Kit (ADK)** ile nasıl AI agent geliştirileceğini adım adım öğretir. Tüm adımlar **Google Cloud Shell** üzerinden yürütülecek ve agent sonunda **Cloud Run**'a deploy edilecektir.

## Bu Workshop'ta Neler Yapacaksınız?

- Google ADK ile bir AI agent oluşturmak
- Agente özel araçlar (tools) eklemek
- Agent'ı Cloud Shell'de yerel olarak test etmek
- Agent'ı Cloud Run'a deploy etmek ve herkese açık bir URL almak

## Mimari

```
Cloud Shell
│
├── s01_adk/
│   └── __init__.py       ← Agent tanımı + araçlar
│
├── Dockerfile             ← Cloud Run için konteyner
└── requirements.txt

     adk web (geliştirme UI)
          │
          ▼
    Cloud Run (production)
```

## Ön Gereksinimler

- Google Cloud hesabı (faturalandırma etkin)
- Google Cloud projesi oluşturulmuş
- Tarayıcıdan [Google Cloud Console](https://console.cloud.google.com)'a erişim

---

## Adım 1: Cloud Shell'i Başlatın

1. [Google Cloud Console](https://console.cloud.google.com)'u açın.
2. Sağ üstteki **"Activate Cloud Shell"** butonuna (`>_`) tıklayın.
3. Cloud Shell açılana kadar bekleyin.

Cloud Shell; `gcloud`, `git`, `python3`, `pip` gibi tüm araçlarla önceden yapılandırılmış ve ücretsiz bir geliştirme ortamıdır.

---

## Adım 2: Proje ID'sini Ayarlayın

Cloud Shell terminalinde aktif projenizi kontrol edin:

```bash
gcloud config get-value project
```

Çıktı `(unset)` ya da boşsa, projenizi doğrudan ayarlayın:

```bash
gcloud config set project PROJE_ID_INIZ
```

---

## Adım 3: Gerekli API'leri Etkinleştirin

Cloud Run'a deploy edebilmek için gerekli API'leri aktif edin:

```bash
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com
```

Bu işlem 1-2 dakika sürebilir.

---

## Adım 4: Depoyu Cloud Shell'e Klonlayın

```bash
git clone https://github.com/fatihatagunn/adk-starter.git
cd adk-starter
```

> **Not:** Repo URL'sini değiştirmeyi unutmayın. Eğer repo henüz GitHub'da yoksa dosyaları Cloud Editor ile oluşturabilirsiniz.

---

## Adım 5: Python Ortamını Kurun

Sanal ortam oluşturun ve bağımlılıkları yükleyin:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Kurulumu doğrulayın:

```bash
adk --version
```

---

## Adım 6: API Key'i Alın ve Ayarlayın

**[aistudio.google.com](https://aistudio.google.com)** adresine gidin ve **"Get API key"** butonuyla ücretsiz bir Gemini API key oluşturun.

Ardından Cloud Shell'de:

```bash
cp .env.example .env
nano .env
```

`your-api-key-here` yerine az önce aldığınız API key'i yazın:

```env
GOOGLE_API_KEY=AIzaSy...
```

Değişkeni terminalinize yükleyin:

```bash
export $(grep -v '^#' .env | xargs)
```

---

## Adım 7: Kodu İnceleyelim

### `s01_adk/__init__.py`

Agent'ın ana dosyasını açın:

```bash
cat s01_adk/__init__.py
```

#### Araçlar (Tools)

**`get_current_time(timezone)`** — `tools/time.py` içinde tanımlı. Belirtilen saat diliminde güncel tarih/saat döndürür.

#### Agent Tanımı

```python
root_agent = Agent(
    name="adk_agent",
    model="gemini-3-flash-preview",        # Kullanılacak Gemini modeli
    description="...",                  # Agentin kısa açıklaması
    instruction="...",                  # Sistem promptu (agent davranışını belirler)
    tools=[get_current_time],           # Agente verilen araçlar
)
```

> `root_agent` değişkeni ADK'nın ana giriş noktasıdır; bu isim değiştirilmemelidir.

---

## Adım 8: Agent'ı Yerel Olarak Test Edin

ADK'nın yerleşik web arayüzünü başlatın:

```bash
adk web --port 8080 --allow_origins "*"
```

Cloud Shell'de **"Web Preview"** butonuna tıklayın ve **"Preview on port 8080"** seçeneğini seçin. Tarayıcınızda agent'ın web arayüzü açılacaktır.

### Test Soruları

```
Şu an İstanbul'da saat kaç?
```

```
New York'ta şu an günün hangi saati?
```

```
Google ADK nedir?
```

Agentin araçları çağırma akışını ADK arayüzünde adım adım izleyebilirsiniz.

Testi bitirince terminalde `Ctrl+C` ile durdurun.

---

## Adım 9: Cloud Run'a Deploy Edin

### 9.1 Deploy Edin

`gcloud run deploy --source .` komutu Cloud Build ile Dockerfile'ı derler ve doğrudan Cloud Run'a deploy eder:

> **Not:** Deploy komutunu çalıştırmadan önce `GOOGLE_API_KEY` değişkeninin shell'inizde tanımlı olduğundan emin olun. Tanımlı değilse [Adım 6'ya](#adım-6-api-keyi-alın-ve-ayarlayın) dönün.

```bash
gcloud run deploy adk-starter \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars "GOOGLE_API_KEY=${GOOGLE_API_KEY}"
```

Komut çalıştıktan sonra şuna benzer bir çıktı göreceksiniz:

```
Service [adk-starter] revision [adk-starter-00001] has been deployed
and is serving 100 percent of traffic.
Service URL: https://adk-starter-XXXX-uc.a.run.app
```

### 9.2 Deploy'u Doğrulayın

Döndürülen URL'yi tarayıcınızda açın. Agent'ın web arayüzü Cloud Run üzerinde çalışıyor olmalıdır.

```bash
# URL'yi değişkene atayın
SERVICE_URL=$(gcloud run services describe adk-starter \
  --region us-central1 \
  --format 'value(status.url)')

echo "Agent URL: $SERVICE_URL"
```

---

## Adım 10: Kaynakları Temizleyin

Workshop bittikten sonra gereksiz maliyet oluşmaması için kaynakları silin:

```bash
# Cloud Run servisini sil
gcloud run services delete adk-starter --region us-central1

# Artifact Registry'deki imajı sil (opsiyonel)
gcloud artifacts repositories delete cloud-run-source-deploy \
  --location=us-central1 \
  --project=$(gcloud config get-value project)
```

---

## Workshop Adımları

Proje kurulumu tamamlandıktan sonra aşağıdaki adımları sırayla takip edin. Her adım bağımsız bir Python paketi olarak tanımlıdır ve `adk web` arayüzünde ayrı ayrı seçilebilir.

| Adım | Paket | Konu | README |
|------|-------|------|--------|
| 1 | `s01_adk/` | Temel Agent — instruction, model, tools | [→ Adım 1](s01_adk/README.md) |
| 2 | `s02_tools/` | Özel Araçlar — Python fonksiyonu tool olarak | [→ Adım 2](s02_tools/README.md) |
| 3 | `s03_builtin_tools/` | Yerleşik Araçlar — Google Search | [→ Adım 3](s03_builtin_tools/README.md) |
| 4 | `s04_agent_as_tool/` | Agent'ı Araç Olarak Kullanmak — AgentTool | [→ Adım 4](s04_agent_as_tool/README.md) |
| 5 | `s05_sub_agents/` | Alt Ajan Yönlendirme — Sub-agent delegation | [→ Adım 5](s05_sub_agents/README.md) |
| 6 | `s06_sequential/` | Sıralı İş Akışı — SequentialAgent | [→ Adım 6](s06_sequential/README.md) |
| 7 | `s07_parallel/` | Paralel İş Akışı — ParallelAgent | [→ Adım 7](s07_parallel/README.md) |
| 8 | `s08_loop/` | Döngüsel İyileştirme — LoopAgent + exit_loop | [→ Adım 8](s08_loop/README.md) |

---

## Proje Yapısı

```
adk-starter/
├── s01_adk/               # Adım 1: Temel Agent
├── s02_tools/             # Adım 2: Özel Araçlar
├── s03_builtin_tools/     # Adım 3: Yerleşik Araçlar
├── s04_agent_as_tool/     # Adım 4: Agent as Tool
├── s05_sub_agents/        # Adım 5: Sub-agent Delegation
├── s06_sequential/        # Adım 6: Sequential Workflow
├── s07_parallel/          # Adım 7: Parallel Workflow
├── s08_loop/              # Adım 8: Loop Workflow
├── Dockerfile             # Cloud Run konteyner tanımı
├── requirements.txt       # Python bağımlılıkları
├── .env.example           # Ortam değişkenleri şablonu
└── README.md              # Bu dosya
```

---

## Faydalı Bağlantılar

- [Google ADK Dokümantasyonu](https://google.github.io/adk-docs/)
- [ADK Resmi Site](https://adk.dev/)
- [Google ADK GitHub](https://github.com/google/adk-python)
- [Google ADK Örnekleri](https://github.com/google/adk-samples)
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)
- [Cloud Run Fiyatlandırma](https://cloud.google.com/run/pricing)
