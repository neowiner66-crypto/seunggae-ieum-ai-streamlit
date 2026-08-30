import streamlit as st

st.title("승계 이음 AI 소개")
st.write(
    "오랜 시간 축적된 제조기업의 기술과 관계, 운영 경험이 다음 세대까지 이어지도록 "
    "AI 기반 진단과 전문가 상담 준비를 제공합니다."
)

with st.container(border=True):
    st.subheader("운영 및 상담")
    st.write("강덕환")
    st.link_button("neowiner66@gmail.com", "mailto:neowiner66@gmail.com", icon=":material/mail:")

st.header("개인정보 및 이용 안내")
st.markdown(
    "- 이 공개 버전은 입력 내용을 서버 데이터베이스에 저장하지 않습니다.\n"
    "- 브라우저 탭을 닫거나 서버가 다시 시작되면 입력 내용이 사라질 수 있습니다.\n"
    "- 실제 상담 접수 기능을 활성화하기 전 수집 목적, 보유 기간, 파기 절차를 확정해야 합니다.\n"
    "- 본 서비스의 진단은 일반 정보이며 법률·세무·투자 자문을 대신하지 않습니다."
)

