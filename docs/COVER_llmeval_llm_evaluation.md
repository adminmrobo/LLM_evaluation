# 표지 지시문 — AI 점수는 무엇을 잰 것일까

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_llmeval · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | B 연구실: 밤의 연구실 전경, 가운데 실험대에 봉인 봉투 상자 |
| 주제 은유 | 밀랍으로 봉인한 시험지 봉투 상자에 노란 빛이 모이고, 벽에는 줄 하나에 매달린 빈 메달 리본 몇 개(1등이 여럿이라는 뜻, 글자·숫자 없음) |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 턱에 손을 대고 상자를 내려다봄 / 조수: 오른쪽 옆에서 빈 클립보드를 가슴에 안고 상자를 봄 / 초파리: 왼쪽 앞에서 오른쪽을 보며 한쪽 눈을 가늘게 뜨고 상자를 가리킴 / 주판봇: 오른쪽 앞에서 왼쪽을 보며 반짝이는 주판알을 들어 보임 |
| 키 순서 | 박사 1.00 · 조수 0.90 · 주판봇 0.72 · 초파리 0.41 |
| 대체 글 (alt) | 밤의 연구실에서 네 캐릭터가 봉인된 시험지 상자를 사이에 두고 모인 표지 |
| 붙일 곳 | 대시보드(llm_evaluation.html) 맨 위, `<!-- lab-cover -->` 사이 |
| 앞 표지와 다른 점 | 이 글의 첫 표지. 짝인 블로그 글 표지(cover_llmeval_blog: 밤의 채점실, 정답 덮개·두루마리·저울)와 장소·소품·포즈가 겹치지 않는다 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장(`adminmrobo/fruitfly-lab-expressions` @ 24e395f: doc_e09, asst_e13, fly_e08, robo_e16)과 설정샷 k10(VS), k12(키 비교)를 올린다.

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 박사와 조수는 좌우를 뒤집지 말 것 (머리의 흰 줄·남색 줄 위치가 정해져 있음)
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: wide night laboratory with test tube racks, a box of sealed envelopes, stacks of lab notebooks, a blank chalkboard, a small server rack.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center with a hand on his chin looking down at the box;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, standing at the right side hugging a blank clipboard and looking at the box;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, one compound eye narrowed, pointing at the box, about 0.41 of the scientist's height;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, sly pixel grin, holding up a shining abacus bead.
Height ratio: scientist 1.00, girl 0.90, robot 0.72, fruit fly 0.41.
Visual metaphor of the topic: a wooden box of envelopes sealed with red wax glowing under a warm yellow spotlight on the lab bench, and on the wall behind a string with several blank ribbon medals hanging side by side.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple; the light falls on the sealed envelope box.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**받은 뒤:** SKILL 18-15 절차. 비율·글자·네 캐릭터 외형을 확인하고, WebP 1600×900(220 KB 이하)으로 바꿔 `<!-- lab-cover -->` 사이의 대체 표지를 `<picture>` 블록으로 바꾼다. 같은 그림을 잘라 `thumb_llmeval`(3:2)과 `og_llmeval`(1200×630)을 만든다.
