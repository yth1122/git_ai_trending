# GitHub AI 트렌드 2026-10-19 (Daily)

Daily 트렌딩 13개 중 AI 관련 13개

## 분석

- 오늘 상승폭 1위는 Claude Code 위에 만든 구직 프레임워크 MadsLorentzen/ai-job-search(+2,213)로, 처음 등장(streak 0)하자마자 정상에 올랐고 로컬 음성 생성 debpalash/VoiceStudio(+2,098)가 근소한 차이로 뒤를 이었습니다.
- Daily AI 저장소 13개 중 8개가 새로 진입(streak 0)했으며, 그중 anomalyco/opencode(+1,417)와 stablyai/orca(+1,146)는 각각 별 216,541개·96,595개의 대형 저장소입니다.
- 이전 리포트에 자주 나온 저장소는 debpalash/VoiceStudio(streak 4), cursor/plugins(streak 3), HKUDS/CLI-Anything(streak 2)로, 음성 생성과 에이전트 확장 도구가 꾸준히 관심을 받고 있습니다.
- 코딩 에이전트 확장 저장소가 세 곳에서 동시에 올라왔습니다 — 공식 디렉터리 anthropics/claude-plugins-official(+1,187), Android 공식 스킬 android/skills(+381, 신규), cursor/plugins(+351).
- 여러 에이전트를 함께 다루는 흐름도 뚜렷해, 에이전트 작업 공간 stablyai/orca(+1,146), 에이전트 간 기억·인계 akitaonrails/ai-memory(+513, 신규), 스웜 하네스 ruvnet/ruflo(+502)가 나란히 올랐습니다.

## Daily AI 저장소

이전 등장: 이전 리포트(10-02 · 10-07 · 10-08 · 10-12 · 10-13 · 10-14 · 10-15 · 10-16)에 등장한 횟수

| 저장소 | 언어 | 전체 ★ | 오늘 ★ | 이전 등장 | 설명 |
|---|---|---:|---:|---:|---|
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 75,270 | +2,098 | 4 | 완전 로컬로 돌아가는 오픈소스 ElevenLabs 대안 — 646개 언어로 음성 복제·음성 디자인·영상 더빙·받아쓰기·전사·오디오북 제작 |
| [cursor/plugins](https://github.com/cursor/plugins) | TypeScript | 12,726 | +351 | 3 | Cursor 플러그인 명세와 공식 플러그인 모음 — Cursor 에이전트를 확장하는 플러그인 저장소 |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Python | 54,572 | +582 | 2 | 모든 소프트웨어를 에이전트 네이티브로 — 기존 프로그램을 AI 에이전트가 쓸 수 있는 CLI로 바꿔 주는 도구와 CLI-Hub |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 42,657 | +1,187 | 1 | Anthropic이 직접 관리하는 공식 Claude Code 플러그인 디렉터리 — 품질이 검증된 플러그인 모음 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 76,500 | +502 | 1 | 원조 에이전트 하네스 — 멀티 에이전트 스웜 배포와 자율 워크플로 조율, 적응형 메모리·자기 학습·벡터 RAG를 갖추고 Claude Code·Codex·Hermes 등과 기본 연동 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 53,059 | +2,213 | 0 | 내 컴퓨터에서 돌아가는 Claude Code 기반 AI 구직 프레임워크 — 채용 공고 평가, 이력서 맞춤 수정, 자기소개서 작성, 면접 준비까지 포크해서 직접 소유 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 216,541 | +1,417 | 0 | 오픈소스 코딩 에이전트 — 터미널에서 쓰는 AI 코딩 도구 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 10,457 | +513 | 0 | 코딩 에이전트 CLI용 장기 기억 솔루션 — 서로 다른 에이전트 제품 간 작업 인계를 도와줌 |
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 96,595 | +1,146 | 0 | 여러 코딩 에이전트(Grok Bot, Claude Code 등)를 한곳에서 함께 다루는 작업 공간 — 내 구독으로 어떤 코딩 에이전트든 실행, 데스크톱·모바일·원격 런타임 지원 |
| [android/skills](https://github.com/android/skills) | Kotlin | 8,754 | +381 | 0 | AI 코딩 에이전트에게 Android 개발 모범 사례를 가르치는 공식 스킬 모음 — Android CLI나 Claude Code·Codex 플러그인으로 설치 |
| [mlabonne/llm-course](https://github.com/mlabonne/llm-course) | - | 84,004 | +81 | 0 | 대규모 언어 모델(LLM) 입문 강좌 — 로드맵과 Colab 노트북 제공 |
| [Kruk2/jasna](https://github.com/Kruk2/jasna) | Python | 2,382 | +115 | 0 | 신경망으로 영상·이미지의 모자이크를 지우는 GPU 가속 복원 도구 — RF-DETR로 영역을 찾고 BasicVSR++·LTX로 복원, 데스크톱 앱과 CLI 제공 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 138,585 | +155 | 0 | 가장 강력하고 모듈화된 디퓨전 모델 GUI·API·백엔드 — 그래프·노드 인터페이스와 빠른 로컬 추론 엔진 |

제외(AI 아님): 없음

전체 리포트(Weekly 포함): [github_trending_2026-10-19.html](2026-10/github_trending_2026-10-19.html)
