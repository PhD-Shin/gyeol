---
title: "GYEOL Suno Prompts"
type: execution
locked: false
version: 2.0
last_updated: 2025-01-10
description: "결 Suno AI 음악 생성 프롬프트 가이드. 48트랙 전곡 MV용."
use_when: "Suno로 음악 생성할 때, 프롬프트 작성 시"
tags: [execution, suno, ai, prompts, audio]
related:
  - "[[02_style/AUDIO_CORE]]"
  - "[[02_style/AUDIO_INSTRUMENTS]]"
  - "[[02_style/AUDIO_STRUCTURE]]"
  - "[[04_strategy/ALBUM_STRUCTURE]]"
---

# SUNO_PROMPTS — Suno 프롬프트 가이드

> **이 문서가 필요한 순간:**
> - Suno로 음악을 생성할 때
> - 프롬프트를 작성할 때
> - 결 스타일 음악을 만들 때

---

## 기본 구조

Suno 프롬프트 = 장르 + 악기 + 분위기 + 보컬 + 구조

```
[장르 태그]
[악기 리스트]
[분위기/무드]
[보컬 스타일]
[구조 힌트]
```

---

## 필수 키워드

### 장르/스타일

```
dark k-pop, trap, hyperpop,
experimental electronic, cinematic,
industrial, ambient, minimal techno
```

### 전통 악기

```
gayageum, traditional korean strings,
janggu percussion, korean drums,
daegeum flute, haegeum strings
```

### 현대 악기

```
808 bass, sub bass,
distorted synths, granular synthesis,
ambient pads, glitch percussion
```

### 분위기

```
dark, atmospheric, mysterious,
ritualistic, hypnotic, unsettling,
cold, mechanical, ancient modern fusion
```

### 보컬

```
minimal vocal, whispered vocals,
vocal chops, processed voice,
not narrative, not emotional,
voice as texture, layered vocals,
korean words as texture not lyrics
```

---

## 템플릿별 프롬프트

### Template A: 인트로 중심

```
dark ambient intro, gayageum solo,
atmospheric, mysterious, building tension,
minimal percussion, sub bass drone,
whispered korean vocals,
cinematic, hypnotic, slow build
```

용도: 세계관 진입, 긴장 구축

### Template B: 트랩 하이퍼팝

```
dark k-pop, trap, hyperpop,
808 bass, janggu percussion layers,
aggressive synths, glitch elements,
processed vocal chops,
hard hitting, industrial, ritualistic
```

용도: Drop, 클라이맥스

### Template C: 미니멀 앰비언트

```
minimal ambient, gayageum texture,
sub bass pulses, sparse percussion,
whispered vocals, atmospheric,
cold, mechanical, meditative
```

용도: Verse, Break

### Template D: 신스 중심

```
dark electronic, distorted synths,
granular textures, 808 bass,
no traditional instruments,
processed vocals, industrial,
hypnotic, repetitive, building
```

용도: 빌드업, Pre-Chorus

---

## 구간별 프롬프트

### Intro (10-15초)

```
ambient intro, gayageum solo,
hanji paper texture sound,
mysterious, ancient, slow,
building atmosphere, no drums yet
```

### Verse (30-45초)

```
minimal beat, sparse 808,
whispered vocals, atmospheric,
gayageum texture in background,
dark, restrained, building slowly
```

### Pre-Chorus (15-20초)

```
building intensity, layered synths,
repetitive vocal hook,
adding percussion layers,
tension rising, hypnotic
```

### Drop (30-45초)

```
full trap beat, 808 bass heavy,
janggu and electronic drums layered,
distorted synths, vocal chops,
climactic, powerful, ritualistic
```

### Break (5-10초)

```
sudden silence, ambient noise only,
breathing space, tension held,
minimal gayageum, no drums
```

### Outro (15-30초)

```
fading out, gayageum solo returns,
ambient atmosphere, peaceful ending,
whispered vocals fading,
open ending, mysterious
```

---

## 가사 포맷

### Metatag 사용

```
[Intro]
(instrumental)

[Verse 1]
흔들린다
(whispered, repeated)

[Pre-Chorus]
멈추지 않아
(building, layered)

[Drop]
(vocal chops only)

[Break]
(silence)

[Outro]
사라진다
(fading whisper)
```

### 가사 규칙

1. **짧은 구절만**
   - 2-4음절 반복
   - 완전한 문장 ❌

