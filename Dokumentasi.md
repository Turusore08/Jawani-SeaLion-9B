# Jawani AI - Bot Telegram

## 📚 Deskripsi Project

**Jawani AI** adalah asisten AI cerdas berbasis bahasa Jawa yang menggunakan teknologi hybrid pipeline untuk memberikan pengalaman interaksi yang autentik dan edukatif. Sistem ini menggabungkan kemampuan klasifikasi tingkat bahasa Jawa (unggah-ungguh) dengan generative AI untuk memberikan respons yang sesuai konteks budaya Jawa.

### 🤖 Teknologi Utama
- **Javanese-BERT-Small Classifier**: Mendeteksi tingkat bahasa Jawa (Ngoko Lugu/Alus, Krama Lugu/Inggil)
- **Sea-Lion 9B LLM**: Model bahasa besar untuk generate respons yang natural
- **Hybrid Pipeline**: Kombinasi klasifikasi + generative AI untuk respons yang kontekstual

## 🚀 Fitur Utama

### 1. **Klasifikasi Unggah-Ungguh**
Sistem secara otomatis mendeteksi tingkat bahasa Jawa yang digunakan user:
- **Ngoko Lugu**: Bahasa sehari-hari santai
- **Ngoko Alus**: Bahasa halus tapi masih kasual
- **Krama Lugu**: Bahasa formal standar
- **Krama Inggil**: Bahasa formal tertinggi

### 2. **Persona AI yang Dapat Dipilih**
- **Guru Basa Jawa**: Menggunakan Krama Inggil, memberikan koreksi jika siswa salah
- **Kanca Cerak**: Menggunakan Ngoko Lugu, lebih santai dan asik
- **Asisten Resmi**: Menggunakan Krama Lugu untuk konteks formal

### 3. **Respons Kontekstual**
AI memberikan respons berdasarkan:
- Tingkat bahasa yang terdeteksi
- Persona yang dipilih
- Konteks percakapan

## 📱 Cara Menggunakan Bot Telegram

### Persiapan Awal

1. **Buka Telegram** dan cari bot: `@JawaniAIBot`
2. **Klik Start** atau kirim perintah `/start`

### Perintah Dasar

| Perintah | Deskripsi |
|----------|-----------|
| `/start` | Memulai percakapan dengan bot |
| `/help` | Menampilkan pesan bantuan |

### Contoh Percakapan

#### 1. **Percakapan Santai (Ngoko Lugu)**
```
User: Halo, aku mau belajar basa Jawa
Bot:  Sugeng rawuh! Kula Guru Basa Jawa AI. Wonten menapa ingkang saged kula biyantu?
```

#### 2. **Percakapan Formal (Krama)**
```
User: Pun mugi kula saged sinau basa Jawa
Bot:  Panjenengan saged kula biyantu. Menapa ingkang kersa dipun pelajari?
```

#### 3. **Koreksi Bahasa**
```
User: Aku mau makan nasi
Bot:  "Aku mau makan nasi" - nggih, nanging menawi ngangge basa Jawa, saged dipun ucap "Kula badhe nedha sekul"
```

### Tips Penggunaan

#### 1. **Sesuaikan Tingkat Bahasa**
- Gunakan bahasa Jawa sesuai tingkat yang Anda kuasai
- Bot akan mendeteksi dan menyesuaikan respons

#### 2. **Pilih Topik Pembelajaran**
- Tanyakan tentang kosakata
- Minta contoh kalimat
- Diskusikan tata bahasa
- Pelajari unggah-ungguh

#### 3. **Praktik Berkelanjutan**
- Latihan setiap hari untuk meningkatkan kemahiran
- Mulai dari kosakata dasar
- Lanjut ke percakapan sederhana

## 🎯 Contoh Skenario Penggunaan

### Skenario 1: Belajar Kosakata
```
User: Apa arti tembung "slamet"?
Bot:  Tembung "slamet" inggih punika "selamat" utawi "aman". Contone: "Sugeng slamet" artos "Selamat pagi"
```

### Skenario 2: Latihan Percakapan
```
User: Kepiye carane ngomong "Terima kasih" ing basa Jawa?
Bot:  "Matur nuwun" utawi "Matur suwun" kangge ngucap "Terima kasih". Menawi formal, saged ngangge "Matur nuwun sanget"
```

### Skenario 3: Koreksi Tata Bahasa
```
User: Saya suka makan gudeg
Bot:  "Saya suka makan gudeg" - nggih, nanging menawi ngangge basa Jawa lugu: "Kula remen nedha gudeg"
```

## ⚙️ Konfigurasi Bot

### Parameter Generation
- **Max Tokens**: 256 token per respons
- **Temperature**: 0.7 (kreativitas sedang)
- **Top-p**: 0.9 (diversitas respons)
- **Sampling**: Aktif untuk variasi

### Handling Error
Bot dilengkapi dengan error handling untuk:
- Masalah koneksi internet
- Limitasi memori GPU
- Token limit tercapai
- Input yang tidak valid

## 🔧 Troubleshooting

### Bot Tidak Merespons
1. Periksa koneksi internet
2. Restart aplikasi Telegram
3. Kirim ulang pesan

### Respons Lambat
- Bot menggunakan model besar (9B parameter)
- Waktu respons: 5-15 detik tergantung kompleksitas
- GPU acceleration aktif untuk performa optimal

### Masalah Bahasa
- Pastikan input dalam bahasa Indonesia/Jawa
- Bot optimal untuk konteks pendidikan bahasa Jawa
- Untuk bahasa lain, respons mungkin kurang akurat

## 📊 Statistik dan Performansi

### Model Specifications
- **Javanese-BERT-Small**: Model BERT khusus bahasa Jawa untuk klasifikasi
- **Sea-Lion 9B**: 9B parameters untuk generation
- **VRAM Usage**: ~16GB untuk inferensi
- **Response Time**: 5-15 detik per pesan

### Akurasi Klasifikasi
- **Unggah-Ungguh**: >90% akurasi
- **Context Understanding**: >85% relevansi
- **Language Generation**: Natural dan kontekstual

## 🤝 Kontribusi dan Pengembangan

Project ini dikembangkan untuk:
- Pendidikan bahasa Jawa
- Preservasi budaya
- Teknologi AI untuk kebaikan

### Feedback
Kirim feedback atau saran melalui bot untuk perbaikan berkelanjutan.

---

**Catatan**: Bot ini masih dalam tahap pengembangan. Beberapa fitur mungkin mengalami perubahan atau peningkatan di masa depan.
