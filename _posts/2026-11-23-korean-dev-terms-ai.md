---
title: "트랜잭션을 '거래'라고 부르는 AI: 개발 용어는 어떻게 옮겨야 하나"
description: "AI가 transaction을 '거래', lock을 '잠금'으로 옮겨서 대화가 피곤해졌다. 쿠버네티스·파이썬·Mozilla·카카오 같은 번역팀은 이 문제를 어떻게 풀었는지 모으고, AI 지시문용 용어 규칙으로 정리했다."
date: 2026-11-23 15:00:00 +0900
categories: [AI 개발, 글쓰기]
tags: [ai-writing, localization, korean, terminology, prompt, agents-md]
---

AI와 DB 작업을 이야기하다가 "두 함수는 거래를 연 채 행을 잠그고"라는 문장을 받았다. 거래가 뭐냐고 되물었더니 DB 트랜잭션을 우리말로 옮긴 말이라고 했다. 같은 답 안에서 commit은 '커밋'으로 그대로 썼다. transaction은 '거래', lock은 '잠금', row는 '행'으로 바꿨다.

한국 개발자 중에 트랜잭션을 거래라고 부르는 사람은 거의 없다. 모르는 말을 만나서 한 번 멈추고, 원래 영어가 뭔지 되묻고, 머릿속에서 다시 바꿔 읽어야 했다. 쉽게 쓰려다 오히려 읽기 어려워진 셈이다.

## 왜 이런 일이 생기나

AI에게 "쉬운 우리말로 써라", "외래어를 줄여라" 같은 지시를 주면 이런 일이 생기기 쉽다. 사실 바로 전 글 [쇠냄새 나는 AI 한국어 고치기](/posts/simple-korean-rules/)에서 만든 규칙에도 "영어를 소리대로 적은 말은 우리말로 쓴다"는 항목이 있었다. 이슈, 리스크, 니즈 같은 업무 은어를 겨냥한 규칙이었는데, 개발 용어를 빼 달라는 말이 없었다. 모델 입장에서는 트랜잭션도 '영어를 소리대로 적은 말'이다.

그래서 이 문제를 먼저 오래 고민한 곳들을 찾아봤다. 공식 문서를 한국어로 옮기는 번역팀들이다.

## 번역팀들은 어떻게 정했나

