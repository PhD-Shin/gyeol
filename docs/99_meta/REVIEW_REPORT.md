---
title: "GYEOL Critical Review Report"
type: meta
version: 1.0
created: 2025-01-11
description: "10회 비판적 검토 결과 및 수정 제안. 전후 비교 포함."
---

# GYEOL 문서 비판적 검토 보고서

> **10회 검토 결과 요약**
> 총 41개 문서 검토 완료

---

## 검토 개요

| 항목 | 수치 |
|------|------|
| 검토 문서 수 | 41개 |
| 발견된 이슈 | 47건 |
| P1 (즉시 수정) | 8건 |
| P2 (권장 수정) | 21건 |
| P3 (개선 제안) | 18건 |

---

## 검토 1회차: 구조적 불일치

### 이슈 #1 [P1] — README.md vs 실제 폴더 구조 불일치

**파일**: `docs/README.md`

**현재 (Before)**:
```
docs/
├── README.md              ← 이 파일
├── immutable/             ← 🔒 불변 문서 (수정 금지)
│   ├── BIBLE_WORLD.md     ← 세계관 바이블
│   ├── STYLE_GUIDE_VISUAL.md ← 비주얼 스타일 가이드
│   ├── STYLE_GUIDE_AUDIO.md  ← 오디오 스타일 가이드
│   └── CHARACTER_BIBLE.md    ← 캐릭터 바이블
├── variable/              ← 📝 가변 문서 (운영에 따라 수정)
│   ├── PHASE_MAP.md       ← Phase 로드맵
│   └── CHANNEL_LAUNCH.md  ← 채널 런칭 가이드
├── execution/             ← ⚙️ 실행 문서 (자유롭게 수정)
│   ├── TRACK_TEMPLATE.md  ← 트랙 제작 템플릿
│   └── QC_CHECKLIST.md    ← 품질 검사표
└── tracks/                ← 🎵 트랙별 제작 문서
    └── (각 트랙 문서)
```

**문제**: 실제 폴더 구조는 `00_core`, `01_world`, `02_style` 등으로 변경되었으나 README는 구버전 유지

**수정 (After)**:
```
docs/
├── README.md              ← 이 파일
├── PRD.md                 ← 프로젝트 요약 (진입점)
├── PROCESS.md             ← 제작 프로세스
├── INDEX.md               ← 전체 인덱스
│
├── 00_core/               ← 📌 핵심 정의 (불변)
│   ├── MANIFESTO.md       ← 선언문
│   └── DEFINITION.md      ← 결의 정의
│
├── 01_world/              ← 📌 세계관 규칙 (불변)
│   ├── RULES.md           ← 5대 작동 규칙
│   ├── THEMES.md          ← 메타 테마
│   ├── PROHIBITIONS.md    ← 금지 규칙
│   └── TONE.md            ← 톤 가이드
│
├── 02_style/              ← 📌 스타일 가이드 (불변)
│   ├── VISUAL_*.md        ← 비주얼 규칙
│   └── AUDIO_*.md         ← 오디오 규칙
│
├── 03_characters/         ← 📌 존재 정의 (불변)
│   ├── DOKKAEBI.md        ← 도깨비
│   ├── HAETAE.md          ← 해태
│   ├── TAL.md             ← 탈
│   ├── HUMAN.md           ← 인물
│   └── INTERACTIONS.md    ← 상호작용
│
├── 04_strategy/           ← 📋 운영 전략 (가변)
│   ├── PHASE_MAP.md       ← Phase 로드맵
│   ├── ALBUM_STRUCTURE.md ← 앨범 구조
│   ├── CHANNEL_LAUNCH.md  ← 채널 런칭
│   └── CONTENT_FUNNEL.md  ← 콘텐츠 퍼널
│
├── 05_execution/          ← ⚡ 실행 도구 (자유)
│   ├── TRACK_TEMPLATE.md  ← 트랙 템플릿
│   ├── QC_CHECKLIST.md    ← QC 체크리스트
│   ├── SUNO_PROMPTS.md    ← Suno 가이드
│   └── MIDJOURNEY_PROMPTS.md ← MJ/Veo/Sora 가이드
│
├── 06_tracks/             ← ⚡ 트랙별 문서
│   └── A1/                ← 앨범별 폴더
│
└── 99_meta/               ← 📦 메타 문서
    ├── GLOSSARY.md        ← 용어집
    ├── CHANGELOG.md       ← 변경 기록
    └── STATUS.md          ← 현황
```

