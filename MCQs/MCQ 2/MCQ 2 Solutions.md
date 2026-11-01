# MCQ 2 — Logistic Regression: Worked Solutions

**Main source:** [handout-02-logistic-regression.pdf](<../../Lecture Slides/handout-02-logistic-regression.pdf>)

> Page references are **PDF page numbers**. For handout-02 they match the printed slide numbers.

## Answer summary

| Q | Answer |
|---|--------|
| 1 | B, D |
| 2 | D ($p\approx0.77$) |
| 3 | D |
| 4 | C |
| 5 | D |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | B |
| 10 | A |
| 11 | A |
| 12 | B |

---

## Question 1

What is Logistic Regression used for? (select all)

A. regression · B. classification · C. clustering · D. supervised learning · E. unsupervised learning

**Lecture material:**
- handout-02 p. 2: "Despite its name, logistic regression is a model for classification, not regression."
- pp. 22–24: the model is trained on labelled pairs $(\mathbf{x}_i, y_i)$.
- [handout-00](<../../Lecture Slides/handout-00-intro.pdf>) p. 7: supervised learning means learning from a labelled dataset $(\mathbf{x}_i,y_i)$.
- [handout-10](<../../Lecture Slides/handout-10-generative-models.pdf>) p. 2: logistic regression is given as an example of a discriminative, supervised model.

**Working:**
- **B:** It predicts a binary class (p. 2). ✅
- **D:** Training needs the labels $y_i$ in the likelihood (p. 23), so it is supervised. ✅
- **A:** Despite the name, it does not predict a continuous output (p. 2). ❌
- **C and E:** Clustering is an unsupervised task with no labels, which logistic regression cannot do. ❌

**Final answer: B, D**

**Check:** The cross-entropy loss on p. 24 contains $y_i$. Without labels you could not compute it.

---

## Question 2

Given weights $w_0=0.1$, $w_1=1$, $w_2=2$, what is the probability $p$ that an observation with $x_1=0.3$, $x_2=0.4$ belongs to class 1?

A. $[0,0.2)$ · B. $[0.2,0.4)$ · C. $[0.4,0.6)$ · D. $[0.6,0.8)$ · E. $[0.1,1]$ (as written)

**Lecture material:** p. 19: $p(y=1\mid\mathbf{x},\mathbf{w}) = f(\mathbf{x}^\top\mathbf{w}) = \dfrac{1}{1+e^{-\mathbf{x}^\top\mathbf{w}}}$, with the bias absorbed by using the feature $x_0 = 1$ ([handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) p. 14).

**Working:**
1. Logit: $\mathbf{x}^\top\mathbf{w} = w_0 + w_1x_1 + w_2x_2 = 0.1 + 1(0.3) + 2(0.4) = 0.1 + 0.3 + 0.8 = 1.2$
2. Sigmoid: $p = \dfrac{1}{1+e^{-1.2}} = \dfrac{1}{1+0.3012} = \dfrac{1}{1.3012} \approx 0.7685$
3. $0.6 \le 0.7685 < 0.8$, which is option D.

**Final answer: D ($p \approx 0.77$)**

> ⚠️ Option E as pasted reads $0.1 \le p \le 1$, which technically also contains 0.77. It is almost certainly a typo for $0.8 \le p \le 1$, the natural last bin. D is the intended answer.

**Check:** The logit is positive, so $p > 0.5$, as expected. $f(1)\approx0.73$ and $f(1.5)\approx0.82$, so $f(1.2)\approx0.77$ sits between them. ✓

---

## Question 3

What is the loss function of Logistic Regression?

A. Sigmoid function · B. Logistic function · C. Logit function · D. none of these

**Lecture material:** p. 24: "This loss function that we need to minimise is called the **cross-entropy**." p. 18: the sigmoid (also called the logistic function) is the c.d.f. that maps the logit to a probability. p. 14: the risk score $\mathbf{x}^\top\mathbf{w}$ is called the logit.

**Working:**
- **A and B:** These are two names for the same function, $f(t) = 1/(1+e^{-t})$, which is the model's output, not its loss. ❌
- **C:** The logit is the linear score $\mathbf{x}^\top\mathbf{w}$, not a loss. ❌
- **D:** The loss is the cross-entropy, $E(\mathbf{w}) = \sum_i -y_i\ln h_\mathbf{w}(\mathbf{x}_i) - (1-y_i)\ln(1-h_\mathbf{w}(\mathbf{x}_i))$, which is not listed. ✅