2. **한국어 텍스처**
   - 의미 전달 목적 ❌
   - 사운드로 사용 ⭕

3. **영어 최소화**
   - 필요시 1-2단어만
   - 설명적 영어 ❌

---

## 생성 워크플로우

### Step 1: 기본 생성

1. Template 선택
2. 프롬프트 입력
3. 10개 이상 생성
4. 베스트 3 선정

### Step 2: 변형

1. 베스트 버전에서 Extend
2. 구간별 조정
3. 추가 5개 생성

### Step 3: 최종 선정

1. 전체 구조 확인
2. 결 스타일 체크
3. 최종 1개 선정

---

## 피해야 할 키워드

### 장르

```
❌ pop, cheerful, upbeat
❌ jazz, blues, country
❌ classical, orchestral (unless dark)
❌ reggae, funk
```

### 분위기

```
❌ happy, joyful, hopeful
❌ romantic, lovely
❌ fun, playful
❌ bright, sunny
```

### 보컬

```
❌ powerful vocals, belting
❌ rap verse (unless whispered)
❌ harmonies (unless dark)
❌ clear lyrics
```

---

## Phase별 프롬프트 가이드

### Phase A 프롬프트

```
dark k-pop, trap, atmospheric,
gayageum intro, 808 bass,
95-110 bpm, Am or Em key,
balanced traditional and electronic,
mysterious, system vs deviation theme
```

특징: 균형, 도입, 미세한 어긋남

### Phase B 프롬프트

```
aggressive trap, hyperpop elements,
janggu heavy, distorted synths,
100-120 bpm, Dm or Gm key,
tension building, border theme,
more electronic, intense
```

특징: 긴장, 경계, 빨라짐

### Phase C 프롬프트

```
dark ambient, minimal beat,
gayageum prominent, sub bass,
85-100 bpm, Cm or Fm key,
record and erasure theme,
fading, echoes, traces
```

특징: 무거움, 기록, 느려짐

### Phase 0 프롬프트

```
pure ambient, drone based,
gayageum solo, almost no drums,
75-90 bpm, Am or Bm key,
origin theme, ancient,
minimal, primordial
```

특징: 태초, 고요, 미니멀

---

## 테마별 프롬프트 가이드

| 테마 | 핵심 키워드 | 추가 요소 |
|------|-----------|----------|
| System vs Deviation | `perfect beat with slight drift, quantized then humanized` | 퀀타이즈 90% |
| Erasure | `fading sounds, reverb decay, dissolving melody` | 긴 리버브 |
| Border | `ambiguous transitions, blending textures` | 경계 없는 전환 |
| Name | `whispered fragments, anonymous voices` | 속삭임 레이어 |
| Record | `distant echoes, layered memories` | 노이즈, 빈티지 |
| Ritual | `hypnotic loop, ceremonial drums` | 장구 반복 |

### 테마 조합 예시

**System + Ritual:**
```
dark k-pop, hypnotic beat,
perfect repetition with janggu accents,
ceremonial atmosphere, ritualistic,
system breaking down gradually
```

**Erasure + Name:**
```
fading ambient, whispered korean,
voices dissolving, anonymous presence,
echoes of identity, traces remaining
```

---

## 실패 사례/안티패턴

### 흔한 실패 패턴

| 실패 | 원인 | 해결 |
|------|------|------|
| "국악 퓨전" 느낌 | 전통 악기 과다 | 전통 악기 키워드 축소 |
| 너무 밝음 | happy/upbeat 키워드 | dark/mysterious로 대체 |
| 구조 엉망 | 구조 힌트 없음 | metatag 추가 |
| K-pop 안 느껴짐 | 808/trap 없음 | 현대 악기 추가 |
| 보컬 과잉 | vocal 키워드 과다 | minimal vocal 명시 |

### 실패 프롬프트 예시

**❌ 나쁜 예:**
```
korean traditional music,
gayageum melody, janggu solo,
beautiful, peaceful, hopeful,
clear vocals, emotional singing
```

→ 결과: 국악 발라드, 밝고 감정적

**⭕ 수정 후:**
```
dark k-pop, trap elements,
gayageum texture (not melody),
janggu over 808, atmospheric,
whispered vocals, cold, mechanical
```

---

## 프롬프트 버전 관리

### 네이밍 규칙

```
[Phase]_[Template]_[Version]_[Date]

예시:
PhaseA_TrapHyper_v03_250110
PhaseB_Ambient_v01_250111
```

