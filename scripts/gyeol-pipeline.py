#!/usr/bin/env python3
"""
GYEOL Master Production Pipeline
결 프로젝트 통합 제작 파이프라인 - 생산성 5배 향상

사용법:
  python gyeol-pipeline.py new A1-09 --title "침묵" --theme "silence"
  python gyeol-pipeline.py analyze A1-01 --music ~/Downloads/track.mp3
  python gyeol-pipeline.py prompts A1-01
  python gyeol-pipeline.py batch A1 --range 1-8
  python gyeol-pipeline.py status
"""

import google.generativeai as genai
import sys
import os
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

# .env 파일 로드
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass

# API 설정
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# 경로 설정
PROJECT_ROOT = Path(__file__).parent.parent
DOCS_ROOT = PROJECT_ROOT / "docs"
TRACKS_ROOT = DOCS_ROOT / "06_tracks"
ASSETS_ROOT = PROJECT_ROOT / "assets"
ANALYSIS_DIR = ASSETS_ROOT / "analysis"

# 색상 출력
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'

def print_header(msg):
    print(f"\n{Colors.CYAN}{'='*60}{Colors.NC}")
    print(f"{Colors.CYAN}  {msg}{Colors.NC}")
    print(f"{Colors.CYAN}{'='*60}{Colors.NC}\n")

def print_success(msg):
    print(f"{Colors.GREEN}✅ {msg}{Colors.NC}")

def print_warning(msg):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.NC}")

def print_error(msg):
    print(f"{Colors.RED}❌ {msg}{Colors.NC}")

def print_info(msg):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.NC}")

# ============================================================
# 1. 트랙 생성 (NEW)
# ============================================================

TRACK_TEMPLATE = '''---
title: "{title_ko} ({title_en})"
type: track
locked: false
version: 1.0
last_updated: {date}
album: {album}
track_number: {track_num}
status: 🔴 대기
description: "Album {album} {track_num}번째 트랙. {theme}"
tags: [track, {album}, phase-a, {title_ko}]
---

# {track_id} {title_ko} ({title_en}) — 제작 현황

> **핵심 목표**: 눈을 못떼게, 귀에서 맴돌게
>
> **앨범**: {album_name}
> **트랙 번호**: {track_num}
> **상태**: 🔴 대기

---

## 📊 진행률

```
전체 진행률: ░░░░░░░░░░ 0%

1. 기획      ██████████ 100%
2. 음악      ░░░░░░░░░░   0%
3. 이미지    ░░░░░░░░░░   0%
4. 영상      ░░░░░░░░░░   0%
5. 편집      ░░░░░░░░░░   0%
6. QC        ░░░░░░░░░░   0%
```

---

## 🎯 훅 포인트

| 포인트 | 목표 | 왜 중요한가 |
|--------|------|-------------|
| **시각적 훅** | TBD | 첫 5초 잡기 |
| **청각적 훅** | TBD | 귀에 박히는 소리 |
| **서사적 훅** | TBD | "뭐지?" 유발 |

---

## 1️⃣ 기획 단계 ✅

### 트랙 정보

| 항목 | 내용 |
|------|------|
| 제목 (한글) | {title_ko} |
| 제목 (영문) | {title_en} |
| 테마 | {theme} |
| 존재 등장 | TBD |
| 키워드 | {title_ko}, {theme} |
| BPM | ~110 |
| 키 | Am |
| 길이 | 3:30 |

### 컨셉

> TBD - 컨셉 작성 필요

---

## 2️⃣ 음악 제작 🔴

### Suno 프롬프트 (Style of Music)

```
atmospheric trap, korean traditional fusion, industrial electronic,
110 bpm, Am, dark ambient hypnotic,
gayageum texture drone, janggu syncopation,
immediate hook, punchy intro, attention-grabbing first 5 seconds,
[Intro] atmospheric tension builds
[Verse] rhythm establishes, world opens
[Pre] intensity rises
[Drop] full impact, overwhelming
[Break] breath, space
[Outro] unresolved, fading
```

### Lyrics

```
[Intro]
(atmospheric sound design)

[Verse]
TBD - 가사 작성 필요

[Pre-Chorus]
TBD

[Drop]
TBD

[Outro]
TBD
```

---

## 3️⃣ 이미지 제작 🔴

### MJ 이미지 리스트 (30장)

> **타임라인**: 3:30 = 210초, 7초당 1장

| # | 타임 | 설명 | 프롬프트 |
|---|------|------|----------|
| 01 | 0:00 | TBD | `TBD --ar 16:9 --style raw --s 250` |
| ... | ... | ... | ... |

---

## 4️⃣ 영상 제작 🔴

### Shot List

| # | 구간 | 도구 | 내용 | 훅 |
|---|------|------|------|-----|
| 1 | Intro | MJ Video | TBD | |
| ... | ... | ... | ... | |

---

## 6️⃣ QC 체크리스트 🔴

- [ ] 초반 5초 훅 있는가?
- [ ] Kage Bow급 쿨함이 느껴지는가?
- [ ] 설명 없이 보여주는가?
- [ ] 금지 규칙 위반 없는가?

---

## 🔗 관련 문서

- [[06_tracks/{album}/]]
- [[05_execution/SUNO_PROMPTS]]
- [[05_execution/MIDJOURNEY_PROMPTS]]

---

*Last updated: {date}*
'''

