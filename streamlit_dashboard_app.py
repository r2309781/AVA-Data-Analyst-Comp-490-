
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="GURU • AI Business Guru",
    page_icon="🧠",
    layout="wide",
)

# ======================
# THEME & GLOBAL STYLES
# ======================
st.markdown(
    """
    <style>
        /* Hide Streamlit default elements */
        #MainMenu, footer, header {visibility: hidden;}

        :root {
            --bg: #0b0f0e;
            --panel: #0f1513;
            --panel-2: #111916;
            --text: #E8ECEA;
            --muted: #9AA5A1;
            --accent: #17c964;
            --accent-2: #0aa14d;
            --card: #0b0f0e;
            --chip: #10231a;
            --danger: #ff4d4f;
        }
        .main {
            background: linear-gradient(180deg, #0b0f0e 0%, #0b0f0e 100%) !important;
            color: var(--text);
        }
        .guru-app {font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;}
        .topbar {
            display:flex; align-items:center; justify-content:space-between;
            padding: 8px 24px; border-bottom: 1px solid #0e1b16; margin-bottom: 8px;
            background: var(--panel);
            position: sticky; top: 0; z-index: 40; border-radius: 14px;
        }
        .brand {display:flex; align-items:center; gap:12px; font-weight:600;}
        .brand .logo {
            width:28px; height:28px; border-radius:8px; display:grid; place-items:center;
            background: #0d261c; color: var(--accent);
            border: 1px solid #143928;
            box-shadow: 0 0 0 2px #0b1913 inset;
            font-size: 16px;
        }
        .top-actions {display:flex; align-items:center; gap:14px; color:var(--muted);}
        .quick-sale {
            background: var(--accent); color:#03150b; padding:8px 12px; border-radius:12px;
            text-decoration:none; font-weight:600; border: 1px solid #0aa14d;
            box-shadow: 0 4px 18px rgba(23,201,100,.25);
        }
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #0c1210; color: var(--text); border-right: 1px solid #0e1b16;
        }
        .sb-logo {
            display:flex; align-items:center; gap:10px; padding:14px 8px 6px 8px; margin-bottom:8px;
        }
        .sb-logo .glyph {background:#0d261c; color:var(--accent); width:34px; height:34px; display:grid; place-items:center; border-radius:10px;}
        .sb-appname {font-weight:700; line-height:1.1}
        .sb-sub {font-size:12px; color:var(--muted); margin-top:-4px;}
        .sb-item {
            padding:10px 12px; border-radius:12px; margin:4px 6px; display:flex; align-items:center; gap:10px;
            color: var(--text);
        }
        .sb-item.active { background: #0d261c; color: var(--text); border:1px solid #133826;}
        .sb-icon {opacity:.9;}
        /* Cards grid */
        .kpi-grid {display:grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap:18px; margin-top:10px;}
        .card {
            background: var(--panel); border: 1px solid #0e1b16; border-radius:16px; padding:18px;
            box-shadow: 0 10px 24px rgba(0,0,0,.35);
        }
        .card h4 {margin: 0 0 6px 0; color: var(--muted); font-weight:600; font-size:14px; display:flex; align-items:center; gap:8px;}
        .card .value {font-size:30px; font-weight:800; margin-top:6px; letter-spacing:.2px;}
        .trend {font-size:12px; color:#7BE0A2; margin-top:4px;}
        .trend.down {color:#ff7a7d;}
        .pill {background:#0f241b; color:var(--accent); padding:5px 8px; border-radius:10px; font-size:12px; border:1px solid #123a28;}
        /* Section cards */
        .section-title {display:flex; align-items:center; gap:8px; font-weight:700; color:var(--text);}
        .subtext {color:var(--muted); font-size:13px; margin-top:2px;}
        .rank-row {display:flex; align-items:center; justify-content:space-between; padding:12px 0; border-bottom:1px dashed #12231c;}
        .rank-row:last-child {border-bottom: 0;}
        .chip {background: var(--chip); border:1px solid #163b2a; padding:4px 10px; border-radius:999px; font-size:12px; color: var(--text);}
        /* Custom progress bar */
        .progress {
            width:100%; height:12px; background:#0d1412; border-radius:999px; border:1px solid #0f1e18; overflow:hidden;
        }
        .progress > span {
            display:block; height:100%; background: linear-gradient(90deg, #17c964, #0aa14d);
        }
        /* Floating chat button */
        .fab {
            position: fixed; right: 24px; bottom: 24px; z-index: 100;
            background: #0d261c; color: var(--text); padding: 10px 14px; border-radius: 999px; border: 1px solid #133826;
            box-shadow: 0 8px 28px rgba(0,0,0,.45); display:flex; align-items:center; gap:8px;
        }
        .avatar {
            width:34px; height:34px; border-radius:999px; background:#0d261c; display:grid; place-items:center;
            color:var(--text); border: 1px solid #163b2a; font-weight:700;
        }
        .muted {color:var(--muted); font-size:13px;}
        .breadcrumb {display:flex; align-items:center; gap:10px; color:var(--muted); font-size:13px;}
        .breadcrumb .dot {width:6px; height:6px; background:#1e2a26; border-radius:999px; display:inline-block;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================
# SIDEBAR
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
        """,
        unsafe_allow_html=True,
    )
    # Sidebar items (static; no navigation wired)
    def sb_item(label, icon, active=False):
        cls = "sb-item active" if active else "sb-item"
        st.markdown(f'<div class="{cls}"><span class="sb-icon">{icon}</span> {label}</div>', unsafe_allow_html=True)

    sb_item("Dashboard", "🧭", active=True)
    sb_item("Sales Analytics", "📈")
    sb_item("Trends & Analysis", "📊")
    sb_item("Inventory Overview", "📦")
    sb_item("Transactions", "💳")
    sb_item("AI Insights", "✨")
    sb_item("Reports", "🧾")

