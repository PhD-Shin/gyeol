---
title: "GYEOL Midjourney Prompts"
type: execution
locked: false
version: 1.0
last_updated: 2025-01-10
description: "결 Midjourney AI 이미지 생성 프롬프트 가이드."
use_when: "Midjourney로 이미지 생성할 때, Shot Library 구축 시"
tags: [execution, midjourney, ai, prompts, visual]
related:
  - "[[02_style/VISUAL_COLOR]]"
  - "[[02_style/VISUAL_TEXTURE]]"
  - "[[02_style/VISUAL_PIPELINE]]"
---

# MIDJOURNEY_PROMPTS — Midjourney 프롬프트 가이드

> **이 문서가 필요한 순간:**
> - Midjourney로 이미지를 생성할 때
> - Shot Library를 구축할 때
> - 결 스타일 비주얼을 만들 때

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

```
faceless human figure, traditional korean hanbok,
seen from behind, anonymous,
ink wash silhouette, hanji background,
isolated, small in frame,
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

## 체크리스트

생성 전:

- [ ] 텍스처 키워드 포함?
- [ ] 색상 키워드 포함?
- [ ] 조명 키워드 포함?
- [ ] 피해야 할 키워드 제거?
- [ ] 파라미터 설정?

생성 후:

- [ ] 결 색상 팔레트와 맞는가?
- [ ] 텍스처가 적절한가?
- [ ] 조명이 단일 광원인가?
- [ ] 분위기가 쿨한가?
- [ ] 일본/중국 요소 없는가?

---

## 관련 문서

- [[02_style/VISUAL_COLOR]] — 색상 팔레트
- [[02_style/VISUAL_TEXTURE]] — 텍스처 규칙
- [[02_style/VISUAL_PIPELINE]] — 제작 파이프라인
- [[03_characters/DOKKAEBI]] — 도깨비 비주얼

---

*End of MIDJOURNEY_PROMPTS*
