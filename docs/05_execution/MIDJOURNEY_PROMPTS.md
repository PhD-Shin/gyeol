---
title: "GYEOL Visual Prompts"
type: execution
locked: false
version: 2.0
last_updated: 2025-01-10
description: "결 비주얼 생성 프롬프트 가이드. Midjourney 이미지 + 비디오 (MJ/Veo/Sora)."
use_when: "이미지/영상 생성할 때, Shot Library 구축 시, MV 제작 시"
tags: [execution, midjourney, veo, sora, ai, prompts, visual, video]
related:
  - "[[02_style/VISUAL_COLOR]]"
  - "[[02_style/VISUAL_TEXTURE]]"
  - "[[02_style/VISUAL_LIGHT]]"
  - "[[02_style/VISUAL_CAMERA]]"
  - "[[02_style/VISUAL_PIPELINE]]"
  - "[[01_world/RULES]]"
  - "[[01_world/THEMES]]"
  - "[[01_world/PROHIBITIONS]]"
  - "[[04_strategy/ALBUM_STRUCTURE]]"
---

# VISUAL_PROMPTS — 비주얼 생성 프롬프트 가이드

> **이 문서가 필요한 순간:**
> - Midjourney로 이미지/영상을 생성할 때
> - Veo/Sora로 영상 클립을 생성할 때
> - Shot Library를 구축할 때
> - MV 제작 시 비주얼 에셋이 필요할 때

---

## 핵심 전략: 음악 먼저 워크플로우

```
┌─────────────────────────────────────────────────────┐
│  🎵 음악 → 🖼️ 이미지 → 🎬 영상 파이프라인              │
├─────────────────────────────────────────────────────┤
│  1. Suno 음악 생성 → 최종 선정                        │
│  2. 음악 분석 (분위기, 에너지, 전환점)                 │
│  3. 음악 기반 MJ 프롬프트 생성                        │
│  4. 이미지 → 비디오 확장                              │
│  5. 편집 (음악 싱크)                                 │
└─────────────────────────────────────────────────────┘
```

> **원칙**: 가사와 직접 연관 없이, 음악의 **분위기**에 맞춘다.
> (Kage Bow 방식: 가사 ≠ 비주얼, 무드 = 비주얼)

---

## 🎵 음악 분석 → 비주얼 결정 프로세스

### Step 1: 음악 들으며 분석

| 분석 항목 | 체크 포인트 |
|----------|------------|
| **에너지 곡선** | 어디서 올라가고 내려가는가? |
| **전환점** | 분위기가 확 바뀌는 지점은? |
| **무드** | 긴장? 해방? 고요? 폭발? |
| **공간감** | 넓은 느낌? 좁은 느낌? |
| **텍스처** | 거친가? 부드러운가? |

### Step 2: 분석 결과 기록

```markdown
## 음악 분석 기록

**전체 무드**: [한 단어]
**에너지 곡선**:
- Intro: 낮음/중간/높음
- Verse:
- Drop:
- Outro:

**전환점**:
- 0:00 - [설명]
- 0:30 - [설명]
- ...

**시각화 키워드**: [음악에서 느껴지는 이미지 3-5개]
```

### Step 3: 프롬프트 생성

음악 분석 결과를 바탕으로 각 구간별 프롬프트 생성

---

## 음악 무드 → 비주얼 키워드 변환표

| 음악 무드 | 비주얼 키워드 |
|----------|--------------|
| 긴장/불안 | `tense atmosphere, unsettling, shadows creeping` |
| 고요/명상 | `still, meditative, vast emptiness, fog` |
| 폭발/해방 | `dramatic reveal, overwhelming scale, light burst` |
| 슬픔/무게 | `heavy, sinking, ink bleeding, dissolving` |
| 신비/미스터리 | `mysterious, hidden, barely visible, emerging` |
| 압도/경외 | `epic scale, jaw-dropping, breathtaking vista` |
| 공허/여운 | `lingering, fading, empty space, echoing` |

### 에너지 레벨 → 조명/색상

| 에너지 | 조명 | 색상 악센트 |
|--------|------|-----------|
| 매우 낮음 | 거의 어둠 | 없음 |
| 낮음 | 희미한 단일 광원 | 최소 |
| 중간 | 뚜렷한 단일 광원 | 5-10% |
| 높음 | 강한 대비 | 15-20% |
| 최고 | 드라마틱 라이팅 | 20-25% |

