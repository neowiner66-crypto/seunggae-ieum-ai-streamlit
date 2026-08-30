import streamlit as st

st.title("기업승계 컨설팅 서비스")
st.write("기업의 상황에 맞춰 개선, 승계, M&A 검토를 체계적으로 준비합니다.")

services = [
    ("기업승계 로드맵", "승계 후보, 지분 구조, 경영 이양 일정과 핵심 과제를 정리합니다."),
    ("M&A·매각 준비", "매각 목적, 준비 자료, 기업가치에 영향을 주는 항목을 점검합니다."),
    ("기업 체질 개선", "재무 투명성, 업무 표준화, 대표자 의존도와 기술 전수 체계를 살핍니다."),
    ("세무·법률 사전 점검", "전문가 상담 전에 확인할 질문과 자료를 정리합니다."),
]
for title, body in services:
    with st.container(border=True):
        st.subheader(title)
        st.write(body)

st.info("개별 법률·세무 판단은 자격을 갖춘 전문가의 검토가 필요합니다.", icon=":material/gavel:")

