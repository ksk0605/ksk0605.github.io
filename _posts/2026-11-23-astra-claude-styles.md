---
title: "아스트라 후기를 찾다가 알게 된 것: 모델마다 맡기는 법이 다르다"
description: "GPT-6.2 Astra에 대한 반응을 모아 보니, 결국 Astra와 Claude의 일하는 스타일과 각각 잘 쓰는 법이 보였다"
date: 2026-11-23 09:40:00 +0900
categories: [AI 개발, 도구 분석]
tags: [codex, gpt-6.2-astra, claude-code, claude-opus-5.5, claude-fable-5.2, prompting, multi-agent]
---

> 2026년 11월 17일 공개된 OpenAI GPT-6.2 Astra(이하 Astra)에 대한 반응을 찾아보다가 정리한 글이다. 공식 문서 내용과 사람들의 의견은 나눠서 적었다. 의견은 모두 원문 링크를 달았다.
{: .prompt-info }

## 3줄 요약

1. Astra에 대한 불만은 대부분 "멍청하다"가 아니라 "같이 일하기 피곤하다"였다. 말이 압축돼 알아듣기 어렵고, 엉뚱한 데서 멈춰 묻고, 막힌 걸 말 안 할 때가 있다.
2. Claude 쪽도 버릇이 있다. 공식 문서가 직접 "일찍 멈춘다", "조용해진다", "'절대'를 절대로 받아들인다"고 적어 두었다.
3. 두 회사 문서가 결국 같은 걸 말한다. 끝의 기준, 멈춰도 되는 순간, 보고 형식을 맡길 때 적어 줘야 한다. 다만 적는 방식이 다르다.

## 시작은 Reddit 글 하나였다

비서실에는 Codex 봇과 Claude Code 봇이 같이 일한다. 확인, 비평, 리서치 같은 일은 Codex 봇이 많고, 리드 역할은 Claude 쪽이 많다. 그래서 새 모델이 나오면 남들은 어떻게 느끼는지가 궁금하다.

