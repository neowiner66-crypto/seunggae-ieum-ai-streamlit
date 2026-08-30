# 승계 이음 AI · Streamlit

전통 뿌리제조업 대표자가 기업 개선, 기업승계, M&A 검토의 우선순위를 정리하고 전문가 상담을 준비하도록 돕는 공개 MVP입니다.

## 주요 기능

- 8문항 AI 규칙 기반 자가진단
- 기업승계·M&A·기업 개선 서비스 안내
- 가상의 상담 사례 예시
- 상담 신청 내용 확인
- 개인정보 및 법률·세무 면책 안내
- 모바일과 데스크톱을 지원하는 Streamlit 내비게이션

## 공개 MVP의 제한

현재 버전은 상담 입력 내용을 서버나 이메일로 전송하지 않습니다. 입력은 해당 브라우저 세션에서만 유지되며 탭을 닫거나 서버가 재시작되면 사라질 수 있습니다.

실제 고객정보를 받기 전에는 다음 기능을 추가해야 합니다.

1. 사용자 인증과 관리자 권한
2. 업체별 데이터 분리
3. 암호화된 데이터베이스와 접근 기록
4. 개인정보 수집 목적·보유 기간·파기 절차
5. 상담 접수 이메일 또는 CRM 연동

## 로컬 실행

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

macOS/Linux에서는 활성화 명령으로 `source .venv/bin/activate`를 사용합니다.

## Streamlit Community Cloud 배포

1. 이 공개 GitHub 저장소를 Streamlit Community Cloud에 연결합니다.
2. 브랜치는 `main`, 진입 파일은 `streamlit_app.py`로 지정합니다.
3. 현재 버전은 Secrets 설정이 필요하지 않습니다.
4. 배포 후 자가진단과 상담 신청 흐름을 확인합니다.

## 디자인

- Primary: `#1f6f8b`
- Background: `#ffffff`
- Surface: `#f6f7f9`
- Text: `#111827`
- Font: Pretendard / Noto Sans KR

## 운영자

- 강덕환
- neowiner66@gmail.com

## 라이선스

Copyright © 2026 강덕환. All rights reserved.

