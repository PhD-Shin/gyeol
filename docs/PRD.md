---
title: "GYEOL Project PRD"
type: meta
version: 1.0
last_updated: 2025-01-10
description: "결 프로젝트 전체 요약. 이 문서만 읽어도 프로젝트를 이해할 수 있다."
---

# PRD — 결(GYEOL) 프로젝트

> **이 문서는 결 프로젝트의 진입점이다.**
> 전체 구조를 파악하고, 필요한 문서로 바로 이동할 수 있다.

---

## 1. 프로젝트 한 줄 정의

> **Korean Mythic Visual Album**
>
> 전통 회화 문법을 껍데기로 쓰고, 현대 시스템을 '신화적 공포'로 시각화하는 유튜브 뮤직 채널.

---

## 2. 핵심 원칙 (3문장)

1. **설명하지 않는다** — 보여줄 뿐이다
2. **일관성이 창의성보다 우선** — IP는 반복으로 만든다
3. **팬이 해석한다** — 정답을 주지 않는다

---

## 3. 문서 구조 맵

```
docs/
├── PRD.md                    ← 지금 이 문서 (진입점)
├── PROCESS.md                ← 제작 프로세스 가이드
│
├── 00_core/                  ← 핵심 정의
│   ├── MANIFESTO.md          ← 선언문
│   └── DEFINITION.md         ← 결의 정의
│
├── 01_world/                 ← 세계관 규칙
│   ├── RULES.md              ← 5대 작동 규칙
│   ├── THEMES.md             ← 메타 테마
│   ├── PROHIBITIONS.md       ← 절대 금지
│   └── TONE.md               ← 톤 슬라이더
│
├── 02_style/                 ← 스타일 가이드
│   ├── VISUAL_COLOR.md       ← 색상 규칙
│   ├── VISUAL_TEXTURE.md     ← 질감 규칙
│   ├── VISUAL_LIGHT.md       ← 조명 규칙
│   ├── VISUAL_CAMERA.md      ← 카메라 규칙
│   ├── VISUAL_EDIT.md        ← 편집 규칙
│   ├── VISUAL_PIPELINE.md    ← 제작 파이프라인
│   ├── AUDIO_CORE.md         ← 오디오 핵심
│   ├── AUDIO_INSTRUMENTS.md  ← 악기 역할
│   ├── AUDIO_STRUCTURE.md    ← 곡 구조
│   └── AUDIO_VOCAL.md        ← 보컬 규칙
│
├── 03_characters/            ← 캐릭터/존재 정의
│   ├── DOKKAEBI.md           ← 도깨비
│   ├── HAETAE.md             ← 해태
│   ├── TAL.md                ← 탈
│   ├── HUMAN.md              ← 인물
│   └── INTERACTIONS.md       ← 상호작용 규칙
│
├── 04_strategy/              ← 전략/운영
│   ├── PHASE_MAP.md          ← Phase 로드맵
│   ├── CHANNEL_LAUNCH.md     ← 채널 런칭
│   └── CONTENT_FUNNEL.md     ← 콘텐츠 퍼널
│
├── 05_execution/             ← 실행 도구
│   ├── TRACK_TEMPLATE.md     ← 트랙 템플릿
│   ├── QC_CHECKLIST.md       ← QC 체크리스트
│   └── SUNO_PROMPTS.md       ← Suno 프롬프트 가이드
│
├── 06_tracks/                ← 개별 트랙
│   └── HEUNDEULM.md          ← 흔들림
│
└── 99_meta/                  ← 메타 문서
    ├── GLOSSARY.md           ← 용어집
    └── CHANGELOG.md          ← 변경 이력
```

---

## 4. 빠른 참조 (Quick Reference)

### 세계관이 뭔지 알고 싶다면
→ [[00_core/MANIFESTO]] → [[00_core/DEFINITION]]

### 비주얼 스타일을 알고 싶다면
→ [[02_style/VISUAL_COLOR]] → [[02_style/VISUAL_TEXTURE]]

### 음악 규칙을 알고 싶다면
→ [[02_style/AUDIO_CORE]] → [[02_style/AUDIO_INSTRUMENTS]]

### 캐릭터가 어떻게 작동하는지 알고 싶다면
→ [[03_characters/DOKKAEBI]] → [[03_characters/INTERACTIONS]]

### 트랙을 만들고 싶다면
→ [[PROCESS]] → [[05_execution/TRACK_TEMPLATE]]

### Phase 전략을 알고 싶다면
→ [[04_strategy/PHASE_MAP]]

---

## 5. 핵심 수치 요약

| 항목 | 값 |
|------|-----|
| 기본 BPM | 95-110 |
| 기본 키 | 마이너 (70%) |
| 컷 길이 | 4-6초 |
| 밝은 장면 비율 | 최대 30% |
| 전통 악기 비율 | 최대 30% |
| Sora/Veo 사용 | 최대 20% |

---

## 6. 절대 금지 요약

- 내레이션/설명 텍스트 ❌
- 선악 구도 ❌
- 희망/구원 메시지 ❌
- 민속/설화 소개 ❌
- 감정 과잉 ❌
- 순수 흰색/검정 ❌

→ 상세: [[01_world/PROHIBITIONS]]

---

## 7. 다음 단계

1. [[PROCESS]] 문서를 읽고 제작 흐름 파악
2. [[05_execution/TRACK_TEMPLATE]] 복사
3. 트랙 제작 시작

---

## 관련 문서

- [[PROCESS]] — 제작 프로세스
- [[00_core/MANIFESTO]] — 선언문
- [[04_strategy/PHASE_MAP]] — Phase 로드맵

---

*End of PRD*
