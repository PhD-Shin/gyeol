---
title: "GYEOL Production Process"
type: meta
version: 1.0
last_updated: 2025-01-10
description: "결 트랙 제작 프로세스. 이 문서를 따라가면 트랙 하나를 완성할 수 있다."
tags: [process, execution, workflow]
related:
  - "[[PRD]]"
  - "[[05_execution/TRACK_TEMPLATE]]"
  - "[[05_execution/QC_CHECKLIST]]"
---

# PROCESS — 결 제작 프로세스

> **이 문서는 트랙 제작의 전체 흐름이다.**
> 순서대로 따라가면 하나의 트랙이 완성된다.

---

## 0. 시작 전 확인

### 필수 문서 확인
- [ ] [[PRD]] 읽었는가?
- [ ] [[00_core/MANIFESTO]] 이해했는가?
- [ ] [[01_world/PROHIBITIONS]] 숙지했는가?

### 필수 자산 확인
- [ ] 샷 라이브러리 40장 준비 (→ [[02_style/VISUAL_PIPELINE]])
- [ ] Suno 접근 가능
- [ ] Midjourney 접근 가능

---

## 1. 기획 단계 (Day 1-2)

### 1.1 Phase 확인
→ [[04_strategy/PHASE_MAP]]

| 질문 | 확인 |
|------|------|
| 이 트랙의 Phase는? | A / B / C / 0 |
| Phase 허용 메시지 강도는? | |
| Phase 금지 사항은? | |

### 1.2 트랙 기본 정보
→ [[05_execution/TRACK_TEMPLATE]] 복사

작성 항목:
- 트랙명
- 핵심 상징
- 한 줄 메시지 (직접 설명 금지)
- 주요 색
- 등장 존재

### 1.3 세계관 충돌 체크
→ [[01_world/RULES]], [[01_world/PROHIBITIONS]]

- [ ] 5대 규칙과 충돌 없음
- [ ] 금지 표현 없음
- [ ] 메타 테마와 연결됨

---

## 2. 음악 제작 단계 (Day 3-6)

### 2.1 음악 파라미터 결정
→ [[02_style/AUDIO_CORE]]

| 항목 | 값 |
|------|-----|
| BPM | (95-110 권장) |
| Key | (마이너 권장) |
| 구조 | Intro-Verse-Drop-Break-Drop-Outro |

### 2.2 Suno 프롬프트 작성
→ [[05_execution/SUNO_PROMPTS]]

```
[Style]
dark k-pop, trap beat, minimal vocal,
korean traditional instrument texture

[Instruments]
808 bass, hi-hats, gayageum riff,
janggu percussion layer

[Mood]
cold, dry, mysterious, not sad

[Avoid]
cheerful, epic orchestral, folk music feel
```

### 2.3 악기 역할 체크
→ [[02_style/AUDIO_INSTRUMENTS]]

| 악기 | 이 트랙에서의 역할 | 배치 |
|------|-------------------|------|
| 가야금 | | |
| 장구 | | |
| 태평소 | | |

### 2.4 음악 QC
→ [[05_execution/QC_CHECKLIST]]

- [ ] 전통 악기가 "소개"처럼 안 들림
- [ ] 전통 악기 비율 30% 이하
- [ ] 감정 과잉 없음
- [ ] 반복 구조 있음

---

## 3. 비주얼 제작 단계 (Day 7-12)

### 3.1 샷 리스트 작성
→ [[02_style/VISUAL_EDIT]]

| # | 샷 설명 | 시간 | 카테고리 |
|---|--------|------|----------|
| 1 | | 4초 | |
| 2 | | 5초 | |
| ... | | | |

### 3.2 Midjourney 이미지 생성
→ [[02_style/VISUAL_COLOR]], [[02_style/VISUAL_TEXTURE]]

프롬프트 기본 구조:
```
[subject], hanji paper texture, ink wash style,
low-key lighting, dark indigo and warm paper tones,
film grain, --ar 16:9 --style raw
```

