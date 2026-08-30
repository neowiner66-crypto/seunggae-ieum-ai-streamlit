import streamlit as st

st.set_page_config(
    page_title="승계 이음 AI",
    page_icon=":material/handshake:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.session_state.setdefault("diagnosis_answers", {})
st.session_state.setdefault("diagnosis_result", None)
st.session_state.setdefault("inquiry", None)

pages = [
    st.Page("app_pages/home.py", title="홈", icon=":material/home:", default=True),
    st.Page("app_pages/diagnosis.py", title="AI 자가진단", icon=":material/psychology:"),
    st.Page("app_pages/services.py", title="서비스", icon=":material/factory:"),
    st.Page("app_pages/cases.py", title="상담 사례", icon=":material/article:"),
    st.Page("app_pages/booking.py", title="상담 신청", icon=":material/calendar_month:"),
    st.Page("app_pages/about.py", title="소개", icon=":material/info:"),
]

with st.sidebar:
    st.markdown("### 승계 이음 AI")
    st.caption("전통 제조기업의 다음 세대를 준비합니다.")
    st.markdown("강덕환 · neowiner66@gmail.com")

navigation = st.navigation(pages, position="top")
navigation.run()

