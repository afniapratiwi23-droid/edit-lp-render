# 🚀 Deploy Landing Page Editor ke Streamlit Cloud

## Langkah 1: Push ke GitHub

```bash
# Inisialisasi git
git init

# Tambahkan semua file
git add .

# Commit
git commit -m "Convert to Streamlit app"

# Tambahkan remote (ganti dengan repo Anda)
git remote add origin https://github.com/username/landing-page-editor.git

# Push
git push -u origin main
```

## Langkah 2: Deploy di Streamlit Cloud

1. **Buka** [share.streamlit.io](https://share.streamlit.io)
2. **Login** dengan GitHub account
3. Klik **"New app"**
4. **Pilih repository** Anda
5. **Main file path**: `streamlit_app.py`
6. Klik **"Deploy"**!

## Langkah 3: Tambahkan API Key (Opsional)

Di Streamlit Cloud dashboard:
1. Buka app Anda
2. Klik **"⋮"** (menu) → **"Settings"**
3. Pilih tab **"Secrets"**
4. Tambahkan:
   ```toml
   GEMINI_API_KEY = "AIzaSy..."
   ```
5. Klik **"Save"**

> **Note**: Jika tidak set API key di secrets, user bisa input sendiri di sidebar app.

## ✅ Selesai!

Aplikasi Anda akan live di: `https://username-landing-page-editor.streamlit.app`

## 🏃 Test Lokal (Opsional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run streamlit_app.py
```

## 📝 Fitur yang Tersedia

- ✅ 8+ Design styles
- ✅ Reference URL extraction
- ✅ AI copywriting rewrite
- ✅ Live preview
- ✅ Download HTML
- ✅ Gratis selamanya!

## 🔄 Update App

Setiap kali Anda push ke GitHub, Streamlit Cloud akan otomatis re-deploy!
