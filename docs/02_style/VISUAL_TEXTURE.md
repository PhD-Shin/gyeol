---
title: "GYEOL Visual Style - Texture"
type: style
locked: true
version: 1.0
last_updated: 2025-01-10
description: "결 비주얼의 질감 규칙. 한지, 먹, 그레인, 단청."
use_when: "비주얼 제작 시 질감 처리, 텍스처 오버레이"
tags: [style, visual, texture, hanji, ink]
related:
  - "[[02_style/VISUAL_COLOR]]"
  - "[[02_style/VISUAL_PIPELINE]]"
---

# VISUAL_TEXTURE — 질감 규칙

> **이 문서가 필요한 순간:**
> - 비주얼 제작 시 질감 처리할 때
> - 텍스처 오버레이를 적용할 때
> - "결다운 질감"을 확인할 때

---

## 핵심 원칙

> **디지털이지만 손으로 만든 것처럼.**
> **깨끗함은 결의 적이다.**

---

## 필수 질감

### 1. 한지 텍스처 (Hanji)
- **모든 배경의 기본 레이어**
- 불투명도: 10-30%
- Soft Light 또는 Overlay
- 미세한 섬유 결 느낌

### 2. 먹 번짐 (Ink Wash)
- 전환부, 페이드에 사용
- 경계를 모호하게
- 완전히 깨끗한 전환 금지

### 3. 필름 그레인 (Film Grain)
- 불투명도: **2-5%**
- 전체 영상에 적용
- 너무 강하면 안 됨 (노이즈 아님)

---

## 허용 질감

| 질감 | 사용 상황 | 설명 |
|------|----------|------|
| 천 (silk, linen) | 의상, 배경 | 부드러운 흐름 |
| 연기 | 전환, 분위기 | 경계 흐림 |
| 물결 | 반사, 움직임 | 변형 효과 |
| 먼지 입자 | 공간감 | 빛 줄기에 |
| 돌/나무 | 오브제, 배경 | 거친 표면 |
| 이끼 | 도깨비, 해태 | 시간의 흔적 |

---

## 금지 질감

| 금지 | 이유 |
|------|------|
| 디지털 글리치 (과도한) ❌ | 사이버펑크 느낌 |
| 깨끗한 그라데이션 ❌ | 너무 디지털 |
| 플라스틱/메탈릭 광택 ❌ | 결의 질감 파괴 |
| 과도한 샤프니스 ❌ | 너무 선명 |
| CG 느낌 ❌ | 손 느낌 필요 |

---

## 단청 패턴 사용

### 원칙
> **단청은 전통 장식이 아니라 기계적/시스템적 구조로 재해석**

### 사용 방법

| 패턴 상태 | 의미 | 사용 |
|----------|------|------|
| 반복 패턴 | 시스템의 규칙성 | 배경, 질서 장면 |
| 깨진 패턴 | 결의 어긋남 | 개입 장면 |
| 흐릿한 패턴 | 배경 텍스처 | 전체 |
| 움직이는 패턴 | 기계처럼 맞물림 | 전환 |

### 금지
- 단청을 "예쁜 장식"으로 ❌
- 전통 건축물 그대로 ❌
- "한국 전통의 아름다움" 프레이밍 ❌

---

## 텍스처 레이어 순서

```
1. 베이스 이미지
2. 한지 텍스처 (Soft Light, 15%)
3. 먹 번짐 (필요시)
4. 연기/입자 (필요시)
5. 필름 그레인 (Overlay, 3%)
6. LUT/컬러 그레이딩
```

---

## Midjourney 프롬프트 질감 키워드

```
hanji paper texture, ink wash style,
rough paper surface, traditional korean texture,
film grain, dust particles in light,
muted tones, hand-painted feel,
not too sharp, organic texture
```

---

## 후처리 가이드

### Photoshop/Premiere
1. 한지 텍스처 오버레이 (Soft Light)
2. Gaussian Blur 0.5px (샤프니스 줄이기)
3. Add Grain (2-5%)
4. Vignette (살짝)

### DaVinci Resolve
1. Texture node (한지)
2. Film Grain (Fine, 10-20%)
3. Glow (매우 약하게)
4. Lens Blur (가장자리)

---

## 체크리스트

질감 완성 전:

- [ ] 한지 텍스처가 있는가?
- [ ] 필름 그레인이 있는가? (2-5%)
- [ ] 너무 깨끗/선명하지 않은가?
- [ ] 디지털 글리치가 과도하지 않은가?
- [ ] 플라스틱/메탈릭 광택이 없는가?
- [ ] 손으로 만든 느낌이 나는가?

---

## 관련 문서

- [[02_style/VISUAL_COLOR]] — 색상 규칙
- [[02_style/VISUAL_LIGHT]] — 조명 규칙
- [[02_style/VISUAL_PIPELINE]] — 제작 파이프라인

---

*End of VISUAL_TEXTURE*
