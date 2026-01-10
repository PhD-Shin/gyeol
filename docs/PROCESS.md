---
title: "GYEOL Production Process"
type: meta
version: 2.0
last_updated: 2025-01-11
description: "결 프로젝트 제작 프로세스. 3단계 워크플로우."
tags: [process, execution, workflow]
---

# PROCESS — 결 제작 프로세스

> **워크플로우**: 셋업 → 퇴고 → 제작

---

## 전체 흐름

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   PHASE 1: 셋업 (SETUP)                                         │
│   └─ 문서 연결성 강화, 파일/폴더 정리                             │
│                                                                 │
│   PHASE 2: 퇴고 (REFINEMENT)                                    │
│   └─ 10라운드 비평 및 수정 → 완성도 비약적 향상                    │
│                                                                 │
│   PHASE 3: 제작 (PRODUCTION)                                    │
│   └─ 트랙별 음악 프롬프트 → 가사 → MJ 이미지                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## PHASE 1: 셋업

### 1.1 문서 연결성 강화

모든 문서 간 참조 확인 및 연결:

| 작업 | 체크 |
|------|------|
| 핵심 문서 (00_core) → 다른 모든 문서 참조 확인 | ⬜ |
| 세계관 문서 (01_world) → 캐릭터/스타일 문서 연결 | ⬜ |
| 스타일 문서 (02_style) → 트랙 템플릿 반영 | ⬜ |
| 캐릭터 문서 (03_characters) → 트랙별 등장 연결 | ⬜ |
| 트랙 문서 (06_tracks) → 관련 문서 모두 링크 | ⬜ |

### 1.2 파일/폴더 정리

```
docs/
├── 00_core/           # 불변 핵심
├── 01_world/          # 불변 세계관
├── 02_style/          # 불변 스타일
├── 03_characters/     # 불변 캐릭터
├── 04_strategy/       # 가변 전략
├── 05_execution/      # 가변 실행
├── 06_tracks/         # 트랙별 문서
│   ├── A1/            # Album A-1
│   ├── A2/            # Album A-2
│   └── ...
└── 99_meta/           # 메타 문서
```

### 1.3 중복 제거

- 동일 내용 다른 파일 → 하나로 통합
- 오래된 버전 → 삭제 또는 archive
- 충돌하는 정보 → 정리

---

## PHASE 2: 퇴고 (10라운드)

### 퇴고 프로세스

```
┌─────────────────────────────────────────────────────────────────┐
│  ROUND 1-3: 구조적 문제                                          │
│  - 문서 간 충돌                                                  │
│  - 논리적 모순                                                   │
│  - 누락된 정보                                                   │
├─────────────────────────────────────────────────────────────────┤
│  ROUND 4-6: 세계관 일관성                                        │
│  - 존재 설정 일관성                                              │
│  - 규칙 준수 여부                                                │
│  - 금지 표현 점검                                                │
├─────────────────────────────────────────────────────────────────┤
│  ROUND 7-9: 톤 & 스타일                                          │
│  - 쿨하고 건조한가?                                              │
│  - 설명하지 않는가?                                              │
│  - Kage Bow급 절제인가?                                          │
├─────────────────────────────────────────────────────────────────┤
│  ROUND 10: 최종 점검                                             │
│  - 전체 흐름                                                     │
│  - 훅 포인트 확인                                                │
│  - 제작 준비 완료                                                │
└─────────────────────────────────────────────────────────────────┘
```

### 퇴고 체크리스트

각 라운드마다:

```
- [ ] 문제 식별
- [ ] 해결책 제시
- [ ] 수정 적용
- [ ] 검증
```

### 퇴고 기록

`99_meta/REFINEMENT_LOG.md`에 기록:

```
## Round [N]
- 발견된 문제:
- 수정 내용:
- 영향받는 문서:
```

---

## PHASE 3: 제작

### 3.1 트랙별 제작 순서

```
1. 음악 프롬프트 작성 (Suno)
2. 가사 작성
3. 음악 생성 및 확정 → 정확한 길이 확인
4. 음악 길이 기준 MJ 이미지 개수 산정
5. 각 이미지별 프롬프트 작성
6. 이미지 생성
7. 영상 제작
8. QC
```

### 3.2 음악 제작 규격

| 항목 | 규격 |
|------|------|
| **BPM** | 110 (고정) |
| **Key** | 마이너 권장 (Am, Em, Dm) |
| **길이** | 3:00 ~ 4:00 |
| **Suno 프롬프트** | 영문 800자 내외 |

### 3.3 Suno 프롬프트 구조

```
[Style of Music] - 약 800 English characters

dark k-pop, [specific trap style], korean traditional fusion,
110 bpm, [key], [mood/atmosphere description],

[instrument 1] with [specific role and texture],
[instrument 2] with [specific role and texture],
[additional instruments...],

[vocal style] - [gender], [technique], [emotional quality],

[production details] - [bass character], [percussion style],
[spatial/reverb qualities], [dynamic progression],

[structure hints]
[Intro] [description]
[Verse] [description]
[Pre-Chorus] [description]
[Drop] [description]
[Break] [description]
[Outro] [description]
```

### 3.4 가사 규격

```
[Lyrics] - 한국어 + 영어 지시

[Section]
가사 내용
(performance direction)

[Section]
가사 내용
(performance direction)
...
```

### 3.5 MJ 이미지 개수 산정

| 음악 길이 | 기준 간격 | 이미지 개수 |
|----------|----------|------------|
| 3:00 (180초) | 6초 | 30장 |
| 3:30 (210초) | 7초 | 30장 |
| 4:00 (240초) | 6초 | 40장 |

> 훅 장면은 추가 이미지 배정

### 3.6 MJ 프롬프트 구조

```
[subject/scene description],
korean traditional context keywords,
hanji paper texture, ink wash style,
[lighting], [color mood],
[emotional/atmospheric keywords],
--ar 16:9 --style raw --s 250
```

---

## 현재 단계

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   📍 CURRENT: PHASE 1 - 셋업                                    │
│                                                                 │
│   진행: 문서 연결성 강화 및 파일/폴더 정리                        │
│   다음: PHASE 2 - 10라운드 퇴고                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 관련 문서

- [[STATUS]] — 현재 상태
- [[05_execution/TRACK_TEMPLATE]] — 트랙 템플릿
- [[05_execution/QC_CHECKLIST]] — QC 체크리스트
- [[99_meta/REFINEMENT_LOG]] — 퇴고 기록

---

*Last updated: 2025-01-11*