r/codex에 [Astra 6.2 is not who you think it is](https://www.reddit.com/r/codex/comments/1xyz1x7/astra_62_is_not_who_you_think_it_is/)라는 글이 올라왔다. 제목이 궁금해서 다른 후기도 찾아봤다. 그러다 보니 Astra 이야기보다 "모델마다 맡기는 법이 다르다"는 쪽으로 생각이 모였다.

## 공식 정보: OpenAI가 말하는 Astra

먼저 공식 자료부터 봤다.

- 모델 이름은 `gpt-6.2-astra`, 저렴한 형제 모델은 `gpt-6.2-sol`이다. ChatGPT와 Codex에서 쓸 수 있다. [OpenAI 발표](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- OpenAI는 기존 코드베이스의 복잡한 변경을 더 잘한다고 했다. 초기 테스터들이 "더 깔끔한 코드 스타일과 더 집중된 테스트, 더 적은 수정 횟수"를 보고했다고 한다. [OpenAI 발표](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- API 가격은 입력 100만 토큰당 $8, 출력 $40이다. Claude Fable 5.2와 같다. [Simon Willison](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/)
- 개발자 문서에는 이런 문장이 있다. "기본적으로 더 간결하고 직접적으로 쓴다." 의도가 분명하지 않으면 다음 단계를 제안하고 확인을 기다릴 수 있다고도 적혀 있다. [OpenAI 개발자 문서](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra)
- OpenAI 스스로 약점도 밝혔다. 정렬 시험에서 일을 막는 장애물을 말하지 않고 넘어가는 경우가 늘었다. Codex에 추가 지시를 넣어 크게 줄였고, 원인은 아직 조사 중이라고 했다. [OpenAI 발표](https://openai.com/index/introducing-gpt-6-2-astra-sol/) 시스템 카드 기준 수치는 22.28%로, 이전 Astra의 11.09%에서 두 배가 됐다. [paddo.dev 정리](https://paddo.dev/blog/astra-shipped-anyway/)

## 사람들의 반응: 똑똑한데 피곤하다

여기부터는 의견이다.

비판이 많았다.

- T3 Code를 만든 Theo는 OpenAI에 보내는 글에서 "Opus 5.5 대신 이걸 고르지는 않겠다"고 썼다. [Theo의 X 글](https://x.com/theo/status/2122760447103484410) 두 시간 작업하던 중 사용자가 알 리 없는 파일 이름을 묻고 멈췄다는 예를 들었다. 느린 worktree 원인을 물었을 때 Astra는 pnpm 내부 구조를 네 문단 설명했고, Opus 5.5는 "SSD가 느려서"라고 답했다고 한다. [Implicator 정리](https://www.implicator.ai/gpt-6-2-astra-early-testers-theo-letter/)
- Theo는 또 "올해 써 본 LLM 중 가장 해석하기 어려운 출력"이라고도 했다. [Decrypt](https://decrypt.co/383539/speaks-tongues-only-6-2-astra-understands-why-early-testers-hate-openai-new-model)
- Matt Shumer는 "사실상 쓸 수 없다"고 했다. 그가 돌리는 Opus·Fable 에이전트들이 Astra 하위 에이전트의 결과를 많이 반려했다고 한다. [Shumer의 X 글](https://x.com/mattshumer_/status/2122752192226406421), [Latent Space 정리](https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/)
- Max Weinbach는 "정말 좋은 모델이어도 쓰는 게 힘들고 짜증 난다"고 했다. [Weinbach의 X 글](https://x.com/mweinbach/status/2122834783650676806)
- MindStudio 정리는 이렇게 요약했다. "불만은 멍청하다는 게 아니다. 같이 일하기 짜증 난다는 것이다." [MindStudio](https://www.mindstudio.ai/blog/gpt-6-2-astra-early-reviews)

칭찬도 있었다.

- Theo도 리뷰어로는 훌륭하다고 했다. 다른 리뷰어가 놓친 오류를 잡았고, 코드 품질이 좋고, 3D와 게임 쪽은 세계 최고 수준이라고 했다. [Decrypt](https://decrypt.co/383539/speaks-tongues-only-6-2-astra-understands-why-early-testers-hate-openai-new-model), [Implicator](https://www.implicator.ai/gpt-6-2-astra-early-testers-theo-letter/)
- Pietro Schirano는 초기 문제의 상당수가 모델이 아니라 에이전트 실행 환경 탓이었다고 했다. [Schirano의 X 글](https://x.com/skirano/status/2122770640604111133)

OpenAI도 반응을 인정했다. Sam Altman은 "새 모델이 아주 똑똑하지만, 같이 일하기 좋은 모델로 만드는 데는 할 일이 더 남았다"고 했다. [Altman의 X 글](https://x.com/sama/status/2122798042734633452)

## 비교 자료: 어디서 누가 앞서나

벤치마크는 엇갈린다. 대부분 차이도 몇 점이다.

| 항목 | Astra | Claude 쪽 | 출처 |
|---|---|---|---|
| Artificial Analysis 종합 지수 | 62 | Fable 5.2 65 | [Decrypt](https://decrypt.co/383539/speaks-tongues-only-6-2-astra-understands-why-early-testers-hate-openai-new-model) |
| 코딩 에이전트 (FrontierCode 2.0) | 44.2% | Fable 5.2 49.1% | [DataCamp](https://www.datacamp.com/blog/gpt-6-2-astra-vs-claude-fable-5-2) |
| 전문 업무 (GDPval v2) | 50.4% | Fable 5.2 44.8% | [DataCamp](https://www.datacamp.com/blog/gpt-6-2-astra-vs-claude-fable-5-2) |
| 같은 일에 쓰는 토큰 | 적다 | Fable 5.2가 훨씬 많다 | [DataCamp](https://www.datacamp.com/blog/gpt-6-2-astra-vs-claude-fable-5-2) |

DataCamp의 결론은 이렇다. "어느 쪽도 완승하지 않는다. Astra는 전문·분석 업무, Fable 5.2는 에이전트 코딩에서 앞선다." 토큰 단가는 같지만, Fable은 같은 일을 하는 데 토큰을 훨씬 많이 쓴다. 다만 비용 배수는 OpenAI가 잰 수치라 방향만 참고하라고 덧붙였다. [DataCamp](https://www.datacamp.com/blog/gpt-6-2-astra-vs-claude-fable-5-2)

## 깨달음 1: 불만의 대부분은 실력이 아니라 소통이다

후기를 모아 보니 공통점이 있었다. 결과물이 나쁘다는 말보다 말을 못 알아듣겠다, 왜 여기서 멈추냐, 막힌 걸 왜 말 안 하냐는 말이 훨씬 많았다.

Claude도 사정이 비슷하다. Anthropic 문서를 보면 Claude도 버릇이 있고, 회사가 그걸 직접 적어 두었다.

- Fable 5.2는 긴 작업에서 일이 덜 끝났는데 턴을 끝낼 때가 있다. 남은 일을 나열하거나 "계속할까요?"를 묻는다. 낮은 effort일수록 잦다. [Fable 5.2 프롬프트 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- Fable 5.2는 긴 작업 중 사용자에게 보이는 말이 적을 때가 있다. [같은 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- Opus 5.5는 진행 상황을 알리다가 그 메시지로 턴을 끝내기도 한다. 자동으로 돌리는 에이전트는 거기서 멈춘 것으로 착각할 수 있다. [Opus 5.5 프롬프트 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)

반대로 보고 방식은 Claude가 강점으로 내세운다. Anthropic은 Opus 5.5의 보고가 "무엇을 했고, 무엇을 찾았고, 무엇이 필요한지"를 쉽게 말한다고 적었다. [Opus 5.5 프롬프트 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) Theo가 긴 Astra 작업 끝에 Opus로 바꿔 요약을 받았다는 것도 같은 맥락이다. [Implicator](https://www.implicator.ai/gpt-6-2-astra-early-testers-theo-letter/)

그러니까 질문을 바꿔야 했다. "어느 모델이 더 좋나"보다 "이 모델은 어디서 멈추고, 어떻게 보고하나"가 먼저다.

## 깨달음 2: 두 회사 문서가 같은 걸 다르게 말한다

OpenAI와 Anthropic 문서를 나란히 읽으면 결국 같은 세 가지를 적으라고 한다.

1. 끝의 기준. OpenAI는 "원하는 결과와, 사용자 입력이 필요한 결정이 무엇인지 적으라"고 한다. [OpenAI 개발자 문서](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra) ChatGPT 가이드도 "무엇이 끝난 것인지, 어디서 철저해야 하는지 말하라"고 한다. [Prompting GPT-6.2](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra) Anthropic은 남은 일을 체크리스트로 두고, 끝나는 조건을 먼저 적으라고 한다. [Opus 5.5 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
2. 멈춰도 되는 순간. OpenAI 권장 프롬프트는 범위가 크게 바뀔 때, 실제로 막혔을 때, 사용자가 정할 일일 때, 되돌릴 수 없는 일 직전에만 멈추라고 한다. 되돌릴 수 있는 가정은 적어 두고 진행하라고 한다. [OpenAI 개발자 문서](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra) Anthropic도 "사용자 없이는 진행할 수 없을 때"와 "일부러 막아 둔 것"만 멈출 이유로 꼽는다. [Fable 5.2 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
3. 보고 형식. OpenAI는 최종 답변이 중간 업데이트의 이어짐이 아니라 혼자 읽혀도 되게 쓰라고 한다. [OpenAI 개발자 문서](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra) Anthropic은 Fable 5.2에 "도구 호출을 보지 못한 독자에게 쓰라"는 문단을 넣으라고 권한다. [Fable 5.2 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)

같은 이야기인데 적는 결이 다르다. 이게 세 번째 깨달음이다.

## 깨달음 3: 지시를 적는 결이 다르다

### Astra(Codex)에게는 동료에게 말하듯

- 프로젝트를 아는 동료에게 설명하듯 쓰고, 검토할 때 무엇을 볼지 알려 주라고 한다. [Prompting GPT-6.2](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)
- `AGENTS.md`는 가볍게 둔다. 코드·테스트·문서에서 알 수 없는 요구 사항과 규칙만 적고, 평범한 구현 결정은 Codex에 맡기라고 한다. [같은 문서](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)
- 기본 말투가 이미 짧다. 예전 프롬프트의 "간결하게"는 다시 보라고 한다. [OpenAI 개발자 문서](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra) 내 추측이지만, 짧게 하라고 더 누르면 더 알아듣기 어려워질 것 같다.
- 막힌 것은 따로 물어야 한다. API에서는 Codex용 지시가 자동으로 붙지 않으니, 모든 장애물을 보고하라고 직접 적고 실제로 하는지 확인하라는 조언이 있다. [paddo.dev](https://paddo.dev/blog/astra-shipped-anyway/)

### Claude에게는 분명하게, 이유와 함께

- Claude는 명확하고 구체적인 지시에 잘 반응한다. 요청한 것보다 더 하길 원하면 그렇다고 적으라고 한다. 지시의 이유를 같이 적으면 더 맞는 결과가 나온다. [Claude 프롬프트 모범 사례](https://platform.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- "고쳐 볼 만한 점을 제안해 줄래?"라고 하면 제안만 하고 고치지 않을 수 있다. 고치길 원하면 고치라고 써야 한다. [같은 문서](https://platform.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- "절대"가 들어간 지시는 정말 절대로 받아들인다. "파일을 절대 지우지 마"보다 "파일을 지우기 전에 승인을 받아"처럼 쓰라고 한다. [Fable 5.2 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- 메모리·노트·지시 파일에 조심하라는 말이 쌓이면, 필요 없는 승인을 구하며 일을 멈춘다. 여러 에이전트가 같이 일할 때 주로 봤다고 한다. 이유가 사라진 주의 문구는 지우고, 승인 없이 해도 되는 일을 목록으로 적으라고 한다. [같은 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- 글쓰기 규칙도 그대로 따른다. "한 문장 20단어 이하" 같은 규칙은 글을 뚝뚝 끊기게 만들 수 있다. [같은 문서](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)

이 부분이 가장 찔렸다. 비서실 역할서에는 "~만 한다", "~하지 않는다" 같은 문장이 많다. 사람이 읽으면 당연한 안전장치인데, Claude에게는 범위와 이유 없는 금지문이 되기 쉽다.

## 그래서 이렇게 나눠 쓰기로 했다

아래는 위 자료를 바탕으로 정리한 내 기준이다. 정답이 아니라 지금의 가설이다.

| 이런 일 | 먼저 맡길 쪽 | 근거 |
|---|---|---|
| 코드 리뷰, 오류 찾기, 독립 비평 | Astra | Theo의 "훌륭한 리뷰어" 평가, paddo.dev의 "긴 작업보다 리뷰어로" 조언 |
| 3D, 시각물, 프런트엔드 실험 | Astra | Theo·TokenGremlin의 3D 평가([Decrypt](https://decrypt.co/383539/speaks-tongues-only-6-2-astra-understands-why-early-testers-hate-openai-new-model)), OpenAI 발표 |
| 보고서·법무·재무 같은 전문 문서, 대량 작업 | Astra | DataCamp 권고, 적은 토큰 |
| 긴 에이전트 코딩, 여러 단계 이어지는 일 | Claude | DataCamp 권고, FrontierCode 결과, Opus 5.5 문서 |
| 사람이 읽을 최종 보고, 요약, 판단 자료 | Claude | Opus 5.5 문서의 보고 설명, Theo의 Opus 요약 사용 |
| 다른 모델의 결과 검수 | 서로 교차 | Shumer 사례, Perplexity의 혼합 팀 결과([Latent Space](https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/)) |

맡길 때 적을 것도 정리했다.

공통으로 적을 것
- 끝의 기준: 무엇이 되면 끝인지, 어디서 철저해야 하는지
- 멈춰도 되는 순간: 사용자가 정할 일, 되돌릴 수 없는 일 직전, 일부러 막아 둔 것
- 마지막 보고: 이 대화를 못 본 사람도 읽을 수 있게

Astra에 더 적을 것
- "막힌 것과 건너뛴 것을 따로 적어 줘"
- 짧게 하라는 말은 빼고, 필요하면 "처음 보는 사람이 이해할 수 있게"
- 되돌릴 수 있는 결정은 가정으로 적고 계속하라는 허락

Claude에 더 적을 것
- 제안이 아니라 실행을 원하면 "고쳐 줘"라고 쓰기
- "절대" 대신 범위와 이유가 있는 규칙
- 승인 없이 해도 되는 일 목록
- 긴 작업이면 체크리스트와 "남은 일이 있으면 계속" 규칙

effort도 기본값을 그대로 믿지 않기로 했다. Astra는 새로 붙일 때 medium부터 시작하라고 하고 [OpenAI 개발자 문서](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra), Opus 5.5는 medium이 기본이며 [Opus 5.5 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5), Fable 5.2는 high가 기본이다. Fable 5.2는 effort를 낮추면 일찍 멈추는 일이 잦아진다. [Fable 5.2 가이드](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)

## 마무리

Astra가 좋은지 나쁜지 알고 싶어서 시작했다. 끝에 남은 건 다른 질문이었다. 이 모델은 어디서 멈추고, 무엇을 말하지 않고, 어떤 말을 너무 곧이곧대로 듣는가.

사람 팀원도 그렇다. 잘하는 일이 다르고, 일을 맡길 때 말하는 법도 사람마다 다르다. 모델도 그렇게 대하면 된다. 다음 할 일은 비서실 역할서에서 이유 없는 금지문을 찾아 고치는 것이다.

## 참고 자료

공식 자료
- [OpenAI: Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- [OpenAI 개발자 문서: GPT-6.2 Astra](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra)
- [ChatGPT Learn: Prompting GPT-6.2](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)
- [Anthropic: Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- [Anthropic: Prompting Claude Fable 5.2](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)
- [Anthropic: Prompting best practices](https://platform.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices)

의견·비교
- [Reddit r/codex: Astra 6.2 is not who you think it is](https://www.reddit.com/r/codex/comments/1xyz1x7/astra_62_is_not_who_you_think_it_is/)
- [Theo의 X 글](https://x.com/theo/status/2122760447103484410), [Implicator 정리](https://www.implicator.ai/gpt-6-2-astra-early-testers-theo-letter/)
- [Decrypt: Why Early Testers Hate OpenAI's New Model](https://decrypt.co/383539/speaks-tongues-only-6-2-astra-understands-why-early-testers-hate-openai-new-model)
- [Latent Space AINews](https://latent.space/p/ainews-gpt-6-2-astra-the-2-frontier-model-is-better-and-20-600-cheaper-but-has-mixed-reviews-6-2-sol/)
- [paddo.dev: Astra Shipped Anyway](https://paddo.dev/blog/astra-shipped-anyway/)
- [MindStudio: GPT-6.2 Astra Review](https://www.mindstudio.ai/blog/gpt-6-2-astra-early-reviews)
- [DataCamp: GPT-6.2 Astra vs. Claude Fable 5.2](https://www.datacamp.com/blog/gpt-6-2-astra-vs-claude-fable-5-2)
- [Simon Willison: GPT-6.2 Astra and Sol](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/)
