---
title: "GYEOL Suno Prompts"
type: execution
locked: false
version: 3.1
last_updated: 2025-01-11
description: "결 Suno AI 음악 생성 프롬프트 가이드. 48트랙 전곡 MV용."
use_when: "Suno로 음악 생성할 때, 프롬프트 작성 시"
tags: [execution, suno, ai, prompts, audio]
related:
  - "[[02_style/AUDIO_CORE]]"
  - "[[02_style/AUDIO_INSTRUMENTS]]"
  - "[[02_style/AUDIO_STRUCTURE]]"
  - "[[02_style/AUDIO_VOCAL]]"
  - "[[01_world/RULES]]"
  - "[[01_world/THEMES]]"
  - "[[04_strategy/ALBUM_STRUCTURE]]"
---

# SUNO_PROMPTS — Suno 프롬프트 가이드

> **이 문서가 필요한 순간:**
> - Suno로 음악을 생성할 때
> - 프롬프트를 작성할 때
> - 결 스타일 음악을 만들 때

---

## 핵심 규격 (v3.1)

| 항목 | 규격 |
|------|------|
| **BPM** | 95-110 |
| **Key** | 마이너 권장 (Am, Em, Dm) |
| **길이** | Suno가 랜덤 생성 (구조 힌트로 유도) |
| **프롬프트 길이** | 영문 500자 내외 |
| **보컬 성별** | 명시 필수 (male/female) |

---

## 프롬프트 구조 (500자 템플릿)

### 🔥 핵심: 간결하게, 구조 힌트 포함

```
[Style of Music] - 약 500 English characters

[장르], [전통악기], [BPM] [Key], [분위기],
[보컬 스타일], [프로덕션 특징],
[Intro] 설명, [Verse] 설명, [Drop] 설명, [Outro] 설명
```

### 500자 예시

```
dark atmospheric trap, korean traditional fusion, 95 bpm Am, haunting gayageum intro, 808 sub bass, janggu percussion, whispered male vocals korean, cold detached, heavy reverb delay, [Intro] gayageum solo drone 30s, [Verse1] sparse 808 30s, [PreChorus] janggu synths tension 20s, [Drop] full trap 808 heavy gayageum 35s, [Verse2] pulled back 25s, [Drop2] maximum energy 30s, [Bridge] silence 10s, [Outro] gayageum fading 25s
```

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

> **"dark k-pop"은 Suno에서 잘 인식되지 않음**
> 대신 인식 가능한 장르들을 조합하여 결의 사운드를 구현

#### Primary (핵심 — 항상 포함)
```
trap, korean fusion, atmospheric electronic
```

#### Secondary (보조 — 상황에 따라 선택)
```
industrial, hyperpop, experimental,
ambient, cinematic, minimal techno,
glitch, dark ambient
```

#### Korean Elements (한국적 요소)
```
korean traditional fusion, pansori influenced,
gugak electronic, jangdan rhythm
```

#### 조합 예시
```
atmospheric trap, korean traditional fusion, industrial electronic
experimental electronic, korean fusion, dark ambient, hypnotic
trap, gugak electronic, cinematic, ritualistic
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

## 🔥 K-판소리 판타지 트랩 (K-Pansori Fantasy Trap)

> **프로듀서 군단 승인 완료** — Top 10 프로듀서 리뷰 반영
> **핵심 공식**: 판타지 팝 접근성 + 판소리 트랩 정체성 (7:3)

### 핵심 키워드

| 카테고리 | 키워드 |
|---------|--------|
| **장르** | `dark korean pansori fantasy trap fusion` |
| **장단** | `jajinmori jangdan`, `jungjoongmori groove` |
| **발성** | `pansori chang shout`, `aniri storytelling rap`, `chuimsae` |
| **악기** | `haegeum haunting melodic`, `gayageum sharp stabs`, `janggu layered 808` |
| **분위기** | `dreamy ethereal`, `cinematic atmosphere`, `orchestral swells` |
| **보컬** | `raw emotional korean vocals pitch bending guttural` |

### A/B/C 테스트 시스템

> 모든 트랙에서 3가지 버전 생성 후 선별

| 버전 | 특징 | 용도 | 키워드 강조 |
|------|------|------|------------|
| **Style A** | 판소리 강조 | 정체성 테스트 | `pansori`, `chang`, `jangdan` |
| **Style B** | 판타지 팝 강조 | 접근성 테스트 | `fantasy pop`, `orchestral`, `ethereal` |
| **Style C** | 하이브리드 | 균형 테스트 | A+B 혼합 |

### 선별 기준 (가중치)

| 순위 | 기준 | 가중치 |
|------|------|--------|
| 1 | **첫 3초 훅 임팩트** | 30% |
| 2 | **해금 존재감** | 20% |
| 3 | **몽환↔폭발 대비** | 20% |
| 4 | **보컬 스타일** | 15% |
| 5 | **전체 밸런스** | 15% |

### 구조 타임라인 (2:00 기준)

```
[Intro] 0:00-0:05 — 폭발 훅 (첫 3초) + 침묵
[Verse] 0:05-0:23 — Dreamy ethereal 아니리
[Pre-Chorus] 0:23-0:33 — 오케스트라 스웰 + 추임새
[Drop] 0:33-0:55 — 창 + 자진모리 + 808 폭발
[Verse2] 0:55-1:07 — Ethereal whisper
[Pre-Chorus2] 1:07-1:15 — 빌드업 + 추임새
[Drop2] 1:15-1:37 — 최대 에너지
[Bridge] 1:37-1:40 — 해금 + 패드
[Outro] 1:40-1:45 — Dreamy fade
```

---

## 추임새 (Chuimsae) 가이드

> **정의**: 판소리의 청중 추임새를 훅/퍼포먼스 요소로 활용
> **원칙**: 훅 폭발점, Pre-Chorus, Drop 끝에 배치

### 1. 전통 추임새 (Traditional)

| 추임새 | 발음 | 느낌 | 사용 |
|--------|------|------|------|
| **얼쑤** | eol-ssu | 폭발, 환호 | Intro 훅, Drop 시작 |
| **좋다** | joh-da | 만족, 확인 | Drop 후, Pre-Chorus |
| **그렇지** | geu-reo-ji | 동의, 강조 | Drop 중간, 빌드업 후 |

### 2. 현대 추임새 (Modern K-Pansori)

| 추임새 | 발음 | 느낌 | 사용 |
|--------|------|------|------|
| **가자** | ga-ja | 출발, 전진 | Drop 끝, 전환점 |
| **간다** | gan-da | 돌진, 에너지 | Pre-Chorus, 빌드업 |

### 3. 하이브리드 추임새 (English-Korean)

| 하이브리드 | 사용 | 효과 |
|-----------|------|------|
| **Let's go 가자** | Drop 끝 | 전진 + 글로벌 |
| **Yeah 좋다** | Drop 후 | 만족 + 트랩 느낌 |

### 가사 배치 규칙

```
[Intro]
훅 구절!
얼쑤—

