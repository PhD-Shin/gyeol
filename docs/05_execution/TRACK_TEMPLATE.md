---
title: "GYEOL Track Template"
type: execution
locked: false
version: 1.1
last_updated: 2025-01-11
description: "결 트랙 제작 템플릿. 새 트랙 기획 시 복사하여 사용."
use_when: "새 트랙 기획 시, 트랙 문서 작성 시"
tags: [execution, template, track, production]
related:
  - "[[PROCESS]]"
  - "[[05_execution/QC_CHECKLIST]]"
  - "[[05_execution/SUNO_PROMPTS]]"
  - "[[05_execution/MIDJOURNEY_PROMPTS]]"
  - "[[04_strategy/PHASE_MAP]]"
  - "[[01_world/RULES]]"
  - "[[01_world/THEMES]]"
  - "[[02_style/AUDIO_CORE]]"
  - "[[02_style/VISUAL_COLOR]]"
---

# TRACK_TEMPLATE — 트랙 제작 템플릿

> **이 문서가 필요한 순간:**
> - 새 트랙을 기획할 때
> - 트랙 문서를 작성할 때
> - 제작 진행 상황을 추적할 때

---

## 사용법

1. 이 파일을 복사
2. `docs/06_tracks/[트랙명].md`로 저장
3. 아래 섹션 채우기
4. 진행 상황 업데이트

---

# [트랙 제목] — [로마자 표기]

> **한 줄 정의:**
> [이 트랙이 표현하는 핵심을 한 문장으로]

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 제목 (한글) | |
| 제목 (로마자) | |
| Phase | A / B / C / 0 |
| 시즌 | Season 1 |
| 길이 (목표) | 2:30-3:00 |
| 상태 | 기획 / 제작중 / 완료 |

---

## 테마 연결

### 메타 테마 (1-2개 선택)
- [ ] Border (경계)
- [ ] Name (이름)
- [ ] Record (기록)
- [ ] Erasure (지움)
- [ ] Ritual (의례)
- [ ] System vs Deviation (시스템과 어긋남)

### 작동 규칙 연결
| 규칙 | 이 트랙에서의 표현 |
|------|-------------------|
| 시간 | |
| 움직임 | |
| 반복 | |
| 개입 | |
| 사라짐 | |

---

## 오디오 설계

### 구조

```
[Intro] 0:00-0:__
  악기:
  분위기:

[Verse 1] 0:__-0:__
  악기:
  분위기:

[Pre-Chorus] 0:__-0:__
  악기:
  분위기:

[Drop 1] 0:__-0:__
  악기:
  분위기:

[Break] 0:__-0:__
  악기:
  분위기:

[Drop 2] 0:__-0:__
  악기:
  분위기:

[Outro] 0:__-0:__
  악기:
  분위기:
```

### Suno 프롬프트 (K-판소리 판타지 트랩)

> **A/B/C 테스트**: 3가지 버전 각 4개씩 생성 후 선별
> **선별 기준**: 첫3초훅(30%) | 해금(20%) | 몽환↔폭발(20%) | 보컬(15%) | 밸런스(15%)

#### 🅰️ Style A — 판소리 강조
```
dark korean pansori fantasy trap fusion, [BPM] bpm [Key], dreamy ethereal synth pads on verses, pansori chang shout hook first 3 seconds chuimsae, orchestral swells before drops, jajinmori jangdan on drops, jungjoongmori groove verses, haegeum haunting melodic texture, gayageum sharp stabs, janggu layered 808, raw emotional korean vocals pitch bending guttural, aniri storytelling rap, vocal percussion texture, cinematic atmosphere, [Intro] pansori shout chuimsae 808 haegeum explosion 3s silence 2s, [Verse] dreamy synth aniri storytelling [길이]s, [PreChorus] orchestral swell building [길이]s, [Drop] chang jajinmori 808 gayageum explosive [길이]s, [Verse2] ethereal space whisper [길이]s, [PreChorus2] building intensity [길이]s, [Drop2] overwhelming maximum energy [길이]s, [Bridge] haegeum melodic drone [길이]s, [Outro] dreamy fade [길이]s
```

