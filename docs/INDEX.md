---
title: "GYEOL Index"
type: index
version: 1.0
last_updated: 2025-01-10
description: "결 프로젝트 최상단 진입점. 이 문서에서 모든 것이 시작된다."
---

# 결(GYEOL) — 문서 인덱스

> **당신이 봐야 할 문서는 상황에 따라 다릅니다.**
> 아래에서 현재 상황을 선택하세요.

---

## 🔥 최근 업데이트

| 날짜 | 문서 | 변경 내용 |
|------|------|----------|
| 2025-01-10 | [[99_meta/STATUS]] | 프로젝트 현황 추가 |
| 2025-01-10 | [[99_meta/GLOSSARY]] | 용어 사전 추가 |
| 2025-01-10 | [[05_execution/MIDJOURNEY_PROMPTS]] | MJ 프롬프트 가이드 |
| 2025-01-10 | [[05_execution/SUNO_PROMPTS]] | Suno 프롬프트 가이드 |
| 2025-01-10 | [[05_execution/QC_CHECKLIST]] | 품질 검사표 |
| 2025-01-10 | 전체 구조 | PARA 기반 모듈화 완성 (30+ 문서) |

---

## 👤 당신의 상황은?

### 🆕 처음 온 사람
1. [[PRD]] — 프로젝트 전체 요약 (5분)
2. [[00_core/MANIFESTO]] — 선언문 (2분)
3. [[00_core/DEFINITION]] — 결의 정의 (2분)

### 🎬 트랙을 만들어야 하는 사람
1. [[PROCESS]] — 제작 프로세스 전체
2. [[05_execution/TRACK_TEMPLATE]] — 트랙 템플릿
3. [[05_execution/QC_CHECKLIST]] — QC 체크리스트

### 🎨 비주얼 작업을 해야 하는 사람
1. [[02_style/VISUAL_COLOR]] — 색상 규칙
2. [[02_style/VISUAL_TEXTURE]] — 질감 규칙
3. [[02_style/VISUAL_PIPELINE]] — 제작 파이프라인

### 🎵 음악 작업을 해야 하는 사람
1. [[02_style/AUDIO_CORE]] — 오디오 핵심
2. [[02_style/AUDIO_INSTRUMENTS]] — 악기 역할
3. [[05_execution/SUNO_PROMPTS]] — Suno 프롬프트

### 📋 전략/기획을 해야 하는 사람
1. [[04_strategy/PHASE_MAP]] — Phase 로드맵
2. [[04_strategy/CHANNEL_LAUNCH]] — 채널 런칭
3. [[04_strategy/CONTENT_FUNNEL]] — 콘텐츠 퍼널

### 🔍 특정 캐릭터를 확인해야 하는 사람
- [[03_characters/DOKKAEBI]] — 도깨비
- [[03_characters/HAETAE]] — 해태
- [[03_characters/TAL]] — 탈
- [[03_characters/HUMAN]] — 인물

---

## 📁 폴더 구조 (PARA 기반)

```
docs/
│
├── INDEX.md              ← 지금 이 문서 (최상단 진입점)
├── PRD.md                ← 프로젝트 요약
├── PROCESS.md            ← 제작 프로세스
│
├── 00_core/              ← 📌 RESOURCES: 불변 핵심 (절대 변경 금지)
│   ├── MANIFESTO.md
│   └── DEFINITION.md
│
├── 01_world/             ← 📌 RESOURCES: 세계관 규칙 (절대 변경 금지)
│   ├── RULES.md
│   ├── THEMES.md
│   ├── PROHIBITIONS.md
│   └── TONE.md
│
├── 02_style/             ← 📌 RESOURCES: 스타일 가이드 (절대 변경 금지)
│   ├── VISUAL_*.md
│   └── AUDIO_*.md
│
├── 03_characters/        ← 📌 RESOURCES: 캐릭터 정의 (절대 변경 금지)
│   ├── DOKKAEBI.md
│   ├── HAETAE.md
│   ├── TAL.md
│   ├── HUMAN.md
│   └── INTERACTIONS.md
│
├── 04_strategy/          ← 📋 AREAS: 운영 전략 (Phase별 업데이트)
│   ├── PHASE_MAP.md
│   ├── CHANNEL_LAUNCH.md
│   └── CONTENT_FUNNEL.md
│
├── 05_execution/         ← ⚡ PROJECTS: 실행 도구 (트랙 제작 시 사용)
│   ├── TRACK_TEMPLATE.md
│   ├── QC_CHECKLIST.md
│   ├── SUNO_PROMPTS.md
│   └── MIDJOURNEY_PROMPTS.md
│
├── 06_tracks/            ← ⚡ PROJECTS: 개별 트랙 (진행 중)
│   └── [트랙명].md
│
└── 99_meta/              ← 📦 ARCHIVES: 메타/참고
    ├── GLOSSARY.md
    ├── CHANGELOG.md
    └── STATUS.md
```

