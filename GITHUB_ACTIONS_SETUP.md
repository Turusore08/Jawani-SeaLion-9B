# GitHub Actions to HuggingFace Upload Setup

Workflow ini mengupload `app.py` dan `requirements.txt` ke HuggingFace Spaces secara otomatis setiap kali ada push ke branch main/master.

## Setup Langkah demi Langkah

### 1. Dapatkan HuggingFace Token
- Buka https://huggingface.co/settings/tokens
- Klik "New token"
- Beri nama token (misal: `github-actions`)
- Pilih role: **Write** (untuk bisa upload)
- Salin token (pastikan disimpan dengan aman!)

### 2. Tambahkan Token ke GitHub Secrets
- Buka repository GitHub Anda: `https://github.com/YOUR_USERNAME/YOUR_REPO`
- Masuk ke **Settings** → **Secrets and variables** → **Actions**
- Klik **New repository secret**
- Name: `HF_TOKEN`
- Value: (paste token dari HuggingFace)
- Klik **Add secret**

### 3. Pastikan Struktur Repository
```
.github/
└── workflows/
    └── upload-to-huggingface.yml  ← Workflow file (sudah ada)
app.py                               ← File utama
requirements.txt                     ← Dependencies
README.md                            ← Dokumentasi (harus ada title)
```

### 4. Verifikasi README.md
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
pinned: false
---
```

## Cara Kerja Workflow

✅ **Trigger otomatis ketika:**
- Ada push ke branch `main` atau `master`
- File `app.py`, `requirements.txt` atau workflow file berubah

🔄 **Proses:**
1. Checkout code dari repository
2. Setup Python 3.10
3. Install `huggingface-hub` library
4. Extract nama HuggingFace Space dari README
5. Upload `app.py` dan `requirements.txt`
6. Push ke HuggingFace Spaces dengan commit message otomatis

## Monitoring Workflow

✓ Lihat status workflow di tab **Actions** di GitHub repository
✓ Setiap run akan menunjukkan:
  - Logs detail dari setiap step
  - Status upload ke HuggingFace
  - Error message jika ada masalah

## Troubleshooting

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
