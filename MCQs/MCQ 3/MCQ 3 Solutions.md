# MCQ 3 — Classic Classifiers (k-NN, Decision Trees, SVM, Kernel Trick): Worked Solutions

**Main source:** [handout-03-classic-classifiers.pdf](<../../Lecture Slides/handout-03-classic-classifiers.pdf>)

> Page references are **PDF page numbers**. For handout-03 they match the printed slide numbers.

## Answer summary

| Q | Answer |
|---|--------|
| 1 | C |
| 2 | D |
| 3 | B |
| 4 | B, C |
| 5 | A |
| 6 | A, C, D |
| 7 | A (3-NN) |
| 8 | A |
| 9 | A, B |
| 10 | B |

---

## Question 1

What datasets are best suited for kernel methods? ($n$ = number of observations, $p$ = number of features)

A. large $n$, large $p$ · B. large $n$, small $p$ · C. small $n$, large $p$ · D. small $n$, small $p$ · E. size doesn't matter

**Lecture material:**
- p. 24: with the kernel trick, the $p\times1$ weight vector $\hat{\mathbf{w}}$ is re-parametrised as an $n\times1$ vector $\boldsymbol{\alpha}$ (the dual coefficients).
- pp. 25–27: you only need kernel values $\kappa(\mathbf{x},\mathbf{x}_i)$. These cost scalar products in dimension $p$, however large the implicit feature space is.
- p. 36: "the cost of evaluating the decision function is proportional to the number of training examples … The cost of training is however still high for large datasets."
- p. 39: kernel techniques "cannot deal efficiently with large datasets (eg. more than 10's of thousands of observations)."

**Working:**
1. **Large $n$ is bad.** Training and prediction costs both grow with $n$ (pp. 36, 39), which rules out A and B.
2. **Large $p$ is fine, even helpful.** The problem is solved over $n$ dual coefficients instead of $p$ (or $\dim\phi$) weights (p. 24), and each kernel evaluation is cheap (p. 27). The method stays efficient when the feature dimension is large.
3. Kernel methods are therefore at their best when $n$ is small and $p$ is large.

**Final answer: C**

> Note: The slides state the "large $n$ is bad" half directly. The "large $p$ is fine" half follows from the $p\to n$ re-parametrisation on p. 24. It is an inference, not a sentence from the slides.

**Check:** On p. 22, $p=100$ with degree 5 makes $\mathbf{X}^\top\mathbf{X}$ about $10^8\times10^8$ in the primal form. In the dual form the problem only has size $n\times n$.

---

## Question 2

When are Machine Learning methods usually less effective? (select all)

A. When the data is linearly separable. · B. When the observations are linearly dependent. · C. When the classes are linearly dependent. · D. When the classes mix (point clouds overlap).

**Lecture material:** pp. 4, 7, 33 and 34 compare classifiers on three toy problems. On the problem where the two classes overlap most, every method gets a lower accuracy. For example, on p. 4 the k-NN accuracies are 87.5–92.5%, compared with up to 97.5% on the other problems.

**Working:**
- **D:** If the class point clouds overlap, some regions of feature space genuinely contain both classes. No classifier can be correct everywhere there. ✅
- **A:** Linearly separable data is the *easiest* case, since even a linear classifier can be perfect. ❌
- **B:** Linearly dependent observations (for example, duplicated or rescaled points) do not by themselves make classification harder. ❌
- **C:** "Linearly dependent classes" is not a meaningful property here. ❌

**Final answer: D**

> Note: The slides show this effect in their examples but do not state it as a rule. The general explanation is added here.

**Check:** On p. 33, the same classifiers reach 95% on the cleaner problems but fall below that wherever the classes mix.

---

## Question 3

An SVM with a polynomial kernel of degree 2 reaches 100% training **and** test accuracy. You now increase the degree $d$. What would happen? (select all)

A. may underfit · B. may overfit · C. nothing (already 100% on training) · D. nothing (already 100% on test) · E. none of the above