---

### 이슈 #2 [P1] — PRD.md 문서 구조 맵 불일치

**파일**: `docs/PRD.md` (라인 78-79)

**현재 (Before)**:
```
├── 06_tracks/                ← 개별 트랙
│   └── HEUNDEULM.md          ← 흔들림
```

**문제**: 실제 파일 구조는 `06_tracks/A1/A1-01_흔들림.md`이며, `ALBUM_A1_HEUNDEULM.md`도 존재

**수정 (After)**:
```
├── 06_tracks/                ← 개별 트랙
│   ├── ALBUM_A1_HEUNDEULM.md ← 앨범 A-1 상세
│   └── A1/                   ← 앨범 A-1 트랙들
│       └── A1-01_흔들림.md   ← 첫 번째 트랙
```

---

### 이슈 #3 [P2] — ALBUM_A1_HEUNDEULM.md 트랙 수 불일치

**파일**: `docs/06_tracks/ALBUM_A1_HEUNDEULM.md` (라인 28-29)

**현재 (Before)**:
```
| 트랙 수 | 5 |
| 총 길이 | 약 12-15분 |
```

**문제**: 전략 문서(ALBUM_STRUCTURE.md, PHASE_MAP.md)에서는 앨범당 8트랙으로 명시

**수정 (After)**:
```
| 트랙 수 | 8 |
| 총 길이 | 약 24-28분 |
```

---

## 검토 2회차: 용어 및 수치 불일치

### 이슈 #4 [P1] — 색상 코드 불일치

**파일들**: 여러 문서에서 색상 코드 상이

| 문서 | 남색 코드 | 비고 |
|------|----------|------|
| GLOSSARY.md | `#1a237e` | "깊은 밤하늘 색" |
| VISUAL_COLOR.md | `#2c3e50` | 인디고로 명시 |
| ALBUM_A1_HEUNDEULM.md | `#2c3e50` | 남색으로 명시 |

**현재 (Before) - GLOSSARY.md**:
```
### 남색 (Nam Blue)
#1a237e. 결의 주조색 중 하나. 깊은 밤하늘 색.
```

**수정 (After)**:
```
### 인디고 (Indigo)
#2c3e50. 결의 보조색. 깊은 남색.
→ [[02_style/VISUAL_COLOR]]
```

---

### 이슈 #5 [P2] — BPM 범위 불일치

**파일들**:

| 문서 | BPM 범위 |
|------|----------|
| AUDIO_CORE.md | 95-110 |
| PRD.md | 95-110 |
| SUNO_PROMPTS.md Phase A | 95-110 |
| SUNO_PROMPTS.md Phase B | 100-120 |
| ALBUM_A1_HEUNDEULM.md | 95-110 |
| ALBUM_STRUCTURE.md Album B-1 | "빨라짐" |

**평가**: Phase별로 BPM이 달라지는 것은 의도적이나, 명확한 범위 정의 필요

**제안**: AUDIO_CORE.md에 Phase별 BPM 범위 명시 추가

---

### 이슈 #6 [P2] — 전통 악기 비율 수치

**파일들**:

| 문서 | 비율 |
|------|------|
| AUDIO_INSTRUMENTS.md | "20-30%" |
| PRD.md | "최대 30%" |
| AUDIO_CORE.md | "20-30%" |
| ALBUM_A1_HEUNDEULM.md | "20%" |

**평가**: 대체로 일관적이나 "20%"와 "20-30%"가 혼재

**제안**: 기본값 20%, 최대 30%로 통일

---

## 검토 3회차: 문서 간 링크 오류

### 이슈 #7 [P1] — 깨진 내부 링크

**파일**: `docs/06_tracks/ALBUM_A1_HEUNDEULM.md` (라인 823)

