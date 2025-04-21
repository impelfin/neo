# Ollama Web Interface PRD

## 1. 개요

Ollama Web Interface는 Ollama API 및 서비스와 상호작용할 수 있는 간단한 웹 인터페이스입니다. Node.js 기반의 백엔드와 HTML5, CSS, JavaScript를 이용한 프론트엔드로 구성되며, MVC(Model-View-Controller) 패턴을 최대한 단순하게 적용합니다.

## 2. 목표

- Ollama API를 웹에서 손쉽게 사용할 수 있도록 지원
- 최소한의 디렉토리 구조와 코드로 빠른 개발 및 유지보수 가능
- 직관적이고 반응성이 좋은 UI 제공

## 3. 주요 기능

- Ollama API와의 연동(예: 텍스트 생성, 모델 관리 등)
- 입력 폼을 통한 사용자 요청 전송 및 결과 표시
- 요청 및 응답 로그(간단한 리스트 형태)

## 4. 기술 스택

- 백엔드: Node.js (Express)
- 프론트엔드: HTML5, CSS, JavaScript
- 구조: 단순 MVC 패턴
- 서버 포트: **8000번 포트 사용**

## 5. 디렉토리 구조 (예시)

```
ollama/
  ├── PRD.md
  ├── app.js           # 메인 서버 파일
  ├── controllers/     # 컨트롤러 (API 연동, 라우팅)
  ├── models/          # 모델 (필요 최소화)
  ├── views/           # HTML, CSS 파일
  └── public/          # 정적 파일(이미지, JS, CSS)
```

## 6. 화면 설계

- **메인 화면**: Ollama API 요청 입력 폼, 결과 출력 영역, 요청/응답 로그
- **에러/로딩 처리**: 단순 메시지 혹은 인디케이터

## 7. API 연동 예시

- POST `/api/generate` : 텍스트 생성 요청
- GET `/api/models` : 사용 가능한 모델 목록 조회

## 8. 일정

- PRD 작성: 2025-04-20
- 개발 시작: 2025-04-20
- 프로토타입: 2025-04-20
- 피드백 및 개선: 2025-04-23~

## 9. 기타

- 최대한 간단한 구조와 코드 지향
- 향후 기능 확장 고려(예: 사용자 인증 등)

---