def create_track(track_id: str, title_ko: str, title_en: str = None, theme: str = "TBD"):
    """새 트랙 문서 생성"""
    print_header(f"새 트랙 생성: {track_id}")

    # 파싱
    parts = track_id.split('-')
    if len(parts) != 2:
        print_error(f"잘못된 트랙 ID 형식: {track_id} (예: A1-01)")
        return False

    album = parts[0]
    track_num = parts[1]

    # 영문 제목 자동 생성
    if not title_en:
        title_en = title_ko.upper()

    # 앨범 이름 매핑
    album_names = {
        'A1': 'A-1 흔들림', 'A2': 'A-2 경계',
        'B1': 'B-1 뒤섞임', 'B2': 'B-2 드러남',
        'C1': 'C-1 기록', 'C2': 'C-2 남은 것',
        'O0': 'O-0 기원'
    }
    album_name = album_names.get(album, album)

    # 템플릿 채우기
    content = TRACK_TEMPLATE.format(
        track_id=track_id,
        title_ko=title_ko,
        title_en=title_en,
        theme=theme,
        album=album,
        album_name=album_name,
        track_num=track_num,
        date=datetime.now().strftime('%Y-%m-%d')
    )

    # 저장
    album_dir = TRACKS_ROOT / album
    album_dir.mkdir(parents=True, exist_ok=True)

    output_file = album_dir / f"{track_id}_{title_ko}.md"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print_success(f"트랙 문서 생성: {output_file}")

    # 작업 폴더 생성
    work_dir = ASSETS_ROOT / "work" / track_id
    for subdir in ["music", "images", "video/raw", "video/edited", "export/shorts"]:
        (work_dir / subdir).mkdir(parents=True, exist_ok=True)

    print_success(f"작업 폴더 생성: {work_dir}")
    print_info(f"음악 파일 저장: {work_dir}/music/")
    print_info(f"이미지 저장: {work_dir}/images/")

    return True

# ============================================================
# 2. 음악 분석 (ANALYZE)
# ============================================================

ANALYSIS_PROMPT = """당신은 결(GYEOL) 프로젝트의 음악 분석 전문가입니다.

이 음악을 분석하여 다음 정보를 **정확한 타임스탬프와 함께** 추출해주세요:

## 1. 구조 분석 (필수 - 정확한 초 단위)
| 섹션 | 시작 | 끝 | 길이 |
|------|------|-----|------|
| Intro | 0:00 | ?:?? | ?? 초 |
| Verse 1 | ?:?? | ?:?? | ?? 초 |
| Pre-Chorus | ?:?? | ?:?? | ?? 초 |
| Drop/Chorus | ?:?? | ?:?? | ?? 초 |
| Break | ?:?? | ?:?? | ?? 초 |
| Verse 2 | ?:?? | ?:?? | ?? 초 |
| Drop 2 | ?:?? | ?:?? | ?? 초 |
| Outro | ?:?? | ?:?? | ?? 초 |

## 2. 섹션별 분위기 키워드
각 섹션에 맞는 한 단어 (결 세계관: 어긋남, 흔들림, 경계, 지움, 그림자, 의례, 기원)

## 3. MidJourney 프롬프트 요소 (섹션별)
| 섹션 | 색상 톤 | 분위기 | 동작 | MJ 키워드 |
|------|---------|--------|------|-----------|
| Intro | ? | ? | ? | ? |
| ... | | | | |

## 4. 훅 포인트 TOP 3
| 순위 | 타임스탬프 | 설명 | 왜 훅인가 |
|------|-----------|------|----------|
| 1 | ?:?? | ? | ? |
| 2 | ?:?? | ? | ? |
| 3 | ?:?? | ? | ? |

## 5. 기술 분석
- **BPM**: (정확히)
- **키**: (추정)
- **주요 악기/사운드**:
- **특이 사항**:

## 6. 30장 이미지 타임라인 제안
7초 간격으로 30장의 이미지 설명과 MJ 프롬프트 핵심 키워드:
| # | 시간 | 설명 | MJ 키워드 |
|---|------|------|-----------|
| 01 | 0:00 | ? | ? |
| 02 | 0:07 | ? | ? |
| ... | | | |
| 30 | 3:23 | ? | ? |

마크다운 테이블 형식으로 정리해주세요."""