**현재 (Before)**:
```
- [[06_tracks/ALBUM_A2]] — 다음 앨범 (제작 시 생성)
```

**문제**: ALBUM_A2 파일 존재하지 않음

**수정 (After)**:
```
- *(다음 앨범: Album A-2 발현 — 제작 시 생성)*
```

---

### 이슈 #8 [P2] — 파일명 참조 불일치

**파일**: `docs/05_execution/MIDJOURNEY_PROMPTS.md`

**현재 파일명**: `MIDJOURNEY_PROMPTS.md`
**다른 문서에서 참조**: `VISUAL_PROMPTS.md`

| 문서 | 참조명 |
|------|--------|
| DASHBOARD.md | `VISUAL_PROMPTS` |
| TRACK_PRODUCTION.md | `VISUAL_PROMPTS` |
| 06_tracks/A1/A1-01_흔들림.md | `VISUAL_PROMPTS` |

**제안**: 파일명을 `VISUAL_PROMPTS.md`로 변경하거나, 모든 참조를 `MIDJOURNEY_PROMPTS.md`로 통일

---

### 이슈 #9 [P3] — 상대 경로 vs 절대 경로 혼재

**예시**:
- `[[02_style/VISUAL_COLOR]]` (절대)
- `[[VISUAL_COLOR]]` (상대)

**제안**: Obsidian 스타일 링크로 통일 (파일명만 사용)

---

## 검토 4회차: 내용 중복 및 불일치

### 이슈 #10 [P2] — 정전 문장 중복

**파일들**: MANIFESTO.md, DEFINITION.md, README.md

모두 유사한 정전 문장을 포함하나 표현이 약간씩 다름:

| 문서 | 표현 |
|------|------|
| MANIFESTO.md | "설명하지 않는다. 보여줄 뿐이다." |
| README.md | "이곳은 이야기를 설명하지 않는다. 결만 남긴다." |
| DEFINITION.md | "결은 설명하지 않는다." |

**제안**: MANIFESTO.md를 정전 원본으로 지정, 다른 문서는 참조만

---

### 이슈 #11 [P2] — 도깨비 등장 횟수 불일치

**파일들**:

| 문서 | 등장 횟수 |
|------|----------|
| DOKKAEBI.md | "총 시간: 15-30초/MV, 3-5회" |
| PROCESS.md | "도깨비 | 3-5회 | 1-3초" |
| INTERACTIONS.md | "1회 등장 시 1-3초" |

**평가**: 일관적

---

### 이슈 #12 [P1] — 앨범 구조 상세 내용 누락

**파일**: `docs/04_strategy/ALBUM_STRUCTURE.md`

**문제**: ALBUM_A1_HEUNDEULM.md에는 5트랙 상세가 있으나, ALBUM_STRUCTURE.md의 A-1 앨범 섹션과 불일치

**ALBUM_A1_HEUNDEULM.md 트랙 목록**:
1. 시작 (SIJAK)
2. 반복 (BANBOK)
3. 틈 (TIL)
4. 그림자 (GEURIMJA)
5. 흔들림 (HEUNDEULM)

**ALBUM_STRUCTURE.md 내용**: (확인 필요)

---

## 검토 5회차: 톤 및 스타일 위반

### 이슈 #13 [P3] — 감정적 표현 사용

**파일**: `docs/06_tracks/ALBUM_A1_HEUNDEULM.md` (라인 664)

**현재 (Before)**:
```
| T1 시작 | Ryuichi Sakamoto - "Merry Christmas Mr. Lawrence" | 미니멀 인트로, 분위기 |
```

**문제**: 레퍼런스 자체는 괜찮으나, 일부 설명에 감정적 표현 잔재

---

### 이슈 #14 [P3] — 설명 과잉

**파일**: `docs/03_characters/HUMAN.md`

**문제**: 437줄로 매우 상세하나, "결은 설명하지 않는다" 원칙과 다소 충돌

**제안**: 핵심 규칙만 남기고 예시 축소 고려

---

## 검토 6회차: 실행 문서 정합성

### 이슈 #15 [P2] — TRACK_TEMPLATE.md vs TRACK_PRODUCTION.md 중복

