# MCQ 1 — Linear Regression / Least Squares: Worked Solutions

**Main source:** [handout-01-linear-regression.pdf](<../../Lecture Slides/handout-01-linear-regression.pdf>)

> Page references are **PDF page numbers**, as shown in a PDF viewer. The slide number printed in the corner can be different because of animation builds. For example, PDF p. 45 is printed slide 38.

## Answer summary

| Q | Answer |
|---|--------|
| 1 | A |
| 2 | D ($1\times1$) |
| 3 | A ($5\times5$) |
| 4 | A |
| 5 | A, C |
| 6 | A, B |
| 7 | D |
| 8 | F |
| 9 | B |
| 10 | A, C |
| 11 | C |
| 12 | F |
| 13 | C |

---

## Question 1

If vectors $\mathbf{w}$ and $\mathbf{x}$ are of dimensions $3\times1$, which statements are correct? (mark all)

- A. $\mathbf{w}^\top\mathbf{x} = \mathbf{x}^\top\mathbf{w}$
- B. $\mathbf{w}\mathbf{x}^\top = \mathbf{x}\mathbf{w}^\top$
- C. size of $\mathbf{w}^\top\mathbf{x}$ is $3\times3$

(The stray word "Selected" in the raw question was copied from the quiz page and has been ignored.)

**Lecture material:** Vector/matrix notation and $y_i = \mathbf{x}_i^\top\mathbf{w}$ as a scalar product (pp. 12, 14).

**Working:**
- **A:** $(1\times3)(3\times1) = 1\times1$, so $\mathbf{w}^\top\mathbf{x} = \sum_i w_i x_i$ is a scalar. A scalar is its own transpose, so $\mathbf{w}^\top\mathbf{x} = (\mathbf{w}^\top\mathbf{x})^\top = \mathbf{x}^\top\mathbf{w}$. ✅
- **B:** $\mathbf{w}\mathbf{x}^\top$ is $(3\times1)(1\times3) = 3\times3$ with entries $w_i x_j$. $\mathbf{x}\mathbf{w}^\top$ has entries $x_i w_j$, so it is the transpose of $\mathbf{w}\mathbf{x}^\top$. The two are only equal when that matrix is symmetric, which is not true in general. ❌
- **C:** It is $1\times1$, not $3\times3$. ❌

**Final answer: A**

**Check:** Take $\mathbf{w}=(1,0,0)^\top$ and $\mathbf{x}=(0,1,0)^\top$. Then $\mathbf{w}\mathbf{x}^\top$ has a 1 at position (1,2), but $\mathbf{x}\mathbf{w}^\top$ has its 1 at (2,1), so B fails.

---

## Question 2

$\mathbf{w}$ is $3\times1$ and $\mathbf{A}$ is $5\times3$. What is the dimension of $\left(\mathbf{w}^\top\mathbf{A}^\top\mathbf{A}\mathbf{w}\right)^\top$?

Options: A $5\times5$ · B $3\times3$ · C $3\times1$ · D $1\times1$ · E $1\times5$ · F $1\times3$ · G incorrect dimensions

**Lecture material:** Matrix notation and the quadratic form $\mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w}$, which appears in the MSE expansion (p. 15).

**Working:** Chain the dimensions through the product:

$$\underbrace{\mathbf{w}^\top}_{1\times3}\underbrace{\mathbf{A}^\top}_{3\times5}\underbrace{\mathbf{A}}_{5\times3}\underbrace{\mathbf{w}}_{3\times1}$$

- $\mathbf{w}^\top\mathbf{A}^\top$: $1\times5$
- $\times\,\mathbf{A}$: $1\times3$
- $\times\,\mathbf{w}$: $1\times1$

Every inner dimension matches, so G is wrong. The transpose of a $1\times1$ is still $1\times1$.

**Final answer: D ($1\times1$)**

**Check:** The expression is $\|\mathbf{A}\mathbf{w}\|^2$, a squared norm, so it must be a scalar. This matches $\mathbf{w}^\top\mathbf{X}^\top\mathbf{X}\mathbf{w}$ inside the scalar loss $E(\mathbf{w})$ on p. 15.

