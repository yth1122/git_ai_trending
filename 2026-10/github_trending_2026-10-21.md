# GitHub AI 트렌드 2026-10-21 (Daily)

Daily 트렌딩 13개 중 AI 관련 13개

## 분석

- 오늘 상승폭 1위는 Claude Code 기반 구직 프레임워크 MadsLorentzen/ai-job-search(+3,890, streak 2)로, 2위 cloudflare/security-audit-skill(+1,680)의 두 배가 넘습니다.
- 코딩 에이전트용 스킬이 상위권에 몰렸습니다 — 보안 감사 cloudflare/security-audit-skill(+1,680), 최소 코드 작성 DietrichGebert/ponytail(+1,396), 코드 지식 그래프 Graphify-Labs/graphify(+906).
- 새로 진입(streak 0)한 저장소는 Graphify-Labs/graphify(+906, 별 130,201개), Claude Cowork용 anthropics/knowledge-work-plugins(+262), LLM 추론 엔진 vllm-project/vllm(+98) 세 곳입니다.
- 이전 리포트 등장이 가장 많은 저장소는 ruvnet/ruflo(streak 3, +683)이고, stablyai/orca(+1,559)·anomalyco/opencode(+1,256)·Comfy-Org/ComfyUI(+1,201)가 streak 2로 뒤를 잇습니다.
- 여러 에이전트를 조직처럼 묶어 쓰는 저장소도 함께 올랐습니다 — 에이전트 작업 공간 stablyai/orca(+1,559), 스웜 하네스 ruvnet/ruflo(+683), 역할별 전문 에이전트 모음 msitarzewski/agency-agents(+590).

## Daily AI 저장소

이전 등장: 이전 리포트(10-02 · 10-07 · 10-08 · 10-12 · 10-13 · 10-14 · 10-15 · 10-16 · 10-19 · 10-20)에 등장한 횟수

| 저장소 | 언어 | 전체 ★ | 오늘 ★ | 이전 등장 | 설명 |
|---|---|---:|---:|---:|---|
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 77,823 | +683 | 3 | 원조 에이전트 하네스 — 멀티 에이전트 스웜 배포와 자율 워크플로 조율, 적응형 메모리·자기 학습·벡터 RAG를 갖추고 Claude Code·Codex·Hermes 등과 기본 연동 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 60,481 | +3,890 | 2 | 내 컴퓨터에서 돌아가는 Claude Code 기반 AI 구직 프레임워크 — 채용 공고 평가, 이력서 맞춤 수정, 자기소개서 작성, 면접 준비까지 포크해서 직접 소유 |
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 99,694 | +1,559 | 2 | 여러 코딩 에이전트(Grok Bot, Claude Code 등)를 한곳에서 함께 다루는 작업 공간 — 내 구독으로 어떤 코딩 에이전트든 실행, 데스크톱·모바일·원격 런타임 지원 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 140,729 | +1,201 | 2 | 가장 강력하고 모듈화된 디퓨전 모델 GUI·API·백엔드 — 그래프·노드 인터페이스와 빠른 로컬 추론 엔진 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 218,884 | +1,256 | 2 | 오픈소스 코딩 에이전트 — 터미널에서 쓰는 AI 코딩 도구 |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 34,117 | +1,680 | 1 | 여러 단계로 보안 감사를 수행하는 코딩 에이전트 스킬 — 발견한 문제를 독립적으로 검증하고 기계가 읽을 수 있는 형식으로 출력 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 169,596 | +1,396 | 1 | AI 에이전트가 가장 게으른 시니어 개발자처럼 생각하게 만드는 스킬 — 기존 코드를 재활용해 꼭 필요한 코드만 쓰고, 검증·보안·테스트는 빼지 않음 |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Shell | 162,320 | +590 | 1 | 손안의 완전한 AI 에이전시 — 프론트엔드 전문가부터 Reddit 커뮤니티 담당·현실 검증 담당까지, 각자 성격·프로세스·산출물을 갖춘 전문 에이전트 모음 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 76,740 | +555 | 1 | 도구 출력·로그·파일·RAG 청크를 LLM에 넣기 전에 압축 — 같은 답을 유지하면서 코딩 에이전트 토큰 20%, JSON은 60~95% 절감, 라이브러리·프록시·MCP 서버로 제공 |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 42,340 | +719 | 1 | 금융 시장의 언어를 위한 파운데이션 모델 — 캔들차트(K-line) 데이터를 학습한 오픈소스 시계열 모델 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 130,201 | +906 | 0 | 코드베이스와 문서·SQL 스키마·설정·PDF를 질의 가능한 지식 그래프로 변환 — Claude Code·Cursor·Codex·Gemini CLI용 /graphify 스킬, 로컬 AST 파싱으로 모든 연결에 근거를 달고 벡터 저장소 없이 동작 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 30,780 | +262 | 0 | 지식 노동자가 Claude Cowork에서 쓰도록 만든 오픈소스 플러그인 저장소 — 업무용 플러그인 모음 |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Python | 94,426 | +98 | 0 | 처리량이 높고 메모리를 효율적으로 쓰는 LLM 추론·서빙 엔진 |

제외(AI 아님): 없음

전체 리포트(Weekly 포함): [github_trending_2026-10-21.html](github_trending_2026-10-21.html)