def analyze_music(track_id: str, music_file: str):
    """음악 파일을 Gemini API로 분석"""
    print_header(f"음악 분석: {track_id}")

    music_path = Path(music_file).expanduser()

    if not music_path.exists():
        # assets/music에서 찾기
        alt_path = ASSETS_ROOT / "music" / music_file
        if alt_path.exists():
            music_path = alt_path
        else:
            print_error(f"파일 없음: {music_file}")
            return None

    print_info(f"파일: {music_path}")

    # 업로드
    print_info("파일 업로드 중...")
    try:
        audio_file = genai.upload_file(str(music_path))
        print_success(f"업로드 완료")
    except Exception as e:
        print_error(f"업로드 실패: {e}")
        return None

    # 분석
    print_info("Gemini 2.5 Pro로 분석 중...")
    try:
        model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06')
        response = model.generate_content([ANALYSIS_PROMPT, audio_file])
        result = response.text
    except Exception as e:
        print_warning(f"2.5-pro 실패, 2.5-flash 시도: {e}")
        try:
            model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
            response = model.generate_content([ANALYSIS_PROMPT, audio_file])
            result = response.text
        except Exception as e2:
            print_error(f"분석 실패: {e2}")
            return None

    # 저장
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = ANALYSIS_DIR / f"{track_id}_analysis_{timestamp}.md"

    content = f"""---
title: "{track_id} Music Analysis"
type: analysis
source_file: "{music_path.name}"
analyzed_at: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
model: "gemini-2.5-pro"
---

# {track_id} — 음악 분석

> 분석 도구: Gemini 2.5 Pro
> 분석 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

{result}

---

## 다음 단계

1. [ ] 타임라인 검증 (직접 들으며 확인)
2. [ ] 트랙 문서에 Suno 프롬프트 업데이트
3. [ ] MJ 이미지 30장 생성
4. [ ] 영상 편집 계획

---

*Generated by GYEOL Pipeline*
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print_success(f"분석 완료: {output_file}")

    # 요약 출력
    print(f"\n{Colors.PURPLE}{'='*60}{Colors.NC}")
    print(f"{Colors.PURPLE}분석 결과 미리보기{Colors.NC}")
    print(f"{Colors.PURPLE}{'='*60}{Colors.NC}\n")
    print(result[:3000])
    if len(result) > 3000:
        print(f"\n{Colors.YELLOW}... (전체 내용은 파일 참조){Colors.NC}")

    return output_file

# ============================================================
# 3. 프롬프트 생성 (PROMPTS)
# ============================================================

SUNO_PROMPT_TEMPLATE = """당신은 결(GYEOL) 프로젝트의 Suno 프롬프트 전문가입니다.

다음 트랙 정보를 바탕으로 최적화된 Suno 프롬프트를 생성해주세요:

트랙 정보:
{track_info}

## 규칙
1. Style of Music은 1000자 이내
2. 필수 키워드: atmospheric trap, korean traditional fusion, immediate hook
3. 전통 악기는 텍스처로만: gayageum texture, janggu syncopation
4. 초반 5초 후킹 필수
5. 한영 혼용 가사 (Hook 60% 영어 / Drop 70% 한국어)

## 출력 형식

