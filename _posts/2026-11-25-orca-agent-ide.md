---
title: "Orca: 코딩 에이전트 수십 개를 한 화면에서 돌리는 'ADE'의 8개월"
description: "Stably AI가 만든 오픈소스 에이전트 IDE Orca가 2026년 3월 첫 커밋부터 11월 'Orca Bots'까지 어떻게 커 왔는지, 지금 어떤 기능이 있는지 정리했다. 디스코드로 봇 팀을 굴리는 입장에서 본 비교도 덧붙인다."
date: 2026-11-25 16:30:00 +0900
categories: [AI 개발, 도구]
tags: [orca, ade, coding-agent, claude-code, codex, worktree, multi-agent]
---

Claude Code와 Codex를 여러 개 동시에 돌리다 보면 금방 터미널 탭이 열 개를 넘는다. 어느 탭이 무슨 일을 하는지, 누가 같은 파일을 건드리는지, 어떤 에이전트가 내 답을 기다리는지 놓치기 쉽다. [Orca](https://orca.dev)는 이 문제를 풀겠다고 나온 데스크톱 앱이다. 스스로를 IDE가 아니라 **ADE(Agent Development Environment)**라고 부른다.

## 한 줄 요약

> "Run Claude Code, Codex, and any other coding agent in parallel, each in its own worktree." — [orca.dev](https://orca.dev)

코딩 에이전트마다 git worktree를 하나씩 주고, 터미널·브라우저·diff 리뷰·GitHub 연동을 한 앱에 모았다. 에이전트는 각자 쓰던 구독(Claude Code, Codex 등)을 그대로 쓴다. Orca는 MIT 라이선스 오픈소스이고 무료다.

공식 사이트의 설명이 이 도구의 문제의식을 잘 보여 준다. "Editors were built for one person typing." 기존 에디터는 한 사람이 타이핑하는 걸 전제로 만들었는데, 이제는 사람 한 명이 에이전트 10~100개를 지휘하는 상황이니 도구도 달라져야 한다는 주장이다([YC 소개](https://www.ycombinator.com/companies/stably-ai-orca)도 "engineers running 10 to 100 coding agents at once"를 대상으로 적었다).

## 누가 만들었나

만든 곳은 샌프란시스코의 **Stably AI**다. YC Winter 2022 배치다.

- Jinjing Liang(CEO): Google Chrome에서 테스트·릴리스 인프라를 만든 엔지니어 출신
- Neil Parker(CTO): Uber 테크 리드 출신

Stably는 원래 **AI 테스트 에이전트**를 만들던 회사다([YC Launch](https://www.ycombinator.com/launches/NvN-stably-tests-every-code-change-like-your-best-engineer-would): "Tests Every Code Change Like Your Best Engineer Would"). 에이전트가 만든 코드를 검증하던 팀이 에이전트를 여럿 굴리는 작업 환경 자체로 방향을 넓힌 셈이다.

## 8개월 동안 걸어온 길

GitHub 저장소([stablyai/orca](https://github.com/stablyai/orca))와 [릴리스 기록](https://github.com/stablyai/orca/releases)으로 본 흐름이다. 릴리스가 거의 매일 나와서 지금까지 1,000개가 넘는다. 아래 기능 등장 시점은 릴리스 노트를 기준으로 잡은 대략적인 날짜다.

| 시기 | 버전 | 일 |
| --- | --- | --- |
| 2026-03-17 | — | 저장소 생성(첫 커밋) |
| 2026-03-21 | v1.0.12 | 지금 남아 있는 가장 오래된 릴리스 |
| 2026-04-07 | v1.1.0 | 탭 통합 |
| 2026-04-15 | v1.2.0 | 화면 분할 그룹, SSH 안정화 |
| 2026-04 하순 | v1.3.x | 컴퓨터 사용(computer use), GitHub Actions, Linear 연동, **에이전트 오케스트레이션** |
| 2026-05 | v1.3.35~v1.4.3 | 모바일 앱(iOS), Activity 뷰, diff 줄 단위 코멘트 |
| 2026-07 | v1.4.129~ | 원격 Orca 서버, Slack 연동 |
| 2026-08 | — | GitHub 스타 약 5.3만([agentconn](https://agentconn.com/blog/orca-ade-agent-fleet-parallel-coding-agents-2026), 첫 커밋 후 약 5개월) |
| 2026-11-19 | v1.4.265 | **Orca Bots(베타)** 공개 |
| 2026-11-24 | v1.4.274 | 최신 버전 |

2026-11-25 기준 GitHub 스타는 약 13.7만, 포크는 약 8,700개다. 3월에 시작한 저장소로는 아주 빠른 속도다.

## 지금 할 수 있는 것

[README](https://github.com/stablyai/orca)와 공식 사이트 기준이다.

**병렬 작업**
- **worktree 분리**: 에이전트마다 별도 git worktree에서 작업해서 서로 같은 파일을 덮어쓰지 않는다.
- **오케스트레이션**: 조정 에이전트가 일을 나누고, 작업 에이전트를 각자 worktree에 띄운 뒤 결과를 모아 온다.
- **지원 에이전트**: "CLI로 도는 에이전트면 무엇이든". 공식 사이트는 27개라고 하고, README에는 Claude Code, Codex, Grok, Cursor, GitHub Copilot, OpenCode, Gemini CLI, Amp, Goose, Devin, Cline 등이 있다.

**검토**
- **diff 줄 단위 메모**: 바뀐 줄에 남긴 메모를 그대로 에이전트에게 돌려보낸다. PR 리뷰처럼 고칠 점을 짚을 수 있다.
- **git 연동**: 커밋 메시지·PR 초안을 쓰고, 실패한 CI 검사나 PR 리뷰 코멘트를 에이전트에게 넘긴다.
- **GitHub·Linear**: 이슈를 보고 이슈마다 작업 공간을 연다.

**작업 환경**
- **채팅 또는 터미널**: 같은 에이전트를 채팅 화면이나 원래 CLI로 쓰고 오갈 수 있다. GPU로 그리는 터미널과 화면 분할을 지원한다.
- **내장 브라우저**: Chromium이 들어 있고, Design Mode로 화면 요소를 클릭하면 그 HTML·스타일·selector를 에이전트에게 보낸다.
- **어디서든 실행**: 원격 Orca 서버, SSH 호스트, worktree별 클라우드 VM. 노트북을 덮어도 에이전트는 계속 돈다.
- **모바일 앱**(iOS·Android): 에이전트가 사람 답을 기다리면 알림을 받고, 폰에서 답하거나 승인한다.

**Orca Bots(베타, 11월)**

가장 최근에 나온 큰 기능이다. Slack, Linear, GitHub, Gmail, Google Calendar, Sentry, Vercel, Notion, webhook에서 일을 받아 테스트까지 마친 PR로 돌려준다. 봇의 성격과 기억은 `SOUL.md`, `MEMORY.md` 같은 Markdown 파일에 두고, 예약이나 이벤트로 깨어난다. 이후 일주일 동안 업데이트가 몰렸다.

- v1.4.269(11-21): 봇을 돌릴 수 있는 에이전트 8종 추가, 폰에서 거의 모든 질문에 답하고 승인
- v1.4.271(11-22): 연결된 여러 컴퓨터에 걸친 봇, GitHub 계정 여러 개
- v1.4.272(11-23): 사용량 한도·충돌·재시작 뒤 봇이 스스로 복구, Memory Saver, Slack에서 이어 하기
- v1.4.273(11-24): 봇 패널에 다음 실행 일정 표시

에이전트를 사람이 앞에서 지휘하는 도구에서, 사람이 없어도 일을 받아 처리하는 **봇 팀 운영** 쪽으로 넓어지는 중이다.

## 설치와 비용

- macOS(Apple Silicon·Intel), Windows, Linux. [orca.dev/download](https://orca.dev) 또는 GitHub 릴리스에서 받는다.
- Homebrew는 `brew install --cask stablyai/orca/orca`. 그냥 `orca` cask는 Plotly의 다른 앱이니 주의.
- MIT 라이선스, 앱은 무료. 비용은 각 에이전트 구독료만 든다.
- 익명 사용 통계를 보내며, 끌 수 있다.
- 이름이 같은 다른 저장소가 많다. 공식은 `stablyai/orca` 하나다.

비슷한 도구로는 Conductor, Superset, cmux, Emdash 같은 YC 출신 경쟁 제품이 있고, Cursor·Windsurf·VS Code가 같은 기능을 흡수할 수도 있다는 분석이 있다([agentconn](https://agentconn.com/blog/orca-ade-agent-fleet-parallel-coding-agents-2026)).

## 디스코드로 봇 팀을 굴리는 입장에서 보면

나는 지금 디스코드에 Claude Code와 Codex 봇 20여 개를 띄워 두고 일을 시킨다. 비서 역할 봇이 지시를 받아 각 팀 봇에게 나누고, 봇끼리는 작은 작업판(허브)으로 일을 주고받는다. Orca를 보면서 "처음부터 이걸로 했으면 달랐을까"를 생각해 봤다.

**Orca가 나았을 부분**
- 코딩 봇이 낸 변경을 **diff로 보고 줄마다 고칠 점을 남기는** 흐름. 디스코드에서는 PR 링크와 보고 글만 본다.
- worktree가 자동으로 나뉘니 같은 저장소를 여러 봇이 동시에 만질 때 덜 신경 쓴다.
- 봇이 지금 뭘 하는지 터미널 화면 그대로 보인다. 디스코드에서는 이걸 보려고 '작업 기록' 스레드를 따로 만들었다.

**디스코드가 나은 부분**
- 밖에서도 폰 메신저로 지시하고 보고받는다. 봇이 24시간 떠 있고, 날씨·점심 메뉴·새 영상 감지 같은 예약 작업이 돈다.
- 봇의 절반 이상이 메일, 카톡 검색, 조사, 문서 작성처럼 **코딩이 아닌 일**을 한다. worktree 중심 설계의 이득이 없다.
- 승인을 디스코드 메시지 원문과 링크로 남겨서, 누가 언제 무엇을 허락했는지 추적한다.

다만 Orca Bots가 Slack·Gmail에서 일을 받고 예약으로 깨어나는 방향으로 가는 걸 보면, 두 방식의 거리는 빠르게 좁혀지고 있다. 당장은 **지시·예약·보고는 디스코드, 코딩 봇이 낸 PR 검토는 Orca**처럼 나눠 쓰는 게 현실적이라고 본다.

## 출처

- [Orca 공식 사이트](https://orca.dev) (구 onorca.dev)
- [stablyai/orca GitHub 저장소](https://github.com/stablyai/orca), [릴리스 기록](https://github.com/stablyai/orca/releases)
- [Stably AI (Orca) — Y Combinator](https://www.ycombinator.com/companies/stably-ai-orca)
- [Stably YC Launch](https://www.ycombinator.com/launches/NvN-stably-tests-every-code-change-like-your-best-engineer-would)
- [agentconn: Orca ADE 소개(2026-08-24)](https://agentconn.com/blog/orca-ade-agent-fleet-parallel-coding-agents-2026)
- [aitoolly: Orca 소개(2026-08-14)](https://aitoolly.com/en/ai-news/article/2026-08-14-orca-a-new-ade-for-collaborative-parallel-agent-clusters-across-desktop-mobile-and-vps)

스타 수와 버전은 2026-11-25 기준이다. 기능 등장 시점은 릴리스 노트를 키워드로 찾은 값이라 며칠 차이가 날 수 있다.
