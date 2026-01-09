# 결 (GYEOL) — Production Bible

> **이곳은 이야기를 설명하지 않는다. 결만 남긴다.**

---

## 폴더 구조

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

---

## 문서 유형

### 🔒 Immutable (불변)

**절대 수정 금지** — 세계관의 근간

- YAML frontmatter에 `locked: true` 표시
- 수정 시 전체 세계관이 흔들림
- Claude Code도 승인 없이 수정 불가

### 📝 Variable (가변)

**운영에 따라 수정 가능** — 전략/계획 문서

- Phase 추가, 트랙 순서 변경 등
- 세계관 규칙은 변경 불가

### ⚙️ Execution (실행)

**자유롭게 수정/확장** — 제작 실무 문서

- 템플릿 개선
- 체크리스트 항목 추가

---

## 사용 방법

### 1. 새 트랙 제작 시

1. `execution/TRACK_TEMPLATE.md` 복사
2. `tracks/[트랙명].md`로 저장
3. 각 섹션 채우기
4. `execution/QC_CHECKLIST.md`로 검증

### 2. Claude Code 사용 시

프로젝트 루트의 `CLAUDE.md` 참조
- Claude가 따라야 할 규칙 정의
- immutable 문서 보호 규칙 포함

### 3. 문서 수정 시

| 문서 유형 | 수정 가능? | 조건 |
|----------|-----------|------|
| immutable | ❌ | 명시적 승인 필요 |
| variable | ⭕ | 세계관 규칙 준수 |
| execution | ⭕ | 자유롭게 |

---

## 핵심 규칙 요약

### 세계관
- 설명하지 않는다
- 보여줄 뿐이다
- 이유는 없다, 방향만 있다

### 톤
- 쿨하고 건조함
- "슬프다" ❌ → "멋있다" ⭕
- Kage Bow급 절제

### 금지
- 내레이션 ❌
- 교훈 ❌
- 민속 설명 ❌
- 감정 과잉 ❌

---

## 정전 문장 (Canonical Statements)

1. **이곳은 이야기를 설명하지 않는다. 결만 남긴다.**

2. **우리는 옳은 길을 보여주지 않는다. 각자의 결을 지나갈 뿐이다.**

3. **이유는 없다. 방향만 있다.**

---

*결을 남긴다.*
