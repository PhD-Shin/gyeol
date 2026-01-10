---
title: "GYEOL Gemini Workflow"
type: execution
locked: false
version: 1.0
last_updated: 2025-01-11
description: "Gemini CLI를 활용한 음악 분석 → 비주얼 제작 워크플로우"
use_when: "음악 완성 후 비주얼 제작 시, 타임라인 기반 이미지/영상 생성 시"
tags: [execution, gemini, ai, workflow, visual, timeline]
related:
  - "[[05_execution/SUNO_PROMPTS]]"
  - "[[05_execution/MIDJOURNEY_PROMPTS]]"
  - "[[02_style/VISUAL_EDIT]]"
  - "[[02_style/AUDIO_STRUCTURE]]"
---

# GEMINI_WORKFLOW — Gemini 음악 분석 워크플로우

> **이 문서가 필요한 순간:**
> - Suno에서 음악이 완성되었을 때
> - 음악에 맞는 비주얼을 제작할 때
> - 타임라인 기반 이미지/영상 프롬프트가 필요할 때

---

## 워크플로우 개요

```
[Suno 음악 완성]
    ↓
[Gemini CLI로 음악 분석]
    ↓
[타임라인 + 감정/분위기 맵 생성]
    ↓
[구간별 MJ 프롬프트 생성]
    ↓
[이미지/영상 제작]
```

---

## Step 1: 음악 파일 준비

```bash
# 음악 파일 경로 확인
ls ~/Downloads/*.mp3
```

| 포맷 | 권장 |
|------|------|
| MP3 | ⭕ (Gemini 지원) |
| WAV | ⭕ |
| M4A | ⭕ |

---

## Step 2: Gemini CLI 음악 분석

### 기본 명령어

```bash
gemini -p "이 음악을 분석해주세요:
1. 전체 구조 (Intro, Verse, Pre-Chorus, Drop, Break, Outro)
2. 각 구간의 시작/끝 타임스탬프 (초 단위)
3. 각 구간의 감정/분위기 (한 단어로)
4. 에너지 레벨 (1-10)
5. 주요 악기/사운드
6. 클라이맥스 순간

결과를 테이블 형식으로 출력해주세요." \
-f ~/Downloads/track.mp3
```

### 예상 출력

```
| 구간 | 시작 | 끝 | 분위기 | 에너지 | 주요 사운드 |
|------|------|-----|--------|--------|------------|
| Intro | 0:00 | 0:12 | 고요 | 3 | 가야금, 앰비언트 |
| Verse 1 | 0:12 | 0:42 | 긴장 | 4 | 808, 속삭임 |
| Pre-Chorus | 0:42 | 0:58 | 빌드업 | 6 | 신스, 레이어 |
| Drop 1 | 0:58 | 1:28 | 폭발 | 9 | 풀비트, 장구 |
| Break | 1:28 | 1:35 | 무음 | 1 | 잔향만 |
| Drop 2 | 1:35 | 2:05 | 클라이맥스 | 10 | 최고조 |
| Outro | 2:05 | 2:30 | 여운 | 3 | 가야금 솔로 |
```

---

## Step 3: 비주얼 프롬프트 생성 요청

### Gemini에 추가 요청

```bash
gemini -p "위 분석 결과를 바탕으로 각 구간에 맞는 Midjourney 프롬프트를 생성해주세요.

조건:
- 결 프로젝트 스타일: 어둡고 쿨하고 한국적
- 필수 키워드: hanji paper texture, ink wash, dark atmospheric
- 비율: 16:9
- 각 구간당 2-3개 이미지

형식:
구간: [구간명] (시작-끝)
분위기: [분위기]
MJ 프롬프트 1: [프롬프트]
MJ 프롬프트 2: [프롬프트]
" \
-f ~/Downloads/track.mp3
```

---

## Step 4: 타임라인 기반 이미지 배치

### 이미지 개수 산정

| 음악 길이 | 기본 간격 | 이미지 개수 |
|----------|----------|------------|
| 2:00 | 4초 | 30장 |
| 2:30 | 5초 | 30장 |
| 3:00 | 6초 | 30장 |
| 3:30 | 7초 | 30장 |
| 4:00 | 6초 | 40장 |

