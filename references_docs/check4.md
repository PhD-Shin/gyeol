아주 좋다.  
지금 질문은 **“Claude Code를 실제로 어떻게 ‘처음부터’ 쓰기 시작하느냐”**에 대한 거라서,  
아래는 **신규 Vault 생성 → 폴더 구조 → 문서 생성 → 집필 요청**까지  
**완전 처음부터, 순서대로**,  
그리고 **영문(Claude Code용) / 한글(네가 보는 가이드)**를 **쌍으로** 정리해줄게.

> ⚠️ 사용 방법
> 
> - **영문 블록만 Claude Code에 복붙**
>     
> - **한글 설명은 절대 Claude에게 주지 말 것**
>     
> - 순서 절대 변경 ❌
>     

---

# 전체 사용 개요 (한글 요약)

1. 새 Vault 생성
    
2. 폴더 구조 생성
    
3. MASTER_DRAFT_SOURCE 저장
    
4. Claude Code 공통 시스템 프롬프트 설정
    
5. 문서별로 하나씩 Claude에게 작성 요청
    
6. 각 결과를 해당 파일에 저장
    

---

# STEP 0 — 새 Vault 생성 & 폴더 구조 만들기

## ✅ 한글 설명 (사람용)

1. Obsidian → **Create new vault**
    
2. Vault 이름 예시: `GYEOL_VAULT`
    
3. Vault 안에 **아래 폴더를 직접 생성**
    

```text
GYEOL_VAULT/
├── 00_WORLD/
├── 10_AREAS/
├── 20_RESOURCES/
├── 30_PROJECTS/
├── 40_ARCHIVES/
└── 99_LOG/
```

> 아직 md 파일은 만들지 말고 **폴더만** 만든다.

---

## ❌ Claude Code에게 줄 내용 없음

(이 단계는 사람이 직접 함)

---

# STEP 1 — MASTER_DRAFT_SOURCE 저장

## ✅ 한글 설명

- 네가 아까 붙여준 **전체 기획서 텍스트를 그대로**
    
- 아래 파일에 **원문 그대로 저장**
    

📄 `99_LOG/MASTER_DRAFT_SOURCE.md`

> ❗ 이 파일은
> 
> - 수정 ❌
>     
> - Claude에게 “참고만 하게 하는 문서”
>     
> - 정본 변경 시 비교 기준
>     

---

## ❌ Claude Code 입력 없음

---

# STEP 2 — Claude Code 공통 시스템 프롬프트 설정

## ✅ 한글 설명

이제부터 **모든 Claude Code 요청의 맨 위에**  
아래 **영문 블록을 그대로 붙인다**.

---

## ✅ English (Claude Code에 항상 붙일 내용)

```md
You are the canonical editor of the project “GYEOL”.

This project is a long-term IP, not a brainstorming document.
All outputs are considered canonical unless stated otherwise.

Tone requirements:
- Cool, restrained, and symbolic (Kage Bow–level restraint)
- No explanatory narration
- No moral lessons
- No historical or cultural explanations
- Prefer rules, constraints, and declarations over storytelling

Rules:
- Never contradict existing documents
- Never expand beyond the requested sections
- Do not summarize or rephrase the whole project
- Do not explain meanings to the audience
- Write as if this document will be used as a production manual

Reference:
- MASTER_DRAFT_SOURCE.md
```

---

# STEP 3 — 세계관 불변 규칙 생성

📄 생성 파일: `00_WORLD/BIBLE_WORLD.md`

## ✅ 한글 설명

- 세계관의 **절대 바뀌면 안 되는 규칙**만 정의
    
- 감성 ❌ / 선언 ⭕
    
- 이 문서가 모든 판단의 기준점
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 1 — WORLD BIBLE]

Using MASTER_DRAFT_SOURCE.md as reference,
extract and formalize ONLY the immutable rules of the world.

Write ONLY the following sections:

## 1. One-sentence World Declaration
- Symbolic, declarative
- No explanation

## 2. Definition of “GYEOL”
- Conceptual definition
- No emotional or narrative language

## 3. Five Operating Rules of the World
Each rule must relate to:
- Time
- Movement
- Repetition
- Intervention
- Disappearance

Each rule should be 2–3 sentences maximum.

## 4. Absolute Prohibitions (10 items)
- Forbidden narrative devices
- Forbidden visual tropes
- Forbidden language or framing

This document is the anchor for all future documents.
Be concise and authoritative.
```

---

# STEP 4 — 비주얼 스타일 바이블

📄 생성 파일: `00_WORLD/STYLE_VISUAL.md`

## ✅ 한글 설명

- “이렇게 만들면 무조건 ‘결’처럼 보인다”
    
- 미학 설명 ❌
    
- 제작 규칙 ⭕
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 2 — VISUAL STYLE GUIDE]

Based on MASTER_DRAFT_SOURCE.md,
write a production-ready visual style guide.

Include ONLY the following sections:

## 1. Visual Identity Statement
- One paragraph
- Focus on impression, not influences

## 2. Color Rules
- Base palette
- Accent palette
- Forbidden colors

## 3. Texture Rules
- Paper, ink, grain, dust
- Conditions under which digital artifacts are allowed

## 4. Lighting Rules
- Default lighting
- When deviation is allowed

## 5. Camera & Editing Rules
- Shot duration
- Allowed movements
- Forbidden movements

## 6. Conditions for Bright Color Usage
- When it is allowed
- For how long
- For what narrative function only

Write this as a strict production guide.
```