### 공간감 → 구도

| 공간감 | 구도 |
|--------|------|
| 압축된 | 클로즈업, 좁은 프레임 |
| 확장되는 | 와이드샷, 여백 많음 |
| 폐쇄적 | 사방이 막힌 느낌 |
| 개방적 | 지평선 보이는 광활함 |

### 도구별 역할

| 도구 | 용도 | 길이 | 강점 |
|------|------|------|------|
| Midjourney 이미지 | 키 비주얼, 스틸컷 | - | 스타일 일관성 |
| Midjourney Video | 정적/느린 장면 | 5초 | 이미지 연속성 |
| Veo | 인물 동작 | 5-10초 | 자연스러운 움직임 |
| Sora | 역동적 장면 | 5-20초 | 드라마틱 트랜지션 |

---

## 기본 구조

```
[주체] + [배경/환경] + [텍스처/재질] + [조명] + [분위기] + [파라미터]
```

---

## 필수 키워드

### 텍스처

```
ink wash, sumi-e style,
hanji paper texture, korean paper,
rough stone texture, weathered,
calligraphy brush strokes
```

### 색상

```
muted colors, desaturated,
black and deep blue dominant,
subtle red accents, crimson touch,
ochre highlights, aged gold
```

### 조명

```
single light source, dramatic lighting,
chiaroscuro, rim lighting,
candlelit, lantern glow,
moonlit, torch light
```

### 분위기

```
mysterious, atmospheric,
ancient modern fusion, ritualistic,
haunting, ethereal,
cinematic, dark aesthetic
```

---

## 존재별 프롬프트

### 도깨비 (Dokkaebi)

```
shadowy dokkaebi figure, asymmetrical horns,
rough stone texture, hanji paper background,
single glowing eye, ink wash style,
mysterious, unsettling,
--ar 16:9 --style raw --s 250
```

변형:
```
dokkaebi silhouette emerging from darkness,
one horn visible, smoky presence,
ancient korean spirit, not cute,
menacing guardian, ink splatter effect,
--ar 16:9 --style raw
```

### 해태 (Haetae)

```
haetae stone guardian, weathered statue,
moss and age, palace courtyard,
single lantern light, watching pose,
ink wash atmospheric, dignified,
--ar 16:9 --style raw --s 250
```

변형:
```
haetae figure at boundary line,
half in shadow half in light,
ancient judge presence, stone texture,
korean mythology modern interpretation,
--ar 16:9 --style raw
```

### 탈 (Tal)

```
korean tal mask floating in darkness,
hanji paper texture, cracked surface,
theatrical, persona concept,
ink wash style, single spotlight,
--ar 16:9 --style raw --s 250
```

변형:
```
collection of tal masks arrangement,
different expressions, social roles,
wooden texture, aged paint,
dramatic shadows, museum display feel,
--ar 16:9 --style raw
```

### 인간 (Human)

**기본 실루엣:**
```
faceless human figure, traditional korean hanbok,
seen from behind, anonymous,
ink wash silhouette, hanji background,
isolated, small in frame,
--ar 16:9 --style raw --s 250
```

**걷는 자:**
```
anonymous figure walking away,
flowing simple garment, bare feet,
path disappearing into fog,
ink wash style, lonely atmosphere,
--ar 16:9 --style raw --s 250
```

**멈춘 자:**
```
solitary figure standing still,
head bowed, side view,
shadow covering face,
contemplative, frozen moment,
--ar 16:9 --style raw --s 250
```

**돌아서는 자:**
```
figure in mid-turn, motion blur,
glimpse of face hidden by hair,
pivoting moment, uncertain direction,
ink wash motion effect,
--ar 16:9 --style raw --s 250
```

**마주 보는 자:**
```
two silhouettes facing each other,
distance between them,
ink wash figures, no features,
tension without conflict,
--ar 16:9 --style raw --s 250
```

---

## 배경/환경 프롬프트

### 궁/단청

```
korean palace interior, dancheong patterns,
geometric painted ceiling, wooden pillars,
lantern light only, deep shadows,
ancient architecture, ink wash style,
--ar 16:9 --style raw
```

### 섬/바다

```
isolated island silhouette, korean sea,
foggy atmosphere, boundary between worlds,
ink wash ocean, hanji paper sky,
liminal space, mysterious,
--ar 16:9 --style raw
```

### 지도/기록

