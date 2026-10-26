---
name: trending
description: GitHub trending(daily/weekly)에서 AI 관련 저장소만 골라 한국어로 정리하고 이 저장소의 YYYY-MM/html/에 github_trending_YYYY-MM-DD.html 리포트, YYYY-MM/md/에 Daily 분석 .md를 만들고, README.md를 오늘자 분석으로 갱신한 뒤 git push한다. "/trending", "트렌딩 정리", "github trending 업데이트" 요청 시 사용.
---

# GitHub AI 트렌드 리포트

스크립트: `.claude/skills/trending/trending.py` (저장소 루트에서 아래 명령 그대로 실행)
저장소: 이 저장소 (origin `yth1122/git_ai_trending`, 브랜치 main)

## 절차

1. 수집
   ```
   python .claude/skills/trending/trending.py fetch
   ```
   - github.com/trending daily·weekly를 파싱해 `work/raw.json`에 저장하고 내용을 출력
   - 저장소마다 owner, repo, lang, stars, delta, desc_en, streak(이전 리포트 등장 횟수)

2. 분류·번역·분석 — raw.json의 daily+weekly 모든 저장소를 아래 둘 중 하나에 넣고, Daily 분석을 붙여 `.claude/skills/trending/work/picks.json`을 작성
   ```json
   {
     "ko": { "owner/repo": "한국어 설명" },
     "excluded": { "owner/repo": "짧은 한국어 설명" },
     "analysis": ["분석 항목", "분석 항목"]
   }
   ```
   - 포함 기준: AI 자체를 다루는 프로젝트 — LLM, 에이전트, 코딩 에이전트 스킬·플러그인, MCP, 모델 학습·추론·평가, AI 기반 생성 도구 등. 일반 개발도구, 게임, 일반 앱, GPU 커널 DSL처럼 AI가 핵심이 아니면 제외
   - `ko` 설명: desc_en을 자연스러운 한국어 한 문장으로. "핵심 — 부연" 형태, 고유명사(Claude Code, Codex 등)는 원문 유지. desc_en이 비었거나 모호하면 저장소 README를 WebFetch로 확인
   - `excluded` 설명: 무엇인지 10자 내외 (예: "운동 기록 앱")
   - daily와 weekly에 같은 저장소가 있어도 한 번만 적음
   - `analysis`: Daily AI 저장소만 근거로 3~5개 항목. 오늘 상승폭 상위, 새로 진입한 저장소(streak 0), 이전 등장이 많은 저장소, 여러 저장소에 걸친 공통 주제를 raw.json 수치와 함께 한 문장씩. weekly 데이터와 raw.json에 없는 사실은 쓰지 않음

3. 생성
   ```
   python .claude/skills/trending/trending.py render
   ```
   - `<YYYY-MM>/html/github_trending_<오늘>.html`: `template.html`을 채운 리포트 (daily·weekly)
   - `<YYYY-MM>/md/github_trending_<오늘>.md`: Daily 분석과 Daily AI 저장소 표
   - `README.md`: 오늘자 .md와 같은 내용 (링크만 저장소 루트 기준)
   - 같은 날 다시 실행하면 세 파일 모두 덮어씀
   - "분류되지 않은 저장소" 에러가 나면 picks.json에 그 저장소를 추가하고, "analysis가 없습니다" 에러가 나면 analysis를 채우고 다시 실행

4. 푸시
   ```
   python .claude/skills/trending/trending.py publish
   ```
   - 오늘자 html·md와 README.md만 add해서 커밋 메시지 `<오늘>`로 커밋하고 push (다른 파일은 건드리지 않음)
   - 바뀐 내용이 없으면 커밋은 건너뛰고 push만 실행
   - push가 실패하면 에러를 그대로 보고하고 force push는 하지 않음

5. 보고 — 저장 경로, Daily/Weekly AI 개수, streak 높은 저장소 2~3개, 커밋·푸시 결과를 짧게 알림

## 주의

- stars, delta, streak는 스크립트 값을 그대로 쓴다. 직접 고치지 않는다.
- 디자인 변경은 `template.html`만 수정한다.
- fetch가 "파싱하지 못했습니다"로 실패하면 GitHub 페이지 구조가 바뀐 것이므로 `trending.py`의 `parse()`를 고친다.