---

## 🏷️ PARA 분류

| 분류 | 폴더 | 설명 | 수정 빈도 |
|------|------|------|----------|
| **Resources** | 00~03 | 불변 자산. 참고만 함 | 거의 없음 |
| **Areas** | 04 | 지속 관리 영역 | Phase별 |
| **Projects** | 05~06 | 현재 진행 작업 | 트랙마다 |
| **Archives** | 99 | 완료/참고 자료 | 드묾 |

---

## ✅ GTD 빠른 참조

### 📥 수집 (Capture)
새 아이디어 → [[99_meta/STATUS]]에서 다음 단계 확인

### 🔍 명확화 (Clarify)
- 세계관 질문? → [[01_world/]]
- 스타일 질문? → [[02_style/]]
- 캐릭터 질문? → [[03_characters/]]

### 📂 정리 (Organize)
- 불변 규칙 → 00~03 폴더
- 운영 전략 → 04 폴더
- 실행 작업 → 05~06 폴더

### 🎯 실행 (Do)
→ [[PROCESS]] 문서 따라 진행

### 🔄 검토 (Review)
→ [[05_execution/QC_CHECKLIST]]로 검증

---

## 🔒 문서 상태

| 상태 | 의미 |
|------|------|
| `locked: true` | 승인 없이 수정 금지 |
| `locked: false` | 검토 중, 수정 가능 |

**현재 locked: false인 문서들:**
- 전체 (세팅 완료 후 lock 예정)

---

## 📊 전체 문서 목록 (카테고리별)

### 00_core — 핵심
| 문서 | 설명 |
|------|------|
| [[00_core/MANIFESTO]] | 결의 선언문 |
| [[00_core/DEFINITION]] | 결의 정의 |

### 01_world — 세계관
| 문서 | 설명 |
|------|------|
| [[01_world/RULES]] | 5개 작동 규칙 |
| [[01_world/THEMES]] | 6개 메타 테마 |
| [[01_world/PROHIBITIONS]] | 금지 규칙 |
| [[01_world/TONE]] | 톤 가이드 |

### 02_style — 스타일
| 문서 | 설명 |
|------|------|
| [[02_style/VISUAL_COLOR]] | 색상 팔레트 |
| [[02_style/VISUAL_TEXTURE]] | 텍스처 규칙 |
| [[02_style/VISUAL_LIGHT]] | 조명 규칙 |
| [[02_style/VISUAL_CAMERA]] | 카메라 규칙 |
| [[02_style/VISUAL_EDIT]] | 편집 규칙 |
| [[02_style/VISUAL_PIPELINE]] | 제작 파이프라인 |
| [[02_style/AUDIO_CORE]] | 오디오 핵심 |
| [[02_style/AUDIO_INSTRUMENTS]] | 악기 역할 |
| [[02_style/AUDIO_STRUCTURE]] | 곡 구조 |
| [[02_style/AUDIO_VOCAL]] | 보컬 규칙 |

### 03_characters — 존재
| 문서 | 설명 |
|------|------|
| [[03_characters/DOKKAEBI]] | 도깨비 정의 |
| [[03_characters/HAETAE]] | 해태 정의 |
| [[03_characters/TAL]] | 탈 정의 |
| [[03_characters/HUMAN]] | 인간 정의 |
| [[03_characters/INTERACTIONS]] | 상호작용 규칙 |

### 04_strategy — 전략
| 문서 | 설명 |
|------|------|
| [[04_strategy/PHASE_MAP]] | Phase 로드맵 |
| [[04_strategy/CHANNEL_LAUNCH]] | 채널 런칭 |
| [[04_strategy/CONTENT_FUNNEL]] | 콘텐츠 퍼널 |

### 05_execution — 실행
| 문서 | 설명 |
|------|------|
| [[05_execution/TRACK_TEMPLATE]] | 트랙 템플릿 |
| [[05_execution/QC_CHECKLIST]] | 품질 검사표 |
| [[05_execution/SUNO_PROMPTS]] | Suno 프롬프트 |
| [[05_execution/MIDJOURNEY_PROMPTS]] | Midjourney 프롬프트 |

### 99_meta — 메타
| 문서 | 설명 |
|------|------|
| [[99_meta/GLOSSARY]] | 용어 사전 |
| [[99_meta/CHANGELOG]] | 변경 기록 |
| [[99_meta/STATUS]] | 프로젝트 현황 |

---

## 관련 문서

- [[PRD]] — 프로젝트 전체 요약
- [[PROCESS]] — 제작 프로세스
- [[99_meta/STATUS]] — 현재 진행 상황
- [[99_meta/CHANGELOG]] — 변경 이력

---

*End of INDEX*