### 구간별 배분 예시 (3분 곡)

| 구간 | 시간 | 이미지 수 | 비고 |
|------|------|----------|------|
| Intro (15초) | 0:00-0:15 | 3장 | 5초/장 |
| Verse (30초) | 0:15-0:45 | 5장 | 6초/장 |
| Pre-Chorus (15초) | 0:45-1:00 | 3장 | 5초/장 |
| Drop 1 (30초) | 1:00-1:30 | 8장 | 4초/장 (빠름) |
| Break (10초) | 1:30-1:40 | 2장 | 5초/장 |
| Drop 2 (35초) | 1:40-2:15 | 10장 | 3.5초/장 (가장 빠름) |
| Outro (15초) | 2:15-2:30 | 4장 | 4초/장 |
| **합계** | **2:30** | **35장** | |

---

## Step 5: 자동화 스크립트 (선택)

### 분석 → 프롬프트 생성 통합

```bash
#!/bin/bash
# analyze_and_prompt.sh

TRACK=$1
OUTPUT_DIR="./output"

mkdir -p $OUTPUT_DIR

# Step 1: 음악 분석
gemini -p "이 음악의 구조를 JSON 형식으로 분석해주세요:
{
  \"sections\": [
    {\"name\": \"구간명\", \"start\": 0, \"end\": 12, \"mood\": \"분위기\", \"energy\": 5}
  ],
  \"total_length\": 180,
  \"key_moments\": [\"클라이맥스 타임스탬프\"]
}" -f "$TRACK" > "$OUTPUT_DIR/analysis.json"

# Step 2: 프롬프트 생성
gemini -p "$(cat $OUTPUT_DIR/analysis.json)

위 분석을 바탕으로 각 구간별 Midjourney 프롬프트를 생성해주세요.
결 스타일: dark, korean, atmospheric, hanji texture
--ar 16:9 --style raw" > "$OUTPUT_DIR/prompts.md"

echo "분석 완료: $OUTPUT_DIR"
```

---

## Gemini 분석 요청 템플릿

### 템플릿 A: 기본 분석

```
이 음악을 분석해주세요:
1. 구조 (각 구간의 시작/끝 시간)
2. 감정 변화 곡선
3. 클라이맥스 순간
4. 주요 악기/사운드
```

### 템플릿 B: 비주얼 매칭

```
이 음악에 어울리는 비주얼을 제안해주세요:
- 각 구간별 색상 팔레트
- 카메라 움직임 (느림/빠름)
- 주요 피사체
- 조명 분위기
```

### 템플릿 C: 가사 타이밍

```
이 음악의 보컬/가사가 나오는 정확한 타이밍을 초 단위로 알려주세요.
각 가사 파트가 시작하고 끝나는 시간을 테이블로 정리해주세요.
```

---

## 주의사항

### Gemini 분석 한계

| 한계 | 대응 |
|------|------|
| 정확한 BPM 측정 어려움 | Suno 설정 참조 |
| 미세한 타이밍 오차 | ±2초 여유 |
| 한국어 가사 인식 | 가사 파일 별도 제공 |

### 권장 사항

1. **음악 품질**: 최종 마스터링 버전 사용
2. **파일 크기**: 50MB 이하 권장
3. **반복 검증**: 중요 타임스탬프는 직접 확인

---

## 워크플로우 체크리스트

- [ ] Suno에서 최종 음악 다운로드
- [ ] Gemini CLI로 구조 분석
- [ ] 타임스탬프 테이블 생성
- [ ] 구간별 이미지 개수 결정
- [ ] MJ 프롬프트 생성
- [ ] 이미지 생성 및 확인
- [ ] 타임라인에 배치

---

## 관련 문서

- [[05_execution/SUNO_PROMPTS]] — 음악 프롬프트
- [[05_execution/MIDJOURNEY_PROMPTS]] — 비주얼 프롬프트
- [[02_style/VISUAL_EDIT]] — 편집 규칙
- [[02_style/AUDIO_STRUCTURE]] — 곡 구조

---

*End of GEMINI_WORKFLOW*
