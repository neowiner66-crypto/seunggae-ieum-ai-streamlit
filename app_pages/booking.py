from datetime import date
from uuid import uuid4

import streamlit as st

st.title("상담 신청")
st.write("상담 준비에 필요한 최소 정보만 입력해 주세요.")
st.warning(
    "현재 공개 MVP는 서버에 상담 정보를 저장하거나 이메일로 전송하지 않습니다. "
    "주민등록번호, 계좌번호, 재무자료, 계약서, 기술도면 등 민감정보를 입력하지 마세요.",
    icon=":material/privacy_tip:",
)

default_topic = st.session_state.get("diagnosis_result") or "기업승계"
topics = ["기업승계", "매각 검토", "기업 개선", "세무·법률 준비", "기타"]
if default_topic not in topics:
    default_topic = "기업승계"

with st.form("booking_form"):
    topic = st.selectbox("상담 분야", topics, index=topics.index(default_topic))
    contact_method = st.segmented_control("선호 연락 방법", ["이메일", "전화"])
    name = st.text_input("성함", max_chars=30)
    email = st.text_input("이메일", placeholder="name@example.com")
    phone = st.text_input("전화번호", placeholder="010-0000-0000")
    company = st.text_input("회사명 (선택)", max_chars=80)
    message = st.text_area("문의 내용", max_chars=1000, placeholder="현재 고민과 확인하고 싶은 내용을 적어 주세요.")
    consent = st.checkbox("상담 준비를 위한 개인정보 처리 안내를 확인했습니다.")
    submitted = st.form_submit_button("상담 요청 확인", type="primary", icon=":material/send:")

if submitted:
    contact_value = email.strip() if contact_method == "이메일" else phone.strip()
    if not contact_method or not name.strip() or not contact_value or not message.strip() or not consent:
        st.error("필수 항목과 개인정보 확인 항목을 모두 입력해 주세요.", icon=":material/error:")
    else:
        request_id = f"SG-{date.today():%Y%m%d}-{uuid4().hex[:6].upper()}"
        st.session_state.inquiry = {
            "request_id": request_id,
            "received_at": date.today().isoformat(),
            "topic": topic,
            "name": name.strip(),
            "company": company.strip(),
        }

if st.session_state.inquiry:
    inquiry = st.session_state.inquiry
    st.success("상담 요청 내용을 확인했습니다.", icon=":material/check_circle:")
    with st.container(border=True):
        st.subheader("접수 확인")
        st.write(f"요청번호: `{inquiry['request_id']}`")
        st.write(f"작성일: {inquiry['received_at']}")
        st.write("공개 MVP에서는 실제 전송되지 않습니다. 정식 상담은 아래 이메일로 문의해 주세요.")
        st.link_button("이메일로 상담 문의", "mailto:neowiner66@gmail.com", icon=":material/mail:")

