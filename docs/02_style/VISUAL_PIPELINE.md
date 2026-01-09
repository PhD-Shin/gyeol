---
title: "GYEOL Visual Style - Pipeline"
type: style
locked: true
version: 1.0
last_updated: 2025-01-10
description: "결 비주얼 제작 파이프라인. AI 도구 분업, 샷 라이브러리."
use_when: "비주얼 제작 시, AI 도구 선택 시, 샷 라이브러리 구축 시"
tags: [style, visual, pipeline, ai, midjourney, sora]
related:
  - "[[02_style/VISUAL_EDIT]]"
  - "[[05_execution/TRACK_TEMPLATE]]"
  - "[[PROCESS]]"
---

# VISUAL_PIPELINE — 제작 파이프라인

> **이 문서가 필요한 순간:**
> - 비주얼 제작을 시작할 때
> - AI 도구를 선택할 때
> - 샷 라이브러리를 구축할 때

---

## 핵심 원칙

> **Midjourney는 정체성을 만들고,
> Sora/Veo는 숨을 불어넣는다.
> 편집이 감독이 된다.**

---

## AI 도구 분업

| 도구 | 역할 | 비율 |
|------|------|------|
| **Midjourney** | 세계관 이미지, 정체성 고정 | 80%+ |
| **Sora/Veo** | 클라이맥스 움직임 | 최대 20% |
| **편집** | 리듬, 동기화, 후처리 | 감독 역할 |

---

## 왜 이런 분업인가?

### Midjourney 우선 이유
- **스타일 고정이 가장 강함**
- 연재형 IP = 일관성 최우선
- 재현 가능한 프롬프트 시스템

### Sora/Veo 제한 이유
- 컷마다 카메라 언어/질감/색 달라질 위험
- 일관성 유지 어려움
- 클라이맥스 한두 컷에만 집중

---

## 영상화 규칙 (필수)

| 규칙 | 값 |
|------|-----|
| 컷 길이 | **4-6초 통일** |
| 모션 | 1컷 = 1모션 (줌/팬/고정) |
| 허용 움직임 | 연기, 안개, 불꽃, 파티클 |
| **금지** | 인물/오브제 변형 |

---

## 샷 라이브러리 전략

> **매 영상마다 새로 만들지 않는다.**
> **축적된 이미지를 재조합한다.**

### 권장 40장 구성

| 카테고리 | 수량 | 내용 |
|----------|------|------|
| 도깨비 (교란자) | 8장 | 다양한 앵글/상태 |
| 해태/궁 (질서) | 6장 | 멀리/가까이/부분 |
| 탈/연극 (사회) | 10장 | 단일/군중/다양한 탈 |
| 단청-기계 (시스템) | 10장 | 패턴/깨진 패턴/움직임 |
| 섬/바다/지도 (경계) | 6장 | 풍경/지도/경계선 |

### 장점
- 제작 속도 상승
- 브랜드 일관성 유지
- 재사용 자산 (IP) 축적
- 새 트랙에서 조합만

---

## 실패 규칙

> **"거의 맞는데" → 버린다**

- 애매한 컷은 과감히 폐기
- 완벽하지 않으면 재생성
- 타협하면 일관성 무너짐

---

## 제작 순서

### 1단계: 샷 리스트 작성
- 25-30컷 계획
- 각 컷의 카테고리 지정
- 기존 라이브러리에서 사용 가능한 것 체크

### 2단계: 신규 이미지 생성 (MJ)
- 부족한 컷만 생성
- 스타일 프롬프트 고정
- 대량 생성 후 엄선

### 3단계: 움직임 컷 생성 (Sora/Veo)
- 클라이맥스 1-2컷만
- 나머지는 MJ + 편집 움직임
- 실패 시 MJ로 대체

### 4단계: 편집
- 비트 동기화
- 움직임 추가 (줌/팬)
- 후처리

---

## Midjourney 프롬프트 템플릿

### 기본 구조
```
[subject], hanji paper texture, ink wash style,
low-key lighting, [color keywords],
film grain, --ar 16:9 --style raw --v 6
```

### 도깨비
```
shadowy dokkaebi figure, asymmetrical horns,
rough stone texture, hanji paper background,
single glowing eye, ink wash style,
mysterious, unsettling, --ar 16:9 --style raw
```

### 해태
```
massive haetae guardian, lion-dragon hybrid,
bronze and stone texture, symmetrical pose,
fog beneath, watching from above,
ink wash style, solemn, --ar 16:9 --style raw
```

### 탈
```
korean hahoe mask, wooden texture,
asymmetrical expression, empty eye holes,
half shadow, hanji paper background,
unsettling presence, --ar 16:9 --style raw
```

---

## 편집 도구 가이드

### 권장
- DaVinci Resolve (컬러)
- Premiere Pro (편집)
- After Effects (모션)

### 필수 플러그인/에셋
- 한지 텍스처 오버레이
- 필름 그레인
- LUT (따뜻한 그림자)

---

## 체크리스트

파이프라인 완성 전:

- [ ] MJ 사용이 80% 이상인가?
- [ ] Sora/Veo가 20% 이하인가?
- [ ] 컷 길이 4-6초인가?
- [ ] 인물/오브제 변형이 없는가?
- [ ] 샷 라이브러리를 활용했는가?
- [ ] 실패 컷은 버렸는가?

---

## 관련 문서

- [[02_style/VISUAL_EDIT]] — 편집 규칙
- [[05_execution/TRACK_TEMPLATE]] — 트랙 템플릿
- [[PROCESS]] — 제작 프로세스

---

*End of VISUAL_PIPELINE*