# ======================
# TOP BAR
# ======================
today = date(2024, 1, 22)  # placeholder to mimic screenshot
col = st.container()
with col:
    st.markdown(
        f"""
        <div class="guru-app">
          <div class="topbar">
            <div class="brand">
              <div class="logo">G</div>
              <div>
                <div style="font-weight:700;">RefreshCorp Beverages</div>
                <div class="muted">Dashboard</div>
              </div>
            </div>
            <div class="top-actions">
              <div>
                <div style="font-weight:700;">RefreshCorp Beverages</div>
                <div class="muted">Today: {today.strftime('%b %d, %Y')}</div>
              </div>
              <a class="quick-sale" href="#">＋ Quick Sale</a>
              <div class="avatar">RB</div>
            </div>
          </div>
        """,
        unsafe_allow_html=True,
    )

# Welcome
st.markdown("""
<div class="guru-app" style="padding: 6px 6px 0 6px;">
  <div class="breadcrumb" style="margin: 6px 4px 14px 4px;">
    <span>Dashboard</span><span class="dot"></span><span class="muted">Welcome back! Here's what's happening with your business today.</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ======================
# KPI CARDS
# ======================
def kpi_card(title, value, trend_txt, trend_up=True, icon=""):
    up_cls = "trend" if trend_up else "trend down"
    st.markdown(
        f"""
        <div class="card">
            <h4>{title} {f'<span class="pill">{icon}</span>' if icon else ''}</h4>
            <div class="value">{value}</div>
            <div class="{up_cls}">{trend_txt}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="kpi-grid">', unsafe_allow_html=True)
kpi_cols = st.columns(4, gap="large")
with kpi_cols[0]:
    kpi_card("Total Revenue", "$125,420", "↑ 12.5% from last month", True, "$")
with kpi_cols[1]:
    kpi_card("Total Sales", "1,247", "↑ 8.3% from last month", True, "🛒")
with kpi_cols[2]:
    kpi_card("Products", "342", "↓ 2.1% from last month", False, "📦")
with kpi_cols[3]:
    kpi_card("Customers", "856", "↑ 15.2% from last month", True, "👥")
st.markdown('</div>', unsafe_allow_html=True)

# ======================
# LOWER SECTIONS
# ======================
left, right = st.columns((2, 2), gap="large")

with left:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">📈 Top Performing Products</div>
            <div class="subtext">Your best sellers this month</div>
            <div class="rank-row">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div class="chip">1</div>
                    <div><div>Coca-Cola Classic 12oz Cans (24-pack)</div>
                        <div class="muted">156 sales • $4,680</div>
                    </div>
                </div>
                <div class="chip">23 in stock</div>
            </div>
            <div class="rank-row">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div class="chip">2</div>
                    <div><div>Pepsi Cola 12oz Cans (12-pack)</div>
                        <div class="muted">121 sales • $2,420</div>
                    </div>
                </div>
                <div class="chip">18 in stock</div>
            </div>
            <div class="rank-row">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div class="chip">3</div>
                    <div><div>Sprite Lemon-Lime 16oz Bottles (12-pack)</div>
                        <div class="muted">98 sales • $2,130</div>
                    </div>
                </div>
                <div class="chip">42 in stock</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="card">
            <div class="section-title">📦 Low Stock Alerts</div>
            <div class="subtext">Products that need restocking</div>
            <div style="margin-top:12px;">
                <div style="margin-bottom:6px; font-weight:600;">Dr Pepper 12oz Cans (6-pack) <span class="chip" style="background:#2a0f12; border-color:#3e161a; color:#ffb3b5;">8 left</span></div>
                <div class="progress"><span style="width: 20%;"></span></div>
            </div>
            <div style="margin-top:18px;">
                <div style="margin-bottom:6px; font-weight:600;">Fanta Orange 12oz Cans (12-pack) <span class="chip">36 left</span></div>
                <div class="progress"><span style="width: 45%;"></span></div>
            </div>
            <div style="margin-top:18px;">
                <div style="margin-bottom:6px; font-weight:600;">Mountain Dew 16oz Bottles (6-pack) <span class="chip">22 left</span></div>
                <div class="progress"><span style="width: 28%;"></span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Floating assistant
st.markdown(
    """
    <div class="fab">💬 Chat with AVA <span class="muted">AI insights</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

