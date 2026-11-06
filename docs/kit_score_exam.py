# 내 업무 시험지 채점 스크립트: 파이썬 기본 기능만 사용 (설치할 것 없음)
# 사용법: python score_exam.py my_exam.csv
import csv, sys
from math import comb

path = sys.argv[1] if len(sys.argv) > 1 else "my_exam.csv"
with open(path, encoding="utf-8-sig") as f:
    rows = [r for r in csv.DictReader(f) if r["split"] == "test"]  # 봉인 시험용만 채점

models = [c for c in rows[0] if c.startswith("model_")]
y = [int(r["label"]) for r in rows]
for m in models:
    p = [int(r[m]) for r in rows]
    tp = sum(a == 1 and b == 1 for a, b in zip(y, p))
    fp = sum(a == 0 and b == 1 for a, b in zip(y, p))
    fn = sum(a == 1 and b == 0 for a, b in zip(y, p))
    prec = tp / (tp + fp) if tp + fp else 0
    rec = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0
    print(f"{m}: 정밀도 {prec:.3f}  재현율 {rec:.3f}  F1 {f1:.3f}  (문항 {len(y)}개)")

# 같은 문항에서 두 모델 비교: 정확(exact) McNemar 검정
if len(models) >= 2:
    a = [int(r[models[0]]) == t for r, t in zip(rows, y)]
    b = [int(r[models[1]]) == t for r, t in zip(rows, y)]
    only_a = sum(x and not z for x, z in zip(a, b))
    only_b = sum(z and not x for x, z in zip(a, b))
    n, k = only_a + only_b, min(only_a, only_b)
    pval = min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n) if n else 1.0
    print(f"{models[0]}만 맞힘 {only_a}개, {models[1]}만 맞힘 {only_b}개, McNemar p = {pval:.3f}")
    print("p가 0.05보다 크면 두 모델의 차이를 우연과 구분하기 어렵습니다.")