```
ancient korean map, worn edges,
ink drawings, official seals,
candlelit desk, scholarly atmosphere,
documents and records, historical feel,
--ar 16:9 --style raw
```

### 시스템/기계

```
korean mechanical device, gears and wood,
dancheong patterns on machinery,
impossible mechanism, ritualistic machine,
dark workshop, single light source,
--ar 16:9 --style raw
```

---

## 구간별 샷 프롬프트

### Intro 샷

```
establishing shot, korean landscape,
fog and mystery, dawn or dusk,
ink wash panorama, minimal presence,
atmospheric, world building,
--ar 16:9 --style raw
```

### Verse 샷

```
medium shot, single figure,
contemplative mood, shadows dominant,
hanji paper texture overlay,
subtle movement implied,
--ar 16:9 --style raw
```

### Drop 샷

```
close up, intense detail,
dramatic lighting, high contrast,
action implied, energy peak,
ink splatter effects, dynamic,
--ar 16:9 --style raw
```

### Outro 샷

```
wide shot, figure retreating,
fade to darkness, lingering,
open ended composition,
ink wash dissolving edges,
--ar 16:9 --style raw
```

---

## 파라미터 가이드

### 기본 설정

```
--ar 16:9        (영상용 비율)
--style raw      (덜 처리된 스타일)
--s 250          (스타일화 중간)
--c 20           (약간의 변형)
```

### 상황별 조정

| 상황 | 파라미터 |
|------|----------|
| 디테일 필요 | --s 100 |
| 추상적 | --s 750 |
| 일관성 필요 | --c 0 |
| 다양성 필요 | --c 50 |

### 버전 참고

```
--v 6.1          (최신, 사실적)
--niji 6         (애니메이션 스타일 - 권장 안 함)
```

---

## 피해야 할 키워드

```
❌ cute, kawaii, chibi
❌ anime, manga style
❌ bright colors, neon
❌ 3D render, CGI look
❌ photorealistic (완전히)
❌ happy, cheerful
❌ japanese (일본 요소)
❌ chinese (중국 요소 명시)
```

---

## Shot Library 구축

### 권장 구성 (40장)

| 카테고리 | 수량 | 내용 |
|----------|------|------|
| 도깨비 | 8장 | 다양한 각도/상황 |
| 해태/궁 | 6장 | 관찰/경계 장면 |
| 탈/연극 | 10장 | 마스크, 의례 |
| 단청-기계 | 10장 | 시스템 비주얼 |
| 섬/바다/지도 | 6장 | 경계 공간 |

### 워크플로우

1. **1차 생성**: 카테고리별 20장씩
2. **선별**: 베스트 10장씩 선정
3. **변형**: 선정본 기반 변형 생성
4. **최종**: 40장 라이브러리 완성

---

## Phase별 스타일 차이

| Phase | 밝기 | 색상 특징 | 추가 키워드 |
|-------|------|----------|-----------|
| Phase A | 45% | 먹색 80%, 악센트 5% | `balanced, emerging` |
| Phase B | 40% | 먹색 75%, 악센트 15% | `tense, borders blurring` |
| Phase C | 35% | 먹색 70%, 청록 등장 | `traces, recorded, heavy` |
| Phase 0 | 30% | 먹색 85%, 악센트 최소 | `primordial, origin, minimal` |

### Phase별 공통 suffix

**Phase A:**
```
, balanced atmosphere, subtle tension,
system with deviation,
--ar 16:9 --style raw --s 250
```

**Phase B:**
```
, intense atmosphere, borders dissolving,
erasure beginning,
--ar 16:9 --style raw --s 300
```

**Phase C:**
```
, heavy atmosphere, traces remaining,
record and memory,
--ar 16:9 --style raw --s 200
```

**Phase 0:**
```
, primordial darkness, origin moment,
minimal presence, ancient,
--ar 16:9 --style raw --s 350
```

---

## 이미지 품질 평가 기준

### 평가 항목 (각 2점, 총 10점)

| 기준 | 0점 | 1점 | 2점 |
|------|-----|-----|-----|
| 색상 | 팔레트 무시 | 일부 맞음 | 완벽히 맞음 |
| 텍스처 | 매끈/CG | 일부 한지 | 먹/한지 느낌 |
| 조명 | 밝음/다중 광원 | 애매함 | 단일 광원/로우키 |
| 구도 | 평범함 | 일부 여백 | 의도적 여백 |
| 분위기 | 밝음/귀여움 | 중립 | 어둡고 쿨함 |

