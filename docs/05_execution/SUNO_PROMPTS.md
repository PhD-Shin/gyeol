---
title: "GYEOL Suno Prompts"
type: execution
locked: false
version: 1.0
last_updated: 2025-01-10
description: "결 Suno AI 음악 생성 프롬프트 가이드."
use_when: "Suno로 음악 생성할 때, 프롬프트 작성 시"
tags: [execution, suno, ai, prompts, audio]
related:
  - "[[02_style/AUDIO_CORE]]"
  - "[[02_style/AUDIO_INSTRUMENTS]]"
  - "[[02_style/AUDIO_STRUCTURE]]"
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

## 체크리스트

Suno 생성 전:

- [ ] 전통 악기 키워드 포함?
- [ ] 어두운 분위기 키워드?
- [ ] 보컬 스타일 명시?
- [ ] 피해야 할 키워드 제거?

생성 후:

- [ ] 결 스타일과 맞는가?
- [ ] 전통 악기 들리는가?
- [ ] 감정 과잉 아닌가?
- [ ] 구조가 맞는가?

---

## 관련 문서

- [[02_style/AUDIO_CORE]] — 오디오 핵심
- [[02_style/AUDIO_INSTRUMENTS]] — 악기 역할
- [[02_style/AUDIO_STRUCTURE]] — 곡 구조

---

*End of SUNO_PROMPTS*
