# 「AI 점수는 무엇을 잰 것일까」 이미지 제작 명세서 (v1.3)

| 항목 | 내용 |
|---|---|
| 페이지 | llm_evaluation.html (시리즈 번호 미정, 키 접미사 `llmeval`) |
| 모드 / 주 앵커 | 교과서 / B 연구실: 밤의 연구실 전경 + 봉인 봉투 상자 |
| 시즌 | 기본 |
| 대결 | "리더보드 점수, 어떻게 올릴까?" → 결과 **X (주판봇 실격)**. 봉인 시험지 정확도는 초파리 0.720, 주판봇 0.655 |
| 캐릭터 그림 | **캐릭터 팩 CHAR_lab4** (`adminmrobo/fruitfly-lab-expressions` @ 107ce63). 말풍선은 96px, 표지·히어로·대결 머리·아웃트로는 192px. 페이지에 base64로 넣음 |
| 새로 그릴 그림 | P1 1장 (표지) · P2 2장 · P3 2장 |
| 재사용 | 표정 16키 모두 캐릭터 팩에 있음 |
| 그림이 없을 때 | 표지는 CSS 대체 표지(벌집 무늬 + 캐릭터 팩 그림 넷), 배경·장면은 픽셀 캔버스 + 캐릭터 팩 그림으로 이미 완성 상태 |

## v1.3 (2026-11-05): 주판봇 v2 그림
- 캐릭터 팩 1.3(`fruitfly-lab-expressions` @ 24e395f)으로 다시 빌드했다. 이 페이지가 쓰는 주판봇 키 가운데 `robo_coin`(E16)·`robo_smile`(E13)·`robo_calc`(E09)는 **공식 gpt2판**, `robo_blush`(E14)는 **임시 Genspark판**이다. gpt2판 E14가 나오면 같은 키로 바꾸고 다시 빌드한다.
- 장면 속 키 비율을 팩 기준(박사 1.00 · 조수 0.90 · 주판봇 0.72 · 초파리 0.41)으로 맞췄다(표지, 히어로, 아웃트로).
- 새로 그릴 장면·표지 프롬프트의 키 순서 문장에 이 비율을 쓴다: *height ratio scientist 1.00, girl 0.90, robot 0.72, fruit fly 0.41*.

## v1.2 (2026-11-04): 연구실 로봇 교체
- Money-Robo(회사 캐릭터)를 **주판봇**(외국어판 AbaBot)으로 바꿨다. 캐릭터 팩 1.1 · 그림 팩 1.2(`fruitfly-lab-expressions` @ 107ce63)의 벡터 그림을 쓴다. 키 이름 `robo_*`는 그대로다.
- 외형: 베이지색 상자형 CRT 몸체, 짙은 초록 화면에 민트 픽셀 눈·입, 끝에 주판알이 달린 짧은 안테나, 회색 마디형 팔, 무한궤도 두 개. 떠 있지 않으며, 흰 둥근 머리·노란 눈·가슴 표시등·금화는 쓰지 않는다.
- 소품은 금화에서 주판알·나무 주판으로 바꿨다. `robo_coin`은 이제 반짝이는 주판알을 들어 보이는 그림이다(키 이름만 옛 이름).

## v1.0과 달라진 점
- 캐릭터 그림을 임시 픽셀 지도에서 **캐릭터 팩 그림**으로 바꿨다. 표정 16키는 "새로 필요"가 아니라 "재사용"이다.
- 18-4 외형 정정(캐릭터 팩 C3)을 반영했다: 박사는 **얇은 청록 테 사각 안경**에 짧은 꽁지머리, 조수는 **긴 분홍 머리**에 두 번, 초파리는 가운 안에 **검은 조끼**와 **검은 장갑**.
- 폐기된 키 `asst_ledger`를 `asst_report`로 바꿨다(18-5 v1.9).
- `robo_chart`는 64px 말풍선에 쓰지 않는다는 규칙(18-5)에 따라 ③칸 말풍선을 `robo_calc`로 바꿨다.
- 글 표지 `cover_llmeval`(L판, 18-14)을 더했다. 표지가 생기므로 히어로 배경 `bg_llmeval`은 P3로 내렸다.
- 바라보는 쪽은 C5대로 처리했다. 초파리 그림(왼쪽을 봄)은 대결·표지·히어로에서 좌우로 뒤집어 오른쪽을 보게 했다. 박사·조수는 뒤집지 않는다.
- 장면 속 키 순서를 **박사 ≥ 조수 > 주판봇 > 초파리**(초파리는 박사의 약 1/3)로 맞췄다(18-8, k12).

