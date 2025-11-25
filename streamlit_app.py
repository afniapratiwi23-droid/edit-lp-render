import streamlit as st
import os
from generator import GeminiCopywriter, DesignExtractor
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(
    page_title="Landing Page Theme Editor",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stTextArea textarea {
        font-family: 'Courier New', monospace;
        font-size: 12px;
    }
    .main {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎨 Landing Page Theme Editor")
st.markdown("Transform your HTML with AI-powered design styles")

# Sidebar for API Keys
with st.sidebar:
    st.header("🔑 API Configuration")
    
    # Check for env var first
    env_key = os.getenv('GEMINI_API_KEY')
    if env_key:
        st.success("✅ Using server API key")
        api_key = env_key
    else:
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            help="Enter your Google Gemini API key"
        )
    
    st.divider()
    st.markdown("### 📚 How to Use")
    st.markdown("""
    1. Paste your HTML code
    2. Choose a design style
    3. (Optional) Add reference URL
    4. Click Generate!
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 HTML Input")
    html_input = st.text_area(
        "Paste your HTML code here",
        height=400,
        placeholder="<html>...</html>"
    )
    
    # Style & Options
    with st.expander("🎨 Style & Options", expanded=True):
        style = st.selectbox(
            "Choose Design Style",
            [
                ("reference_style", "🔗 Follow Reference Link"),
                ("pink_curhat", "🎀 Pink Curhat (Feminine & Friendly)"),
                ("minimalist_clean", "✨ Minimalist Clean (Professional)"),
                ("bold_dark", "🔥 Bold Dark (High Impact)"),
                ("luxury_elegant", "💎 Luxury Elegant (Premium & Exclusive)"),
                ("eco_natural", "🌿 Eco Natural (Organic & Fresh)"),
                ("tech_modern", "🚀 Tech Modern (SaaS & Futuristic)"),
                ("high_energy", "⚡ High Energy (Urgent & Salesy)"),
                ("ebook_bestseller", "📚 Ebook Best Seller (Professional & Authoritative)"),
                ("custom", "🎨 Custom Style")
            ],
            format_func=lambda x: x[1]
        )
        style_value = style[0]
        
        # Custom style prompt
        custom_prompt = ""
        if style_value == "custom":
            custom_prompt = st.text_area(
                "Describe your custom style",
                placeholder="e.g., Cyberpunk neon green, dark background, futuristic fonts..."
            )
        
        # Reference URL
        reference_url = st.text_input(
            "🔗 Reference Design URL (Optional)",
            placeholder="https://example.com",
            help="AI will extract and mimic the design from this URL"
        )
        
        # Rewrite copywriting
        rewrite_copywriting = st.checkbox(
            "✍️ Rewrite Copywriting",
            help="AI will rewrite the text to be more persuasive"
        )
    
    # Generate button
    if st.button("⚡ Generate Landing Page", type="primary", use_container_width=True):
        if not html_input.strip():
            st.error("Please paste HTML code first!")
        elif not api_key:
            st.error("Please enter your Gemini API key in the sidebar!")
        elif style_value == "custom" and not custom_prompt.strip() and not reference_url:
            st.error("Please provide custom style description or reference URL!")
        else:
            with st.spinner("🎨 Generating your landing page..."):
                try:
                    # Extract design tokens if reference URL provided
                    design_tokens = None
                    if reference_url:
                        with st.status("Extracting design from reference URL..."):
                            extractor = DesignExtractor(reference_url, api_key)
                            design_tokens = extractor.extract()
                            if design_tokens:
                                st.write("✓ Design tokens extracted")
                    
                    # Generate
                    copywriter = GeminiCopywriter(
                        html_input, 
                        api_key, 
                        style_value, 
                        rewrite_copywriting, 
                        custom_prompt, 
                        design_tokens
                    )
                    result_html = copywriter.generate()
                    
                    # Clean up markdown code blocks
                    if result_html.startswith('```html'):
                        result_html = result_html.replace('```html', '', 1)
                    if result_html.endswith('```'):
                        result_html = result_html.replace('```', '', 1)
                    
                    # Store in session state
                    st.session_state['generated_html'] = result_html
                    st.success("✅ Generation complete!")
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

with col2:
    st.subheader("👁️ Preview & Output")
    
    if 'generated_html' in st.session_state:
        # Tabs for preview and code
        tab1, tab2 = st.tabs(["Preview", "HTML Code"])
        
        with tab1:
            st.components.v1.html(
                st.session_state['generated_html'],
                height=600,
                scrolling=True
            )
        
        with tab2:
            st.code(st.session_state['generated_html'], language='html')
            
            # Download button
            st.download_button(
                label="📥 Download HTML",
                data=st.session_state['generated_html'],
                file_name="landing_page.html",
                mime="text/html"
            )
    else:
        st.info("👈 Generate a landing page to see the preview here")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px;'>
    Made with ❤️ using Streamlit & Google Gemini
</div>
""", unsafe_allow_html=True)
