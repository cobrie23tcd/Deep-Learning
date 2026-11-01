# MCQ 4 — Evaluating Classifier Performance: Worked Solutions

**Main source:** [handout-04-evaluating-classifier-performance.pdf](<../../Lecture Slides/handout-04-evaluating-classifier-performance.pdf>)

> Page references are **PDF page numbers**. For handout-04 they match the printed slide numbers.

## Answer summary

| Q | Answer |
|---|--------|
| 1 | C (68.00%) |
| 2 | A (37.04%) |
| 3 | D (90.32%) |
| 4 | B (74.00%; C is an identical duplicate) |
| 5 | D |
| 6 | B (False) |
| 7 | C (3) |
| 8 | D (80%) |

## Formulas used (handout-04 pp. 8, 11–13)

The confusion matrix layout is: rows = predicted, columns = actual (p. 8).

| | actual 0 | actual 1 |
|---|---|---|
| **predicted 0** | TN | FN |
| **predicted 1** | FP | TP |

- Recall (TPR) $= \dfrac{TP}{TP+FN}$, p. 11
- Precision $= \dfrac{TP}{TP+FP}$, p. 11
- False positive rate $= \dfrac{FP}{FP+TN}$, p. 12
- Accuracy $= \dfrac{TP+TN}{TP+TN+FP+FN}$, p. 13
- $F_1 = \dfrac{2\cdot\text{recall}\cdot\text{precision}}{\text{precision}+\text{recall}} = \dfrac{2TP}{2TP+FP+FN}$, p. 13

---

## Question 1

![Q1 confusion matrix](<q1 image.png>)

TN = 52, FN = 30, FP = 2, TP = 16. What is the **Accuracy**?

A. 3.70% · B. 11.11% · C. 68.00% · D. 88.89%

**Working:**
- Total $= 52+30+2+16 = 100$
- Accuracy $= \dfrac{TP+TN}{\text{total}} = \dfrac{16+52}{100} = \dfrac{68}{100} = 68.00\%$

**Final answer: C (68.00%)**

**Check:** The other options are other metrics computed from the same matrix:
- FPR $= 2/54 = 3.70\%$
- $1-\text{precision} = 2/18 = 11.11\%$
- Precision $= 16/18 = 88.89\%$

---

## Question 2

![Q2 confusion matrix](<q2 image.png>)

TN = 34, FN = 9, FP = 20, TP = 37. What is the **False Positive Rate**?

A. 37.04% · B. 64.91% · C. 71.00% · D. 79.07%

**Working:** FPR $= \dfrac{FP}{FP+TN} = \dfrac{20}{20+34} = \dfrac{20}{54} = 0.37037 = 37.04\%$

The denominator is the number of **actual negatives**, which is the "actual: 0" column (p. 12).

**Final answer: A (37.04%)**

**Check:** The other options are:
- Precision $= 37/57 = 64.91\%$
- Accuracy $= 71/100 = 71.00\%$
- $TN/(TN+FN) = 34/43 = 79.07\%$

So the distractors come from using the wrong row or column.

---

## Question 3

![Q3 confusion matrix](<q3 image.png>)

TN = 15, FN = 23, FP = 6, TP = 56. What is the **Precision**?

A. 28.57% · B. 71.00% · C. 79.43% · D. 90.32%

**Working:** Precision $= \dfrac{TP}{TP+FP} = \dfrac{56}{56+6} = \dfrac{56}{62} = 0.90323 = 90.32\%$

The denominator is everything that was **predicted** positive, which is the "predicted: 1" row (p. 11).

**Final answer: D (90.32%)**

**Check:** The other options are:
- FPR $= 6/21 = 28.57\%$
- Accuracy $= 71/100 = 71.00\%$
- $F_1 = 112/141 = 79.43\%$

---

## Question 4

![Q4 confusion matrix](<q4 image.png>)

TN = 37, FN = 12, FP = 14, TP = 37. What is the **F1 score**?

A. 27.45% · B. 74.00% · C. 74.00% · D. 75.51%

**Working:**
- $F_1 = \dfrac{2TP}{2TP+FP+FN} = \dfrac{74}{74+14+12} = \dfrac{74}{100} = 74.00\%$
- Using the harmonic mean instead: precision $= 37/51 = 0.7255$ and recall $= 37/49 = 0.7551$, so $F_1 = \dfrac{2(0.7255)(0.7551)}{0.7255+0.7551} = \dfrac{1.0957}{1.4806} = 0.7400$ ✓