[Pre-Chorus]
빌드업 구절
Yeah 좋다—

[Drop]
훅 반복
얼쑤!
펀치 구절
그렇지— 가자

[Drop 2]
훅 반복
얼쑤!
클라이맥스 구절
Yeah 좋다—
```

---

## 코드스위칭 (Code-Switching) 전략

> **핵심 원칙**: 같은 의미 반복 ❌ → 영어+한국어가 **연결/확장**
> **K-pop 스타일**: 영어 구절 → 한국어가 다른 내용으로 이어짐

### K-pop 코드스위칭 유형

| 유형 | 설명 | 예시 |
|------|------|------|
| **Intra-sentential** | 한 문장 안에서 전환 | "Darkness coming 눈을 떠" |
| **Inter-sentential** | 문장 간 전환 (다른 의미) | "Let it burn / 재만 남아" |
| **Tag-switching** | 감탄사/추임새로 전환 | "좋다—", "deeper now" |

### ❌ 피해야 할 패턴 (같은 의미 반복)

```
❌ Can't stop 멈출 수 없어     ← 같은 의미!
❌ Burn it all 다 태워버려     ← 같은 의미!
❌ Break it all 다 부숴버려    ← 같은 의미!
```

### ⭕ 올바른 패턴 (연결/확장)

**Pattern A: 연결 (원인→결과)**
```
Let it burn 재만 남아         ← burn → ashes (결과)
Break it down 먼지만 남아     ← break → dust (결과)
```

**Pattern B: 확장 (상황→감각)**
```
Darkness coming 눈을 떠       ← darkness → open eyes
숨이 막혀 I can feel it       ← can't breathe → feeling
```

**Pattern C: 이어짐 (시작→계속)**
```
Something changing 어둠 속에   ← changing → in darkness
빠져들어 deeper now           ← falling → deeper
```

### 가사 예시 (v3)

```
[Verse]
Darkness coming 눈을 떠       ← 어둠이 온다 + 눈을 떠 (연결)
숨이 막혀 I can feel it       ← 숨막힘 + 느낌 (확장)
Something changing 어둠 속에   ← 변화 + 장소 (이어짐)
빠져들어 deeper now           ← 빠짐 + 깊이 (이어짐)