### [Style of Music] (복사용)
```
(여기에 프롬프트)
```

### [Lyrics] (복사용)
```
(여기에 가사)
```

### 생성 팁
- 권장 설정
- 주의 사항"""

MJ_PROMPT_TEMPLATE = """당신은 결(GYEOL) 프로젝트의 MidJourney 프롬프트 전문가입니다.

다음 트랙 분석을 바탕으로 30장의 MJ 프롬프트를 생성해주세요:

분석 정보:
{analysis}

## 규칙
1. 필수 키워드: hanji paper texture, ink wash, --ar 16:9 --style raw --s 250
2. 금지 색상: 순수 흰색, 순수 검정, 네온, 파스텔
3. 조명: 황혼, 새벽, 달빛, 불빛 (밝은 대낮 금지)
4. 7초 간격 = 30장 (3:30 기준)
5. 훅 포인트에 ★★★ 표시

## 출력 형식

| # | 시간 | 설명 | 프롬프트 (복사용) |
|---|------|------|-------------------|
| 01 | 0:00 | ... | `...` |
| ... | | | |

### 핵심 훅 이미지 (우선 제작)
1. #?? - ★★★
2. #?? - ★★
3. #?? - ★"""

def generate_prompts(track_id: str, prompt_type: str = "all"):
    """트랙에 맞는 Suno/MJ 프롬프트 생성"""
    print_header(f"프롬프트 생성: {track_id}")

    # 트랙 문서 찾기
    album = track_id.split('-')[0]
    track_files = list((TRACKS_ROOT / album).glob(f"{track_id}*.md"))

    if not track_files:
        print_error(f"트랙 문서 없음: {track_id}")
        return None

    track_file = track_files[0]
    print_info(f"트랙 문서: {track_file}")

    with open(track_file, 'r', encoding='utf-8') as f:
        track_content = f.read()

    # 분석 파일 찾기
    analysis_files = sorted(ANALYSIS_DIR.glob(f"{track_id}_analysis_*.md"), reverse=True)
    analysis_content = ""
    if analysis_files:
        with open(analysis_files[0], 'r', encoding='utf-8') as f:
            analysis_content = f.read()
        print_info(f"분석 파일: {analysis_files[0]}")

    results = {}

    # Suno 프롬프트
    if prompt_type in ["all", "suno"]:
        print_info("Suno 프롬프트 생성 중...")
        try:
            model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06')
            prompt = SUNO_PROMPT_TEMPLATE.format(track_info=track_content[:3000])
            response = model.generate_content(prompt)
            results['suno'] = response.text
            print_success("Suno 프롬프트 생성 완료")
        except Exception as e:
            print_error(f"Suno 프롬프트 생성 실패: {e}")

    # MJ 프롬프트
    if prompt_type in ["all", "mj"] and analysis_content:
        print_info("MidJourney 프롬프트 생성 중...")
        try:
            model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06')
            prompt = MJ_PROMPT_TEMPLATE.format(analysis=analysis_content[:5000])
            response = model.generate_content(prompt)
            results['mj'] = response.text
            print_success("MJ 프롬프트 생성 완료")
        except Exception as e:
            print_error(f"MJ 프롬프트 생성 실패: {e}")

    # 저장
    if results:
        output_file = ANALYSIS_DIR / f"{track_id}_prompts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        content = f"# {track_id} — 프롬프트 생성 결과\n\n"
        content += f"> 생성 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"

        if 'suno' in results:
            content += f"## Suno 프롬프트\n\n{results['suno']}\n\n---\n\n"
        if 'mj' in results:
            content += f"## MidJourney 프롬프트\n\n{results['mj']}\n\n"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print_success(f"프롬프트 저장: {output_file}")

        # 미리보기
        print(f"\n{Colors.PURPLE}{'='*60}{Colors.NC}")
        for key, value in results.items():
            print(f"\n{Colors.CYAN}[{key.upper()}]{Colors.NC}\n")
            print(value[:2000])
            if len(value) > 2000:
                print(f"\n{Colors.YELLOW}... (전체 내용은 파일 참조){Colors.NC}")

    return results

# ============================================================
# 4. 배치 처리 (BATCH)
# ============================================================

