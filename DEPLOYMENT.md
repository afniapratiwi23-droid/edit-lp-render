# Landing Page Theme Editor - Deployment Guide

## Deploy ke Render.com

### Langkah 1: Push ke GitHub
```bash
# Inisialisasi git (jika belum)
git init

# Tambahkan semua file
git add .

# Commit
git commit -m "Initial commit - Landing Page Editor"

# Tambahkan remote repository (ganti dengan repo Anda)
git remote add origin https://github.com/username/repo-name.git

# Push
git push -u origin main
```

### Langkah 2: Deploy di Render
1. Buka [Render.com](https://render.com) dan login
2. Klik **"New +"** → **"Web Service"**
3. Connect repository GitHub Anda
4. Render akan otomatis detect `render.yaml`
5. Klik **"Apply"**

### Langkah 3: Set Environment Variables
Di Render dashboard:
1. Buka service Anda
2. Pergi ke **"Environment"**
3. Tambahkan variable:
   - Key: `GEMINI_API_KEY`
   - Value: `[API key Anda]`
4. Klik **"Save Changes"**

### Langkah 4: Deploy!
Render akan otomatis build dan deploy aplikasi Anda.

## Catatan Penting
- **Port**: Render otomatis set port, jadi `app.run()` di `app.py` sudah benar
- **API Keys**: Jangan commit file `.env` ke GitHub (sudah ada di `.gitignore`)
- **Logs**: Bisa dilihat di Render dashboard untuk debugging

## Local Development
```bash
# Activate virtual environment
source .venv/bin/activate  # Mac/Linux
# atau
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run locally
python3 app.py
```

Aplikasi akan berjalan di `http://localhost:8080`
