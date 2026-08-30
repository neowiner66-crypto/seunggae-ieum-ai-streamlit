import streamlit as st

st.title("상담 사례 예시")
st.caption("아래 내용은 이해를 돕기 위한 가상의 예시이며 실제 기업명이나 성과가 아닙니다.")

cases = [
    ("금속가공업 · 가족 승계 검토", "후계 후보의 역할과 대표자 권한 이양 순서를 정리하고 세무 전문가 상담 항목을 준비했습니다."),
    ("산업부품업 · 매각 가능성 검토", "재무자료와 거래 의존도를 점검하고 매각 전 개선 과제를 우선순위로 정리했습니다."),
    ("주조업 · 통합 상담", "현장 기술 문서화와 승계 일정을 병행하는 단계별 준비안을 검토했습니다."),
]
for title, body in cases:
    with st.container(border=True):
        st.subheader(title)
        st.write(body)
        st.badge("상담 사례 예시", color="blue")

