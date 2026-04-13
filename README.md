# 🦁 FP-KCV/jawani-sealion-gatra-2-9b

<div align="center">

![Java](https://img.shields.io/badge/Language-Javanese-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9%2B-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

**Asisten AI cerdas berbasis bahasa Jawa dengan teknologi hybrid pipeline** 🦁✨

Arya Pratama Rhama Putra, Raditya Akmal, Fa'iz Akbar Hizbullah

</div>

---

## 📚 Tentang Proyek

**Jawani AI** adalah sistem asisten cerdas berbasis bahasa Jawa yang dirancang untuk membantu pembelajaran dan praktik bahasa Jawa secara interaktif. Menggunakan teknologi **hybrid pipeline**, sistem menggabungkan kekuatan klasifikasi berbasis BERT dengan kemampuan generative AI untuk memberikan pengalaman pembelajaran yang autentik dan sesuai konteks budaya Jawa.

### 🤖 Teknologi Utama

| Komponen | Deskripsi |
|----------|-----------|
| **Javanese-BERT Classifier** | Mendeteksi tingkat bahasa Jawa (unggah-ungguh) dengan akurasi tinggi |
| **Sea-Lion 9B LLM** | Model bahasa berperforma tinggi untuk generasi respons yang natural |
| **Hybrid Pipeline** | Integrasi seamless antara klasifikasi + generasi untuk respons kontekstual |
| **Streamlit Interface** | UI interaktif untuk eksperimen dan demonstrasi |

---

## 🎓 Cara Menggunakan untuk Pembelajaran

### **Untuk Pemula Bahasa Jawa**

1. **Mulai dengan Kosakata Dasar**
   ```
   Tanyakan: "Apa arti 'tembung [kata]'?"
   Contoh: "Apa arti tembung 'slamet'?"
   ```

2. **Praktik Percakapan Sederhana**
   ```
   Mulai dengan Ngoko Lugu (santai)
   Misalkan: "Halo, aku senang belajar Jawa"
   ```

3. **Request Koreksi**
   ```
   Jawani akan otomatis memberikan saran perbaikan
   dan penjelasan tata bahasa
   ```

### **Untuk Learner Tingkat Menengah**

- 🔄 Praktik switching antara tingkat bahasa
- 📖 Pelajari nuansa unggah-ungguh
- 🎯 Fokus pada konteks penggunaan yang tepat

### **Untuk Advanced Learners**

- 💬 Diskusi tentang dialek dan variasi regional
- 🏛️ Pelajari bahasa Jawa klasik
- 📚 Berlatih literasi dalam bahasa Jawa

---

## 🚀 Fitur Utama

### ✨ **1. Klasifikasi Unggah-Ungguh (Tingkat Bahasa)**

Sistem secara otomatis mendeteksi dan mengidentifikasi tingkat bahasa Jawa yang digunakan:

### TINGKAT BAHASA JAWA (UNGGAH-UNGGUH)

| Tingkat Bahasa | Keterangan |
|---|---|
| **Ngoko Lugu** | Santai & Kasual |
| **Ngoko Alus** | Halus Kasual |
| **Krama Lugu** | Formal Standar |
| **Krama Inggil** | Formal Tertinggi |

### 👥 **2. Tiga Persona AI yang Berbeda**

| Persona | Tingkat Bahasa | Gaya | Keahlian |
|---------|---|---|---|
| 🎓 **Guru Basa Jawa** | Krama Inggil | Edukatif & Formal | Koreksi tata bahasa, pembelajaran sistematis |
| 👫 **Kanca Cerak (Teman Dekat)** | Ngoko Lugu | Santai & Friendly | Percakapan sehari-hari, motivasi |
| 👔 **Asisten Resmi** | Krama Lugu | Professional | Konsultasi, informasi formal |

### 🎯 **3. Respons Kontekstual & Cerdas**

- ✅ Deteksi otomatis tingkat bahasa pengguna
- ✅ Penyesuaian respons berdasarkan persona terpilih
- ✅ Koreksi tata bahasa dengan penjelasan
- ✅ Memori percakapan untuk konteks yang lebih baik
- ✅ Rekomendasi pembelajaran yang dipersonalisasi

---

## 📦 Model yang Digunakan

### **Javanese-BERT Classifier**
- Model: `Javanese-BERT-Small`
- Tugas: Klasifikasi tingkat bahasa Jawa
- Akurasi: Tinggi pada dataset Javanese
- File: [classification-javanese-lanjutan.ipynb](training%20model/classification-javanese-lanjutan.ipynb)

### **Sea-Lion 9B LLM**
- Model: Sea-Lion 9B
- Tugas: Generasi respons natural
- Parameter: 9 Billion
- Optimasi: Accelerated inference dengan CUDA

---

## 💻 Penggunaan

### **Bot Telegram** (Jika Dikonfigurasi)

1. Cari bot: `@JawaniAIBot`
2. Ketik `/start` untuk memulai
3. Pilih persona dan tingkat bahasa
4. Mulai percakapan!

---

## 📂 Struktur Proyek

```
Jawani-SeaLion-9B/
├── README.md                          # Dokumentasi utama
├── requirements.txt                   # Python dependencies
│
├── bot/                               # 🤖 Bot Applications
│   ├── asistenbot.ipynb              # Streamlit UI yang interaktif
│   ├── gurubot.ipynb                 # Mode guru (Krama Inggil)
│   ├── kancabot.ipynb                # Mode teman (Ngoko Lugu)
│   └── gatra2_test.jsonl             # Test dataset
│
├── training model/                    # 📚 Model Training
│   ├── classification-javanese-lanjutan.ipynb   # BERT classifier training
│   └── jawani-gatra-2.ipynb          # LLM fine-tuning benchmark
│
├── preprocessing/                     # 🔄 Data Processing
│   ├── ekstrak.py                    # Data extraction script
│   └── ekstrak_test.py               # Test data extraction
│
└── data/                              # 📊 Dataset & Resources
    └── [Data files here]
```

### 📝 Penjelasan File Penting

| File | Fungsi |
|------|--------|
| `bot/asistenbot.ipynb` | Interface utama dengan Streamlit |
| `bot/gurubot.ipynb` | Bot dengan persona guru (Krama Inggil) |
| `bot/kancabot.ipynb` | Bot dengan persona teman (Ngoko Lugu) |
| `training model/classification-javanese-lanjutan.ipynb` | Training BERT untuk klasifikasi unggah-ungguh |
| `training model/jawani-gatra-2.ipynb` | Benchmark dan testing LLM |

---

## 📊 Dataset & Training

### **Preprocessing Data**

Run script untuk ekstrak dan proses data:

```bash
python preprocessing/ekstrak.py --input raw_data/ --output processed_data/
python preprocessing/ekstrak_test.py --input test_data/ --output test_processed/
```

### **Training Custom Classifier**

```bash
# Buka training model notebook
jupyter notebook "training model/classification-javanese-lanjutan.ipynb"
```

### **Fine-tuning LLM**

```bash
# Jalankan benchmark LLM
jupyter notebook "training model/jawani-gatra-2.ipynb"
```

---

## ⚙️ Konfigurasi & Performance

### **Parameter Generative AI**

```yaml
Generation Settings:
  max_tokens: 256              # Panjang respons maksimal
  temperature: 0.7             # Kreativitas (0.0-1.0)
  top_p: 0.9                   # Diversitas respons
  top_k: 50                    # Top-k sampling
  repetition_penalty: 1.1      # Penghindaran repetisi
  use_cache: true              # Optimasi kecepatan
```

### **Spesifikasi Sistem**

| Aspek | Requirement |
|-------|-------------|
| **Python Version** | 3.9+ |
| **RAM** | Minimal 16GB, Recommended 32GB |
| **GPU** | VRAM 8GB+ (CUDA 11.8+) |
| **Storage** | ~18GB untuk models |
| **Response Time** | 5-15 detik per pesan |

---

## 📊 Performa & Metrics

### **Model Performance**

### JAVANESE-BERT CLASSIFIER

| Metric | Value |
|---|---|
| **Accuracy (Unggah-Ungguh)** | 85% |
| **Inference Device** | GPU |

---

### SEA-LION 9B LLM

| Metric | Value |
|---|---|
| **Context Length** | 8192 |
| **Output Tokens (Max)** | 1256 |
| **Response Quality** | Good |

---

## 📚 Referensi & Resources

### **Paper & Research**
- BERT: [Devlin et al., 2018] (https://arxiv.org/abs/1810.04805)
- Sea-Lion LLM: Southeast Asia focus language model (https://arxiv.org/abs/2504.05747)

### **Citation**
Jika menggunakan model ini dalam penelitian, silakan cite:
```bibtex
@misc{sea-lion_inggil_2026,
	author       = { Sea-LION Inggil },
	title        = { jawani-sealion-gatra-2-9b (Revision 2f42973) },
	year         = 2026,
	url          = { https://huggingface.co/FP-KCV/jawani-sealion-gatra-2-9b },
	doi          = { 10.57967/hf/8277 },
	publisher    = { Hugging Face }
}
```

---

## 🤝 Kontribusi

Kami menerima kontribusi dalam bentuk:

### **Bug Reports**
```
- Deskripsi bug
- Steps untuk reproduce
- Screenshot/error message
- Environment info
```

### **Feature Requests**
```
- Deskripsi fitur
- Use case
- Priority level
```

### **Pull Requests**
```
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request
```

### **Kontribusi Non-Code**
- 📝 Improve dokumentasi
- 🌍 Translate ke bahasa lain
- 🎨 Perbaikan desain
- 📢 Membantu promosi

---


<div align="center">

**Selamat Belajar Bahasa Jawa! Matur Suwun! 🎓✨**

Dibuat dengan ❤️ untuk pelestarian bahasa Jawa

[⬆ back to top](#-jawani-ai---asisten-bahasa-jawa)

</div>
