# Landing Page Theme Editor

AI-powered landing page redesigner using Google Gemini.

## 🚀 Deploy to Streamlit Cloud

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Main file: `streamlit_app.py`
   - Click "Deploy"!

3. **Add API Key (in Streamlit Cloud):**
   - Go to your app settings
   - Click "Secrets"
   - Add:
     ```toml
     GEMINI_API_KEY = "your-api-key-here"
     ```

## 🏃 Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run streamlit_app.py
```

## ✨ Features

- 🎨 Multiple design styles (Pink Curhat, Minimalist, Bold Dark, etc.)
- 🔗 Design extraction from reference URLs
- ✍️ AI-powered copywriting rewrite
- 📱 Live preview
- 💾 Download generated HTML

## 🔑 API Key

You can either:
1. Set `GEMINI_API_KEY` in Streamlit Cloud secrets (recommended)
2. Enter API key in the sidebar when using the app