[Drop]
Let it burn 재만 남아         ← 태워라 + 결과 (연결)
Let it burn 재만 남아
얼쑤!                         ← 전통 추임새
어둠 속에 ashes fall          ← 장소 + 결과 (연결)
그렇지— 가자                  ← 전통 + 현대 추임새
```

---

## A1-01 시작 프롬프트 (Reference)

> **제목**: 시작 (SIJAK)
> **BPM**: 110 | **Key**: Am | **길이**: 2:00

### Style A — 판소리 강조 (698자)

```
dark korean pansori fantasy trap fusion, 110 bpm Am, dreamy ethereal synth pads on verses, pansori chang shout hook first 3 seconds chuimsae, orchestral swells before drops, jajinmori jangdan on drops, jungjoongmori groove verses, haegeum haunting melodic texture, gayageum sharp stabs, janggu layered 808, raw emotional korean vocals pitch bending guttural, aniri storytelling rap, vocal percussion texture, cinematic atmosphere, [Intro] pansori shout chuimsae 808 haegeum explosion 3s silence 2s, [Verse] dreamy synth aniri storytelling 18s, [PreChorus] orchestral swell building 10s, [Drop] chang jajinmori 808 gayageum explosive 22s, [Verse2] ethereal space whisper 12s, [PreChorus2] building intensity 8s, [Drop2] overwhelming maximum energy 22s, [Bridge] haegeum melodic drone 3s, [Outro] dreamy fade 5s
```

### Style B — 판타지 팝 강조 (695자)

```
dark fantasy pop korean trap fusion, 110 bpm Am, ethereal dreamy synth pads shimmering, explosive traditional korean shout hook first 3 seconds, cinematic orchestral swells before drops, fast traditional rhythm on drops, groovy mid-tempo verses, haegeum haunting melodic texture, string stabs, layered 808 bass, raw emotional vocals pitch bending, storytelling rap verses, atmospheric reverb, [Intro] explosive korean shout 808 string hit 3s silence 2s, [Verse] dreamy synth storytelling ethereal 18s, [PreChorus] orchestral swell strings building emotional 10s, [Drop] explosive fast rhythm 808 strings maximum energy 22s, [Verse2] ethereal space whisper floating 12s, [PreChorus2] building intensity dramatic 8s, [Drop2] overwhelming climax 22s, [Bridge] melodic drone emotional pad 3s, [Outro] dreamy atmospheric fade 5s
```

### Style C — 하이브리드 균형 (699자)

```
dark korean fantasy trap pansori fusion, 110 bpm Am, dreamy ethereal pads verses, korean traditional shout hook first 3 seconds, orchestral swells drops, jajinmori rhythm drops, groovy verses, haegeum melodic texture signature, gayageum stabs, janggu 808 layered, raw emotional korean vocals guttural pitch bend, aniri rap storytelling, vocal percussion layer subtle, cinematic dark atmosphere, [Intro] korean shout chuimsae 808 haegeum hit explosion 3s silence 2s, [Verse] dreamy synth aniri storytelling floating 18s, [PreChorus] orchestral swell emotional building 10s, [Drop] chang jajinmori 808 gayageum explosive energy 22s, [Verse2] ethereal whisper space 12s, [PreChorus2] intensity building 8s, [Drop2] maximum overwhelming climax 22s, [Bridge] haegeum drone pad 3s, [Outro] dreamy haegeum fade 5s
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

## 가사 포맷 (3분 기준)

### 필수 출력 형식

모든 Suno 프롬프트는 다음 3개 블록으로 출력:

```
### 제목
[한글 제목] ([영문 제목])

### Style of Music (~500자)
[프롬프트]

### Lyrics
[가사]
```

### 3분 곡 구조 템플릿

```
[Intro] ~30초
(instrumental, mood setting)

[Verse 1] ~30초
[핵심 단어] 반복 3-4회
(whispered, layered)
[보조 구절]
(spoken/distant)

[Pre-Chorus] ~20초
[빌드업 구절] 반복 3회
(building intensity)

[Drop] ~35초
[훅 구절] chopped/rhythmic
[보조 훅] 2회 반복
(layered vocal chops)

[Verse 2] ~25초
[변형 단어] 반복
(whispered)
[새 구절]
(fading)

[Pre-Chorus 2] ~15초
[빌드업 구절] 반복 2회
(faster building)

[Drop 2] ~30초
[훅 구절] maximum energy
[클라이맥스 구절]
(overwhelming)

[Bridge] ~10초
(silence or minimal)

[Outro] ~25초
[핵심 단어]...
(fading to silence)
```

### 가사 규칙

1. **제목/정체성 언급 금지**
   - 트랙 제목 가사에 반복 ❌
   - 프로젝트명("결") 언급 ❌
   - **분위기만 전달** ⭕

2. **짧고 임팩트 있는 구절**
   - 2-4음절
   - 같은 단어 최대 2회 반복
   - 완전한 문장 ❌

3. **긴장/압박 분위기**
   - 명령형 ("눈을 떠", "숨을 참아")
   - 질문형 ("느껴지냐")
   - 상황 묘사 ("어둠이 움직여")

4. **한국어 텍스처**
   - 의미 전달 목적 ❌
   - 사운드로 사용 ⭕

5. **구조**
   - Verse 2개 + Drop 2개 필수
   - Drop은 chopped/rhythmic
   - Bridge는 짧게 (5초 침묵)

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
| A-1 흔들림 | 110 | Am/Em | `emerging tension, system, deviation begins` |
| A-2 발현 | 110 | Em/Dm | `manifestation, presence grows, watching` |
| B-1 대면 | 110 | Dm/Gm | `encounter, borders visible, confrontation` |
| B-2 균형 | 110 | Gm/Am | `balance, tension held, equilibrium` |
| C-1 흐림 | 110 | Cm/Fm | `blur, fading, traces, heavy memory` |
| C-2 실 | 110 | Fm/Bbm | `thread, final record, weaving, closure` |
| 0 기원 | 110 | Am/Bm | `primordial, origin, pure, before all` |

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