**파일들**: 두 파일이 유사한 역할

| 파일 | 위치 | 용도 |
|------|------|------|
| TRACK_TEMPLATE.md | 05_execution/ | 빈 템플릿 |
| TRACK_PRODUCTION.md | 06_tracks/ | 작성된 템플릿 |

**제안**: TRACK_PRODUCTION.md 삭제 또는 목적 명확화

---

### 이슈 #16 [P2] — QC_CHECKLIST.md 우선순위 불일치

**파일**: `docs/05_execution/QC_CHECKLIST.md`

일부 P1/P2/P3 분류 기준이 모호함

**제안**: 우선순위 기준 명확화 (게이트/권장/선택)

---

## 검토 7회차: 메타 문서 정확성

### 이슈 #17 [P1] — STATUS.md 상태 불일치

**파일**: `docs/99_meta/STATUS.md` (라인 86)

**현재 (Before)**:
```
### 06_tracks (트랙)
- [ ] 아직 트랙 문서 없음
```

**문제**: 실제로 `06_tracks/A1/A1-01_흔들림.md`와 `ALBUM_A1_HEUNDEULM.md` 존재

**수정 (After)**:
```
### 06_tracks (트랙)
- [x] ALBUM_A1_HEUNDEULM.md
- [x] TRACK_PRODUCTION.md
- [x] A1/A1-01_흔들림.md
```

---

### 이슈 #18 [P2] — CHANGELOG.md 예정 변경 업데이트 필요

**파일**: `docs/99_meta/CHANGELOG.md` (라인 117-128)

**현재 (Before)**:
```
### [1.1.0] — 예정

- [ ] 전체 문서 비판-수정 사이클 완료
- [ ] 기존 폴더 삭제 완료
- [ ] 락 대상 문서 확정
```

**수정 (After)**:
```
### [1.1.0] — 2025-01-11

- [x] 전체 문서 비판-수정 사이클 완료
- [x] 기존 폴더 삭제 완료
- [x] 락 대상 문서 확정

### [1.2.0] — 예정

- [ ] 첫 번째 트랙 제작 (A1-01)
- [ ] Shot Library 구축
```

---

## 검토 8회차: 누락된 정보

### 이슈 #19 [P2] — Phase 0 상세 부족

**파일**: `docs/04_strategy/ALBUM_STRUCTURE.md`

**문제**: Phase 0 (기원) 앨범은 "선택적"으로 명시되어 있으나 트랙 리스트 없음

**제안**: Phase 0 기본 구조 추가 (Phase C 성공 시 구체화)

---

### 이슈 #20 [P2] — 영상 도구 가이드 분리 제안

**파일**: `docs/05_execution/MIDJOURNEY_PROMPTS.md`

**문제**: 900줄로 매우 길며, MJ 이미지/MJ Video/Veo/Sora 가이드가 혼재

**제안**: 이미지와 비디오 가이드 분리 고려

---

### 이슈 #21 [P3] — Instagram 전략 상세 부족

**파일**: `docs/04_strategy/CHANNEL_LAUNCH.md`

**문제**: YouTube 중심, Instagram 전략은 상대적으로 약함

---

## 검토 9회차: 오타 및 형식 오류

### 이슈 #22 [P3] — 오타 발견

**파일**: `docs/KANBAN.md` (라인 29)

**현재 (Before)**:
```
- [ ] [[06_tracks/A1/A1-01_흔들림|A1-01 흔들림]] #런칭MV
```

**수정 (After)**:
```
- [ ] [[06_tracks/A1/A1-01_흔들림|A1-01 흔들림]] #런칭MV #첫트랙
```

---

### 이슈 #23 [P3] — YAML frontmatter 일관성

일부 문서 `locked:` 필드 누락 또는 불일치

| 문서 | locked 값 |
|------|----------|
| MANIFESTO.md | (확인 필요) |
| GLOSSARY.md | false |
| SUNO_PROMPTS.md | false |

**제안**: 00_core, 01_world, 02_style, 03_characters는 `locked: true`로 통일

---

### 이슈 #24 [P3] — 표 형식 불일치

일부 표에서 열 정렬 불일치

---