#### 🅱️ Style B — 판타지 팝 강조
```
dark fantasy pop korean trap fusion, [BPM] bpm [Key], ethereal dreamy synth pads shimmering, explosive traditional korean shout hook first 3 seconds, cinematic orchestral swells before drops, fast traditional rhythm on drops, groovy mid-tempo verses, haegeum haunting melodic texture, string stabs, layered 808 bass, raw emotional vocals pitch bending, storytelling rap verses, atmospheric reverb, [Intro] explosive korean shout 808 string hit 3s silence 2s, [Verse] dreamy synth storytelling ethereal [길이]s, [PreChorus] orchestral swell strings building emotional [길이]s, [Drop] explosive fast rhythm 808 strings maximum energy [길이]s, [Verse2] ethereal space whisper floating [길이]s, [PreChorus2] building intensity dramatic [길이]s, [Drop2] overwhelming climax [길이]s, [Bridge] melodic drone emotional pad [길이]s, [Outro] dreamy atmospheric fade [길이]s
```

#### 🅲 Style C — 하이브리드 균형
```
dark korean fantasy trap pansori fusion, [BPM] bpm [Key], dreamy ethereal pads verses, korean traditional shout hook first 3 seconds, orchestral swells drops, jajinmori rhythm drops, groovy verses, haegeum melodic texture signature, gayageum stabs, janggu 808 layered, raw emotional korean vocals guttural pitch bend, aniri rap storytelling, vocal percussion layer subtle, cinematic dark atmosphere, [Intro] korean shout chuimsae 808 haegeum hit explosion 3s silence 2s, [Verse] dreamy synth aniri storytelling floating [길이]s, [PreChorus] orchestral swell emotional building [길이]s, [Drop] chang jajinmori 808 gayageum explosive energy [길이]s, [Verse2] ethereal whisper space [길이]s, [PreChorus2] intensity building [길이]s, [Drop2] maximum overwhelming climax [길이]s, [Bridge] haegeum drone pad [길이]s, [Outro] dreamy haegeum fade [길이]s
```

### 가사 템플릿 (K-pop 코드스위칭 + 추임새)

> **핵심 원칙**: 같은 의미 반복 ❌ → 영어+한국어가 **연결/확장**
> **추임새**: 전통(얼쑤/좋다/그렇지) + 현대(가자/간다)

```
[Intro]
[한국어 훅]!
(explosive shout + 808 + haegeum)
얼쑤—

(silence)

[Verse 1]
(dreamy, ethereal)
[영어 시작] [한국어 연결]     ← 연결 (다른 의미)
[한국어 상황] [영어 감각]     ← 확장 (감각 추가)
[영어 변화] [한국어 장소]     ← 이어짐 (장소)
[한국어 행동] [영어 정도]     ← 이어짐 (깊이)

[Pre-Chorus]
(orchestral swell)
[한국어 상태] [영어 상태]     ← 다른 의미
[한국어 훅]
좋다—

[Drop]
(explosive + fast rhythm)
[영어 행동] [한국어 결과]     ← 원인→결과
[영어 행동] [한국어 결과]
얼쑤!
[한국어 장소] [영어 결과]     ← 장소+결과
그렇지— 가자

[Verse 2]
(ethereal whisper)
[영어 시작] [한국어 감각]
[한국어 상황] [영어 인지]
[영어 상황] [한국어 결론]

[Pre-Chorus 2]
[한국어 상태] [영어 상태]
[한국어 훅]
간다—

[Drop 2]
(maximum energy)
[영어 행동] [한국어 결과]
[영어 행동] [한국어 결과]
얼쑤!
[한국어 상태] [영어 상태]
좋다—

[Bridge]
(haegeum + pad)

[Outro]
(dreamy fade)
[한국어 마무리]...
```

### 코드스위칭 패턴 가이드

| 패턴 | 영어 | 한국어 | 예시 |
|------|------|--------|------|
| **연결** | 원인/행동 | 결과 | "Let it burn 재만 남아" |
| **확장** | 상황 | 감각/느낌 | "숨이 막혀 I can feel it" |
| **이어짐** | 시작 | 계속/깊이 | "빠져들어 deeper now" |

### ❌ 피해야 할 패턴

```
❌ Can't stop 멈출 수 없어     ← 같은 의미 반복!
❌ Burn it all 다 태워버려     ← 같은 의미 반복!
```

### 추임새 사용 맵 (템플릿)

| 추임새 | 타입 | 위치 | 효과 |
|--------|------|------|------|
| **Eolssu (얼쑤)** | 전통 | Intro, Drop | 폭발, 정체성 |
| **Yeah 좋다** | 하이브리드 | Pre-Chorus, Drop | 만족 + 트랩 |
| **그렇지** | 전통 | Drop | 동의, 강조 |
| **가자** | 현대 | Drop 끝 | 전진, 에너지 |
| **간다** | 현대 | Pre-Chorus 2 | 돌진, 빌드업 |