### 점수별 판정

| 점수 | 판정 | 조치 |
|------|------|------|
| 9-10 | 채택 | 라이브러리 추가 |
| 7-8 | 후보 | Vary로 개선 시도 |
| 5-6 | 보류 | 프롬프트 수정 후 재생성 |
| 0-4 | 폐기 | 새 프롬프트 |

---

## 스타일 참조 (--sref) 가이드

### 스타일 참조 사용법

```
[프롬프트] --sref [이미지URL] --sw 100
```

### --sw (스타일 가중치)

| 값 | 효과 | 사용 |
|-----|------|------|
| 50 | 약한 영향 | 영감만 |
| 100 | 중간 (기본) | 대부분 |
| 200 | 강한 영향 | 일관성 필요 시 |

### 결 스타일 참조 이미지 유형

| 유형 | 설명 | 사용 |
|------|------|------|
| 먹 번짐 | sumi-e, ink wash | 기본 텍스처 |
| 한지 | paper texture | 배경 |
| 단청 | dancheong pattern | 시스템 장면 |
| 로우키 | chiaroscuro | 조명 참조 |

### 스타일 참조 조합

```
--sref [먹번짐URL] [한지URL] --sw 150
```

> 여러 참조 이미지 조합으로 복합 스타일 생성 가능

---

## 캐릭터 참조 (--cref) 가이드

### 존재별 캐릭터 참조

> 결의 존재들은 "캐릭터"가 아니지만, 일관성을 위해 참조 사용 가능

### 사용 원칙

| 원칙 | 설명 |
|------|------|
| 실루엣만 | 얼굴/디테일 고정 ❌ |
| 기능적 일관성 | 뿔/갈기 등 핵심 요소만 |
| 변형 허용 | 완전히 같을 필요 없음 |

### --cw (캐릭터 가중치)

| 값 | 효과 | 사용 |
|-----|------|------|
| 0 | 참조 무시 | 새로운 변형 |
| 50 | 약한 참조 | 기본 (권장) |
| 100 | 강한 참조 | 연속 장면 |

### 존재별 참조 전략

| 존재 | 고정 요소 | 변형 허용 |
|------|----------|----------|
| 도깨비 | 비대칭 뿔 | 질감, 크기, 각도 |
| 해태 | 사자-용 하이브리드 | 포즈, 이끼 양 |
| 탈 | 빈 눈구멍 | 표정, 갈라짐 |
| 인물 | 실루엣 비율 | 의상, 포즈 |

---

## 앨범별 비주얼 톤 차이

### 앨범별 색상 설정

| 앨범 | 주조색 | 악센트 | 배경 |
|------|--------|--------|------|
| A-1 | 먹색 80% | 빨강 5% | 따뜻한 종이 |
| A-2 | 먹색 78% | 빨강 8% | 탁한 종이 |
| B-1 | 먹색 75% | 빨강 15% | 짙은 남색 |
| B-2 | 먹색 73% | 빨강 18% | 거의 검정 |
| C-1 | 먹색 70% | 청록 10% | 회색 종이 |
| C-2 | 먹색 68% | 청록 12% | 탈색된 느낌 |
| 0 | 먹색 85% | 없음 | 어둠 |

### 앨범별 프롬프트 suffix

**Album A-1:**
```
, balanced atmosphere, emerging system,
subtle hints, not too dark,
--ar 16:9 --style raw --s 250
```

**Album B-1:**
```
, tense atmosphere, borders dissolving,
more intense, confrontation,
--ar 16:9 --style raw --s 300
```

**Album C-1:**
```
, heavy atmosphere, traces only,
fading presence, recorded memory,
--ar 16:9 --style raw --s 200
```

**Album 0:**
```
, primordial darkness, before everything,
origin moment, pure atmosphere,
--ar 16:9 --style raw --s 350
```

### 앨범 진행에 따른 변화

```
A-1 → A-2: 악센트 증가, 긴장 시작
B-1 → B-2: 어두워짐, 경계 모호
C-1 → C-2: 탈색, 흔적화
```

---

## 체크리스트

### 이미지 생성 전

- [ ] 텍스처 키워드 포함?
- [ ] 색상 키워드 포함?
- [ ] 조명 키워드 포함?
- [ ] 피해야 할 키워드 제거?
- [ ] 파라미터 설정?
- [ ] Phase별 suffix 적용?

### 이미지 생성 후