### 버전 기록 템플릿

| 버전 | 프롬프트 | 결과 점수 | 메모 |
|------|----------|----------|------|
| v01 | (프롬프트) | /10 | 초안 |
| v02 | (수정본) | /10 | 전통 악기 축소 |
| v03 | (최종) | /10 | 채택 |

### 성공 프롬프트 아카이브

> 성공한 프롬프트는 반드시 저장하고 시드와 함께 기록

| 트랙 | 프롬프트 | 시드 |
|------|----------|------|
| (예시) | dark k-pop... | 123456789 |

---

## 생성물 평가 점수 시스템

### 평가 기준 (각 2점, 총 10점)

| 기준 | 0점 | 1점 | 2점 |
|------|-----|-----|-----|
| 스타일 | 완전 다름 | 비슷함 | 정확 |
| 구조 | 구조 없음 | 일부 맞음 | K-pop 구조 |
| 전통 악기 | 없거나 과다 | 애매함 | 적절 (20-30%) |
| 분위기 | 밝음/촌스러움 | 중립 | 어둡고 쿨함 |
| 보컬 | 과다/감정적 | 애매함 | 텍스처로 사용 |

### 점수별 조치

| 점수 | 판정 | 조치 |
|------|------|------|
| 9-10 | 채택 | 바로 사용 |
| 7-8 | 후보 | Extend로 개선 시도 |
| 5-6 | 보류 | 프롬프트 수정 후 재생성 |
| 0-4 | 폐기 | 완전히 다른 접근 |

---

## 앨범별/트랙별 커스터마이징

### 앨범별 기본 설정 (6 앨범 × 8 트랙 = 48 트랙)

| 앨범 | BPM | 키 | 특수 키워드 |
|------|-----|-----|-----------|
| A-1 흔들림 | 100-110 | Am/Em | `emerging tension, system, deviation begins` |
| A-2 발현 | 105-115 | Em/Dm | `manifestation, presence grows, watching` |
| B-1 대면 | 110-120 | Dm/Gm | `encounter, borders visible, confrontation` |
| B-2 균형 | 100-115 | Gm/Am | `balance, tension held, equilibrium` |
| C-1 흐림 | 90-100 | Cm/Fm | `blur, fading, traces, heavy memory` |
| C-2 실 | 85-95 | Fm/Bbm | `thread, final record, weaving, closure` |
| 0 기원 | 75-90 | Am/Bm | `primordial, origin, pure, before all` |

### 8트랙 구조별 에너지 곡선

| 트랙 위치 | 에너지 | 조정 |
|----------|--------|------|
| Track 1 (오프닝) | 중간 | `intro focused, world entry, establishing` |
| Track 2 | 상승 시작 | `building, layered, tension grows` |
| Track 3 | 상승 중 | `momentum, energy building` |
| Track 4 (첫 정점) | 최고 | `climactic, full production, peak` |
| Track 5 (전환점) | 전환 | `shift, new direction, surprise` |
| Track 6 | 하강 | `descent, reflection, calming` |
| Track 7 (심화) | 깊음 | `deeper, contemplative, heavy` |
| Track 8 (클로징) | 여운 | `finale, open ending, lingering`

### 존재 등장 트랙 조정

| 존재 | 추가 키워드 |
|------|-----------|
| 도깨비 등장 | `rhythm break, dissonance, unsettling` |
| 해태 등장 | `low drone, minimal drums, watching` |
| 탈 등장 | `whisper layers, anonymous voices` |

---

## 체크리스트

Suno 생성 전:

- [ ] 전통 악기 키워드 포함?
- [ ] 어두운 분위기 키워드?
- [ ] 보컬 스타일 명시?
- [ ] 피해야 할 키워드 제거?
- [ ] Phase별 가이드 적용?
- [ ] 테마별 가이드 적용?

생성 후:

- [ ] 결 스타일과 맞는가?
- [ ] 전통 악기 들리는가?
- [ ] 감정 과잉 아닌가?
- [ ] 구조가 맞는가?
- [ ] Phase 분위기가 맞는가?
- [ ] 테마가 표현되었는가?

---

## 관련 문서

- [[02_style/AUDIO_CORE]] — 오디오 핵심
- [[02_style/AUDIO_INSTRUMENTS]] — 악기 역할
- [[02_style/AUDIO_STRUCTURE]] — 곡 구조

---

*End of SUNO_PROMPTS*