**Lecture material:**
- p. 21: a higher degree $d$ means a much larger implicit feature space, with dimension $(p+d)!/(p!\,d!)$.
- p. 33 (polynomial-kernel results): on the middle problem, $d=2$ gets 95% but $d=3$ drops to 40%. Changing $d$ changes the model and can make it worse.
- [handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) pp. 31–32: more model complexity than the data needs leads to overfitting.

**Working:**
1. Increasing $d$ gives the classifier a richer, more flexible feature space than this problem needs, since $d=2$ is already perfect. Extra flexibility can fit noise, which means it **may overfit**. **B** ✅
2. **A:** Underfitting comes from too little capacity, but we are *adding* capacity. ❌
3. **C and D:** The model *does* change when $d$ changes, and p. 33 shows the accuracy can change a lot. 100% now does not guarantee 100% after the change. ❌

**Final answer: B**

**Check:** This is the same pattern as the degree-2 vs degree-9 polynomial fits in handout-01 (pp. 28, 31): extra capacity is not needed and risks overfitting.

---

## Question 4

Which statements about kernel functions are true? (select all)

A. The kernel function maps low-dimensional data into a high-dimensional space. · B. The kernel function is a similarity function. · C. The computational complexity of the kernel function is independent of the corresponding mapped feature space. · D. Kernel functions are specific to SVM.

**Lecture material:**
- p. 25: $\kappa(\mathbf{u},\mathbf{v}) = \phi(\mathbf{u})^\top\phi(\mathbf{v})$. The **feature map** $\phi$ does the mapping. The kernel returns a scalar dot product.
- p. 26: "we can define $\kappa$ without having to explicitly define $\phi$."
- p. 27: "instead of requiring 100's of millions of dimensions, we only need to take scalar products between vectors of dimension $p$."
- p. 28: the RBF kernel's $\phi$ is infinite-dimensional, "but that's OK because we never need to evaluate $\phi(\mathbf{x})$."
- p. 29: the RBF kernel "is a measure of similarity between observations."
- p. 35: SVMs are not the only algorithm that can use the kernel trick.

**Working:**
- **B:** Stated directly on p. 29. ✅
- **C:** The cost depends only on the input dimension $p$, not on $\dim\phi$, which can even be infinite (pp. 27–28). ✅
- **D:** Other linear models, including logistic regression, can be kernelised (p. 35). ❌
- **A:** The *feature map* $\phi$ maps data to a high-dimensional space. The kernel function $\kappa:\mathbb{R}^p\times\mathbb{R}^p\to\mathbb{R}$ returns a single number, and the whole point is that you never compute the mapping. ❌

**Final answer: B, C**

> ⚠️ **Judgement call on A:** Informally, people often say "the kernel maps data into a high-dimensional space." If the quiz uses that loose wording, it may accept A. Strictly, following the lecture's definitions, the mapping is done by $\phi$, not $\kappa$.

**Check:** The RBF kernel takes two $p$-vectors and returns $e^{-\gamma\|\mathbf{u}-\mathbf{v}\|^2}$. That is one scalar, computed in $O(p)$ time, even though $\phi$ is infinite-dimensional.

---

## Question 5

Which facts about SVM and the kernel trick are true?

A. The kernel trick can be used for both SVM and Logistic Regression. · B. The loss for Linear SVM and Logistic Regression are the same. · C. Linear SVM is a priori more performant than Logistic Regression.

**Lecture material:**
- p. 35: "Many other linear models (including logistic regression) can be enhanced in this way."
- p. 12: SVM uses the hinge loss. Logistic regression uses the cross-entropy.
- p. 15: "there is a priori no advantage of using linear SVM over logistic regression in terms of performance alone." This is the No Free Lunch theorem (p. 16).

**Working:** A is stated on p. 35 ✅. B is false because the losses are hinge vs cross-entropy (p. 12) ❌. C is false (p. 15) ❌.

**Final answer: A**

**Check:** p. 38 lists "kernel Logistic Regression" under further reading, which confirms A.

---

## Question 6

Consider the binary dataset below (features $x_1, x_2$; classes cross and circle). Which classifiers are suitable without any prior feature recombination?

![Q6 figure](<q6 image.png>)

A. Decision Tree · B. Logistic Regression · C. Random Forest · D. SVM with RBF kernel