---

## 비주얼 설계

### 핵심 이미지 3개

1. **[이미지명]**
   - 구간:
   - 설명:
   - 색상:

2. **[이미지명]**
   - 구간:
   - 설명:
   - 색상:

3. **[이미지명]**
   - 구간:
   - 설명:
   - 색상:

### 등장 존재

| 존재 | 등장 구간 | 역할 |
|------|----------|------|
| 도깨비 | | |
| 해태 | | |
| 탈 | | |
| 인간 | | |

### 색상 계획

| 구간 | 주조색 | 악센트 |
|------|--------|--------|
| Intro | | |
| Verse | | |
| Drop | | |
| Outro | | |

### Midjourney 프롬프트 (초안)

**장면 1:**
```

```

**장면 2:**
```

```

**장면 3:**
```

```

---

## 제작 체크리스트 (음악 먼저 워크플로우)

### Phase 1: 기획 + 음악
- [ ] 테마 연결 완료
- [ ] Suno 프롬프트 작성
- [ ] Suno 생성 (10+ 버전)
- [ ] **음악 베스트 1개 확정** ★

### Phase 2: 음악 분석 → 비주얼 기획
- [ ] 음악 분석 (무드/에너지/전환점)
- [ ] 시각화 키워드 도출
- [ ] MJ 프롬프트 생성 (음악 기반)

### Phase 3: 이미지 생성
- [ ] MJ 이미지 30장+ 생성
- [ ] 베스트 선별
- [ ] 스타일 일관성 체크

### Phase 4: 영상 + 편집
- [ ] 이미지 → 비디오 확장 (필요시)
- [ ] 오디오-비주얼 싱크
- [ ] 컬러 그레이딩
- [ ] 최종 렌더링

### Phase 5: QC
- [ ] [[05_execution/QC_CHECKLIST]] 통과
- [ ] 피드백 반영

---

## 금지 사항 체크

- [ ] 역사/정치 직접 언급 없음
- [ ] 지명/국가명 없음
- [ ] 감정 직접 설명 없음
- [ ] 민속 설명 없음
- [ ] 희망/구원 메시지 없음

---

## 참고 자료

### 영감 소스
-

### 참조 트랙
-

### 비주얼 레퍼런스
-

---

## 리소스 계획

### 시간 예산

| 단계 | 예상 시간 | 실제 시간 |
|------|----------|----------|
| 기획 | 3일 | |
| 오디오 | 4일 | |
| 비주얼 | 7일 | |
| 편집 | 4일 | |
| QC | 2일 | |
| **총계** | **20일** | |

### 비용 예산 (선택)

| 항목 | 예상 | 실제 |
|------|------|------|
| Suno 크레딧 | | |
| Midjourney 크레딧 | | |
| 추가 에셋 | | |
| **총계** | | |

### 제작 모드

- [ ] 1인 제작
- [ ] 협업 (역할 분담 아래 기입)

| 역할 | 담당 |
|------|------|
| 기획 | |
| 오디오 | |
| 비주얼 | |
| 편집 | |

---

## 리스크/대안

### 예상 리스크

| 리스크 | 대안 |
|--------|------|
| Suno 스타일 불일치 | 템플릿 변경, 추가 생성 |
| MJ 일관성 부족 | 시드 고정, 스타일 참조 |
| 일정 지연 | 컷 수 축소, 라이브러리 활용 |
| 품질 미달 | 부분 재작업, QC 항목 축소 |

---

## 앨범 내 위치

### 트랙 순서

| 항목 | 내용 |
|------|------|
| 앨범 내 순서 | Track _ of _ |
| 이전 트랙 | |
| 다음 트랙 | |

### 연결 계획

| 연결 | 방법 |
|------|------|
| 이전 트랙에서 연결 | 키: / BPM: |
| 다음 트랙으로 연결 | 키: / BPM: |
| 아웃트로 → 인트로 | |

---

## 버전 히스토리

| 버전 | 날짜 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| v0.1 | | 초안 작성 | |
| v0.5 | | 오디오 완료 | |
| v0.8 | | 비주얼 완료 | |
| v1.0 | | 최종 완료 | |

---

## 진행 로그

| 날짜 | 작업 내용 | 상태 |
|------|----------|------|
| | | |

---

## 관련 문서

- [[PROCESS]] — 제작 프로세스
- [[05_execution/QC_CHECKLIST]] — 품질 검사
- [[04_strategy/PHASE_MAP]] — Phase 확인

---

*End of TRACK_TEMPLATE*
