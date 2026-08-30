import streamlit as st

QUESTIONS = [
    ("succession", "가업을 이어받을 후보자가 정해져 있습니까?"),
    ("intent", "대표자가 5년 안에 경영 일선에서 물러날 계획이 있습니까?"),
    ("finance", "최근 3년의 재무자료가 체계적으로 정리되어 있습니까?"),
    ("process", "핵심 기술과 생산 노하우가 문서화되어 있습니까?"),
    ("governance", "주주·가족 간 승계 방향에 대한 공감대가 있습니까?"),
    ("valuation", "기업가치 평가나 매각 가능성을 검토한 적이 있습니까?"),
    ("tax", "상속·증여·양도 관련 세무 검토를 받은 적이 있습니까?"),
    ("dependency", "대표자 개인에게 영업·기술 의사결정이 집중되어 있습니까?"),
]

st.title("AI 기업승계 자가진단")
st.write("현재 상황에 가장 가까운 답을 선택하세요. 회사명과 대표자명은 필요하지 않습니다.")

with st.form("diagnosis_form"):
    answers = {}
    for key, question in QUESTIONS:
        answers[key] = st.segmented_control(
            question,
            ["예", "아니오", "잘 모르겠습니다"],
            key=f"q_{key}",
            persist_state="session",
        )
    submitted = st.form_submit_button("결과 보기", type="primary", icon=":material/analytics:")

if submitted:
    missing = [question for (key, question) in QUESTIONS if answers[key] is None]
    if missing:
        st.error("모든 질문에 답해 주세요.", icon=":material/error:")
    else:
        succession_score = sum(
            answers[key] == "예" for key in ["succession", "intent", "governance", "tax"]
        )
        improvement_score = sum(
            answers[key] == "아니오" for key in ["finance", "process"]
        ) + (answers["dependency"] == "예")
        if succession_score >= 3 and improvement_score >= 2:
            result = "통합 상담"
        elif succession_score >= 3:
            result = "승계 우선"
        elif improvement_score >= 2:
            result = "기업 개선 우선"
        else:
            result = "추가 확인 필요"
        st.session_state.diagnosis_answers = answers
        st.session_state.diagnosis_result = result

if st.session_state.diagnosis_result:
    with st.container(border=True):
        st.subheader(f"진단 결과: {st.session_state.diagnosis_result}")
        guidance = {
            "통합 상담": "경영 체질 개선과 승계 계획을 함께 설계하는 것이 좋습니다.",
            "승계 우선": "후보자, 지분, 세무, 일정 중심으로 승계 로드맵을 먼저 준비하세요.",
            "기업 개선 우선": "재무·업무 프로세스와 대표자 의존도를 먼저 정리하세요.",
            "추가 확인 필요": "현재 정보만으로 우선순위를 정하기 어려워 전문가 확인이 필요합니다.",
        }
        st.write(guidance[st.session_state.diagnosis_result])
        st.warning(
            "이 결과는 일반적인 상담 준비 안내입니다. 지원금 선정, 기업 매매 성사, "
            "기업가치 상승 또는 법률·세무 결과를 보장하지 않습니다.",
            icon=":material/warning:",
        )
        if st.button("이 결과로 상담 신청", type="primary", icon=":material/calendar_month:"):
            st.switch_page("app_pages/booking.py")