---

## Question 3

Same sizes as Question 2. What is the dimension of $\mathbf{A}\mathbf{w}\mathbf{w}^\top\mathbf{A}^\top$?

**Lecture material:** Matrix notation (pp. 12–15).

**Working:**

$$\underbrace{\mathbf{A}}_{5\times3}\underbrace{\mathbf{w}}_{3\times1}\underbrace{\mathbf{w}^\top}_{1\times3}\underbrace{\mathbf{A}^\top}_{3\times5}$$

- $\mathbf{A}\mathbf{w}$: $5\times1$
- $\times\,\mathbf{w}^\top$: $5\times3$
- $\times\,\mathbf{A}^\top$: $5\times5$

**Final answer: A ($5\times5$)**

**Check:** Write $\mathbf{v} = \mathbf{A}\mathbf{w}$ ($5\times1$). The expression is then $\mathbf{v}\mathbf{v}^\top$, an outer product, which is $5\times5$.

---

## Question 4

$$E(\mathbf{w}) = \frac{1}{1 + \mathbf{w}^\top\mathbf{x} + \mathbf{w}^\top\mathbf{w}}$$

What is $\dfrac{\partial E}{\partial \mathbf{w}}$?

- A. $-\dfrac{\mathbf{x} + 2\mathbf{w}}{(1 + \mathbf{w}^\top\mathbf{x} + \mathbf{w}^\top\mathbf{w})^2}$
- B. $-\dfrac{\mathbf{x}^\top + 2\mathbf{w}^\top}{(\dots)^2}$
- C. $-\dfrac{\mathbf{w}}{(\dots)^2}$
- D. $-\dfrac{\mathbf{x}}{(\dots)^2}$

**Lecture material:** Gradient identities on p. 16: $\dfrac{\partial \mathbf{a}^\top\mathbf{w}}{\partial \mathbf{w}} = \mathbf{a}$ and $\dfrac{\partial \mathbf{w}^\top\mathbf{w}}{\partial \mathbf{w}} = 2\mathbf{w}$. The gradient is written as a column vector with the same shape as $\mathbf{w}$ (pp. 15–16). For the chain rule, see [handout-05](<../../Lecture Slides/handout-05-deep-feedforward-networks.pdf>) p. 37.

**Working:**
1. Let $g(\mathbf{w}) = 1 + \mathbf{w}^\top\mathbf{x} + \mathbf{w}^\top\mathbf{w}$, so $E = g^{-1}$.
2. $\dfrac{\partial g}{\partial \mathbf{w}} = \mathbf{x} + 2\mathbf{w}$. Here $\mathbf{w}^\top\mathbf{x} = \mathbf{x}^\top\mathbf{w}$ gives $\mathbf{x}$, and $\mathbf{w}^\top\mathbf{w}$ gives $2\mathbf{w}$. The result is a $p\times1$ column, like $\mathbf{w}$.
3. Chain rule: $\dfrac{\partial E}{\partial \mathbf{w}} = \dfrac{dE}{dg}\dfrac{\partial g}{\partial \mathbf{w}} = -\dfrac{1}{g^2}(\mathbf{x}+2\mathbf{w})$.

**Final answer: A**

**Check:**
- **Shape:** The gradient is a column vector with the same shape as $\mathbf{w}$. Option B is its transpose (a row vector), which does not match the lecture's convention $\partial(\mathbf{a}^\top\mathbf{w})/\partial\mathbf{w} = \mathbf{a}$.
- **1‑D case:** With $E = 1/(1 + wx + w^2)$, $dE/dw = -(x+2w)/(1+wx+w^2)^2$. ✓

---

## Question 5

Which models (inputs $x_1, x_2$; parameters $w_1, w_2$; $\epsilon\sim\mathcal{N}(0,\sigma^2)$) are linear in the parameters and follow the Least Squares assumptions?