**Lecture material:**
- [handout-02](<../../Lecture Slides/handout-02-logistic-regression.pdf>) pp. 11 and 32: logistic regression's decision boundary $\mathbf{x}^\top\mathbf{w}=0$ is a straight line.
- handout-03 p. 6: decision trees split the input space along the axes.
- p. 7: Random Forest and AdaBoost combine many trees.
- pp. 29–30 and 34: an RBF SVM gives smooth, local, non-linear boundaries similar to k-NN.

**Working:**
1. **What the figure shows:** The crosses form a compact cluster in the centre, and the circles form a ring around them. The true boundary is roughly a circle.
2. **B:** Logistic regression can only draw one straight line, which cannot enclose the central cluster without feature engineering such as adding $x_1^2, x_2^2$. ❌
3. **A:** A decision tree can carve out a central box using axis-aligned splits ($a<x_1<b$, $c<x_2<d$), then refine it with further splits. This gives a staircase approximation of the circle. ✅
4. **C:** A random forest averages many such trees and gives a smoother approximation of the circular region (p. 7). ✅
5. **D:** The RBF kernel works by neighbourhood similarity (p. 29), so it handles a closed, round boundary naturally. ✅

**Final answer: A, C, D**

**Check:** This looks like the middle "concentric" toy problem in the slides. There, linear SVM only gets 40% (p. 33), while tree-based methods and RBF SVM get 77.5–87.5% (pp. 7 and 34) even with noisier, overlapping data.

---

## Question 7

Which binary classifier produced this decision-boundary map? (shading shows $p$ in four bins: 0–0.25, 0.25–0.5, 0.5–0.75, 0.75–1)

![Q7 figure](<q7 image.png>)

A. 3-NN · B. 5-NN · C. 1-NN · D. Decision Tree · E. AdaBoost or Random Forest · F. SVM with RBF kernel

**Lecture material:**
- p. 3: k-NN returns "the confidence as a proportion of the majority class", so the output is always a multiple of $1/k$.
- p. 4: example k-NN maps, with polygon-shaped regions.
- p. 6: decision trees split along the axes, so they produce horizontal and vertical edges.
- p. 34: RBF SVM gives smooth, curved boundaries.

**Working:**
1. **Boundary shape:** The regions are polygons with *diagonal* straight edges, like Voronoi cells. That is typical of k-NN. Trees, AdaBoost and Random Forest would give axis-aligned, rectangular edges (D, E ❌). An RBF SVM would give smooth curves (F ❌).
2. **Number of shade levels:** I measured the image pixels. The plot contains exactly 4 grey levels, one for each colour-bar bin.
   - 1-NN can only output $p\in\{0,1\}$, giving 2 levels. ❌ (C)
   - 3-NN outputs $p\in\{0,\tfrac13,\tfrac23,1\}$, one value in each bin, giving 4 levels.
   - 5-NN outputs $p\in\{0,0.2,0.4,0.6,0.8,1\}$, which also fills 4 bins.
3. **Isolated points tell 3-NN and 5-NN apart:** Look at the two lone white circles inside the cross region (one at the far left and one at the bottom centre).
   - Each is surrounded by an island of the **0.25–0.5** shade (measured grey value 133, against 73 for the surrounding 0–0.25 region).
   - With 3-NN, one circle among its 3 neighbours gives $p=1/3$, which falls in 0.25–0.5. ✓
   - With 5-NN, one circle among 5 neighbours gives $p=0.2$, which stays in the darkest bin, so no island would appear. ✗
   - With 1-NN, the island would be fully white ($p=1$). ✗

**Final answer: A (3-nearest neighbours)**

**Check:** The 90% accuracy also fits 3-NN. A few training points (the isolated circles) are outvoted by their neighbours and misclassified, which 1-NN would not do on its own training points.

---

## Question 8

Consider the binary dataset below. Which classifier is least likely to overfit? (one answer)

![Q8 figure](<q 8 image.png>)

A. Logistic Regression · B. SVM with RBF kernel · C. Decision Tree · D. $k$-NN · E. Random Forest · F. Least Squares

