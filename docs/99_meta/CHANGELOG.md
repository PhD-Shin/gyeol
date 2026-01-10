---
title: "GYEOL Changelog"
type: meta
locked: false
version: 1.0
last_updated: 2025-01-10
description: "결 프로젝트 변경 기록. 주요 업데이트 히스토리."
use_when: "변경 이력 확인 시, 업데이트 내용 파악 시"
tags: [meta, changelog, history, updates]
related:
  - "[[INDEX]]"
  - "[[99_meta/STATUS]]"
---

# CHANGELOG — 변경 기록

> **이 문서가 필요한 순간:**
> - 최근 변경 사항을 확인할 때
> - 문서 버전을 추적할 때
> - 프로젝트 진행 히스토리를 파악할 때

---

## 버전 규칙

- **Major (X.0)**: 구조 변경, 대규모 리팩토링
- **Minor (0.X)**: 새 문서 추가, 섹션 추가
- **Patch**: 오타 수정, 작은 수정 (기록 안 함)

---

## [1.0.0] — 2025-01-10

### 🎉 초기 구조 완성

#### Added (추가)

**00_core/**
- `MANIFESTO.md` — 핵심 선언문
- `DEFINITION.md` — 결의 정의

**01_world/**
- `RULES.md` — 5개 작동 규칙
- `THEMES.md` — 6개 메타 테마
- `PROHIBITIONS.md` — 금지 규칙
- `TONE.md` — 톤 가이드

**02_style/**
- `VISUAL_COLOR.md` — 색상 팔레트
- `VISUAL_TEXTURE.md` — 텍스처 규칙
- `VISUAL_LIGHT.md` — 조명 규칙
- `VISUAL_CAMERA.md` — 카메라 규칙
- `VISUAL_EDIT.md` — 편집 규칙
- `VISUAL_PIPELINE.md` — 제작 파이프라인
- `AUDIO_CORE.md` — 오디오 핵심
- `AUDIO_INSTRUMENTS.md` — 악기 역할
- `AUDIO_STRUCTURE.md` — 곡 구조
- `AUDIO_VOCAL.md` — 보컬 규칙

**03_characters/**
- `DOKKAEBI.md` — 도깨비 정의
- `HAETAE.md` — 해태 정의
- `TAL.md` — 탈 정의
- `HUMAN.md` — 인간 정의
- `INTERACTIONS.md` — 상호작용 규칙

**04_strategy/**
- `PHASE_MAP.md` — Phase 로드맵
- `CHANNEL_LAUNCH.md` — 채널 런칭
- `CONTENT_FUNNEL.md` — 콘텐츠 퍼널

**05_execution/**
- `TRACK_TEMPLATE.md` — 트랙 템플릿
- `QC_CHECKLIST.md` — 품질 검사표
- `SUNO_PROMPTS.md` — Suno 프롬프트
- `MIDJOURNEY_PROMPTS.md` — Midjourney 프롬프트

**99_meta/**
- `GLOSSARY.md` — 용어 사전
- `CHANGELOG.md` — 변경 기록 (이 문서)
- `STATUS.md` — 프로젝트 현황

**루트 문서**
- `INDEX.md` — 전체 인덱스
- `PRD.md` — 프로젝트 요약
- `PROCESS.md` — 제작 프로세스

#### Changed (변경)

- 기존 `immutable/` 구조 → 새 모듈 구조로 전환
- PARA/GTD 프레임워크 적용
- 각 문서에 `use_when` 필드 추가 (RAG 최적화)

#### Removed (제거)

- 예정: `immutable/`, `variable/`, `execution/` 폴더
- 예정: `references_docs/` 폴더

---

## [0.1.0] — 2025-01-10 (이전)

### 초기 문서 작성

#### Added

- `immutable/BIBLE_WORLD.md` — 세계관 정의
- `immutable/STYLE_GUIDE_VISUAL.md` — 비주얼 가이드
- `immutable/STYLE_GUIDE_AUDIO.md` — 오디오 가이드
- `immutable/CHARACTER_BIBLE.md` — 캐릭터 정의
- `variable/PHASE_MAP.md` — Phase 로드맵
- `execution/TRACK_TEMPLATE.md` — 트랙 템플릿

---

## 예정 변경

### [1.1.0] — 2025-01-11

#### Added (추가)
- `99_meta/REVIEW_REPORT.md` — 10회 비판적 검토 보고서

#### Fixed (수정)
- `CLAUDE.md` — 폴더 구조 참조 업데이트 (immutable → 00_core 등)
- `README.md` — 폴더 구조 업데이트
- `PRD.md` — 트랙 경로 수정
- `ALBUM_A1_HEUNDEULM.md` — 트랙 수 5→8, 깨진 링크 수정
- `GLOSSARY.md` — 색상 코드 통일 (#1a237e → #2c3e50)
- `STATUS.md` — 트랙 문서 상태 업데이트

#### Changed (변경)
- 전체 문서 비판-수정 사이클 완료 (10회 검토)
- P1 이슈 8건 해결

### [1.2.0] — 예정

- [ ] 첫 번째 트랙 제작 (A1-01)
- [ ] Shot Library 구축
- [ ] P2/P3 이슈 후속 처리

---

## 관련 문서

- [[INDEX]] — 전체 문서 구조
- [[99_meta/STATUS]] — 현재 진행 상황

---

*End of CHANGELOG*