- A. $y = \log(x_1)w_1 + \log(x_2+1)(w_2+1) + \epsilon$
- B. $y = \sin(x_1 w_1 + w_2) + \epsilon$
- C. $y = w_1x_1^2 + w_2x_2^2 + 3\epsilon$
- D. $y = w_1^2x_1 + w_2^2x_1 + 3\epsilon$

**Lecture material:**
- p. 23: $y = w_0 + w_1x + w_2x^2 + w_3x^3$ is still linear because $y$ is a linear combination of fixed features. $y = w_0^2 + x$ is **not** linear in the parameters.
- p. 24: a model is linear if $y = \sum_i w_i f_i(\mathbf{x})$, where the $f_i$ do not depend on $\mathbf{w}$.
- pp. 50–53: LS is the maximum-likelihood estimate when the error is Gaussian, $\epsilon \sim \mathcal{N}(0,\sigma^2)$, with the same variance for every observation.

**Working:**
- **A:** $y = w_1\log(x_1) + w_2\log(x_2+1) + \log(x_2+1) + \epsilon$. The features $\log x_1$ and $\log(x_2+1)$ do not depend on $\mathbf{w}$. The leftover term $\log(x_2+1)$ is a known offset with no parameter, so it can be moved to the left-hand side: $y' = y - \log(x_2+1)$. The noise is additive Gaussian. ✅
- **B:** $\sin(\cdot)$ wraps the parameters, so the model cannot be written as $\sum w_i f_i(\mathbf{x})$. ❌
- **C:** The features are $x_1^2$ and $x_2^2$. $3\epsilon \sim \mathcal{N}(0, 9\sigma^2)$ is still zero-mean Gaussian with constant variance, so the LS assumptions hold. ✅
- **D:** $w_1^2$ and $w_2^2$ are not linear in the parameters, exactly like the $w_0^2$ counter-example on p. 23. ❌

**Final answer: A, C**

**Check:** For A and C, $\partial y/\partial w_i$ does not depend on $\mathbf{w}$. That is the test for linearity in the parameters. For B and D it does.

---

## Question 6

Same set-up. Which models are linear in the parameters and follow the LS assumptions?

- A. $y = w_1x_1 + w_2x_2 + \epsilon$
- B. $y = w_1x_1 + w_2x_1^2 + 3w_1x_2 + 2w_2x_1^2x_2^2 + \epsilon$
- C. $y = w_1x_1 + w_2x_2 + (x_1+x_2)\epsilon$
- D. $y = x_1w_1 + x_1w_1^2 + x_2w_1^3 + w_2 + \epsilon$

**Lecture material:** p. 24 (definition of a linear model); pp. 50–51 (each $\epsilon_i \sim \mathcal{N}(0,\sigma^2)$ with the same $\sigma$, which gives the LS likelihood).

**Working:**
- **A:** This is the standard linear model. ✅
- **B:** Group the terms by parameter: $y = w_1(x_1 + 3x_2) + w_2(x_1^2 + 2x_1^2x_2^2) + \epsilon$. That is $\sum w_i f_i(\mathbf{x})$ with $f_1 = x_1+3x_2$ and $f_2 = x_1^2+2x_1^2x_2^2$. ✅
- **C:** The model is linear in $\mathbf{w}$, but the noise term is $(x_1+x_2)\epsilon \sim \mathcal{N}(0,(x_1+x_2)^2\sigma^2)$. Its variance changes with the input, so the errors no longer share a single $\sigma^2$. The derivation on pp. 51–52 relies on a common $\sigma^2$, so the LS assumptions fail. ❌
- **D:** $w_1^2$ and $w_1^3$ are not linear in the parameters. ❌

**Final answer: A, B**

**Check:** Option B shows that a model can look complicated in $\mathbf{x}$ and still be linear. Only the dependence on $\mathbf{w}$ matters.

---

## Question 7

Same set-up. Which models are linear in the parameters and follow the LS assumptions?

