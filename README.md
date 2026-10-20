# GitHub AI 트렌드 2026-10-20 (Daily)

Daily 트렌딩 12개 중 AI 관련 11개

## 분석

- 오늘 상승폭 1위는 Claude Code 기반 구직 프레임워크 MadsLorentzen/ai-job-search(+3,856, streak 1)로, 2위 stablyai/orca(+1,590)보다 두 배 넘게 올랐습니다.
- 새로 진입(streak 0)한 저장소는 금융 파운데이션 모델 shiyu-coder/Kronos(+363), LLM 입력 압축 도구 headroomlabs-ai/headroom(+310), anthropics/claude-code(+167) 세 곳입니다.
- 이전 리포트에 가장 자주 나온 저장소는 HKUDS/CLI-Anything(streak 3, +606)와 ruvnet/ruflo(streak 2, +564)로, 소프트웨어를 에이전트용으로 바꾸거나 여러 에이전트를 묶어 돌리는 도구입니다.
- 코딩 에이전트 본체와 작업 환경이 함께 올랐습니다 — 에이전트 작업 공간 stablyai/orca(+1,590), 별 217,800개의 오픈소스 코딩 에이전트 anomalyco/opencode(+1,311), anthropics/claude-code(+167).
- 에이전트의 컨텍스트를 아끼는 도구도 나란히 올랐습니다 — 에이전트 간 장기 기억·인계 akitaonrails/ai-memory(+666)와 토큰 압축 headroomlabs-ai/headroom(+310).

## Daily AI 저장소

이전 등장: 이전 리포트(10-02 · 10-07 · 10-08 · 10-12 · 10-13 · 10-14 · 10-15 · 10-16 · 10-19)에 등장한 횟수

| 저장소 | 언어 | 전체 ★ | 오늘 ★ | 이전 등장 | 설명 |
|---|---|---:|---:|---:|---|
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 55,233 | +606 | 3 | 모든 소프트웨어를 에이전트 네이티브로 — 기존 프로그램을 AI 에이전트가 쓸 수 있는 CLI로 바꿔 주는 도구와 CLI-Hub |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 77,180 | +564 | 2 | 원조 에이전트 하네스 — 멀티 에이전트 스웜 배포와 자율 워크플로 조율, 적응형 메모리·자기 학습·벡터 RAG를 갖추고 Claude Code·Codex·Hermes 등과 기본 연동 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 57,233 | +3,856 | 1 | 내 컴퓨터에서 돌아가는 Claude Code 기반 AI 구직 프레임워크 — 채용 공고 평가, 이력서 맞춤 수정, 자기소개서 작성, 면접 준비까지 포크해서 직접 소유 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 217,800 | +1,311 | 1 | 오픈소스 코딩 에이전트 — 터미널에서 쓰는 AI 코딩 도구 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 11,339 | +666 | 1 | 코딩 에이전트 CLI용 장기 기억 솔루션 — 서로 다른 에이전트 제품 간 작업 인계를 도와줌 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 139,715 | +1,011 | 1 | 가장 강력하고 모듈화된 디퓨전 모델 GUI·API·백엔드 — 그래프·노드 인터페이스와 빠른 로컬 추론 엔진 |
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 98,268 | +1,590 | 1 | 여러 코딩 에이전트(Grok Bot, Claude Code 등)를 한곳에서 함께 다루는 작업 공간 — 내 구독으로 어떤 코딩 에이전트든 실행, 데스크톱·모바일·원격 런타임 지원 |
| [Kruk2/jasna](https://github.com/Kruk2/jasna) | Python | 2,885 | +498 | 1 | 신경망으로 영상·이미지의 모자이크를 지우는 GPU 가속 복원 도구 — RF-DETR로 영역을 찾고 BasicVSR++·LTX로 복원, 데스크톱 앱과 CLI 제공 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 76,239 | +310 | 0 | 도구 출력·로그·파일·RAG 청크를 LLM에 넣기 전에 압축 — 같은 답을 유지하면서 코딩 에이전트 토큰 20%, JSON은 60~95% 절감, 라이브러리·프록시·MCP 서버로 제공 |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | TypeScript | 152,647 | +167 | 0 | 터미널에서 동작하는 에이전트형 코딩 도구 Claude Code — 코드베이스를 이해하고 반복 작업 실행, 복잡한 코드 설명, git 작업을 자연어 명령으로 처리 |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 41,661 | +363 | 0 | 금융 시장의 언어를 위한 파운데이션 모델 — 캔들차트(K-line) 데이터를 학습한 오픈소스 시계열 모델 |

제외(AI 아님): withmarbleapp/os-taxonomy(초등 교육과정 분류 데이터)

전체 리포트(Weekly 포함): [github_trending_2026-10-20.html](2026-10/github_trending_2026-10-20.html)
