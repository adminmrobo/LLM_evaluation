# 표지 지시문 — AI 점수는 무엇을 잰 것일까 (블로그 글판)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_llmeval_blog · L (16:9, 가로 1920 이상) |
| 붙일 곳 | 블로그 글(Claude 문서) 맨 위 제목 바로 아래 |
| 장소 (앵커) | D 생활·현장: 밤의 채점실(시험 교실). 나무 책상 줄, 창문 너머 연구실 보라 불빛이 한쪽에서 새어 듦 |
| 주제 은유 | 책상 두 개가 나란히 놓인 "두 가지 채점". 왼쪽 책상: 구멍 뚫린 정답 덮개(스텐실)를 객관식 카드 위에 대면 칸마다 초록 빛이 켜짐(정답이 하나인 분류 채점). 오른쪽 책상: 바닥까지 늘어진 긴 손글씨 두루마리 답안(글자는 알아볼 수 없는 물결선)과 저울, 돋보기(정답이 하나가 아닌 LLM 채점) |
| 네 캐릭터 포즈 | 박사: 두 책상 사이 뒤쪽에 서서 큰 빨간 색연필을 들고 두 책상을 번갈아 봄 / 조수: 오른쪽 책상에 앉아 돋보기로 두루마리를 들여다봄 / 초파리: 왼쪽 책상 위에 올라서서 오른쪽을 보며 정답 덮개를 두 손으로 들어 올림 / 주판봇: 오른쪽 앞에서 왼쪽을 보며 주판알을 튕겨 셈 |
| 키 순서 | 박사 1.00 · 조수 0.90 · 주판봇 0.72 · 초파리 0.41 |
| 대체 글 (alt) | 밤의 채점실에서 네 캐릭터가 정답 덮개로 채점하는 책상과 긴 두루마리 답안을 살피는 책상을 나란히 두고 모인 표지 |
| 앞 표지와 다른 점 | 대시보드 표지(cover_llmeval)는 연구실 전경 · 봉인 봉투 상자 · 메달 리본 · 박사 턱 괴기 · 조수 클립보드 · 초파리 손가락질 · 주판봇 주판알 들기. 이 표지는 장소(채점실), 소품(정답 덮개 · 두루마리 · 저울), 포즈를 모두 바꾼다 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장(`adminmrobo/fruitfly-lab-expressions` @ 24e395f: doc_e09, asst_e13, fly_e08, robo_e16)과 설정샷 k10(VS), k12(키 비교)를 올린다. 대시보드 표지를 먼저 받았다면 그 그림도 "같은 세계·같은 그림체" 참고로 함께 올린다.

**Genspark에 붙여 넣기 ↓**
```
웹페이지(블로그 글) 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 박사와 조수는 좌우를 뒤집지 말 것 (머리의 흰 줄·남색 줄 위치가 정해져 있음)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (두루마리의 글씨도 알아볼 수 없는 물결선으로만)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration for a blog article, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night mood, purple lab light spilling in from one side window, soft magenta and green fluorescent accents.
Scene: a quiet night grading room rendered as part of the same night lab world, rows of wooden school desks, a desk lamp on each of two desks placed side by side in the center.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center between the two desks, holding up a big red grading pencil and glancing from one desk to the other;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, sitting at the right desk, leaning in and looking through a magnifying glass at a long paper scroll;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, standing on top of the left desk facing right, lifting a punched answer-key stencil sheet with both hands, about 0.41 of the scientist's height;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right front facing left, flicking beads on a wooden abacus with a focused pixel smile.
Height ratio: scientist 1.00, girl 0.90, robot 0.72, fruit fly 0.41.
Visual metaphor of the topic: two ways of grading side by side. On the left desk, a punched stencil sheet laid over a multiple-choice card, each hole glowing soft green where it matches. On the right desk, a very long hand-written answer scroll (only illegible wavy lines) unrolling over the edge to the floor, next to a small brass balance scale.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple; warm desk lamp light falls on the two desks.
Mood: curious, calm, thoughtful comparison, nobody winning or losing.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands, no microscope.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**받은 뒤:** 비율 16:9, 글자·숫자 없음, 네 캐릭터 외형(박사·조수 좌우 안 뒤집힘, 주판봇 v2 모습), 안전 영역을 확인한다. 블로그 글(Claude 문서) 맨 위 제목 바로 아래에 그림으로 넣고, 대체 글은 위 alt를 쓴다. 공유 미리보기용으로 같은 그림을 잘라 `og_llmeval_blog`(1200×630)도 만든다.
