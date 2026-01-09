---
title: "GYEOL Audio Style - Instruments"
type: style
locked: true
version: 1.0
last_updated: 2025-01-10
description: "결 오디오의 악기 역할 정의. 가야금, 장구, 태평소."
use_when: "악기 사용법 확인, 전통 악기 배치 결정"
tags: [style, audio, instruments, gayageum, janggu, taepyeongso]
related:
  - "[[02_style/AUDIO_CORE]]"
  - "[[02_style/AUDIO_STRUCTURE]]"
  - "[[05_execution/SUNO_PROMPTS]]"
---

# AUDIO_INSTRUMENTS — 악기 역할 정의

> **이 문서가 필요한 순간:**
> - 전통 악기를 어떻게 사용할지 결정할 때
> - 악기별 역할을 확인할 때
> - 금지 사용법을 확인할 때

---

## 핵심 원칙

> **전통 악기를 "전통처럼" 쓰면 실패한다.**
> **악기는 악기가 아니라 기능(Function)이다.**

---

## 사용량 규칙

- 이 세 악기면 충분하다
- **더 많이 쓰면 = "국악"이 된다**
- 전통 악기 = 전체 사운드의 **20-30%** 이하

---

## 1. 가야금 (Gayageum)

### 기능
> **결의 선 (Line of 결)**

### 규칙

| 항목 | 규칙 |
|------|------|
| 멜로디 | ❌ 금지 |
| 사용법 | 반복 리프, 신스 패드처럼 깔기 |
| 느낌 | 차갑고 세련됨 |
| 배치 | Intro, Break, Outro |

### 좋은 예
- 반복되는 짧은 리프 (2-4노트)
- 앰비언트 패드처럼 깔림
- 다른 악기와 레이어

### 나쁜 예
- 전통 가야금 산조 ❌
- 멜로디 연주 ❌
- 솔로 연주 ❌

---

## 2. 장구 (Janggu)

### 기능
> **인간의 호흡 (Human Breath)**

### 규칙

| 항목 | 규칙 |
|------|------|
| 전통 장단 | ❌ 금지 |
| 사용법 | 트랩/드릴 비트 위에 레이어 |
| 느낌 | 살아 있음, 불완전함 |
| 배치 | Drop 섹션, 리듬 강조 |

### 좋은 예
- 808 위에 장구 레이어
- 비트와 약간 어긋나는 타이밍
- 숨쉬는 느낌의 불규칙

### 나쁜 예
- 전통 장단 (굿거리, 중모리) ❌
- 솔로 장구 ❌
- 명확한 전통 리듬 ❌

---

## 3. 태평소 / 피리 (Taepyeongso / Piri)

### 기능
> **경고 / 신호 (Warning / Signal)**

### 규칙

| 항목 | 규칙 |
|------|------|
| 긴 연주 | ❌ 금지 |
| 사용법 | 짧은 찢어지는 샘플 |
| 느낌 | 불안, 각성 |
| 배치 | 전환 직전, 클라이맥스 진입 |

### 좋은 예
- 1-2초 짧은 샘플
- 갑작스럽게 등장
- 전환 신호로만

### 나쁜 예
- 긴 태평소 연주 ❌
- 멜로디 연주 ❌
- 전통 대취타 ❌

---

## 악기별 배치 맵

| 구간 | 가야금 | 장구 | 태평소 |
|------|--------|------|--------|
| Intro | ⭕ | ❌ | ❌ |
| Verse | △ | △ | ❌ |
| Pre-Chorus | △ | ⭕ | ❌ |
| Drop | ❌ | ⭕ | △ |
| Break | ⭕ | ❌ | ❌ |
| Climax | △ | ⭕ | ⭕ |
| Outro | ⭕ | ❌ | ❌ |

⭕ = 권장, △ = 선택, ❌ = 금지/불필요

---

## 현대 악기와의 조합

| 전통 악기 | 조합 파트너 | 효과 |
|----------|------------|------|
| 가야금 | 신스 패드, 스트링 | 레이어, 깊이 |
| 장구 | 808, 트랩 비트 | 인간적 어긋남 |
| 태평소 | 베이스 드롭 | 충격, 전환 |

---

## Suno 프롬프트 악기 키워드

```
gayageum riff (not melody),
janggu percussion layer over trap beat,
taepyeongso short sample,
korean traditional instruments as texture,
not folk music, not traditional ensemble
```

---

## 체크리스트

악기 사용 전:

- [ ] 전통 악기가 20-30% 이하인가?
- [ ] 가야금이 멜로디가 아닌가?
- [ ] 장구가 전통 장단이 아닌가?
- [ ] 태평소가 짧은 샘플인가?
- [ ] 전체적으로 "국악" 느낌이 아닌가?
- [ ] 악기가 "소개"되지 않는가?

---

## 관련 문서

- [[02_style/AUDIO_CORE]] — 오디오 핵심
- [[02_style/AUDIO_STRUCTURE]] — 곡 구조
- [[05_execution/SUNO_PROMPTS]] — Suno 프롬프트

---

*End of AUDIO_INSTRUMENTS*