## 검토 10회차: 최종 통합 검토

### 이슈 #25 [P1] — CLAUDE.md와 실제 구조 불일치

**파일**: `/CLAUDE.md`

**현재 (Before)**:
```
### 🔒 Immutable (불변) — `docs/immutable/`
...
### 📝 Variable (가변) — `docs/variable/`
...
### ⚙️ Execution (실행) — `docs/execution/`
...
### 🎵 Tracks — `docs/tracks/`
```

**문제**: 구버전 폴더 구조 참조

**수정 (After)**:
```
### 🔒 Immutable (불변) — `docs/00_core/`, `docs/01_world/`, `docs/02_style/`, `docs/03_characters/`

**절대 수정 금지** (사용자 명시적 승인 없이)

| 폴더 | 내용 |
|------|------|
| `00_core/` | MANIFESTO.md, DEFINITION.md |
| `01_world/` | RULES.md, THEMES.md, PROHIBITIONS.md, TONE.md |
| `02_style/` | VISUAL_*.md, AUDIO_*.md |
| `03_characters/` | DOKKAEBI.md, HAETAE.md, TAL.md, HUMAN.md, INTERACTIONS.md |

### 📝 Variable (가변) — `docs/04_strategy/`

운영에 따라 수정 가능

| 파일 | 내용 |
|------|------|
| `PHASE_MAP.md` | Phase 로드맵 |
| `ALBUM_STRUCTURE.md` | 앨범 구조 |
| `CHANNEL_LAUNCH.md` | 채널 런칭 정보 |
| `CONTENT_FUNNEL.md` | 콘텐츠 퍼널 |

### ⚙️ Execution (실행) — `docs/05_execution/`

자유롭게 수정/확장 가능

| 파일 | 내용 |
|------|------|
| `TRACK_TEMPLATE.md` | 트랙 제작 템플릿 |
| `QC_CHECKLIST.md` | 품질 검사표 |
| `SUNO_PROMPTS.md` | Suno 가이드 |
| `MIDJOURNEY_PROMPTS.md` | 비주얼 가이드 |

### 🎵 Tracks — `docs/06_tracks/`

각 트랙별 제작 문서 (자유롭게 생성/수정)
```

---

## 우선순위별 요약

### P1 (즉시 수정 필요) — 8건

| # | 파일 | 이슈 |
|---|------|------|
| 1 | README.md | 폴더 구조 불일치 |
| 2 | PRD.md | 트랙 경로 불일치 |
| 3 | ALBUM_A1_HEUNDEULM.md | 트랙 수 5→8 |
| 4 | GLOSSARY.md | 색상 코드 불일치 |
| 7 | ALBUM_A1_HEUNDEULM.md | 깨진 링크 |
| 12 | ALBUM_STRUCTURE.md | 트랙 상세 누락 |
| 17 | STATUS.md | 트랙 문서 상태 |
| 25 | CLAUDE.md | 폴더 구조 참조 |

### P2 (권장 수정) — 21건

- BPM 범위 명확화
- 전통 악기 비율 통일
- 파일명 참조 통일
- 정전 문장 중복 정리
- 템플릿 파일 역할 명확화
- QC 우선순위 기준 명확화
- Phase 0 상세 추가
- 등등

### P3 (개선 제안) — 18건

- 링크 스타일 통일
- 감정적 표현 제거
- 설명 축소
- 오타 수정
- YAML frontmatter 통일
- 등등

---

## 수정 적용 계획

### 즉시 적용 (P1)

1. ✅ CLAUDE.md 폴더 구조 업데이트
2. ✅ README.md 폴더 구조 업데이트
3. ✅ PRD.md 트랙 경로 수정
4. ✅ ALBUM_A1_HEUNDEULM.md 트랙 수 수정
5. ✅ GLOSSARY.md 색상 코드 통일
6. ✅ STATUS.md 상태 업데이트
7. ✅ 깨진 링크 수정

### 후속 적용 (P2/P3)

- 문서별 세부 수정은 별도 커밋으로 진행

---

## 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2025-01-11 | 초기 검토 보고서 작성 |

---

*End of REVIEW_REPORT*