def batch_process(album: str, track_range: str, action: str = "status"):
    """여러 트랙 일괄 처리"""
    print_header(f"배치 처리: {album} ({track_range})")

    # 범위 파싱
    start, end = map(int, track_range.split('-'))

    for i in range(start, end + 1):
        track_id = f"{album}-{i:02d}"
        print(f"\n{Colors.CYAN}--- {track_id} ---{Colors.NC}")

        if action == "status":
            # 상태 확인
            track_files = list((TRACKS_ROOT / album).glob(f"{track_id}*.md"))
            analysis_files = list(ANALYSIS_DIR.glob(f"{track_id}_analysis_*.md"))

            status = []
            if track_files:
                status.append("📄 문서")
            if analysis_files:
                status.append("🎵 분석")

            if status:
                print(f"  {' | '.join(status)}")
            else:
                print(f"  {Colors.YELLOW}미생성{Colors.NC}")

# ============================================================
# 5. 상태 확인 (STATUS)
# ============================================================

def show_status():
    """전체 프로젝트 상태"""
    print_header("GYEOL 프로젝트 상태")

    # 앨범별 트랙 수
    albums = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'O0']

    print(f"{Colors.CYAN}앨범별 트랙 현황:{Colors.NC}\n")
    print("| 앨범 | 트랙 수 | 분석 완료 |")
    print("|------|---------|----------|")

    total_tracks = 0
    total_analyzed = 0

    for album in albums:
        album_dir = TRACKS_ROOT / album
        if album_dir.exists():
            tracks = list(album_dir.glob("*.md"))
            analyzed = len(list(ANALYSIS_DIR.glob(f"{album}-*_analysis_*.md")))
            print(f"| {album}   | {len(tracks):7d} | {analyzed:8d} |")
            total_tracks += len(tracks)
            total_analyzed += analyzed
        else:
            print(f"| {album}   |       0 |        0 |")

    print(f"|------|---------|----------|")
    print(f"| 합계 | {total_tracks:7d} | {total_analyzed:8d} |")

    # 최근 분석
    print(f"\n{Colors.CYAN}최근 분석:{Colors.NC}\n")
    recent = sorted(ANALYSIS_DIR.glob("*_analysis_*.md"), key=os.path.getmtime, reverse=True)[:5]
    for f in recent:
        print(f"  - {f.name}")

# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='GYEOL Master Production Pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
예시:
  %(prog)s new A1-09 --title 침묵 --theme silence
  %(prog)s analyze A1-01 --music ~/Downloads/track.mp3
  %(prog)s prompts A1-01
  %(prog)s batch A1 --range 1-8
  %(prog)s status
        '''
    )

    subparsers = parser.add_subparsers(dest='command', help='명령')

    # new
    new_parser = subparsers.add_parser('new', help='새 트랙 생성')
    new_parser.add_argument('track_id', help='트랙 ID (예: A1-09)')
    new_parser.add_argument('--title', '-t', required=True, help='한글 제목')
    new_parser.add_argument('--title-en', '-e', help='영문 제목')
    new_parser.add_argument('--theme', default='TBD', help='테마')

    # analyze
    analyze_parser = subparsers.add_parser('analyze', help='음악 분석')
    analyze_parser.add_argument('track_id', help='트랙 ID')
    analyze_parser.add_argument('--music', '-m', required=True, help='음악 파일 경로')

    # prompts
    prompts_parser = subparsers.add_parser('prompts', help='프롬프트 생성')
    prompts_parser.add_argument('track_id', help='트랙 ID')
    prompts_parser.add_argument('--type', '-t', choices=['all', 'suno', 'mj'], default='all')

    # batch
    batch_parser = subparsers.add_parser('batch', help='배치 처리')
    batch_parser.add_argument('album', help='앨범 (예: A1)')
    batch_parser.add_argument('--range', '-r', default='1-8', help='트랙 범위 (예: 1-8)')
    batch_parser.add_argument('--action', '-a', choices=['status'], default='status')

    # status
    subparsers.add_parser('status', help='전체 상태')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == 'new':
        create_track(args.track_id, args.title, args.title_en, args.theme)
    elif args.command == 'analyze':
        analyze_music(args.track_id, args.music)
    elif args.command == 'prompts':
        generate_prompts(args.track_id, args.type)
    elif args.command == 'batch':
        batch_process(args.album, args.range, args.action)
    elif args.command == 'status':
        show_status()

if __name__ == "__main__":
    main()