## 1. 그림체와 고정 외형
- 스타일: 18-3 (16비트 RPG 픽셀아트, 굵은 어두운 외곽선, 2~3단계 명암)
- 캐릭터 고정 외형: 캐릭터 팩 18-4 (아래 영어 묘사 그대로)
  - 박사: *chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie*
  - 조수: *girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans*
  - 초파리 연구원: *anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings*
  - 주판봇: *boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus*
- 이 페이지 장소: 밤의 연구실 전경. 시험관 선반, 가운데 실험대의 봉인 봉투 상자(노란 빛), 실험 노트 더미, 글자 없는 칠판, 작은 서버 랙
- 장소 영어 묘사: *wide night laboratory with test tube racks, a box of sealed envelopes, stacks of lab notebooks, a blank chalkboard, a small server rack*
- 생물 앵커가 아니므로 현미경·초파리 해부 소품은 넣지 않는다.

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 0 | cover_llmeval | L | 1920×1080 | **반영 2026-11-05** (WebP 1600×900, 158 KB) | P1 | 맨 위 글 표지 | CSS 대체 표지 + 캐릭터 팩 그림 넷 |
| 0b | cover_llmeval_blog | L | 1920×1080 | **반영 2026-11-05** (블로그 글 문서, WebP 113 KB) | P1 | 블로그 글 제목·날짜 줄 아래 | 없음 |
| 1 | bg_llmeval | F | 1920×720 | 새로 | P3 (표지 있음) | 히어로 배경 `.hero-bg` | 픽셀 캔버스 + 캐릭터 팩 그림 넷 |
| 2 | sc_llmeval_outro | E | 1200×800 | 새로 | P2 | 아웃트로 장면 | 픽셀 캔버스 + 캐릭터 팩 그림 넷 |
| 3 | thumb_llmeval | I | 600×400 | 새로 (cover 3:2 자르기) | P2 | 목차 카드 (페이지 밖) | 색 카드 |
| 4 | og_llmeval | K | 1200×630 | 새로 (cover 자르기) | P3 | 공유 미리보기 (페이지 밖) | 없음 |
| 5 | doc_think | A | 96 · 192 | 재사용 (doc_e09) | — | 히어로 대화창, 히어로 배경 | — |
| 6 | doc_front | A | 96 · 192 | 재사용 (doc_e08) | — | 등장인물, 아웃트로 말풍선, 표지 | — |
| 7 | doc_board | A | 96 | 재사용 (doc_e07, near) | — | ④칸 말풍선 | — |
| 8 | doc_judge | A | 96 · 192 | 재사용 (doc_e10, near) | — | 대결 판정, 아웃트로 장면 | — |
| 9 | asst_smile | B | 96 · 192 | 재사용 (asst_e13) | — | 히어로, 등장인물, 아웃트로, 표지 | — |
| 10 | asst_firm | B | 96 | 재사용 (asst_e12) | — | ②칸 말풍선 | — |
| 11 | asst_report | B | 96 | 재사용 (asst_e07) | — | 대결 발표 자리, 꾸러미 섹션 | — |
| 12 | asst_shock | B | 96 · 192 | 재사용 (asst_e24) | — | 대결 결과 X (스크립트가 바꿈), 아웃트로 장면 | — |
| 13 | fly_clip | C | 96 | 재사용 (fly_e10) | — | 등장인물 | — |
| 14 | fly_point | C | 96 · 192 | 재사용 (fly_e08), 왼쪽을 봄 → 대결·표지·히어로에서 뒤집음 | — | 히어로, 왜, ①칸, 대결 전, 표지 | — |
| 15 | fly_magnify | C | 96 | 재사용 (fly_e07) | — | ⑤칸 말풍선 | — |
| 16 | fly_arms | C | 96 · 192 | 재사용 (fly_e16) | — | 대결 결과 X, 아웃트로 | — |
| 17 | robo_smile | D | 96 | 재사용 (robo_e13) | — | 등장인물 | — |
| 18 | robo_coin | D | 96 · 192 | 재사용 (robo_e16) | — | 히어로, 대결 전, 표지 | — |
| 19 | robo_calc | D | 96 | 재사용 (robo_e09, near: 톱니바퀴 생각) | — | ③칸 말풍선 | — |
| 20 | robo_blush | D | 96 · 192 | 재사용 (robo_e14) | — | 대결 결과 X, 아웃트로 | — |
| — | 행동으로 보기 | — | — | 코드 | — | 도형·카드 | — |

대결 결과 X의 표정은 5-8 표와 같다(실격: doc_judge, asst_shock, fly_arms, robo_blush). 결과 전에는 fly_point, robo_coin만 보이고, 발표·판정 말풍선은 결과를 보기 전까지 숨겨져 있다.

## 3. 새로 그릴 그림 상세

### 3-0. `cover_llmeval` — 글 표지
상세와 Genspark 지시문은 `COVER_llmeval_llm_evaluation.md`에 있다.