- A. $y = w_1x_1^2 + x_2w_2^2 + \epsilon$
- B. $y = w_1w_2 + x_1x_2 + \epsilon$
- C. $y = (w_1x_1 + x_2)/(w_2x_2 + x_3) + \epsilon$
- D. $y = x_1x_1 + w_1 + \exp(-0.7)\epsilon$

**Lecture material:** pp. 23–24 (linearity in the parameters); pp. 50–53 (Gaussian noise assumption).

**Working:**
- **A:** $w_2^2$ is not linear. ❌
- **B:** The product $w_1w_2$ is not linear in the parameters. ❌
- **C:** $w_2$ appears in a denominator, so the model is not linear. ❌
- **D:** $y = x_1^2 + w_1\cdot1 + c\,\epsilon$, where $c = e^{-0.7}\approx0.50$ is a constant.
  - $w_1$ multiplies the constant feature 1, so it is the bias (p. 13).
  - $x_1^2$ is a known offset, as in Question 5A.
  - $c\,\epsilon \sim \mathcal{N}(0, c^2\sigma^2)$ is Gaussian with constant variance.
  
  ✅

**Final answer: D**

**Check:** D is the only option without a product, power, or ratio of parameters. It also confirms that known offset terms and constant noise scaling are allowed, which is consistent with Question 5 (A and C).

---

## Question 8

We fit a polynomial model with LS. We have a **very large** training set, but the predictions are poor. What could help?

A. decrease the training set · B. increase the training set · C. increase the test set · D. decrease the test set · E. increase the Tikhonov regularisation · F. increase the polynomial order

**Lecture material:**
- pp. 29–30: underfitting happens when the model order is too low, and "the error cannot get low enough".
- pp. 35–36: more data cures **overfitting**, and with plenty of data it is fine to use a more complex model.
- p. 46: regularisation pulls the weights towards 0.
- [handout-04](<../../Lecture Slides/handout-04-evaluating-classifier-performance.pdf>) pp. 34–35: the test set is only used to *assess* the model, not to train it.

**Working:**
1. With a very large training set, overfitting is unlikely (pp. 35–36). Poor predictions therefore point to **underfitting**: the model is too simple.
2. **F:** A higher polynomial order adds capacity, which is the cure for underfitting shown on pp. 28–29 (degree 1 underfits and degree 2 fits). ✅
3. **A and B:** Changing the training set size does not fix a model that is too simple. Removing data can only make things worse. ❌
4. **C and D:** The test set does not affect the fitted model (handout-04 pp. 34–35). ❌
5. **E:** More regularisation shrinks the weights further towards 0 (p. 46), which makes underfitting worse. ❌

**Final answer: F**

**Check:** This matches the lecture's guidance. Plenty of data lets you safely use a richer model (p. 36).

---

## Question 9

We fit a 3rd-degree polynomial to data that really comes from a 3rd-degree polynomial, but we are overfitting. Which strategy gives the best chance of estimating the **true coefficients**?

(Same options A–F as Question 8.)

**Lecture material:**
- p. 35: when the model is right but overfits, "you simply don't have enough observations … The cure is then to get more data."
- pp. 46–47: regularisation "acts as a bias that pulls the estimation of $\mathbf{w}$ slightly towards 0 … this comes at the cost of biasing the estimation. Thus in practice you want to avoid it … get plenty data!"

**Working:**
1. The model order is correct, so overfitting here comes from **too few observations** (p. 35).
2. **B:** More training data is the lecture's cure, and it does not bias the coefficients. ✅
3. **E:** Tikhonov regularisation reduces overfitting but biases the coefficients towards 0 (pp. 46–47). That is a worse estimate of the *true* coefficients. ❌
4. **F:** Raising the order adds unnecessary parameters and makes overfitting worse. ❌
5. **A:** Less training data makes overfitting worse. **C and D:** The test set does not affect the fit. ❌

**Final answer: B**

**Check:** The question asks for the best estimate of the true coefficients, not just less overfitting. Only extra data reduces variance without adding bias.

---

## Question 10

Which facts are true?

