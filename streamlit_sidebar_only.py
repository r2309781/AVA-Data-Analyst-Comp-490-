
import streamlit as st

st.set_page_config(
    page_title="GURU • Sidebar Dashboard",
    page_icon="🧠",
    layout="wide",
)

# ======================
# THEME & GLOBAL STYLES
# ======================
st.markdown(
    """
    <style>
        /* Hide Streamlit default menu/footer */
        #MainMenu, footer {visibility: hidden;}
        :root {
            --bg: #0b0f0e;
            --panel: #0f1513;
            --text: #E8ECEA;
            --muted: #9AA5A1;
            --accent: #17c964;
        }
        .main {background: var(--bg); color: var(--text);}
        section[data-testid="stSidebar"] {
            background: #0c1210; color: var(--text); border-right: 1px solid #0e1b16;
            padding-top: 8px;
        }
        .sb-logo {
            display:flex; align-items:center; gap:10px; padding:14px 8px 10px 8px; margin-bottom:4px;
        }
        .sb-logo .glyph {
            background:#0d261c; color:var(--accent); width:34px; height:34px;
            display:grid; place-items:center; border-radius:10px; border:1px solid #133826;
            box-shadow: 0 0 0 2px #0b1913 inset;
        }
        .sb-appname {font-weight:700; line-height:1.1}
        .sb-sub {font-size:12px; color: var(--muted); margin-top:-4px;}
        .sb-divider {height:1px; background:#0e1b16; margin:8px 6px;}
        .sb-item {
            padding:10px 12px; border-radius:12px; margin:4px 6px;
            display:flex; align-items:center; gap:10px; color: var(--text);
            border: 1px solid transparent;
        }
        .sb-item:hover {background:#0e1715; border-color:#10211a; cursor:pointer;}
        .sb-item.active { background:#0d261c; border-color:#133826; }
        .sb-icon {opacity:.9;}
        .placeholder-title {color: var(--muted); margin-top: 12px; font-size: 14px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================
# SIDEBAR ONLY
# ======================
with st.sidebar:
    st.markdown(
        """
        <div class="sb-logo">
          <div class="glyph">🧠</div>
          <div>
            <div class="sb-appname">GURU</div>
            <div class="sb-sub">AI Business Guru</div>
          </div>
        </div>
        <div class="sb-divider"></div>
        """,
        unsafe_allow_html=True,
    )

    def sb_item(label, icon, active=False):
        cls = "sb-item active" if active else "sb-item"
        st.markdown(f'<div class="{cls}"><span class="sb-icon">{icon}</span> {label}</div>', unsafe_allow_html=True)

    # Sidebar menu (Dashboard active)
    sb_item("Dashboard", "🧭", active=True)
    sb_item("Sales Analytics", "📈")
    sb_item("Trends & Analysis", "📊")
    sb_item("Inventory Overview", "📦")
    sb_item("Transactions", "💳")
    sb_item("AI Insights", "✨")
    sb_item("Reports", "🧾")

# ======================
# MAIN PLACEHOLDER (minimal)
# ======================
st.title("Dashboard")
st.markdown('<div class="placeholder-title">Sidebar-only layout demo. Add your content here.</div>', unsafe_allow_html=True)