### 3.3 캐릭터/존재 체크
→ [[03_characters/DOKKAEBI]], [[03_characters/HAETAE]], [[03_characters/TAL]]

| 존재 | 등장 횟수 | 등장 길이 | 규칙 준수 |
|------|----------|----------|----------|
| 도깨비 | 3-5회 | 1-3초 | [ ] |
| 해태 | 1-2회 | 5-15초 | [ ] |
| 탈 | 가변 | 2-5초 | [ ] |

### 3.4 비주얼 QC
→ [[05_execution/QC_CHECKLIST]]

- [ ] 순수 흰색/검정 없음
- [ ] 한지 텍스처 있음
- [ ] 역광/측광 주 조명
- [ ] 밝은 장면 30% 이하

---

## 4. 영상화 단계 (Day 13-16)

### 4.1 영상화 규칙
→ [[02_style/VISUAL_PIPELINE]]

| 규칙 | 체크 |
|------|------|
| 컷 길이 4-6초 | [ ] |
| 1컷 = 1모션 | [ ] |
| Sora/Veo 20% 이하 | [ ] |

### 4.2 움직임 결정

| 컷 | 움직임 | 도구 |
|----|--------|------|
| 1 | 고정 | MJ |
| 2 | 느린 줌인 | MJ+편집 |
| 3 | 연기 움직임 | Sora |
| ... | | |

### 4.3 실패 규칙
> **"거의 맞는데" → 버린다**

---

## 5. 편집 단계 (Day 17-18)

### 5.1 편집 규칙
→ [[02_style/VISUAL_EDIT]]

| 요소 | 값 |
|------|-----|
| 기본 전환 | 하드컷 (70%) |
| 섹션 전환 | 페이드 투 블랙 (15%) |
| 시간 경과 | 디졸브 (10%) |
| 특별 전환 | 먹 번짐 (5%) |

### 5.2 비트 동기화
- 음악 비트와 컷 동기화
- 의도적으로 어긋나는 컷 포함 (결의 어긋남)

### 5.3 후처리
- LUT 적용 (일관된 색감)
- 필름 그레인 2-5%
- 한지 텍스처 오버레이

---

## 6. 최종 QC (Day 19)

→ [[05_execution/QC_CHECKLIST]]

### 세계관 체크
- [ ] 설명 텍스트 없음
- [ ] 선악 구도 없음
- [ ] 금지 표현 없음

### 비주얼 체크
- [ ] 모든 컷 4-6초
- [ ] 색상 규칙 준수
- [ ] 조명 규칙 준수

### 오디오 체크
- [ ] 전통 악기 "소개" 안 됨
- [ ] 감정 과잉 없음

### 캐릭터 체크
- [ ] 등장 규칙 준수
- [ ] 금지 연출 없음

---

## 7. 업로드 (Day 20)

### 제목/설명
- 설명 최소화
- 해석 유도 (정답 주지 않음)
- 영어 우선

### 썸네일
- 샷 라이브러리에서 선택
- 텍스트 최소화

---

## 타임라인 요약

| 단계 | 기간 | 산출물 |
|------|------|--------|
| 기획 | Day 1-2 | 트랙 문서 |
| 음악 | Day 3-6 | 완성 트랙 |
| 비주얼 | Day 7-12 | 이미지 30장+ |
| 영상화 | Day 13-16 | 컷 영상 |
| 편집 | Day 17-18 | 완성 영상 |
| QC | Day 19 | 검수 완료 |
| 업로드 | Day 20 | 공개 |

> 파이프라인이 잡히면 **7-10일**로 단축 가능

---

## 관련 문서

- [[PRD]] — 프로젝트 전체 요약
- [[05_execution/TRACK_TEMPLATE]] — 트랙 템플릿
- [[05_execution/QC_CHECKLIST]] — QC 체크리스트
- [[04_strategy/PHASE_MAP]] — Phase 전략

---

*End of PROCESS*
