---
title: "Quick Start Guide"
type: guide
version: 1.0
last_updated: 2025-01-11
description: "결 프로젝트 빠른 시작 가이드 - 5분 안에 제작 시작"
---

# GYEOL Quick Start — 5분 안에 시작하기

> **목표**: 복잡한 문서 읽지 말고, 바로 제작 시작

---

## 🚀 즉시 시작

### 1. 새 트랙 만들기
```bash
python3 scripts/gyeol-pipeline.py new A1-09 --title "침묵" --theme "silence"
```

### 2. 음악 분석하기
```bash
# Suno에서 음악 생성 후 다운로드
python3 scripts/gyeol-pipeline.py analyze A1-09 --music ~/Downloads/track.mp3
```

### 3. 프롬프트 받기
```bash
python3 scripts/gyeol-pipeline.py prompts A1-09
# → Suno 프롬프트 + MidJourney 30장 프롬프트 생성
```

---

## 📋 제작 파이프라인

```
┌─────────────────────────────────────────────────────────┐
│  1. 기획          │  2. 음악          │  3. 분석        │
│  new 명령         │  Suno 생성        │  analyze 명령   │
│  → 트랙 문서      │  → MP3 다운로드   │  → 타임라인     │
└───────┬───────────┴───────┬───────────┴───────┬─────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌─────────────────────────────────────────────────────────┐
│  4. 이미지        │  5. 영상          │  6. QC          │
│  MJ 30장 생성     │  타임라인 편집    │  /qc 스킬       │
│  → PNG 저장       │  → 최종 영상      │  → 검증 완료    │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 핵심 규칙 (3가지만 기억)

### 1. 설명하지 않는다
- 내레이션 ❌
- 텍스트 설명 ❌
- 교훈/메시지 ❌

### 2. 쿨하게 유지
- 감정 과잉 ❌
- "슬프다" ❌ → "멋있다" ⭕
- Kage Bow급 절제

### 3. 초반 5초가 전부
- 0-2초: 귀를 잡는 소리
- 2-5초: "이게 뭐지?" 유발
- 바로 시작, 페이드인 금지

---

## 🛠️ Claude 스킬

| 명령 | 용도 | 예시 |
|------|------|------|
| `/make` | 통합 제작 | `/make 새 트랙 A1-09` |
| `/qc` | 품질 검사 | `/qc A1-05_의례` |
| `/audio` | 오디오 규칙 | `/audio Suno 키워드` |
| `/visual` | 비주얼 규칙 | `/visual 색상 팔레트` |
| `/prohibitions` | 금지 규칙 | `/prohibitions 이 장면` |

---

## 📂 파일 구조

```
gyeol/
├── scripts/
│   └── gyeol-pipeline.py    ← 이것만 쓰면 됨
│
├── assets/
│   ├── music/               ← 음악 파일 여기에
│   └── analysis/            ← 분석 결과 자동 저장
│
└── docs/06_tracks/[앨범]/   ← 트랙 문서
```

---

## 🔥 자주 쓰는 명령

```bash
# 상태 확인
python3 scripts/gyeol-pipeline.py status

# 앨범 전체 현황
python3 scripts/gyeol-pipeline.py batch A1 --range 1-8

# 도움말
python3 scripts/gyeol-pipeline.py --help
```

---

## 📚 더 알고 싶다면

| 주제 | 문서 |
|------|------|
| 세계관 전체 | `docs/MASTER_PLAN.md` |
| 제작 프로세스 | `docs/PROCESS.md` |
| 오디오 상세 | `docs/02_style/AUDIO_*.md` |
| 비주얼 상세 | `docs/02_style/VISUAL_*.md` |
| 금지 규칙 상세 | `docs/01_world/PROHIBITIONS.md` |

---

*5분 끝. 이제 만들어라.*