- [ ] 결 색상 팔레트와 맞는가?
- [ ] 텍스처가 적절한가?
- [ ] 조명이 단일 광원인가?
- [ ] 분위기가 쿨한가?
- [ ] 일본/중국 요소 없는가?
- [ ] Phase 분위기가 맞는가?

---

## 비디오 생성 가이드

### MV 구성 원칙

```
1 MV (3-4분) = 15-25 클립 조합
├── 정적 컷 (40%): Midjourney Video
├── 인물 동작 (30%): Veo
├── 역동적 컷 (20%): Sora
└── 이미지 패닝 (10%): Ken Burns 효과
```

### 클립 길이 가이드

| 구간 | 평균 클립 길이 | 컷 수 |
|------|--------------|-------|
| Intro | 5-8초 | 2-3 |
| Verse | 3-5초 | 6-8 |
| Pre-Chorus | 2-4초 | 4-5 |
| Drop | 1-3초 | 8-12 |
| Break | 5-10초 | 1-2 |
| Outro | 5-8초 | 2-3 |

---

## Midjourney Video 프롬프트

### 사용 상황
- 배경 천천히 움직이는 장면
- 안개/연기/먹 번짐 효과
- 정적 인물 주변 환경 변화
- 조명 변화 (촛불 흔들림)

### 프롬프트 구조

```
[이미지 프롬프트] + [모션 키워드] + --video
```

### 모션 키워드

```
slow drift, subtle movement,
atmospheric shift, fog rolling,
light flickering, smoke rising,
gentle camera push, slight zoom
```

### 예시 프롬프트

**배경 안개:**
```
korean mountain landscape, ink wash style,
fog slowly rolling through valleys,
atmospheric, mysterious, slow movement,
--ar 16:9 --style raw --video
```

**촛불 장면:**
```
single candle in darkness, hanji paper,
flickering light, shadows dancing,
intimate, atmospheric, minimal movement,
--ar 16:9 --style raw --video
```

**먹 번짐:**
```
ink spreading on wet paper,
calligraphy brush strokes forming,
slow diffusion, meditative,
--ar 16:9 --style raw --video
```

---

## Veo 프롬프트 가이드

### 사용 상황
- 인물 실루엣 걷기/서기/돌아보기
- 탈 회전, 손 움직임
- 자연스러운 의상 펄럭임
- 느린 인물 동작

### 프롬프트 구조

```
A [주체], [동작], [환경], [스타일], [분위기]
```

### 핵심 키워드

```
silhouette figure, anonymous person,
slow walking, turning away,
flowing hanbok, ink wash aesthetic,
atmospheric lighting, mysterious
```

### 예시 프롬프트

**걷는 인물:**
```
A silhouette figure in flowing hanbok walking slowly
through fog, seen from behind, anonymous,
ink wash style, single light source from above,
atmospheric, mysterious, cinematic
```

**돌아보는 인물:**
```
Anonymous figure in simple garment turning to look back,
face hidden in shadow, motion blur on hair,
korean traditional architecture background,
ink wash atmospheric, dramatic lighting
```

**탈 회전:**
```
Korean tal mask slowly rotating in darkness,
cracked wooden surface, theatrical lighting,
single spotlight, hanji paper texture background,
unsettling, hypnotic rotation
```

### Veo 설정

| 설정 | 권장값 |
|------|-------|
| 길이 | 5-10초 |
| 해상도 | 1080p |
| 스타일 | Cinematic |
| 모션 강도 | Low-Medium |

---

## Sora 프롬프트 가이드

### 사용 상황
- 드라마틱 카메라 무브
- 빠른 트랜지션
- 도깨비/해태 등장 장면
- 액션성 있는 순간

### 프롬프트 구조

```
[카메라 움직임] + [주체] + [동작] + [환경] + [스타일]
```

### 카메라 키워드

```
dramatic camera push, sweeping crane shot,
quick dolly in, rotating around subject,
smooth tracking shot, dynamic angle shift
```

### 예시 프롬프트

**도깨비 등장:**
```
Dramatic camera push into darkness,
a dokkaebi figure with asymmetrical horns
emerging from shadows, stone texture,
ink splatter effect, single glowing eye,
unsettling, mythical, cinematic
```

**해태 시선:**
```
Sweeping camera reveals stone haetae guardian,
weathered statue with moss, watching silently,
palace courtyard at dusk, lantern light,
dramatic atmosphere, ancient modern fusion
```

