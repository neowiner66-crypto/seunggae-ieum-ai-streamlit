import streamlit as st

st.title("기업의 시간과 기술, 다음 세대까지 안전하게 잇습니다.")
st.write(
    "승계 이음 AI는 전통 뿌리제조업 대표자가 기업 개선, 가업 승계, "
    "M&A 검토의 우선순위를 정리하도록 돕는 상담 준비 서비스입니다."
)

with st.container(horizontal=True):
    if st.button("AI 자가진단 시작", type="primary", icon=":material/arrow_forward:"):
        st.switch_page("app_pages/diagnosis.py")
    if st.button("상담 신청", icon=":material/calendar_month:"):
        st.switch_page("app_pages/booking.py")

st.space("large")
st.header("복잡한 승계 준비를 세 단계로 정리합니다")

cols = st.columns(3)
cards = [
    ("1. 현황 진단", "10개 이하의 질문으로 현재 준비 상태와 우선 과제를 확인합니다."),
    ("2. 방향 설계", "기업 개선, 승계, 매각 검토 중 먼저 준비할 방향을 정리합니다."),
    ("3. 전문가 연결", "진단 내용을 바탕으로 필요한 분야의 전문가 상담을 준비합니다."),
]
for col, (title, body) in zip(cols, cards):
    with col.container(border=True):
        st.subheader(title)
        st.write(body)

st.header("신뢰를 우선하는 상담 원칙")
with st.container(border=True):
    st.markdown(
        "- 회사명과 대표자명을 입력하지 않고도 자가진단을 시작할 수 있습니다.\n"
        "- 진단은 의사결정을 돕는 일반 정보이며, 거래 성사나 기업가치 상승을 보장하지 않습니다.\n"
        "- 주민등록번호, 계좌번호, 기술도면, 거래처 정보 등 민감정보는 입력하지 마세요."
    )

st.caption("운영/상담: 강덕환 · neowiner66@gmail.com")

