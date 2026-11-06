**[한국어](#ko) · [English](#en) · [中文](#zh) · [日本語](#ja) · [Oʻzbekcha](#uz) · [Русский](#ru) · [Tiếng Việt](#vi)**

---

<a id="ko"></a>

# AI 점수는 무엇을 잰 것일까 — 분류 모델 채점에서 LLM 리더보드까지

![밤의 연구실에서 네 캐릭터가 봉인된 시험지 상자를 사이에 두고 모인 표지](assets/og_llmeval.jpg)

다들 1등이라는데, 그 1등은 어떤 시험의 1등일까? 분류 모델 채점에서 출발해 대형 언어모델(LLM)의 시험지와 채점 방식까지 다섯 칸으로 올라가는 연구실 해설 대시보드입니다.

- 사이트: https://adminmrobo.github.io/LLM_evaluation/
- 대시보드: [llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.html)
- 글 · 안상선 ((주)M-Robo 대표) · AI 보조 제작 · 논문 리뷰·해설

## 언어

이 시리즈는 한국어 원본과 외국어판 6개로 볼 수 있다.

- 고르는 방법: 화면 최상단 메뉴의 🌐 언어 선택 상자나 오른쪽 아래 🌐 배너에서 고른다. 고른 언어는 브라우저에 기억된다.
- 자동 전환: 한국어 페이지에 처음 들어오면, 브라우저 언어가 지원 언어일 때 그 언어판으로 옮겨 간다. 번역판 주소로 들어오면 그대로 연다.
- 주소 끝에 `?lang=en`처럼 붙이면 그 언어로 바로 연다.
- 언어판 파일은 `이름.언어코드.html` 꼴이다.

<!-- i18n:langtable -->
| 언어 | 파일 이름 | 바로 보기 |
|---|---|---|
| 한국어 | `index.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [바로 보기](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## 무엇을 배우나

| 칸 | 주제 | 직접 해 보는 것 |
|---|---|---|
| ① | 칸 하나 고르기 — 분류 모델 채점 | 시험셋 나누기, stratify, 혼동행렬, 정밀도·재현율 |
| ② | 숫자 맞히기 — 회귀 모델 채점 | MAE와 RMSE, 교차검증 |
| ③ | 정답 있는 긴 답 — 실행해서 채점하기 | 여러 번 풀게 할 때 점수 변화(pass@k) |
| ④ | 정답 없는 답 — 쌍대 투표 | Bradley-Terry 점수, AI 심판의 편향 |
| ⑤ | 시험지 지키기 | 오염, Wilson 구간과 오차막대 |
| 대결 | 리더보드 점수, 어떻게 올릴까? | 초파리 연구원과 주판봇의 점수 올리기 시합 |

## 페이지에 들어 있는 것

- 확인 퀴즈 13문항
- 지식 색인: 개념 130개, 관계 168개
- 실습 키트: 시험지 양식(CSV)과 채점 스크립트(파이썬, 표준 라이브러리만 사용)
- 온톨로지·서지 꾸러미: JSON-LD, Turtle, CSL-JSON, BibTeX, RIS

## 등장인물

| 이름 | 역할 |
|---|---|
| 박사 | 해설과 심판. 판정은 숫자대로 내린다 |
| 조수(하루) | 실험 진행과 숫자 발표. 판정은 하지 않는다 |
| 초파리 연구원 | 의심하는 쪽. 기준선과 검증부터 본다 |
| 주판봇 | 확신하는 쪽. 높은 숫자에 건다 |

## 파일 구성

| 파일 | 내용 |
|---|---|
| `index.html` | 첫 화면 |
| `llm_evaluation.html` | 해설 대시보드 (그림이 모두 들어 있는 단일 파일) |
| `*.en.html` 등 | 외국어판 |
| `assets/` | 첫 화면 표지, 공유 미리보기 그림 |
| `docs/` | 이미지 명세서, 표지 지시문, 지식 색인 등록분, 채점 스크립트 |

로컬에서 볼 때는 HTML 파일을 브라우저로 바로 열면 됩니다. 언어 자동 전환까지 보려면 이 폴더에서 `python3 -m http.server`를 실행한 뒤 http://localhost:8000/ 을 엽니다.

## 리뷰한 논문·자료

1. Hendrycks 외 (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein 외 (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez 외 (2024), SWE-bench
4. Chen 외 (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang 외 (2024), Chatbot Arena, ICML
6. Zheng 외 (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White 외 (2025), LiveBench, ICLR
8. Zhang 외 (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh 외 (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika 외 (2024), HarmBench, arXiv:2402.04249
13. Merrill 외 (2026), Terminal-Bench, arXiv:2601.11868

각 논문의 실험 결과와 수치의 원저작은 논문 저자에게 있습니다. 출처별로 페이지에서 쓴 수치는 대시보드 맨 아래 출처 표에 있습니다.

## 라이선스

- 글: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
- 캐릭터(박사 · 조수 하루 · 초파리 연구원 · 주판봇)의 이름·설정·그림은 저작권자 안상선에게 있으며 허락 없이 쓸 수 없습니다.

## 만든 도구

- 해설 대시보드: [ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- 캐릭터 그림: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (캐릭터 팩 1.3)
- 외국어판: [ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack) (언어팩 v1.3). 외국어판은 원어민 검수 전입니다.

---

<a id="en"></a>

# What Did the AI Score Actually Measure? From Classification Model Scoring to LLM Leaderboards

![Cover: four characters gathered at night in the lab, with a sealed exam-paper box between them](assets/og_llmeval.jpg)

Everyone says they're number one, but which test's number one is it? A lab explainer dashboard that climbs in five steps, from classification model scoring to the exam papers and scoring methods of large language models (LLMs).

- Site: https://adminmrobo.github.io/LLM_evaluation/index.en.html
- Dashboard: [llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.en.html)
- Written by Ahn Sangsun (CEO, M-Robo Inc.) · Produced with AI assistance · Paper review and explainer

## Language

This series is available in the Korean original and six translated editions.

- How to choose: pick from the 🌐 language selector in the top menu bar, or the 🌐 banner at the bottom right. Your choice is remembered in the browser.
- Automatic switching: on your first visit to the Korean page, if your browser language is a supported language, the page switches to that edition. If you open a translated address, it opens as is.
- Append `?lang=en` to the address to open directly in that language.
- Translated edition files follow the pattern `name.languagecode.html`.

<!-- i18n:langtable -->
| Language | File name | Open |
|---|---|---|
| 한국어 | `index.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [Open](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## What you'll learn

| Step | Topic | What you do |
|---|---|---|
| ① | Picking one box — scoring a classification model | Splitting the test set, stratify, confusion matrix, precision and recall |
| ② | Guessing a number — regression model scoring | MAE and RMSE, cross-validation |
| ③ | Long answers with a correct answer — scoring by running the code | How the score changes when you let it try several times (pass@k) |
| ④ | Answers with no single correct one — pairwise voting | Bradley-Terry scores, bias in AI judges |
| ⑤ | Guarding the exam | Contamination, Wilson interval, and error bars |
| Showdown | How do you raise a leaderboard score? | A score-raising contest between the Fruit Fly Researcher and AbaBot |

## What's on this page

- 13-question check-your-understanding quiz
- Knowledge index: 130 concepts, 168 relations
- Practice kit: exam sheet template (CSV) and scoring script (Python, standard library only)
- Ontology & bibliography package: JSON-LD, Turtle, CSL-JSON, BibTeX, RIS

## Cast

| Name | Role |
|---|---|
| Doctor | Explains and judges. Verdicts follow the numbers |
| Assistant (Haru) | Runs the experiments and announces the numbers. Does not judge |
| Fruit Fly Researcher | The skeptic. Checks baselines and validation first |
| AbaBot | The believer. Bets on the high numbers |

## File layout

| Files | Content |
|---|---|
| `index.html` | Front page |
| `llm_evaluation.html` | Explainer dashboard (single file with all figures inside) |
| `*.en.html` etc. | Translated editions |
| `assets/` | Front-page cover, share-preview image |
| `docs/` | Image spec, cover instructions, knowledge index registration, scoring script |

To view locally, open the HTML file directly in a browser. For automatic language switching, run `python3 -m http.server` in this folder and open http://localhost:8000/.

## Papers and sources reviewed

1. Hendrycks et al. (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein et al. (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez et al. (2024), SWE-bench
4. Chen et al. (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang et al. (2024), Chatbot Arena, ICML
6. Zheng et al. (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White et al. (2025), LiveBench, ICLR
8. Zhang et al. (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh et al. (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika et al. (2024), HarmBench, arXiv:2402.04249
13. Merrill et al. (2026), Terminal-Bench, arXiv:2601.11868

The original authors of each paper hold the rights to its experimental results and figures. The sources for the numbers used on this page are listed in the source table at the bottom of the dashboard.

## License

- Text: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en)
- The names, settings, and artwork of the characters (Doctor · Assistant Haru · Fruit Fly Researcher · AbaBot) belong to the copyright holder, Ahn Sangsun, and may not be used without permission.

## Tools used

- Explainer dashboard: [ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- Character artwork: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (character pack 1.3)
- Translated editions: [ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack) (langpack v1.3). The translated editions have not yet been reviewed by native speakers.

---

<a id="zh"></a>

# AI 分数究竟测量了什么 — 从分类模型评分到 LLM 排行榜

![夜晚的实验室里，四个角色围绕封印试卷箱的封面](assets/og_llmeval.jpg)

大家都说自己第一，可那个第一是哪场考试的第一？从分类模型评分出发，一路走到大语言模型（LLM）试卷与评分方式的五格实验室解说仪表板。

- 网站：https://adminmrobo.github.io/LLM_evaluation/index.zh.html
- 仪表板：[llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.zh.html)
- 文 · Ahn Sangsun（M-Robo 公司 CEO）· AI 辅助制作 · 论文评述·解说

## 语言

本系列有韩语原版和 6 个外语版本可供阅读。

- 选择方法：在页面最上方菜单的 🌐 语言选择框或右下角的 🌐 横幅中选择。所选语言会记录在浏览器中。
- 自动切换：首次进入韩语页面时，如果浏览器语言为支持语言，会切换到该语言版本。若通过译文地址进入，则直接打开。
- 在地址末尾加上 `?lang=en` 这样的参数，即可直接以该语言打开。
- 语言版文件的格式为 `名称.语言代码.html`。

<!-- i18n:langtable -->
| 语言 | 文件名 | 直接查看 |
|---|---|---|
| 한국어 | `index.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [直接查看](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## 学习内容

| 格 | 主题 | 亲自操作的内容 |
|---|---|---|
| ① | 选一格 — 分类模型评分 | 划分测试集、stratify、混淆矩阵、精确率·召回率 |
| ② | 猜数字 — 回归模型评分 | MAE 与 RMSE、交叉验证 |
| ③ | 有标准答案的长答案 — 执行评分 | 让模型多次作答时的分数变化（pass@k） |
| ④ | 没有标准答案的回答 — 两两投票 | Bradley-Terry 分数、AI 裁判的偏置 |
| ⑤ | 守住试卷 | 污染、Wilson 区间与误差线 |
| 对决 | 排行榜分数，怎么提高？ | 果蝇研究员与算盘宝的分数提升比赛 |

## 页面包含的内容

- 确认测验 13 题
- 知识索引：130 个概念，168 条关系
- 实践工具包：试卷模板（CSV）与评分脚本（Python，仅使用标准库）
- 本体·文献包：JSON-LD、Turtle、CSL-JSON、BibTeX、RIS

## 登场人物

| 名称 | 角色 |
|---|---|
| 博士 | 解说与裁判。按数字下判定 |
| 助手（Haru） | 推进实验并公布数字。不做判定 |
| 果蝇研究员 | 质疑的一方。先看基线与验证 |
| 算盘宝 | 深信的一方。押注高数字 |

## 文件构成

| 文件 | 内容 |
|---|---|
| `index.html` | 首页 |
| `llm_evaluation.html` | 解说仪表板（所有图片都包含在一个文件中） |
| `*.en.html` 等 | 外语版 |
| `assets/` | 首页封面、分享预览图 |
| `docs/` | 图像说明书、封面指令、知识索引登记、评分脚本 |

本地查看时，用浏览器直接打开 HTML 文件即可。若要体验自动语言切换，请在此文件夹中运行 `python3 -m http.server`，然后打开 http://localhost:8000/ 。

## 已评述的论文·资料

1. Hendrycks 等 (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein 等 (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez 等 (2024), SWE-bench
4. Chen 等 (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang 等 (2024), Chatbot Arena, ICML
6. Zheng 等 (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White 等 (2025), LiveBench, ICLR
8. Zhang 等 (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh 等 (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika 等 (2024), HarmBench, arXiv:2402.04249
13. Merrill 等 (2026), Terminal-Bench, arXiv:2601.11868

各论文的实验结果与数值的原作权归论文作者所有。页面中各出处使用的数值，见仪表板底部的出处表。

## 许可协议

- 文章：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.zh-hans)
- 角色（博士 · 助手 Haru · 果蝇研究员 · 算盘宝）的名称、设定与插图的著作权归版权人 Ahn Sangsun 所有，未经许可不得使用。

## 制作工具

- 解说仪表板：[ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- 角色插图：[fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (角色包 1.3)
- 外语版：[ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack)（语言包 v1.3）。外语版尚未经过母语者审校。

---

<a id="ja"></a>

# AIスコアは何を測ったものか — 分類モデルの採点からLLMリーダーボードまで

![夜の研究室で四人のキャラクターが封印された試験用紙の箱を囲んで集まった表紙](assets/og_llmeval.jpg)

みんな1位だというけれど、その1位はどの試験の1位なのか？ 分類モデルの採点から出発し、大規模言語モデル（LLM）の試験用紙と採点方式まで五つの段階で上がっていく研究室解説ダッシュボードです。

- サイト: https://adminmrobo.github.io/LLM_evaluation/index.ja.html
- ダッシュボード: [llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.ja.html)
- 文 · Ahn Sangsun（株式会社M-Robo 代表） · AI補助制作 · 論文レビュー・解説

## 言語

このシリーズは韓国語の原本と外国語版6つで読むことができます。

- 選び方: 画面最上部のメニューの🌐言語選択ボックス、または右下の🌐バナーから選びます。選んだ言語はブラウザに記憶されます。
- 自動切り替え: 韓国語ページに初めて入ると、ブラウザの言語が対応言語の場合にその言語版へ移ります。翻訳版のアドレスで入った場合はそのまま開きます。
- アドレスの末尾に `?lang=en` のように付けると、その言語で直接開きます。
- 言語版ファイルは `名前.言語コード.html` の形式です。

<!-- i18n:langtable -->
| 言語 | ファイル名 | すぐ見る |
|---|---|---|
| 한국어 | `index.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [すぐ見る](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## 何を学ぶか

| 段階 | テーマ | 実際にやってみること |
|---|---|---|
| ① | 一つ選ぶ — 分類モデルの採点 | 試験セットの分割、stratify、混同行列、適合率・再現率 |
| ② | 数を当てる — 回帰モデルの採点 | MAEとRMSE、交差検証 |
| ③ | 正解のある長い答え — 実行して採点する | 複数回解かせたときのスコアの変化（pass@k） |
| ④ | 正解のない答え — ペア投票 | Bradley-Terryスコア、AI審判のバイアス |
| ⑤ | 試験用紙を守る | 汚染、Wilson区間とエラーバー |
| 対決 | リーダーボードのスコア、どう上げる？ | ショウジョウバエ研究員とアバボットのスコア上げ対決 |

## ページに入っているもの

- 確認クイズ13問
- 知識索引: 概念130個、関係168個
- 実習キット: 試験用紙の書式（CSV）と採点スクリプト（Python、標準ライブラリのみ使用）
- オントロジー・書誌パッケージ: JSON-LD, Turtle, CSL-JSON, BibTeX, RIS

## 登場人物

| 名前 | 役割 |
|---|---|
| 博士 | 解説と審判。判定は数字どおりに下す |
| 助手（ハル） | 実験の進行と数字の発表。判定はしない |
| ショウジョウバエ研究員 | 疑う側。基準線と検証から見る |
| アバボット | 確信する側。高い数字に賭ける |

## ファイル構成

| ファイル | 内容 |
|---|---|
| `index.html` | 最初の画面 |
| `llm_evaluation.html` | 解説ダッシュボード（図がすべて入った単一ファイル） |
| `*.en.html` など | 外国語版 |
| `assets/` | 最初の画面の表紙、共有プレビュー用の画像 |
| `docs/` | 画像仕様書、表紙の指示文、知識索引の登録分、採点スクリプト |

ローカルで見るときは、HTMLファイルをブラウザで直接開けば十分です。言語の自動切り替えまで確認するには、このフォルダで `python3 -m http.server` を実行してから http://localhost:8000/ を開きます。

## レビューした論文・資料

1. Hendrycks ら (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein ら (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez ら (2024), SWE-bench
4. Chen ら (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang ら (2024), Chatbot Arena, ICML
6. Zheng ら (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White ら (2025), LiveBench, ICLR
8. Zhang ら (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh ら (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika ら (2024), HarmBench, arXiv:2402.04249
13. Merrill ら (2026), Terminal-Bench, arXiv:2601.11868

各論文の実験結果と数値の原著作権は論文の著者にあります。出典ごとにこのページで使った数値は、ダッシュボード最下部の出典表にあります。

## ライセンス

- 文章: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.ja)
- キャラクター（博士・助手ハル・ショウジョウバエ研究員・アバボット）の名前・設定・絵は著作権者のAhn Sangsunにあり、許可なく使用することはできません。

## 作成したツール

- 解説ダッシュボード: [ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- キャラクターの絵: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (キャラクターパック 1.3)
- 外国語版: [ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack) (言語パック v1.3)。外国語版はネイティブによる検収前です。

---

<a id="uz"></a>

# AI ballari nimani oʻlchaydi — tasniflash modelini baholashdan LLM reytinglarigacha

![Tungi laboratoriyada toʻrt qahramon muhrlangan imtihon qutisi atrofida yigʻilgan muqova](assets/og_llmeval.jpg)

Hamma «birinchi oʻrin»man deydi, lekin bu qaysi imtihondagi birinchi oʻrin? Tasniflash modelini baholashdan boshlab katta til modeli (LLM) imtihoni va baholash usullarigacha besh bosqichda koʻtariladigan laboratoriya tushuntirish paneli.

- Sayt: https://adminmrobo.github.io/LLM_evaluation/index.uz.html
- Panel: [llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.uz.html)
- Muallif · Ahn Sangsun (M-Robo kompaniyasi rahbari) · AI yordamida tayyorlangan · Maqola sharhi va tushuntirishi

## Til

Bu seriyani koreyscha asl nusxa va 6 ta chet tilidagi nashrda koʻrish mumkin.

- Tanlash usuli: ekranning yuqori menyusidagi 🌐 til tanlash qutisidan yoki oʻng pastdagi 🌐 bannerdan tanlanadi. Tanlangan til brauzerda eslab qolinadi.
- Avtomatik oʻtish: koreyscha sahifaga birinchi marta kirganingizda, brauzer tili qoʻllab-quvvatlanadigan til boʻlsa, shu til nashriga oʻtiladi. Tarjima nashri manzili bilan kirsangiz, oʻshandayligicha ochiladi.
- Manzil oxiriga `?lang=en` kabi qoʻshsangiz, shu tilda darrov ochiladi.
- Til nashri fayli `nom.tilkodi.html` koʻrinishida.

<!-- i18n:langtable -->
| Til | Fayl nomi | Darrov koʻrish |
|---|---|---|
| 한국어 | `index.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [Darrov koʻrish](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## Nimani oʻrganamiz

| Bosqich | Mavzu | Oʻzingiz qiladigan ish |
|---|---|---|
| ① | Bitta katak tanlash — tasniflash modelini baholash | Imtihon toʻplamini ajratish, stratify, chalkashlik matritsasi, precision·recall |
| ② | Son topish — regressiya modelini baholash | MAE va RMSE, kross-validatsiya |
| ③ | Toʻgʻri javobli uzun javob — ijro etib baholash | Bir necha marta yechtirganda ball oʻzgarishi (pass@k) |
| ④ | Toʻgʻri javobsiz javob — juft ovoz berish | Bradley-Terry bali, AI hakamning siljishi (bias) |
| ⑤ | Imtihon varaqasini himoya qilish | Ifloslanish, Wilson oraligʻi va xato chiziqlari |
| Bellashuv | Reyting balini qanday oshirish mumkin? | Meva pashshasi tadqiqotchisi bilan AbaBotning ball oshirish musobaqasi |

## Sahifada nimalar bor

- 13 ta tekshiruv testi savoli
- Bilimlar indeksi: 130 ta tushuncha, 168 ta bogʻlanish
- Amaliy toʻplam: imtihon varaqasi shabloni (CSV) va baholash skripti (Python, faqat standart kutubxona)
- Ontologiya va bibliografiya toʻplami: JSON-LD, Turtle, CSL-JSON, BibTeX, RIS

## Qahramonlar

| Ism | Vazifa |
|---|---|
| Doktor | Tushuntiradi va hakamlik qiladi. Hukmni raqamlarga qarab chiqaradi |
| Yordamchi (Haru) | Tajribani olib boradi va raqamlarni eʼlon qiladi. Hukm chiqarmaydi |
| Meva pashshasi tadqiqotchisi | Shubhalanuvchi tomon. Avval asosiy chiziq va tekshiruvga qaraydi |
| AbaBot | Ishonuvchi tomon. Yuqori raqamga tikadi |

## Fayllar tarkibi

| Fayllar | Mazmun |
|---|---|
| `index.html` | Bosh sahifa |
| `llm_evaluation.html` | Tushuntirish paneli (barcha rasmlar ichida, yagona fayl) |
| `*.en.html` va h.k. | Chet tilidagi nashrlar |
| `assets/` | Bosh sahifa muqovasi, ulashish uchun koʻrinish rasmi |
| `docs/` | Rasm spetsifikatsiyasi, muqova koʻrsatmasi, bilimlar indeksiga kiritilganlar, baholash skripti |

Lokal koʻrishda HTML faylni brauzerda toʻgʻridan-toʻgʻri ochsangiz boʻladi. Tilning avtomatik almashishini ham koʻrmoqchi boʻlsangiz, shu jildda `python3 -m http.server` ni ishga tushirib, http://localhost:8000/ ni oching.

## Sharh qilingan maqola va manbalar

1. Hendrycks va boshq. (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein va boshq. (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez va boshq. (2024), SWE-bench
4. Chen va boshq. (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang va boshq. (2024), Chatbot Arena, ICML
6. Zheng va boshq. (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White va boshq. (2025), LiveBench, ICLR
8. Zhang va boshq. (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh va boshq. (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika va boshq. (2024), HarmBench, arXiv:2402.04249
13. Merrill va boshq. (2026), Terminal-Bench, arXiv:2601.11868

Har bir maqoladagi tajriba natijalari va raqamlarning asl muallifligi maqola mualliflariga tegishli. Sahifada ishlatilgan raqamlar manbalar boʻyicha panelning eng pastidagi manbalar jadvalida.

## Litsenziya

- Matn: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en)
- Qahramonlar (Doktor · yordamchi Haru · Meva pashshasi tadqiqotchisi · AbaBot)ning ismi, xarakteri va rasmlari muallif Ahn Sangsunga tegishli boʻlib, ruxsatsiz ishlatib boʻlmaydi.

## Yaratilgan vositalar

- Tushuntirish paneli: [ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- Qahramon rasmlari: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (qahramonlar toʻplami 1.3)
- Chet tilidagi nashrlar: [ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack) (til toʻplami v1.3). Chet tilidagi nashrlar ona tilida soʻzlashuvchilar tekshiruvidan oʻtmagan.

---

<a id="ru"></a>

# Что измеряет оценка ИИ — от оценки классификаторов до рейтингов LLM

![Обложка: ночью в лаборатории четверо персонажей собрались вокруг ящика с запечатанными экзаменационными листами](assets/og_llmeval.jpg)

Все говорят, что они первые, но первые в каком экзамене? Это панель-пояснение лаборатории: начиная с оценки классификаторов, вы поднимаетесь по пяти ступеням к экзаменационным листам и способам оценки больших языковых моделей (LLM).

- Сайт: https://adminmrobo.github.io/LLM_evaluation/index.ru.html
- Панель: [llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.ru.html)
- Автор: Ahn Sangsun (генеральный директор M-Robo) · создано с помощью ИИ · обзор и пояснение статьи

## Язык

Эту серию можно смотреть в корейском оригинале и в 6 версиях на других языках.

- Как выбрать: в выпадающем списке 🌐 в верхнем меню экрана или в баннере 🌐 справа внизу. Выбранный язык запоминается в браузере.
- Автопереключение: при первом заходе на корейскую страницу, если язык браузера поддерживается, вас перенаправляют на эту языковую версию. При заходе по адресу переводной версии она открывается как есть.
- Если добавить в конец адреса, например, `?lang=en`, страница сразу откроется на этом языке.
- Файл языковой версии имеет вид `имя.код_языка.html`.

<!-- i18n:langtable -->
| Язык | Имя файла | Смотреть сразу |
|---|---|---|
| 한국어 | `index.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [Смотреть сразу](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## Чему учимся

| Ступень | Тема | Что делаем сами |
|---|---|---|
| ① | Выбор одного варианта — оценка классификатора | Деление экзаменационной выборки, stratify, матрица ошибок, прецизионность и полнота |
| ② | Угадывание числа — оценка регрессионной модели | MAE и RMSE, кросс-валидация |
| ③ | Длинный ответ с верным решением — оценка запуском | Изменение балла при нескольких попытках (pass@k) |
| ④ | Ответ без верного решения — парное голосование | Балл Bradley-Terry, смещение ИИ-судьи |
| ⑤ | Охрана экзаменационных листов | Загрязнение, интервал Wilson и планки погрешности |
| Поединок | Как поднять балл в рейтинге? | Соревнование Исследователя-дрозофилы и АбаБота по поднятию балла |

## Что внутри страницы

- 13 вопросов проверочного теста
- Указатель знаний: 130 понятий, 168 связей
- Практический набор: бланк экзамена (CSV) и скрипт оценки (Python, только стандартная библиотека)
- Пакет онтологии и библиографии: JSON-LD, Turtle, CSL-JSON, BibTeX, RIS

## Действующие лица

| Имя | Роль |
|---|---|
| Доктор | Объяснения и судейство. Вердикт выносится по цифрам |
| ассистент (Хару) | Проводит эксперименты и объявляет цифры. Вердиктов не выносит |
| Исследователь-дрозофила | Скептик. Сначала смотрит на базовый уровень и проверку |
| АбаБот | Уверенная сторона. Ставит на большие цифры |

## Состав файлов

| Файлы | Содержание |
|---|---|
| `index.html` | Главная страница |
| `llm_evaluation.html` | Панель-пояснение (один файл со всеми рисунками) |
| `*.en.html` и т. д. | Версии на других языках |
| `assets/` | Обложка главной страницы, картинка для предпросмотра при публикации |
| `docs/` | Спецификация изображений, указания к обложке, записи указателя знаний, скрипт оценки |

Для локального просмотра достаточно открыть HTML-файл в браузере. Чтобы увидеть и автоматическое переключение языка, запустите в этой папке `python3 -m http.server`, затем откройте http://localhost:8000/ .

## Рассмотренные статьи и материалы

1. Hendrycks и др. (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein и др. (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez и др. (2024), SWE-bench
4. Chen и др. (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang и др. (2024), Chatbot Arena, ICML
6. Zheng и др. (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White и др. (2025), LiveBench, ICLR
8. Zhang и др. (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh и др. (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika и др. (2024), HarmBench, arXiv:2402.04249
13. Merrill и др. (2026), Terminal-Bench, arXiv:2601.11868

Авторские права на результаты экспериментов и цифры принадлежат авторам соответствующих статей. Цифры, использованные на странице, приведены по источникам в таблице источников в самом низу панели.

## Лицензия

- Текст: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
- Имена, образы и рисунки персонажей (Доктор · ассистент Хару · Исследователь-дрозофила · АбаБот) принадлежат правообладателю Ahn Sangsun; использование без разрешения запрещено.

## Использованные инструменты

- Панель-пояснение: [ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- Рисунки персонажей: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (пакет персонажей 1.3)
- Версии на других языках: [ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack) (языковой пакет v1.3). Носители языка эти версии ещё не проверяли.

---

<a id="vi"></a>

# Điểm AI đo cái gì — từ chấm điểm mô hình phân loại đến bảng xếp hạng LLM

![Bìa truyện: trong phòng thí nghiệm ban đêm, bốn nhân vật tụ họp quanh chiếc hộp đề thi đã niêm phong](assets/og_llmeval.jpg)

Ai cũng bảo mình hạng nhất, nhưng hạng nhất ở kỳ thi nào? Đây là bảng giải thích của phòng thí nghiệm, đi từ chấm điểm mô hình phân loại lên đến đề thi và cách chấm của mô hình ngôn ngữ lớn (LLM) qua năm ô.

- Trang web: https://adminmrobo.github.io/LLM_evaluation/index.vi.html
- Bảng điều khiển: [llm_evaluation.html](https://adminmrobo.github.io/LLM_evaluation/llm_evaluation.vi.html)
- Viết bởi Ahn Sangsun (Giám đốc điều hành M-Robo) · Sản xuất với sự hỗ trợ của AI · Đánh giá bài báo · Giải thích

## Ngôn ngữ

Bộ này có thể xem bằng bản gốc tiếng Hàn và 6 bản ngoại ngữ.

- Cách chọn: chọn ở hộp chọn ngôn ngữ 🌐 trên menu cao nhất của màn hình hoặc ở biển 🌐 góc dưới bên phải. Ngôn ngữ đã chọn được trình duyệt ghi nhớ.
- Tự động chuyển: khi lần đầu vào trang tiếng Hàn, nếu ngôn ngữ trình duyệt là ngôn ngữ được hỗ trợ thì sẽ chuyển sang bản ngôn ngữ đó. Nếu vào bằng địa chỉ bản dịch thì mở nguyên như vậy.
- Thêm `?lang=en` vào cuối địa chỉ thì mở ngay bằng ngôn ngữ đó.
- Tệp bản ngôn ngữ có dạng `tên.mã-ngôn-ngữ.html`.

<!-- i18n:langtable -->
| Ngôn ngữ | Tên tệp | Xem ngay |
|---|---|---|
| 한국어 | `index.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.html) |
| English | `index.en.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.en.html) |
| 中文 | `index.zh.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.zh.html) |
| 日本語 | `index.ja.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.ja.html) |
| Oʻzbekcha | `index.uz.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.uz.html) |
| Русский | `index.ru.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.ru.html) |
| Tiếng Việt | `index.vi.html` | [Xem ngay](https://adminmrobo.github.io/LLM_evaluation/index.vi.html) |
<!-- /i18n:langtable -->

## Học được gì

| Ô | Chủ đề | Việc tự làm thử |
|---|---|---|
| ① | Chọn một trong các ô — chấm mô hình phân loại | Chia tập thi, stratify, ma trận nhầm lẫn, precision·recall |
| ② | Đoán con số — chấm mô hình hồi quy | MAE và RMSE, kiểm định chéo |
| ③ | Câu trả lời dài có đáp án — chấm bằng chạy mã | Thay đổi điểm khi cho giải nhiều lần (pass@k) |
| ④ | Câu trả lời không có đáp án — bỏ phiếu cặp | Điểm Bradley-Terry, độ lệch của giám khảo AI |
| ⑤ | Giữ gìn đề thi | Nhiễm bẩn, khoảng Wilson và thanh sai số |
| Đối đầu | Nâng điểm bảng xếp hạng thế nào? | Cuộc thi nâng điểm giữa Nhà nghiên cứu Ruồi giấm và AbaBot |

## Trong trang có gì

- 13 câu hỏi quiz kiểm tra
- Chỉ mục tri thức: 130 khái niệm, 168 mối quan hệ
- Bộ thực hành: mẫu bài thi (CSV) và script chấm điểm (Python, chỉ dùng thư viện chuẩn)
- Gói bản thể học · thư mục: JSON-LD, Turtle, CSL-JSON, BibTeX, RIS

## Nhân vật

| Tên | Vai trò |
|---|---|
| Tiến sĩ | Giải thích và làm trọng tài. Phán quyết theo đúng con số |
| Trợ lý (Haru) | Tiến hành thí nghiệm và công bố con số. Không đưa ra phán quyết |
| Nhà nghiên cứu Ruồi giấm | Bên hoài nghi. Xem đường cơ sở và kiểm định trước |
| AbaBot | Bên tin chắc. Dồn hết vào con số cao |

## Cấu trúc tệp

| Tệp | Nội dung |
|---|---|
| `index.html` | Màn hình đầu |
| `llm_evaluation.html` | Bảng giải thích (một tệp duy nhất chứa đủ hình ảnh) |
| `*.en.html` v.v. | Bản ngoại ngữ |
| `assets/` | Ảnh bìa màn hình đầu, ảnh xem trước khi chia sẻ |
| `docs/` | Bảng mô tả ảnh, lời dặn vẽ bìa, mục đã đăng ký của chỉ mục tri thức, script chấm điểm |

Khi xem trên máy cục bộ, chỉ cần mở tệp HTML bằng trình duyệt. Để xem cả tính năng tự chuyển ngôn ngữ, hãy chạy `python3 -m http.server` trong thư mục này rồi mở http://localhost:8000/ .

## Bài báo · tài liệu đã đánh giá

1. Hendrycks và cộng sự (2021), Measuring Massive Multitask Language Understanding (MMLU), ICLR
2. Rein và cộng sự (2023), GPQA, arXiv:2311.12022
3. OpenAI (2024), Introducing SWE-bench Verified · Jimenez và cộng sự (2024), SWE-bench
4. Chen và cộng sự (2021), Evaluating Large Language Models Trained on Code (HumanEval, pass@k), arXiv:2107.03374
5. Chiang và cộng sự (2024), Chatbot Arena, ICML
6. Zheng và cộng sự (2023), Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, NeurIPS
7. White và cộng sự (2025), LiveBench, ICLR
8. Zhang và cộng sự (2024), A Careful Examination of LLM Performance on Grade School Arithmetic (GSM1k), NeurIPS
9. Singh và cộng sự (2025), The Leaderboard Illusion, arXiv:2504.20879
10. Miller (2024), Adding Error Bars to Evals, arXiv:2411.00640
11. OpenAI (2024), Measuring short-form factuality in large language models (SimpleQA), arXiv:2411.04368
12. Mazeika và cộng sự (2024), HarmBench, arXiv:2402.04249
13. Merrill và cộng sự (2026), Terminal-Bench, arXiv:2601.11868

Quyền tác giả gốc của kết quả thí nghiệm và số liệu trong mỗi bài báo thuộc về tác giả bài báo. Các số liệu dùng trong trang, theo từng nguồn, nằm ở bảng nguồn cuối bảng điều khiển.

## Giấy phép

- Bài viết: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.vi)
- Tên, thiết lập và hình vẽ của các nhân vật (Tiến sĩ · Trợ lý Haru · Nhà nghiên cứu Ruồi giấm · AbaBot) thuộc bản quyền của tác giả Ahn Sangsun và không được sử dụng khi chưa được phép.

## Công cụ đã dùng

- Bảng giải thích: [ahnboat_lab_explainer](https://github.com/adminmrobo/ahnboat_lab_explainer) (ai-lab-explainer)
- Hình nhân vật: [fruitfly-lab-expressions](https://github.com/adminmrobo/fruitfly-lab-expressions) (gói nhân vật 1.3)
- Bản ngoại ngữ: [ahnboat_lab_langpack](https://github.com/adminmrobo/ahnboat_lab_langpack) (gói ngôn ngữ v1.3). Bản ngoại ngữ chưa được người bản ngữ kiểm duyệt.