### 3-1. `sc_llmeval_outro` — 실격 판정 뒤의 연구실
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 배경 | 그림 전체 |
| 구도 | 박사가 가운데 뒤에서 엄지를 세워 판정한다. 초파리 연구원은 왼쪽 앞에서 오른쪽을 보며 팔짱을 낀다(박사 키의 약 1/3). 주판봇은 가운데 오른쪽에서 왼쪽을 보며 머리를 긁고, 초록 화면 얼굴에 분홍 픽셀 볼이 뜬다(글자 없음). 조수는 오른쪽 끝에서 놀란 얼굴로 두 손을 든다. 가운데 바닥에는 열린 봉인 봉투가 있다 |
| 표정·몸짓 | doc_judge, fly_arms, robo_blush, asst_shock |
| 키 순서 | 박사 ≥ 조수 > 주판봇 > 초파리 |
| 소품 | 열린 봉투와 흩어진 빈 종이, 바닥에 굴러가는 주판알 몇 개 |
| 빛·분위기 | 보라 조명, 봉투 쪽에 노란 빛 |
| 피할 것 | 조롱하는 몸짓(주판봇도 인정하는 몸짓으로), 글자, 피·무기 |
| 대체 글 (alt) | 박사가 판정하고, 초파리 연구원이 팔짱을 끼고, 주판봇이 머리를 긁는 연구실 장면 |
| 대신 쓰는 그림 | 픽셀 캔버스 + 캐릭터 팩 그림 넷 (지금 페이지) |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, wide night laboratory with test tube racks, a box of sealed envelopes, stacks of lab notebooks, a blank chalkboard, a small server rack, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center giving a thumbs up with a wink as the judge, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, in the front left facing right with arms crossed and a confident look, about 0.41 of the scientist's height, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, center right facing left scratching its head with drooping pixel eyes and pink pixel blush on its green screen, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at the far right with wide surprised eyes, a sweat drop and both hands raised, height ratio scientist 1.00, girl 0.90, robot 0.72, fruit fly 0.41, an opened envelope sealed with red wax on the floor in the center with a few red-brown abacus beads rolling away, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-2. `bg_llmeval` — 봉인 봉투가 놓인 밤의 연구실 (P3)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | F · 1920×720 |
| 구도 | 왼쪽 45%는 어두운 벽과 바닥만 둔다(제목 글자 자리). 오른쪽 가운데 실험대에 봉인 봉투 상자를 놓고, 그 뒤로 시험관 선반과 서버 랙, 오른쪽 끝에 모니터를 둔다. 인물 없음(캐릭터 팩 그림을 페이지가 얹는다) |
| 피할 것 | 글자·숫자, 현미경·초파리 소품, 실존 브랜드 |
| 대체 글 (alt) | 봉인된 시험지 봉투 상자가 노란 빛을 받는 밤의 연구실 |

**프롬프트 (복사해서 사용)**
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, wide night laboratory with test tube racks, a box of sealed envelopes, stacks of lab notebooks, a blank chalkboard, a small server rack, a wooden lab bench on the right holding a box of envelopes sealed with red wax under a warm yellow spotlight, test tubes glowing magenta green and blue, a monitor with a soft teal glow at the far right, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `thumb_llmeval`, `og_llmeval`
`cover_llmeval`을 받은 뒤 잘라서 만든다. 썸네일은 봉투 상자를 가운데 두고 3:2로, 공유 미리보기는 1200×630으로 자른다. 대체 글: "봉인된 시험지 상자를 사이에 둔 연구실 네 식구".

## 4. 일관성 지침
- 참고 이미지: 캐릭터 팩 그림(`fruitfly-lab-expressions` @ 107ce63)과 설정샷 k02~k05(3면도), k10(VS), k12(키 비교)를 함께 올린다
- 같은 캐릭터는 같은 세션에서 만든다. 시드를 고정할 수 있으면 고정한다
- 표정만 바꿀 때 추가 문장: *same character, same size and position, only change the facial expression and pose to ...*
- 박사·조수는 좌우를 뒤집지 않는다(브릿지 위치, C5)

## 5. 넘겨받은 뒤 처리
1. `build_character_pack.py --ingest ./받은그림 --plates cover_llmeval=L,sc_llmeval_outro=E,bg_llmeval=F --out received_llmeval`
2. 표지는 18-15 절차를 따른다: 비율·글자·네 캐릭터 외형 확인 → WebP 1600 (220 KB 이하) → 390·768·1280 폭에서 점검
3. `data-img` 키 자리에 넣는다. 표지는 `<!-- lab-cover -->` 사이의 대체 표지를 `<picture>` 블록으로 바꾼다
4. 그림 합계를 확인한다. 지금 캐릭터 그림은 base64로 약 239 KB이고, 표지까지 더해도 600 KB 이하여야 한다

