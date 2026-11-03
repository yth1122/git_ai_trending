# GitHub AI 트렌드 2026-11-03 (Daily)

Daily 트렌딩 15개 중 AI 관련 13개

## 분석

- 오늘 상승폭 1위는 pingdotgg/t3code(+3,229)로 5회째 등장이고, 처음 들어온 vercel-labs/agent-desktop(+2,275)과 thedotmack/claude-mem(+1,803)이 뒤를 이었습니다.
- Daily AI 13개 중 5개가 처음 등장했습니다: vercel-labs/agent-desktop, JustVugg/colibri(+675), p-e-w/heretic(+420), karpathy/nanochat(+321), max-sixty/worktrunk(+77).
- thedotmack/claude-mem과 mattpocock/skills(+858)는 이전 리포트에 각각 8번 등장했고 오늘도 상위권을 지켰습니다.
- 가진 장비로 큰 모델을 돌리는 저장소가 함께 올랐습니다. 대형 모델을 로컬에서 서빙하는 FlashML-org/FreeToken(+653)과 MoE 전문가 가중치를 디스크에서 스트리밍하는 JustVugg/colibri(+675)입니다.
- 코딩 에이전트를 지휘하거나 병렬로 돌리는 도구 4개가 같은 날 Daily에 들었습니다: t3code(+3,229), agent-desktop(+2,275), paperclipai/paperclip(+412), worktrunk(+77).

## Daily AI 저장소

이전 등장: 이전 리포트(10-02 · 10-07 · 10-08 · 10-12 · 10-13 · 10-14 · 10-15 · 10-16 · 10-19 · 10-20 · 10-21 · 10-22 · 10-23 · 10-26 · 10-27 · 10-28 · 10-29 · 10-30 · 11-02)에 등장한 횟수

| 저장소 | 언어 | 전체 ★ | 오늘 ★ | 이전 등장 | 설명 |
|---|---|---:|---:|---:|---|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 110,722 | +1,803 | 8 | 모든 에이전트에 세션 간 지속 컨텍스트를 주는 도구 — 세션 중 작업을 기록해 AI로 압축하고 이후 세션에 관련 맥락을 다시 넣어 주며 Claude Code·Codex·Gemini 등을 지원 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 310,207 | +858 | 8 | 실무 엔지니어를 위한 에이전트 스킬 모음 — 작성자의 .agents 디렉터리를 그대로 공개 |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | TypeScript | 41,832 | +3,229 | 4 | 내 컴퓨터의 코딩 에이전트를 조종하는 에이전트 하네스 제어판 — Claude Code·Codex·Cursor·OpenCode 등 기존 구독을 모바일·웹·데스크톱 앱에서 제어 |
| [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | Python | 46,006 | +857 | 4 | 금융 시장의 언어를 위한 파운데이션 모델 — 캔들차트(K-line) 데이터를 학습한 오픈소스 시계열 모델 |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | 33,525 | +1,379 | 2 | Claude Code를 완전한 게임 개발 스튜디오로 바꾸는 구성 — AI 에이전트 49개·워크플로 스킬 72개와 실제 스튜디오 위계를 본뜬 조율 체계 |
| [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | Python | 16,035 | +653 | 1 | 데이터센터급 모델 서빙을 데스크톱으로 — 대형 모델을 로컬에서 빠르고 효율적으로 실행 |
| [kornia/kornia](https://github.com/kornia/kornia) | Python | 12,123 | +412 | 1 | 공간 AI를 위한 기하학적 컴퓨터 비전 라이브러리 — 파이썬 기반 |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TypeScript | 110,377 | +412 | 1 | 업무용 에이전트를 관리하는 오픈소스 앱 — 회사에서 쓰는 여러 에이전트를 한곳에서 운영 |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | 9,573 | +2,275 | 0 | AI 에이전트를 위한 컴퓨터 사용(Computer use) CLI — 에이전트가 데스크톱 화면을 직접 조작하도록 지원 |
| [JustVugg/colibri](https://github.com/JustVugg/colibri) | C | 46,515 | +675 | 0 | 이미 가진 하드웨어로 최전선 MoE 모델을 돌리는 추론 엔진 — 의존성 없는 순수 C 구현으로 전문가(expert) 가중치를 디스크에서 스트리밍 |
| [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | Rust | 10,021 | +77 | 0 | 병렬 AI 에이전트 작업을 위해 설계된 Git worktree 관리 CLI — 에이전트마다 따로 쓸 작업 공간을 만들고 전환 |
| [karpathy/nanochat](https://github.com/karpathy/nanochat) | Python | 59,874 | +321 | 0 | 100달러로 만드는 최고의 ChatGPT — 토큰화부터 학습·추론·웹 UI까지 담은 최소 풀스택 LLM 구현 |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 38,082 | +420 | 0 | 학습 없이 언어 모델을 수정하는 도구 — 검열 제거, 상투적 출력(slop) 억제, 아첨 성향 완화 등 |

제외(AI 아님): D4Vinci/Scrapling(웹 스크래핑 프레임워크) · hyprwm/Hyprland(Wayland 타일링 컴포지터)

전체 리포트(Weekly 포함): [github_trending_2026-11-03.html](../html/github_trending_2026-11-03.html)