**Final answer: B (74.00%)**

> Options B and C are both "74.00%" in the pasted quiz. This is probably a duplicate in the quiz itself, possibly a mistake where one was meant to be the accuracy, which is also $(37+37)/100 = 74\%$. Pick the first one, B, unless the quiz shows something different.

**Check:** The other options are $FP/(FP+TP) = 14/51 = 27.45\%$ and recall $= 75.51\%$. The F1 score must lie between precision (72.55%) and recall (75.51%), and 74.00% does. ✓

---

## Question 5

A clinical lab reports 99% accuracy on its latest screening test. What can we say about the False Positive Rate?

A. FPR = 1% · B. FPR < 1% · C. FPR > 1% · D. not enough information

**Lecture material:**
- p. 14: "you will always need at least two metrics to really capture the performance of a classifier. Performing well on a single metric can be meaningless."
- pp. 15–17: worked example where a classifier that always outputs 0 has 85% accuracy and 0% recall.

**Working:**
1. Accuracy $= 99\%$ only tells us that $\dfrac{FP+FN}{P+N} = 1\%$.
2. FPR $= \dfrac{FP}{N}$. It depends on how the 1% of errors split between FP and FN, and on how many negatives $N$ there are.
3. Two examples with 10,000 tests show the range:
   - All errors are FN: then FP = 0, so FPR = 0%.
   - $N = 200$ and all 100 errors are FP: then FPR $= 100/200 = 50\%$.
4. Any of A, B or C is possible, so we cannot tell.

**Final answer: D (not enough information)**

**Check:** This is the lecture's main point on p. 17: "you need two metrics."

---

## Question 6

Consider the ROC curve below. Is Method B more performant than Method A?

![Q6 ROC curve](<q 6 image.png>)

A. True · B. False

**Lecture material:**
- p. 18: the ROC curve plots TPR against FPR as the threshold $T$ varies.
- p. 20: a perfect classifier is at TPR = 100% and FPR = 0% (top-left corner).
- p. 23: AUC is the area under the ROC curve.

**Working:**
1. At every FPR, Method A's curve (solid blue) is **on or above** Method B's (dashed red). For example:
   - At FPR = 0.1: A ≈ 0.79, B ≈ 0.62.
   - At FPR = 0.2: A ≈ 0.94, B ≈ 0.84.
2. So for any acceptable false-positive rate, A detects more true positives. A's curve is also closer to the ideal top-left corner, and it has the larger AUC.
3. Method B is therefore **not** more performant than A.

**Final answer: B (False)**

**Check:** The curves never cross, so there is no threshold where B does better. The comparison does not depend on which operating point you choose.

---

## Question 7

When training and comparing ML algorithms, how many types of datasets should you consider?

A. 1 · B. 2 · C. 3 · D. more than 3

**Lecture material:** p. 34: "You usually need: a **Training** set …, a **Dev or Validation** set …, a **Test** set." p. 35 explains why: tuning on the test set would overfit it.

**Working:** You need three sets:
- **Training set:** to fit the weights.
- **Validation (dev) set:** to tune hyper-parameters and choose models.
- **Test set:** for an unbiased final estimate of performance.

**Final answer: C (3)**

**Check:** p. 35 shows why the validation set must be separate from the test set. Otherwise you would end up tuning to the test data, and the test result would no longer be a fair measure.

---

## Question 8

A binary classifier gets 90% accuracy. The test set is balanced (50/50 positives/negatives). What is the worst possible Recall?

A. not enough information · B. 40% · C. 50% · D. 80% · E. 100%

**Lecture material:** p. 11 (recall $= TP/(TP+FN)$); p. 13 (accuracy).

**Working:**
1. Take 100 test samples, so $P = 50$ and $N = 50$. 90% accuracy means 10 errors: $FP + FN = 10$.
2. Recall $= \dfrac{TP}{P} = \dfrac{50-FN}{50}$. This is lowest when $FN$ is as large as possible, i.e. when **all** 10 errors are false negatives.
3. Then $FN = 10$, $TP = 40$, and recall $= 40/50 = 80\%$.

**Final answer: D (80%)**

**Check:** With $FN = 10$, $FP = 0$ we get $TN = 50$, so accuracy $= (40+50)/100 = 90\%$ ✓. Recall cannot go lower, because more than 10 FNs would push accuracy below 90%. The result does not depend on the 100-sample choice: in general recall $\ge 1 - 0.1\cdot(P+N)/P = 1 - 0.2 = 80\%$.