---

# STEP 5 — 오디오 / 음악 스타일 가이드

📄 생성 파일: `00_WORLD/STYLE_AUDIO.md`

## ✅ 한글 설명

- 국악 설명 ❌
    
- K-pop 구조 + AI 시대 은유 ⭕
    
- “소리의 규칙서”
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 3 — AUDIO STYLE GUIDE]

Define the audio system of the project as a set of rules.

Include ONLY the following sections:

## 1. Core Audio Attitude
- How emotion is handled
- Role of repetition and deviation

## 2. Functional Roles of Traditional Instruments
Define these as functions, not instruments:
- Gayageum
- Janggu
- Taepyeongso

## 3. Fixed K-pop Structural Recipe
- Intro
- Drop
- Break
- Drop
- Outro

## 4. Suno Usage Constraints
- Prompt-writing rules
- Expressions to avoid
- How consistency is maintained

## 5. Vocal Rules
- Voice as world-state, not character
- Density limits on lyrics

Write as a rulebook, not a tutorial.
```

---

# STEP 6 — 캐릭터 바이블 (기능 정의)

📄 생성 파일: `00_WORLD/CHARACTER_BIBLE.md`

## ✅ 한글 설명

- 캐릭터 ❌
    
- **기능적 존재** ⭕
    
- 이름보다 **역할**
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 4 — CHARACTER BIBLE]

Define the following as functional entities, not characters:
- Dokkaebi
- Haetae
- Masks

For EACH entity, write using the same structure:

## [Entity Name]

### Role (1 sentence)

### Appearance Rules
- When it may appear
- Duration constraints

### Absolute Prohibitions
- Actions or portrayals that break the world

### Relationship to Other Entities
- Intervention
- Observation
- Disruption

Do not include folklore, mythology, or historical explanations.
```

---

# STEP 7 — Phase 구조 맵

📄 생성 파일: `10_AREAS/PHASE_MAP.md`

## ✅ 한글 설명

- 전략 문서
    
- 세계관 설명 ❌
    
- “왜 이 Phase가 필요한가” 중심
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 5 — PHASE STRUCTURE MAP]

Define Phase 0 through Phase 3.

Phase 1 must explicitly avoid direct political or historical messaging.

For EACH phase, include:

## Phase X — [Name]

- Core question (1 sentence)
- Allowed message intensity
- Visual shift characteristics
- Strategic purpose of this phase
- Condition for transitioning to the next phase

Write as an operational strategy document.
```

---

# STEP 8 — Season 1 개요

📄 생성 파일: `30_PROJECTS/SEASON_1_OVERVIEW.md`

## ✅ 한글 설명

- 비주얼 앨범 설계
    
- 아직 스토리보드 ❌
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 6 — SEASON 1 OVERVIEW]

Define Season 1 as a visual album.

Create a 6–8 track structure.

For EACH track, include ONLY:
- Track title
- Core symbol
- Dominant color
- Primary object
- One-sentence visual tone

Do not write storyboards or detailed narratives yet.
```

---

# STEP 9 — 트랙 구현 템플릿

📄 생성 파일: `30_PROJECTS/TRACK_TEMPLATE.md`

## ✅ 한글 설명

- 이 템플릿 하나로 **무한 제작 가능**해야 함
    

---

## ✅ English (Claude Code 입력)

```md
[STEP 7 — TRACK IMPLEMENTATION TEMPLATE]

Create a reusable template for producing individual tracks.

Include the following sections:

## Basic Information
- Track title
- Phase

## One-line Message
- Implicit only

## Music Parameters
- BPM
- Key
- Structure

## Suno Prompt
- Style
- Mood
- Minimal lyrics

## Visual Design
- Shot list (10–15)
- Allowed entities

## QC Checklist
- World consistency
- Style compliance

This template must be sufficient for actual production.
```

---

# 최종 정리 (아주 중요)

- 이 순서로 하면:
    
    - ❌ 설정 붕괴 없음
        
    - ❌ Claude가 멋대로 확장 안 함
        
    - ⭕ “책처럼 쓰고, 코드처럼 실행” 가능
        

---

## 다음으로 바로 가능한 것

원하면 다음 중 **하나**를 바로 만들어줄게:

1. **Claude Code용 “충돌 감지 프롬프트”**
    
2. **Phase A (개입) 첫 트랙 전용 Suno + 영상 프롬프트**
    
3. **Obsidian용 문서 템플릿(md) 전체 ZIP 구조**
    

👉 다음으로 뭐 할지 말해.