**트랜지션 (씬 전환):**
```
Quick camera rotation through ink wash clouds,
transitioning from interior to exterior,
korean architecture elements morphing,
dreamlike, fluid movement, surreal
```

### Sora 설정

| 설정 | 권장값 |
|------|-------|
| 길이 | 5-20초 |
| 해상도 | 1080p+ |
| 스타일 | Cinematic |
| 카메라 | Dynamic |

---

## 도구별 사용 비율

### MV 구간별 도구 배합

| 구간 | MJ Video | Veo | Sora | 이미지 |
|------|----------|-----|------|--------|
| Intro | 60% | 20% | 10% | 10% |
| Verse | 30% | 50% | 10% | 10% |
| Pre-Chorus | 20% | 40% | 30% | 10% |
| Drop | 10% | 30% | 50% | 10% |
| Break | 70% | 20% | 0% | 10% |
| Outro | 50% | 30% | 10% | 10% |

### 존재별 도구 선호

| 존재 | 선호 도구 | 이유 |
|------|----------|------|
| 도깨비 | Sora | 갑작스러운 등장, 역동성 |
| 해태 | MJ Video | 정적, 관찰자 |
| 탈 | Veo | 회전, 느린 동작 |
| 인물 | Veo | 자연스러운 움직임 |
| 환경 | MJ Video | 분위기 유지 |

---

## 스타일 일관성 유지

### 시드 고정 전략

```
1. 기준 이미지 생성 (시드 기록)
2. 같은 시드로 변형 생성
3. --sref로 스타일 참조
4. 비디오 생성 시 이미지 기반
```

### 일관성 체크리스트

- [ ] 색상 팔레트 통일?
- [ ] 조명 방향 일관?
- [ ] 텍스처 (먹/한지) 유지?
- [ ] 캐릭터 실루엣 일관?
- [ ] 분위기 톤 통일?

### 프롬프트 템플릿 시스템

모든 프롬프트에 공통 suffix 추가:

```
, ink wash aesthetic, hanji paper texture,
single light source, muted colors with subtle red accent,
dark k-pop visual style, korean mythic atmosphere
```

---

## MV 제작 워크플로우

### Step 1: 이미지 생성 (1-2일)

```
1. 트랙별 핵심 장면 10-15개 정의
2. Midjourney로 키 비주얼 생성
3. 시드/프롬프트 기록
4. 스타일 참조 이미지 선정
```

### Step 2: 비디오 클립 생성 (2-3일)

```
1. 장면별 도구 선택
2. 이미지 기반 비디오 생성
3. 각 클립 5-10초
4. 대안 클립 준비 (클립당 2-3개)
```

### Step 3: 편집 (1-2일)

```
1. 타임라인 배치
2. 컷 편집 (음악 싱크)
3. 트랜지션 추가
4. 컬러 그레이딩
5. 최종 출력
```

### 주간 MV 제작 일정

| 요일 | 작업 | 산출물 |
|------|------|--------|
| 월-화 | 이미지 생성 | 키 비주얼 15장 |
| 수-목 | 비디오 클립 | 클립 20-30개 |
| 금 | 편집 | 초안 MV |
| 토 | 수정/QC | 최종 MV |
| 일 | 숏폼 추출 | Shorts/Reels |

---

## 비디오 체크리스트

### 클립 생성 전

- [ ] 이미지 기준 설정?
- [ ] 시드/스타일 참조 준비?
- [ ] 도구 선택 완료?
- [ ] 모션 방향 결정?

### 클립 생성 후

- [ ] 스타일 일관성?
- [ ] 움직임 자연스러움?
- [ ] 길이 적절?
- [ ] 편집에 사용 가능?

### MV 완성 후

- [ ] 음악 싱크 정확?
- [ ] 컷 전환 자연스러움?
- [ ] 색상 일관?
- [ ] 숏폼 추출 포인트 기록?

---

## 관련 문서

- [[02_style/VISUAL_COLOR]] — 색상 팔레트
- [[02_style/VISUAL_TEXTURE]] — 텍스처 규칙
- [[02_style/VISUAL_PIPELINE]] — 제작 파이프라인
- [[03_characters/DOKKAEBI]] — 도깨비 비주얼
- [[04_strategy/ALBUM_STRUCTURE]] — 앨범 구조
- [[05_execution/SUNO_PROMPTS]] — 음악 프롬프트

---

*End of VISUAL_PROMPTS*