**Final answer: D**

**Check:** The takeaways (p. 39) say finding the maximum-likelihood parameters "is equivalent to minimising the cross entropy loss function."

---

## Question 4

What is the range of possible values for the logit?

A. $[-1,1]$ · B. $[0,1]$ · C. $(-\infty,+\infty)$ · D. $[0,+\infty)$

**Lecture material:** pp. 12 and 14: the logit is the risk score $\mathbf{x}^\top\mathbf{w}$. It can be $\gg0$, $\ll0$ or $\approx0$.

**Working:** $\mathbf{x}^\top\mathbf{w}$ is an unconstrained linear combination of real features and weights, so it can take any real value. Only after the sigmoid is it squashed into $(0,1)$.

**Final answer: C**

**Check:** The plot of $f(t)$ on p. 18 uses $t\in(-\infty,\infty)$ as its input axis, and the logit is that input.

---

## Question 5

What do large values of the negative log-likelihood indicate? (select all)

A. High likelihood of class 1 · B. High likelihood of class 0 · C. The model fits the data well · D. The model is a poor fit of the data

**Lecture material:** pp. 23–24: $E(\mathbf{w}) = -\ln p(\mathbf{y}\mid\mathbf{X},\mathbf{w})$. We *maximise* the likelihood by *minimising* the NLL.

**Working:**
1. $-\ln(\cdot)$ is decreasing, so a large NLL means a small likelihood $p(\mathbf{y}\mid\mathbf{X},\mathbf{w})$.
2. A small likelihood means the model gives low probability to the labels that were actually observed, so the fit is poor. **D** ✅ and C ❌.
3. **A and B:** The NLL is computed for the observed labels of both classes together. A large value does not say which class is likely. ❌

**Final answer: D**

**Check:** A perfect model has $p(\mathbf{y}\mid\mathbf{X})=1$, so NLL $=0$. As predictions get worse, $p\to0$ and NLL $\to\infty$.

---

## Question 6

What does Logistic Regression assume? (select all)

A. Linear relationship between the features and the outcome · B. Linear relationship between the features and the **logit** · C. Linear relationship between features · D. Linear relationship between observations

**Lecture material:** pp. 11–14: $y = [\mathbf{x}^\top\mathbf{w} + \epsilon > 0]$, and the risk score $\mathbf{x}^\top\mathbf{w}$ "is called the logit". p. 19: $p(y=1\mid\mathbf{x}) = f(\mathbf{x}^\top\mathbf{w})$, which is non-linear in $\mathbf{x}$.

**Working:**
- **B:** The logit is assumed to be a linear function of the features. ✅
- **A:** The outcome probability is the sigmoid of the logit, so it is non-linear in the features. ❌
- **C and D:** The model makes no assumption that features (or observations) are linearly related to each other. The likelihood (p. 23) only assumes the observations are independent. ❌

**Final answer: B**

**Check:** In the 2-feature example (p. 32), the probability contours (5%, 50%, 95%) are straight lines. These are lines of constant logit, which shows the logit is linear in $\mathbf{x}$.

---

## Question 7

The logistic model is estimated by way of?

A. Least Squares · B. Maximum Likelihood Estimation · C. Gaussian Distribution · D. Logistic Distribution

**Lecture material:** p. 22: "To estimate the weights $\mathbf{w}$, we will again use the concept of Maximum Likelihood." p. 25: LS on $h_\mathbf{w}$ "would not maximise the likelihood" and is harder to optimise.

**Working:** The weights maximise $p(\mathbf{y}\mid\mathbf{X},\mathbf{w})$, which is the same as minimising the cross-entropy, and this is solved by gradient descent (pp. 26–30). The logistic distribution (D) is the assumed distribution of the error $\epsilon$ (p. 14), not the estimation method. The Gaussian distribution (C) is used in probit regression (p. 15).

**Final answer: B**

**Check:** Takeaways, p. 39. ✓

---

## Question 8

What is the probability of belonging to class 1 for a logit of 0?

**Lecture material:** p. 18: $f(t) = 1/(1+e^{-t})$. p. 12: $\mathbf{x}^\top\mathbf{w}\approx0$ means "undecided".

**Working:** $f(0) = \dfrac{1}{1+e^{0}} = \dfrac{1}{2} = 0.5$

**Final answer: B (0.5)**