A. Regularisation biases the parameters towards 0. · B. Regularisation is usually used to reduce underfitting. · C. Regularisation is usually used to reduce overfitting. · D. Tikhonov regularisation adds significant numerical complexity to LS.

**Lecture material:** pp. 44–45 (regularisation as the alternative to more data for combating overfitting); p. 45 (direct solution $\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X} + \alpha\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$); p. 46 ("acts as a bias that pulls the estimation of $\mathbf{w}$ slightly towards 0").

**Working:**
- **A:** True, stated directly on p. 46. ✅
- **B:** False. Regularisation constrains the model, which would make underfitting worse. ❌
- **C:** True. It is introduced as the alternative to more data for combating overfitting (p. 44). ✅
- **D:** False. The only change is adding $\alpha\mathbf{I}$ before the inverse, and there is still a direct closed-form solution (p. 45). It actually *improves* the conditioning. ❌

**Final answer: A, C**

**Check:** As $\alpha \to \infty$, $\hat{\mathbf{w}} \to 0$, which confirms A. As $\alpha \to 0$, you recover the normal equations of p. 19.

---

## Question 11

Given a loss $E(\mathbf{w})$, we also want $\sum_{j=0}^p w_jb_j$ to be close to zero. Which new loss achieves this?

- A. $E + \lambda(\mathbf{b}-\mathbf{w})^\top(\mathbf{b}-\mathbf{w})$
- B. $E + \lambda\mathbf{w}^\top\mathbf{b}$
- C. $E + \lambda\mathbf{w}^\top\mathbf{b}\mathbf{b}^\top\mathbf{w}$
- D. $E + \lambda\mathbf{b}^\top\mathbf{b}$

**Lecture material:** Tikhonov regularisation (p. 45). Add a penalty term $\alpha\|\mathbf{w}\|^2$ that is non-negative and smallest at the quantity you want to be zero. The same idea appears in [handout-05](<../../Lecture Slides/handout-05-deep-feedforward-networks.pdf>) p. 73: $E' = E + \lambda w_i^2$.

**Working:**
1. $\sum_j w_jb_j = \mathbf{w}^\top\mathbf{b}$ is a scalar. A good penalty should be $\ge0$ and equal 0 exactly when $\mathbf{w}^\top\mathbf{b}=0$. The natural choice is its square, which mirrors the $w_i^2$ penalty.
2. $(\mathbf{w}^\top\mathbf{b})^2 = (\mathbf{w}^\top\mathbf{b})(\mathbf{b}^\top\mathbf{w}) = \mathbf{w}^\top\mathbf{b}\mathbf{b}^\top\mathbf{w}$. This is option C. ✅
3. **A:** Pulls $\mathbf{w}$ towards $\mathbf{b}$, which is a different goal. ❌
4. **B:** Linear in $\mathbf{w}$ and unbounded below, so minimising it drives $\mathbf{w}^\top\mathbf{b} \to -\infty$, not to 0. ❌
5. **D:** Does not depend on $\mathbf{w}$, so it has no effect. ❌

**Final answer: C**

**Check:**
- **Dimensions:** $(1\times p)(p\times1)(1\times p)(p\times1) = 1\times1$, a scalar penalty.
- **Gradient:** From p. 16, $\partial(\mathbf{a}^\top\mathbf{w}\mathbf{w}^\top\mathbf{b})/\partial\mathbf{w} = (\mathbf{a}\mathbf{b}^\top + \mathbf{b}\mathbf{a}^\top)\mathbf{w}$. With $\mathbf{a}=\mathbf{b}$ this gives $2\lambda\mathbf{b}\mathbf{b}^\top\mathbf{w}$, which is 0 when $\mathbf{b}^\top\mathbf{w}=0$. ✓

---

## Question 12

Consider the Least Squares prediction below. Which statements are correct?

![Q12 figure](<image q12.png>)

A. A larger test set improves the error · B. A larger training set improves the error · C. More Tikhonov regularisation improves the error · D. Less Tikhonov regularisation improves the error · E. This is overfitting · F. This is underfitting

