---
title: "Devin Bots 출시: '작업'이 아니라 '결과'를 맡기는 에이전트"
description: "Cognition이 2026-11-17 공개한 Devin Bots 정리 — 무엇이 다르고, 어떻게 쓰고, 얼마이며, 무엇을 조심해야 하나"
date: 2026-11-18 18:10:00 +0900
categories: [AI 소식, AI 개발]
tags: [devin, cognition, coding-agent, devin-bots, multi-agent]
---

> Cognition이 2026년 11월 17일 [Introducing Devin Bots: from tasks to outcomes](https://devin.ai/blog/introducing-devin-bots)를 발표했다. 이 글은 공식 발표·문서·요금표를 읽고 정리한 것이다.
{: .prompt-info }

## 3줄 요약

1. **Devin Bot은 '작업' 대신 '책임'을 맡는 상시 에이전트다.** "결제 화면을 맡아라", "안드로이드 앱을 iOS와 같은 수준으로 유지해라" 같은 목표를 주면, 스스로 일을 쪼개 여러 Devin 세션에 나눠 맡기고 결과를 보고 다음 할 일을 정한다.
2. **사람에게는 판단이 필요한 것만 올라온다.** 결정, PR 검토·머지, 새 권한 요청이 'Needs you' 함에 모인다.
3. **Max(월 $200)와 Teams 요금제부터 쓸 수 있다.** 공식 사례에서는 한 Bot이 44일 동안 PR 1,134개를 머지해 안드로이드 앱을 만들었다.

## 기존 Devin 세션과 무엇이 다른가

지금까지 Devin은 **세션 하나가 작업 하나를 맡아 PR 하나를 여는** 구조였다. Bot은 그 위에 한 층이 더 있다.

| | Devin 세션 | Devin Bot |
|---|---|---|
| 맡기는 것 | 작업 하나("이 버그 고쳐") | 결과·책임("checkout을 맡아") |
| 수명 | 작업이 끝나면 끝 | 계속 살아 있음 |
| 일하는 방식 | 직접 코드 작성 | 하위 세션(child session)을 여러 개 띄워 병렬로 맡기고 결과를 평가 |
| 기억 | 세션 단위 | Bot이 스스로 쓰는 메모리 파일(선호, 정정, 프로젝트 정보) |
| 사람과의 접점 | 세션 채팅 | Bot 전용 채팅 하나 + Needs you 함 |

공식 발표의 정의는 이렇다. Bot은 "자기 기억과 도구를 가지고 여러 Devin을 병렬로 이끄는 상시 에이전트(a persistent agent with its own memory and tools that can lead multiple Devins in parallel)"다.

하위 세션은 각자 자기 머신에서 돌고, 사람이 직접 연 세션과 똑같이 하나씩 열어 볼 수 있다.

## 어떻게 쓰나

### 만들기
- Devin 웹앱 사이드바 **Bots → 새 Bot**. 직접 만들거나 템플릿에서 고른다.
- 공식 템플릿 예: **QA Engineer**(PR마다 브라우저로 테스트), **Data Analyst**(데이터 질문에 쿼리와 차트로 답함). 공개 마켓플레이스는 [devin.ai/bots/templates](https://devin.ai/bots/templates)에 있다.
- 일반 Devin 세션이 "이건 Bot으로 만드는 게 좋겠다"고 제안할 수도 있다. 이때는 사람이 승인해야 만들어진다.
- Bot의 **General 설정에 지시문**을 적는다. Bot이 모든 세션을 시작할 때 이 지시문을 읽는다.

### 말 거는 곳
- Devin 웹앱
- **Slack**: Bot마다 자기 Slack 앱이 생긴다. @멘션하거나 DM을 보내면 된다.
- **iMessage**: 휴대폰에서 문자로 지시할 수 있다.

### 자동 실행 (Automations)
- 일정에 맞춰 돌거나, 연결된 도구에서 일이 생기면 실행된다.
- 연결 도구: Slack, GitHub, Linear 등. 요금표 기준으로는 Slack·Teams, Linear·Jira, GitHub·GitLab·Bitbucket, 사내 git까지 지원한다.
- Bot이 자동화를 직접 만들 수 있다. 필요하면 승인을 요청하고, 사람은 Automations 페이지에서 멈추거나 지울 수 있다.

### Needs you 함
사람이 처리할 것만 모인다.
- **Decision**: 방향 결정
- **Review PR / Merge PR**: PR 검토·머지
- **Permission request**: 새 권한 요청
- **Report / FYI**: 보고와 참고 소식

각 항목은 답하거나, 미루거나, 닫을 수 있다.

## 공식 사례의 숫자

> 아래 숫자는 모두 Cognition이 발표한 수치다. 독립적으로 검증된 결과가 아니다.
{: .prompt-warning }

**Android Bot**
- 2026-09-28에 만들었다. 44일 뒤에 안드로이드 앱이 나왔고, 지금 Google Play 공개 테스트 중이다.
- PR **1,134개** 머지, Kotlin **344,651줄**, 스크린샷 테스트 **2,841개**, 티켓 **1,217개** 처리.
- 담당자가 보낸 메시지는 44일 동안 183개다. PR 6개당 하나꼴이고, 그중 22일은 메시지를 하나도 보내지 않았다.

**Layout Bot**
- 3시간마다 레이아웃 검사를 지켜보는 Bot이다.
- 활동한 3주 동안 PR 159개를 머지했고, 화면 지연을 70% 줄였다.
- 참고로 Cognition 전체에서는 일주일에 PR이 2,000개 넘게 머지된다고 한다.

**게임 스튜디오**
- Bot 20여 개를 조율 Bot 하나("Super Jenny Bot")가 이끈다. Unity, 릴리스, iOS, Android, 테스트를 각각 맡은 Bot들이다.
- 주간 PR이 약 50개에서 1,900개로 늘었고, 매주 릴리스한다.

**고객사 Bilt**: "한 주에 PR 약 1,600개를 머지했다."

## 가격

| 요금제 | 가격 | Bots |
|---|---|---|
| Free | $0 | 없음 |
| Pro | 월 $20 | 요금표 카드에 언급 없음 |
| **Max** | 월 $200 | 포함 |
| **Teams** | 월 $80 + 개발자 좌석당 월 $40 | 포함(최대 100명) |
| Enterprise | 별도 문의 | 포함, Bot 전용 권한 역할 |

Bot이 하는 일은 일반 세션처럼 요금제 사용량에서 빠진다. 초과하면 API 가격으로 추가 구매한다. ([요금표](https://devin.ai/pricing))

## 권한과 보안에서 볼 것

- **새 권한은 먼저 묻는다.** 로그인, 비밀값, 새 세션, 자동화, 네트워크 호스트, 사용량 한도 증가는 승인 카드로 요청한다.
- **연결과 비밀값은 Bot 단위다.** 메시지를 보내는 사람의 계정이 아니라 Bot 자신의 연결을 쓴다. 새 Bot은 공유하기 전까지 비공개다.
- **공유한 Bot은 기억도 공유된다.** Bot을 쓸 수 있는 사람은 누구나 그 Bot이 기억하는 내용을 읽을 수 있다. 민감한 내용을 말할 때 조심해야 한다.
- **보관(Archive)하면** Bot이 멈추고 Slack 앱과 Bot 간 접근이 사라진다. 보관을 풀어도 그 접근은 돌아오지 않는다. **삭제는 되돌릴 수 없다.**
- 공식 발표도 "어떤 시스템에 접근하고, 무엇을 바꿀 수 있고, 언제 지출이나 릴리스에 승인이 필요한지"는 엔지니어가 정한다고 말한다. 권한이 허용되면 Bot이 직접 머지할 수도 있다. 사람 승인이 꼭 필요한 저장소는 **GitHub 브랜치 보호**로 강제해 두는 편이 안전하다.

## 내 생각: 직접 꾸린 에이전트 팀과 비교하면

나는 지금 Mac 한 대에서 Claude Code·Codex 봇 여러 개를 Discord에 붙여 팀처럼 쓰고 있다. 조사 봇, 제품 리드, 구현, QA, 운영 봇이 작업판(허브)으로 일을 주고받는 구조다. Devin Bots를 보고 든 생각을 적어 둔다.

**Devin Bots가 나은 점**
- **운영 부담이 없다.** 봇 재시작, 메시지 유실, 세션 잠금 같은 문제를 내가 직접 고치지 않아도 된다. Mac을 꺼도 클라우드에서 돈다.
- **병렬 하위 세션과 Needs you 함이 기본 기능이다.** 내 쪽은 이걸 직접 만들고 있다.
- **세션마다 자기 머신을 쓴다.** 앱 빌드나 브라우저 테스트처럼 무거운 검증을 동시에 여러 개 돌리기 쉽다.

**직접 꾸린 팀이 나은 점**
- **모델과 도구를 섞을 수 있다.** Claude와 Codex를 섞어 쓰고, 로컬 도구·NAS·Discord를 마음대로 붙인다.
- **승인 규칙을 내 방식대로 세밀하게 정한다.** "DB 변경은 건마다 승인" 같은 규칙이다.
- **비용이 예측된다.** 이미 내고 있는 구독 안에서 돈다.

**시험해 볼 만한 것**
- 저장소 하나에서 **QA Engineer 템플릿**으로 PR마다 브라우저 회귀 테스트를 돌려 본다.
- 또는 **야간 CI 실패를 재현해서 수정 PR까지 만드는 Bot**을 맡겨 본다.
- 그다음 사람이 검토하는 데 든 시간과 추가 비용을 지금 팀과 비교한다.

Lauren Tan의 발표([정리 글](/posts/all-code-is-slop-except-mine/))와 [No AI Slop 선언문](/posts/no-ai-slop-manifesto-ko/)에서 본 관점을 그대로 적용하면 이렇다. **"PR 1,134개"보다 중요한 질문은 그 PR을 누가 어떤 증거로 믿을 수 있게 만들었느냐다.** Devin도 앱 코드와 함께 스크린샷 테스트 2,841개를 쌓았다는 점을 강조한다. 숫자보다 그 검증 구조가 더 볼 만한 대목이다.

## 출처

- [Introducing Devin Bots: from tasks to outcomes](https://devin.ai/blog/introducing-devin-bots) — Cognition, 2026-11-17
- [Devin Docs: Bots](https://docs.devin.ai/work-with-devin/bots)
- [Devin 요금표](https://devin.ai/pricing)
- [Bot 템플릿 마켓플레이스](https://devin.ai/bots/templates)
