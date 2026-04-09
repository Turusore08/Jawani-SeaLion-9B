# GitHub Actions to HuggingFace Upload Setup

Workflow ini mengupload `app.py` dan `requirements.txt` ke HuggingFace Spaces secara otomatis setiap kali ada push ke branch main/master.

## Setup Langkah demi Langkah

### 1. Buat HuggingFace Space
- Buka https://huggingface.co/spaces
- Klik **"Create new Space"**
- **Owner**: Pilih username Anda
- **Space name**: `jawani-ai-guru` (harus lowercase, tanpa spasi, gunakan `-` atau `_`)
- **SDK**: Pilih **Streamlit**
- **Visibility**: Public atau Private sesuai kebutuhan
- Klik **Create Space**

### 2. Update README.md
Setelah membuat space, update `README.md` dengan repo_id yang benar:
```yaml
---
title: Jawani AI Guru
emoji: 👨‍🏫
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
hf_repo: YOUR_USERNAME/jawani-ai-guru  # ← Ganti YOUR_USERNAME dengan username HF Anda
pinned: false
---
```

**⚠️ Penting:** Repo ID harus mengikuti aturan:
- Hanya alphanumeric, `-`, `_`, atau `.`
- Tidak boleh mulai/akhir dengan `-` atau `.`
- Maksimal 96 karakter
- Format: `username/space-name`

### 3. Dapatkan HuggingFace Token
- Buka https://huggingface.co/settings/tokens
- Klik "New token"
- Beri nama token (misal: `github-actions`)
- Pilih role: **Write** (untuk bisa upload)
- Salin token (pastikan disimpan dengan aman!)

### 4. Tambahkan Token ke GitHub Secrets
- Buka repository GitHub Anda: `https://github.com/YOUR_USERNAME/YOUR_REPO`
- Masuk ke **Settings** → **Secrets and variables** → **Actions**
- Klik **New repository secret**
- Name: `HF_TOKEN`
- Value: (paste token dari HuggingFace)
- Klik **Add secret**

### 5. Pastikan Struktur Repository
```
.github/
└── workflows/
    └── upload-to-huggingface.yml  ← Workflow file (sudah ada)
app.py                               ← File utama
requirements.txt                     ← Dependencies
README.md                            ← Dokumentasi (harus ada hf_repo)
```

### 6. Verifikasi README.md
Pastikan `README.md` memiliki format HuggingFace Spaces dengan yaml frontmatter:
```yaml
---
title: Jawani AI Guru
emoji: 👨‍🏫
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.32.0
app_file: app.py
hf_repo: YOUR_USERNAME/jawani-ai-guru
pinned: false
---
```

### 7. Push ke GitHub
- Commit dan push semua perubahan ke branch `main` atau `master`
- Workflow otomatis akan jalan dan upload ke HuggingFace Space

## Cara Kerja Workflow

✅ **Trigger otomatis ketika:**
- Ada push ke branch `main` atau `master`
- File `app.py`, `requirements.txt` atau workflow file berubah

🔄 **Proses:**
1. Checkout code dari repository
2. Setup Python 3.10
3. Install `huggingface-hub` library
4. Extract nama HuggingFace Space dari README (`hf_repo` field)
5. Upload `app.py` dan `requirements.txt`
6. Push ke HuggingFace Spaces dengan commit message otomatis

## Monitoring Workflow

✓ Lihat status workflow di tab **Actions** di GitHub repository
✓ Setiap run akan menunjukkan:
  - Logs detail dari setiap step
  - Status upload ke HuggingFace
  - Error message jika ada masalah

## Troubleshooting

**❌ Repo ID invalid?**
- Pastikan `hf_repo` di README.md menggunakan format yang benar
- Contoh: `username/jawani-ai-guru` (bukan `Jawani AI Guru`)
- Tidak boleh ada spasi, gunakan `-` atau `_` sebagai separator

**❌ Token tidak valid?**
- Verifikasi token sudah benar di GitHub Secrets
- Pastikan token punya permission **Write**

**❌ HuggingFace Space tidak ditemukan?**
- Pastikan space sudah dibuat di https://huggingface.co/spaces
- Verifikasi nama di README.md `title` field

**❌ Workflow tidak trigger?**
- Push file ke branch `main` atau `master` (bukan branch lain)
- Cek apakah file `.github/workflows/upload-to-huggingface.yml` sudah commit

## Customization

**Mengubah branch trigger:**
Buka `.github/workflows/upload-to-huggingface.yml` dan ubah:
```yaml
on:
  push:
    branches:
      - main        # Ubah sesuai branch Anda
      - master
```

**Menambah file lain untuk di-upload:**
Edit bagian `files_to_upload` di workflow:
```python
files_to_upload = ['app.py', 'requirements.txt', 'config.yaml']
```

**Mengubah repo type:**
Default adalah `repo_type="space"` untuk HuggingFace Spaces. 
Jika ingin ke Model/Dataset, ubah ke:
- `repo_type="model"` untuk Models
- `repo_type="dataset"` untuk Datasets