**Lecture material:**
- pp. 29–30: underfitting. The degree-1 fit cannot follow the curved ground truth, and "the error cannot get low enough".
- pp. 32–33: overfitting means a low training error but poor behaviour between and beyond the data.
- p. 46: Tikhonov pulls **all** weights towards 0.
- [handout-04](<../../Lecture Slides/handout-04-evaluating-classifier-performance.pdf>) pp. 34–35: role of the test set.

**Working:**
1. **What the figure shows:**
   - The ground truth is a downward parabola, about $y\approx-2x^2$, reaching about $-128$ at $x=\pm8$.
   - There are many data points.
   - The prediction is an almost flat line at $y\approx-45$, so it misses the training data badly. That is **underfitting** (F ✅, E ❌).
2. **Why the line is flat:** Over $x\in[-8,8]$, the mean of $-2x^2$ is $-2\cdot64/3\approx-43$. That is the height of the red line. This is what an unregularised degree-0 or degree-1 LS fit gives on symmetric data: the slope is about 0 and the intercept is the data mean. Heavy Tikhonov regularisation would instead pull **all** weights, including the bias $w_0$, towards 0 (p. 46), so the line would sit near $y=0$, not $-45$.
3. **B:** There is already plenty of data, and more data does not fix a model that is too simple. ❌
4. **A:** The test set does not change the fit. ❌
5. **C:** More regularisation makes underfitting worse. ❌
6. **D:** The fit sits at the data mean, so the model order is what limits it, not regularisation. Lowering regularisation cannot make a straight line curve. ❌ The real fix (raising the polynomial order to at least 2) is not one of the options.

**Final answer: F**

> ⚠️ **Judgement call:** If the quiz treats "less regularisation" as a generic cure for underfitting, it may also accept D. The figure (a flat line at the data mean, not near 0) suggests regularisation is not the cause, so D is not selected here.

**Check:** This is the same situation as p. 29: a model that is too low-order for curved data gives a large error even with lots of samples.

---

## Question 13

We fit a polynomial of order 7 using LS. Why does the estimated model look so poor?

![Q13 figure](<image q13.png>)

A. The dataset is too small. · B. We should use regularisation. · C. The error is not independent and Gaussian. · D. The model order is too high.

**Lecture material:**
- pp. 50–53: LS is the maximum-likelihood solution **only if** $\epsilon_i \sim \mathcal{N}(0,\sigma^2)$, independent and identically distributed.
- p. 61 ("going further", non-examinable): "Always check your model. LS assumes $y = \mathbf{x}^\top\mathbf{w} + \epsilon$ with $\epsilon$ Gaussian."
- pp. 34–36: model order and the amount of data.

**Working:**
1. **What the figure shows:**
   - Over $x\in[-5,5]$ the points sit almost exactly on the ground truth (near-zero noise).
   - At the ends ($|x|>7$) the scatter is huge (±300 or more).
   - So the noise variance grows strongly with $|x|$ (the noise is heteroscedastic), and it may also contain outliers. This is not i.i.d. $\mathcal{N}(0,\sigma^2)$ noise.
2. LS minimises $\sum_i(\mathbf{x}_i^\top\mathbf{w}-y_i)^2$ and gives every point equal weight (p. 52). The large-noise points at the ends dominate the sum. The fit bends to chase them and misses the very clean, flat middle section. **C** ✅
3. **A:** There are well over 100 points for 8 coefficients, which is not a small dataset in the sense of p. 35. ❌
4. **B:** Regularisation would bias the coefficients towards 0 (p. 46) without fixing the noise model. ❌
5. **D:** The ground truth (flat in the middle, steep at the ends) looks like a high odd-order polynomial, so order 7 is appropriate. The fit is poor because of the noise, not because the order is too high. ❌

**Final answer: C**

**Check:** If the noise were constant-variance Gaussian, this many points would pin an order-7 fit closely to the ground truth, as in the lecture's degree-9 fit with plenty of data on p. 36.
