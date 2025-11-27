import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client, Client

# ---------- LOAD ENV ----------
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

# ---------- STREAMLIT PAGE CONFIG ----------
st.set_page_config(
    page_title="GURU • Sidebar Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- BASIC CHECK ----------
if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    st.error(
        "Supabase credentials not found.\n\n"
        "Make sure SUPABASE_URL and SUPABASE_ANON_KEY are set in your .env file."
    )
    st.stop()

# ---------- SUPABASE CLIENT ----------
@st.cache_resource
def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

supabase: Client = get_supabase_client()

# ---------- SESSION HELPERS ----------
def set_session(user, access_token):
    st.session_state["user"] = {
        "id": getattr(user, "id", None),
        "email": getattr(user, "email", None),
    }
    st.session_state["access_token"] = access_token
    st.session_state["is_logged_in"] = True

def clear_session():
    st.session_state["user"] = None
    st.session_state["access_token"] = None
    st.session_state["is_logged_in"] = False

# Initialize keys once
if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False
if "user" not in st.session_state:
    st.session_state["user"] = None
if "access_token" not in st.session_state:
    st.session_state["access_token"] = None

# ---------- LOGIN / SIGNUP UI ----------
def auth_page():
    st.title("Welcome to GURU")
    st.write("Sign in to access your analytics dashboard.")

    tab_login, tab_signup = st.tabs(["Sign In", "Sign Up"])

    # ----- SIGN IN TAB -----
    with tab_login:
        with st.form("login_form"):
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            submitted = st.form_submit_button("Sign In")

        if submitted:
            if not email or not password:
                st.error("Please enter both email and password.")
            else:
                try:
                    res = supabase.auth.sign_in_with_password(
                        {"email": email, "password": password}
                    )
                    if res.user and res.session:
                        set_session(res.user, res.session.access_token)
                        st.success("Signed in successfully.")
                        st.rerun()
                    else:
                        st.error("Invalid credentials.")
                except Exception as e:
                    st.error(f"Sign-in error: {e}")

        st.markdown("---")
        st.caption("Or use your Google account:")
        if st.button("Continue with Google"):
            try:
                res = supabase.auth.sign_in_with_oauth(
                    {
                        "provider": "google",
                        # "options": {"redirect_to": "https://your-app-url"},
                    }
                )
                st.write("Open this link to continue Google sign-in:")
                st.write(res.url)
            except Exception as e:
                st.error(f"Google OAuth error: {e}")

    # ----- SIGN UP TAB -----
    with tab_signup:
        with st.form("signup_form"):
            new_email = st.text_input("Email", key="signup_email")
            new_password = st.text_input(
                "Password", type="password", key="signup_password"
            )
            submitted_signup = st.form_submit_button("Create Account")

        if submitted_signup:
            if not new_email or not new_password:
                st.error("Please enter email and password.")
            else:
                try:
                    res = supabase.auth.sign_up(
                        {"email": new_email, "password": new_password}
                    )
                    st.success(
                        "Account created. Check your email for confirmation (if enabled), "
                        "then sign in from the Sign In tab."
                    )
                except Exception as e:
                    st.error(f"Sign-up error: {e}")

# ---------- MAIN FLOW ----------
if not st.session_state["is_logged_in"]:
    # NOT LOGGED IN → ONLY show auth page, NO sidebar/nav at all
    auth_page()

else:
    # LOGGED IN → sidebar + navigation
    with st.sidebar:
        user = st.session_state.get("user") or {}
        email = user.get("email", "Unknown user")
        st.write(f"Signed in as: {email}")
        if st.button("Log out"):
            clear_session()
            st.rerun()

    pages = {
        "Navigation Bar": [
            st.Page("app_pages/Dashboard.py",           title="Dashboard Home"),
            st.Page("app_pages/Sales_Analytics.py",     title="Sales and Analytics"),
            st.Page("app_pages/Trends_and_Analysis.py", title="Trends and Analysis"),
            st.Page("app_pages/Inventory_Overview.py",  title="Inventory Overview"),
            st.Page("app_pages/Transactions.py",        title="Transactions and Inventory"),
            st.Page("app_pages/Agent.py",               title="AI Insights"),
            st.Page("app_pages/Reports.py",             title="Reports"),
            st.Page("app_pages/AIAgent.py",             title="Another Agent"),
        ]
    }

    st.navigation(pages).run()