## 6. 체크리스트 (18-13, 18-15-1)
- [x] HTML의 `data-img` 키 19개가 모두 이 명세서에 있음 (thumb·og는 페이지 밖)
- [x] 대결 결과 X의 표정이 5-8 표와 일치
- [x] 결과 전 그림(fly_point, robo_coin)에 승패 암시 없음
- [x] 바라보는 쪽: 초파리는 오른쪽, 주판봇은 왼쪽(정면 그림은 그대로), 박사·조수는 뒤집지 않음
- [x] 모든 프롬프트에 정정된 18-4 영어 묘사와 금지 구절이 들어감
- [x] 장소가 B 연구실 앵커와 일치하고, 현미경·해부 소품이 없음
- [x] 그림 안 글자, 실존 브랜드, 회사 캐릭터 Money-Robo의 특징(흰 둥근 머리·노란 눈·부유·금화) 없음
- [x] 장면·배경·표지마다 대체 글이 있음
- [x] 새로 그릴 P1은 표지 1장
- [x] 페이지 그림 합계: 캐릭터 팩 약 239 KB(base64), 표지 반영 후 600 KB 이하 예정

## 7. 매니페스트
```json
{
  "page": "llm_evaluation",
  "version": "1.3",
  "anchor": "B:night-lab-sealed-envelopes",
  "season": "default",
  "characterPack": {"id": "CHAR_lab4", "repo": "adminmrobo/fruitfly-lab-expressions", "commit": "24e395f", "sizes": [96, 192]},
  "duel": {"result": "X", "gap": 0.065, "metric": "sealed test accuracy (400 items)"},
  "images": [
    {"key":"cover_llmeval","plate":"L","size":[1920,1080],"status":"done","priority":"P1","slot":"cover","fallback":"css-pack-four","received":"2026-11-05","bytes":161424,"alt":"밤의 연구실에서 네 캐릭터가 봉인된 시험지 상자를 사이에 두고 모인 표지"},
    {"key":"bg_llmeval","plate":"F","size":[1920,720],"status":"new","priority":"P3","slot":"hero-bg","fallback":"pixel-canvas+pack","alt":"봉인된 시험지 봉투 상자가 노란 빛을 받는 밤의 연구실"},
    {"key":"sc_llmeval_outro","plate":"E","size":[1200,800],"status":"new","priority":"P2","slot":"outro","fallback":"pixel-canvas+pack","alt":"박사가 판정하고, 초파리 연구원이 팔짱을 끼고, 주판봇이 머리를 긁는 연구실 장면"},
    {"key":"thumb_llmeval","plate":"I","size":[600,400],"status":"new-crop","priority":"P2","slot":"index-card","fallback":"color-card","alt":"봉인된 시험지 상자를 사이에 둔 연구실 네 식구"},
    {"key":"og_llmeval","plate":"K","size":[1200,630],"status":"new-crop","priority":"P3","slot":"og","fallback":"none","alt":"봉인된 시험지 상자를 사이에 둔 연구실 네 식구"},
    {"key":"doc_think","pack":"doc_e09","status":"reuse","sizes":[96,192]},
    {"key":"doc_front","pack":"doc_e08","status":"reuse","sizes":[96,192]},
    {"key":"doc_board","pack":"doc_e07","status":"reuse","sizes":[96]},
    {"key":"doc_judge","pack":"doc_e10","status":"reuse","sizes":[96,192]},
    {"key":"asst_smile","pack":"asst_e13","status":"reuse","sizes":[96,192]},
    {"key":"asst_firm","pack":"asst_e12","status":"reuse","sizes":[96]},
    {"key":"asst_report","pack":"asst_e07","status":"reuse","sizes":[96]},
    {"key":"asst_shock","pack":"asst_e24","status":"reuse","sizes":[96,192]},
    {"key":"fly_clip","pack":"fly_e10","status":"reuse","sizes":[96]},
    {"key":"fly_point","pack":"fly_e08","status":"reuse","sizes":[96,192],"facing":"left","flipTo":"right"},
    {"key":"fly_magnify","pack":"fly_e07","status":"reuse","sizes":[96]},
    {"key":"fly_arms","pack":"fly_e16","status":"reuse","sizes":[96,192]},
    {"key":"robo_smile","pack":"robo_e13","status":"reuse","sizes":[96]},
    {"key":"robo_coin","pack":"robo_e16","status":"reuse","sizes":[96,192]},
    {"key":"robo_calc","pack":"robo_e09","status":"reuse","sizes":[96]},
    {"key":"robo_blush","pack":"robo_e14","status":"reuse","sizes":[96,192]}
  ]
}
```