**Lecture material:**
- [handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) pp. 32–34: overfitting grows with model complexity, so use the simplest model that does not underfit.
- [handout-02](<../../Lecture Slides/handout-02-logistic-regression.pdf>) p. 32: logistic regression gives a single linear boundary.
- handout-02 pp. 9–10: least squares is a poor loss for classification, because it "heavily penalises correctly classified but distant points, pulling the decision boundary away from a good position."
- handout-03 p. 5: k-NN "may generalise very badly."

**Working:**
1. **What the figure shows:** The crosses are mostly top and right, and the circles mostly bottom-left. The split is roughly a diagonal line, with a few points on the wrong side (label noise). A linear boundary is the right model.
2. **B, C, D, E:** These are flexible, non-linear models. They can bend around the few noisy points, which is overfitting. ❌
3. **A or F:** Both have a linear boundary and few parameters. Logistic regression is the *classification* model designed for this, while LS is pulled by distant, correctly classified points (handout-02 p. 10). Logistic regression is the single best answer. ✅

**Final answer: A**

**Check:** The model has only 3 parameters ($w_0, w_1, w_2$) and a single straight-line boundary, so it cannot memorise the few outlying points.

---

## Question 9

What are the effects of increasing $k$ in $k$-NN? (true in general)

A. increases the area of the decision map where $0<p<1$ · B. increases the computational time of a prediction · C. increases overall accuracy · D. decreases overall accuracy

**Lecture material:** p. 3: the prediction is the majority class among the $k$ nearest neighbours, and the confidence is the proportion of the majority class. p. 4: as $k$ goes from 1 → 3 → 10 the uncertain (intermediate-shade) bands grow. The accuracy goes **up or down** depending on the problem: 87.5 → 92.5 → 87.5 in one case, and 97.5 → 97.5 → 95.0 in another. p. 5: finding nearest neighbours is computationally expensive.

**Working:**
- **A:** With more neighbours, more locations have a mix of both classes in their neighbourhood, so $p$ is strictly between 0 and 1 over a larger area. This is visible on p. 4. ✅
- **B:** More neighbours must be retrieved, sorted and counted for each prediction, so the cost rises (modestly). ✅
- **C and D:** Neither holds in general. On p. 4, accuracy goes up on one problem and down on another as $k$ increases. ❌

**Final answer: A, B**

> Note on B: The extra cost is small, because computing distances to all $n$ training points dominates either way. It is still a real increase, so B counts as true "in general".

**Check:** For 1-NN, $p\in\{0,1\}$ only, so no region has $0<p<1$. That area can only grow as $k$ increases.

---

## Question 10

Which statements about Decision Trees are true?

A. DT-based methods (e.g. AdaBoost) only predict the most likely class, not a probability. · B. Decision Trees are computationally more efficient than kernel SVMs. · C. Decision Trees decide using binary tests like $\mathbf{x}^\top\mathbf{w}>0$. · D. Decision Trees are robust to a rotation of the feature space.

**Lecture material:**
- p. 6: "The regions are split along the axes of the input space (eg. … a binary test such as $x_2 < 3$)."
- p. 7: "In Ada Boost and Random Forests multiple decision trees are used to aggregate a **probability** on the prediction."
- p. 8: random forests "can be very efficiently computed."
- p. 9: pro: "It is fast." Con: decisions are taken along axes, while a diagonal split might be better.
- p. 36: kernel methods cost grows with the number of training examples.

**Working:**
- **A:** False. These methods output probabilities (p. 7). ❌
- **B:** True. Trees are fast (pp. 8–9), while kernel SVMs scale with $n$ (p. 36). ✅
- **C:** False. Tree tests are single-feature thresholds such as $x_2<3$, not oblique tests like $\mathbf{x}^\top\mathbf{w}>0$, which is how linear classifiers decide. ❌
- **D:** False. Axis-aligned splits depend on the orientation of the axes. Rotating the features turns a clean axis-aligned boundary into a diagonal one, which a tree can only approximate with a staircase (p. 9). ❌

**Final answer: B**

**Check:** On p. 7, the AdaBoost and Random Forest maps show intermediate shades between 0 and 1, which are probabilities. This confirms A is false.
