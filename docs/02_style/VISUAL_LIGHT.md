---
title: "GYEOL Visual Style - Lighting"
type: style
locked: true
version: 1.0
last_updated: 2025-01-10
description: "결 비주얼의 조명 규칙. 로우키, 역광, 등롱광."
use_when: "조명 설정 시, 밝기 규칙 확인 시"
tags: [style, visual, lighting]
related:
  - "[[02_style/VISUAL_COLOR]]"
  - "[[02_style/VISUAL_CAMERA]]"
  - "[[01_world/TONE]]"
---

# VISUAL_LIGHT — 조명 규칙

> **이 문서가 필요한 순간:**
> - 조명을 설정할 때
> - 밝기 규칙을 확인할 때
> - "결다운 조명"인지 검증할 때

---

## 핵심 원칙

> **빛은 인물을 비추지 않고 지나간다.**
> **광원은 항상 화면 밖 또는 모호하게.**

---

## 기본 원칙

- **로우키 (Low-key)** 기본
- 빛은 인물을 직접 비추지 않음
- 광원의 위치가 명확하지 않음
- 그림자가 주인공

---

## 조명 유형

| 유형 | 비율 | 설명 | 사용 |
|------|------|------|------|
| 역광 (Backlight) | 60% | 기본, 실루엣 강조 | 대부분 |
| 측광 (Side light) | 25% | 얼굴 반만 드러냄 | 인물 샷 |
| 등롱광 (Lantern glow) | 10% | 따뜻한 포인트 | 청사초롱 |
| 정면광 | 5% | 클라이맥스만 | 드물게 |

---

## 밝기 규칙

### 기본
- 전체 영상의 **70-80%**: 어두움
- 전체 영상의 **20-30%**: 밝음 허용

### 밝음의 의미
- 밝음 = 의례 완료 또는 시스템 역전
- 밝음 ≠ 희망, 승리, 해피엔딩
- **밝더라도 "기이함"이어야 함**

---

## 광원 종류

### 허용 광원

| 광원 | 색온도 | 사용 |
|------|--------|------|
| 청사초롱 | 따뜻함 | 포인트 광원 |
| 달빛 | 차가움 | 전체 조명 |
| 횃불/불꽃 | 따뜻함 | 악센트 |
| 모호한 빛 | 중립 | 출처 불명 |

### 금지 광원
- 태양 (대낮) ❌
- 형광등 (현대) ❌
- 네온사인 ❌
- 스포트라이트 ❌

---

## 그림자 규칙

- 그림자가 얼굴을 가림
- 그림자가 공간을 채움
- 그림자의 경계는 부드럽게
- 완전한 검정 그림자 ❌

---

## Phase별 조명 전략

| Phase | 조명 특징 |
|-------|----------|
| Phase A | 가장 어두움, 역광 위주 |
| Phase B | 측광 증가, 긴장 |
| Phase C | 등롱광 증가, 의례 |
| Phase 0 | 극단적 어둠 |

---

## Midjourney 프롬프트 조명 키워드

```
low-key lighting, backlit silhouette,
side lighting half face, lantern glow,
mysterious light source, dim atmosphere,
no direct sunlight, night scene,
warm accent light, dramatic shadows
```

---

## 체크리스트

조명 완성 전:

- [ ] 로우키 기본인가?
- [ ] 역광/측광이 주 조명인가?
- [ ] 밝은 장면이 30% 이하인가?
- [ ] 광원이 모호한가?
- [ ] 정면광이 극히 드문가?
- [ ] 그림자가 충분한가?

---

## 관련 문서

- [[02_style/VISUAL_COLOR]] — 색상 규칙
- [[02_style/VISUAL_CAMERA]] — 카메라 규칙
- [[01_world/TONE]] — 톤 슬라이더

---

*End of VISUAL_LIGHT*