**Check:** On p. 32, the 50% line is the decision boundary $\mathbf{x}^\top\mathbf{w}=0$.

---

## Question 9

Which variant of Logistic Regression is recommended for a categorical dependent variable with more than two values?

A. Binary LR · B. Multinomial LR · C. Monomial LR · D. Softmax

**Lecture material:** p. 34: "In these cases, we need to use **multinomial logistic regression**, which is an extension of logistic regression to more than 2 classes." p. 35: softmax is the *function* used inside multinomial LR.

**Working:** Binary LR (A) only handles two classes, and "Monomial LR" (C) is not a real method. Softmax (D) is a component that turns $K$ logits into $K$ probabilities, not a variant of logistic regression.

**Final answer: B**

**Check:** Takeaways, p. 39: "The extension of Logistic Regression to more than 2 classes is called the Multinomial Logistic Regression."

---

## Question 10

Which are true?

A. In Linear Regression errors are assumed normal, but not in Logistic Regression. · B. The reverse. · C. Normal in both. · D. Normal in neither.

**Lecture material:**
- [handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) p. 50: linear regression assumes $\epsilon \sim \mathcal{N}(0,\sigma^2)$.
- handout-02 p. 14: "In logistic regression, the error $\epsilon$ is assumed to follow a **logistic** distribution."
- p. 15: a normally distributed error gives **probit** regression instead.

**Working:** Linear regression assumes normal errors and logistic regression assumes logistic errors, so A is true and B, C and D are false.

**Final answer: A**

**Check:** If logistic regression did assume normal errors, it would become probit regression (p. 15), which is a different model.

---

## Question 11

Consider the 2-class scatter plot (red cross: class 1, blue circle: class 0). What is the expected logit for the new observation (circled green cross)?

![Q11 figure](<q11 image.png>)

A. high · B. low · C. near zero · D. cannot say

**Lecture material:** p. 12: $\mathbf{x}^\top\mathbf{w}\gg0 \Rightarrow y=1$, $\mathbf{x}^\top\mathbf{w}\ll0 \Rightarrow y=0$, and $\approx0$ means undecided. p. 32: the contours for 5%, 50% and 95% are parallel lines, and the logit grows linearly with distance from the 50% line.

**Working:**
1. The dashed line labelled $p=0.5$ is where the logit is 0.
2. The green point lies on the class-1 (red cross) side, well to the bottom-right and far from that line.
3. The logit is linear in $\mathbf{x}$, so it grows in proportion to the distance from the $p=0.5$ line. A point far into the class-1 side therefore has a large positive logit.

**Final answer: A (high)**

**Check:** It is surrounded by red crosses and far from any blue circles, so it should have $p(y=1)\approx1$, which means a large positive logit.

---

## Question 12

A general linear model for binary classification has 100% training accuracy (every output is correctly predicted). What is the maximum value $h$ that the average cross-entropy on the training set can take?

A. $[0,0.5)$ · B. $[0.5,1)$ · C. $[1,2)$ · D. $[2,10)$ · E. $\ge10$

**Lecture material:** p. 24: average cross-entropy $E = \frac{1}{n}\sum_i -y_i\ln h_\mathbf{w}(\mathbf{x}_i) - (1-y_i)\ln(1-h_\mathbf{w}(\mathbf{x}_i))$. pp. 8 and 12: the predicted class is 1 when $p>0.5$ (logit $>0$).

**Working:**
1. **Per-sample loss:** For a sample with $y_i=1$ the loss is $-\ln h_i$. For $y_i=0$ it is $-\ln(1-h_i)$.
2. **What 100% accuracy means:** Every sample is on the correct side of the threshold. So $h_i > 0.5$ when $y_i=1$, and $1-h_i > 0.5$ when $y_i=0$. Either way, the probability given to the true class is above 0.5.
3. **Worst case per sample:** Each loss is $-\ln(q_i)$ with $q_i > 0.5$, so it is less than $-\ln 0.5 = \ln 2 \approx 0.693$. The worst case is when every point sits just on the correct side of the boundary.
4. **Average:** The average of values below 0.693 is also below 0.693, so $0 \le h < \ln2 \approx 0.693$.
5. The largest possible value, about 0.693, lies in $[0.5, 1)$.

**Final answer: B**

**Check:** Natural log is used, as in the lecture's $\ln$. In base 2 the bound would be exactly 1, so the answer would still be B (approached but never reached).