| 곳 | 규칙(원문 인용) | 요점 |
| --- | --- | --- |
| [쿠버네티스 한국어 문서](https://kubernetes.io/ko/docs/contribute/localization_ko/) | "영문 용어를 한글화할 때는 다음의 우선 순위를 따르나, 자연스럽지 않은 용어를 무리하게 선택하지는 않는다." | 한글 표기, 첫 등장 병기, 영어 유지 중 문맥에 맞게 고르고 용어집으로 고정 |
| [Mozilla 한국어 스타일 가이드](https://mozilla-l10n.github.io/styleguides/ko/#용어) | "개발 관련 용어는 개발자들이 일반적으로 쓰는 용어를 사용합니다." | bug는 버그, Ctrl은 Ctrl |
| [카카오디벨로퍼스 문서 가이드](https://developers.kakao.com/docs/ko/documentation-guideline/document-style-open) | "플랫폼, 프로그래밍 언어, 국문으로 표현이 어색한 영문 용어는 영문 그대로 작성합니다." | 익숙한 외래어는 '메서드(Method)'처럼 처음에만 병기 |
| [파이썬 문서 한국어 번역팀](https://github.com/python/python-docs-ko/blob/3.14/.pdk/guide.md#L35) | "용어는 이미 번역된 파일들을 참고해서 일관성을 유지해 주시기 바랍니다." | 공식 용어집 번역어와 원문을 병기, 한 번 정한 말은 계속 유지 |
| [Vite 한국어 번역](https://ko.vite.dev/contributing) | "소스 코드는 주석만 번역하며 … 에러 내용은 번역하지 않습니다." | 검색하고 재현할 때 쓰는 문자열은 원문 그대로 |
| [Microsoft 한국어 스타일 가이드](https://aka.ms/korean-styleguide) | "Use approved terminology from Microsoft language resources where applicable" | 승인된 용어집을 먼저 따른다. 제품 이름은 원어 유지 |

공통점은 두 가지다. 첫째, 우리말로 옮길지 말지를 용어마다 정하고, 그 결정을 용어집에 적어 둔다. 둘째, 기준은 "순우리말인가"가 아니라 "독자가 실제로 그 말을 쓰고 검색하는가"다.

재미있는 점도 있다. Microsoft의 [SQL Server 한국어 문서](https://learn.microsoft.com/ko-kr/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver17)는 transaction을 '트랜잭션', commit을 '커밋'으로 쓰면서 lock은 '잠금'으로 쓴다. 공식 문서와 현업 대화의 말이 다를 수 있다는 뜻이다. 그래서 "무조건 음차"도 정답이 아니다. 내 팀과 내 프로젝트가 쓰는 말이 기준이 된다.

## 반대쪽 사례: 누리사랑방

국립국어원은 2005년 '다듬은 말'로 블로그를 '누리사랑방'으로 바꾸자고 했다. 블루투스를 '쌈지무선망'으로 부르자는 제안도 있었다. 이듬해 국어원 [소식지](https://www.korean.go.kr/nkview/onletter/20061001/print/06.html)에서도 누리사랑방을 널리 알려지지 않은 말로 소개했다. 지금 네이버 도움말도, Windows 설정 화면도 블로그와 블루투스를 쓴다.

반대로 '댓글'은 국어원의 2019년 말뭉치 분석에서 '리플'보다 더 많이 쓰였다. 우리말로 바꾸는 것 자체가 나쁜 게 아니다. 사람들이 실제로 쓰게 된 말이면 좋은 번역이고, 아무도 안 쓰는 말이면 독자만 피곤하다. AI가 만든 '거래'는 누리사랑방 쪽이다.

## AI 지시문에 넣을 규칙

조사한 내용을 AI 지시문(CLAUDE.md, AGENTS.md, 채팅 앱의 개인 설정)에 넣을 수 있게 줄였다.

```text
개발 용어는 한국 개발자가 실제로 쓰는 말 그대로 쓴다.
- 사용자와 프로젝트가 이미 쓰는 표기를 따른다. 용어집이 없으면 DB 문맥의 transaction은 트랜잭션, lock은 락, commit은 커밋으로 쓴다.
- 낯설거나 검색이 필요한 개념은 처음에만 '트랜잭션(transaction)'처럼 병기하고, 이후 같은 말을 유지한다.
- API 이름, 명령어, 오류 문구, 파일 경로, 설정 키는 원문과 대소문자를 그대로 둔다.
- 같은 영어라도 문맥을 따른다. 결제 내역의 transaction은 '거래', DB의 transaction은 '트랜잭션'이다.
- 억지로 우리말을 만들지 않는다.
```

대화 중이라면 "용어는 개발자들이 쓰는 그대로 써줘" 한마디로도 그 대화 안에서는 대부분 돌아온다. 다만 매번 말해야 하므로, 자주 쓰는 도구라면 지시문에 넣어 두는 편이 낫다.

## 지난 규칙도 고쳤다

[지난 글](/posts/simple-korean-rules/)의 SIMPLE_KOREAN 규칙도 고쳤다. "0. 고치지 않는 것"에 개발 용어 항목을 넣었고, 12번 규칙의 대상을 '업무 은어로 쓰는 영어'로 좁혔다. 고친 파일은 [SIMPLE_KOREAN.md](/assets/files/simple-korean-rules/SIMPLE_KOREAN.md)에 있다.

쉬운 글의 기준은 독자다. 개발자에게는 트랜잭션이 쉬운 말이다.

## 출처

- [쿠버네티스 문서 한글화 가이드](https://kubernetes.io/ko/docs/contribute/localization_ko/)
- [Mozilla 한국어 스타일 가이드](https://mozilla-l10n.github.io/styleguides/ko/)
- [카카오디벨로퍼스 문서 스타일 가이드](https://developers.kakao.com/docs/ko/documentation-guideline/document-style-open)
- [python-docs-ko 번역팀 가이드](https://github.com/python/python-docs-ko/blob/3.14/.pdk/guide.md)
- [Vite 한국어 번역 가이드](https://ko.vite.dev/contributing)
- [Microsoft 한국어 스타일 가이드(PDF)](https://aka.ms/korean-styleguide)
- [SQL Server 트랜잭션 잠금 및 행 버전 관리 가이드](https://learn.microsoft.com/ko-kr/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver17)
- [국립국어원 소식지(2006)](https://www.korean.go.kr/nkview/onletter/20061001/print/06.html)
