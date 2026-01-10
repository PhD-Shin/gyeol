---
title: "GYEOL Changelog"
type: meta
locked: false
version: 1.1
last_updated: 2025-01-11
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

## [1.3.0] — 2025-01-11

### 🎯 K-pop 코드스위칭 v3 적용

#### Fixed (수정)
- **가사 v2→v3 전면 수정**: 같은 의미 반복 제거
  - ❌ "Can't stop 멈출 수 없어" → ⭕ "Let it burn 재만 남아" (원인→결과)
  - ❌ "Burn it all 다 태워버려" → ⭕ "Break it down 먼지만 남아" (원인→결과)
- `A1-01_시작.md` — v3 가사 + 훅 포인트 테이블 수정
- `TODAY.md` — v3 가사 + 작업 순서 업데이트
- `AUDIO_VOCAL.md` (v1.4) — 좋은 예/나쁜 예 수정, 한국어 텍스처 테이블 수정
- `QC_CHECKLIST.md` (v1.2) — 코드스위칭 체크 항목 수정
- `SUNO_PROMPTS.md` — 코드스위칭 가이드 전면 수정
- `TRACK_TEMPLATE.md` — 가사 템플릿 v3 적용

#### Added (추가)
- `GLOSSARY.md` (v1.1) — 신규 용어 추가
  - K-판소리 판타지 트랩
  - 창 (Chang)
  - 추임새 (Chuimsae)
  - 해금 (Haegeum)
  - 한영 혼용 / 코드스위칭

#### Research (리서치)
- K-pop 코드스위칭 패턴 연구 (학술 자료 기반)
  - Intra-sentential, Inter-sentential, Tag-switching 패턴 정리
  - K-pop은 절대 같은 의미를 양 언어로 반복하지 않음 확인

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

### [1.2.0] — 2025-01-11

#### Added (추가)
- `99_meta/ENHANCEMENT_REPORT.md` — 전통 문헌 기반 보강 리포트
- `DOKKAEBI.md` — 문헌적 기원 섹션 (삼국유사, 석보상절)
- `DOKKAEBI.md` — 오방색 연계 섹션
- `HAETAE.md` — 문헌적 기원 섹션 (설문해자, 사헌부)
- `HAETAE.md` — 오방색 연계 섹션
- `TAL.md` — 문헌적 기원 섹션 (하회탈 9종)
- `TAL.md` — 턱 분리 표현 섹션
- `AUDIO_INSTRUMENTS.md` — 전통 악기 문헌적 배경 섹션
- `VISUAL_COLOR.md` — 오방색 체계 섹션
- `VISUAL_TEXTURE.md` — 민화 레퍼런스 섹션

#### Changed (변경)
- `TAL.md` — 탈 종류 5종→9종 확장
- `AUDIO_INSTRUMENTS.md` — 추가 악기 목록 확장 (아쟁, 거문고)

#### Research (리서치)
- 삼국유사 비형설화 조사
- 설문해자/해동잡록 해태 기록 조사
- 하회탈 9종 및 봉산탈춤 조사
- 오방색/오방간색 체계 정리
- 민화 (호작도, 십장생도) 조사

---

### [1.1.0] — 2025-01-11 (이전)

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
