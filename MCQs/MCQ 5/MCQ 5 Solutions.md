# MCQ 5 — Deep Feedforward Neural Networks: Worked Solutions

**Main source:** [handout-05-deep-feedforward-networks.pdf](<../../Lecture Slides/handout-05-deep-feedforward-networks.pdf>)

> Page references are **PDF page numbers**, as shown in a PDF viewer. The slide number printed in the corner differs from about p. 22 onwards because of animation builds. For example, PDF p. 57 is printed slide 38.

## Answer summary

| Q | Answer |
|---|--------|
| 1 | B |
| 2 | B, D |
| 3 | C |
| 4 | C |
| 5 | A |
| 6 | A (True) |
| 7 | A, C |
| 8 | D |
| 9 | C, D |
| 10 | A, B |
| 11 | C (2000) |
| 12 | B (True) |
| 13 | A, B, C, F |
| 14 | D |
| 15 | B (False) |
| 16 | E |
| 17 | B (False) |
| 18 | B (False) |
| 19 | C (it depends) |
| 20 | A, B |

---

## Question 1

In a Neural Network, what is a unit? (only one answer)

A. a linear combination of inputs followed by an activation function · B. a differentiable function · C. the loss function · D. a set of neurons

**Lecture material:**
- p. 5: "Neural Networks are called networks because they can be associated with a directed acyclic graph … **Each node in the graph is called a unit.** … All other units (eg. $u_1, u_2$) correspond to function outputs."
- p. 7: "it mainly relies on **neuron-like units**. A neuron unit first takes a linear combination of its inputs and then applies a non-linear function."
- pp. 41–48: back-propagation needs $\partial u_j/\partial u_i$ for every unit, and the example units include $u_{14} = u_5 + 0.2u_{10} + 0.7u_{11} + 0.3u_9$, which has no activation at all.

**Working:**
1. A **unit** is any node of the computational graph. Apart from the inputs and parameters, each unit is the output of some function of other units. Back-propagation needs to differentiate each one (p. 56), so they must be **differentiable functions**. **B** ✅
2. **A** describes a *neuron* unit (p. 7). That is one special kind of unit, not the general definition. The $u_{14}$ example (p. 48) is a unit that is just a linear combination with no activation. ❌
3. **C:** The loss is one particular node, $e$. **D:** A set of neurons is a layer. ❌

**Final answer: B**

> ⚠️ **Judgement call:** If the quiz is using "unit" loosely to mean "neuron", it would expect A. The handout separates the two: a unit is any graph node (p. 5), while a neuron is a "neuron-like unit" (p. 7). So B is chosen here.

**Check:** p. 15 calls any non-input, non-output node a "hidden unit". That also treats a unit as a general node rather than a specific formula.

---

## Question 2

Which statements are true? (select all)

A. In the LIF neuron model, LIF stands for Leaky Intensity-and-Fire. · B. The relationship between input intensity and output firing rate resembles an activation function. · C. Both the mathematical model of artificial neurons and their training method were inspired by biology. · D. The membrane potential drops in the absence of stimulus.

**Lecture material:**
- p. 11: "the **Leaky Integrate-and-Fire** model (LIF)".
- p. 13: "The membrane potential drops in the absence of stimulus."
- p. 14: "In this LIF model, the neuron effectively behaves as an activation function for the current intensity."
- p. 10: artificial neurons were originally meant to model biological neurons.
- pp. 32–36: training uses gradient descent with back-propagation, which is the chain rule.

**Working:**
- **A:** False. It is *Integrate*, not *Intensity* (p. 11). ❌
- **B:** True (p. 14). ✅
- **C:** False. The neuron *model* was inspired by biology (p. 10), but the *training method* (gradient descent with back-propagation, pp. 32–36) is a purely mathematical tool built on the chain rule. The slides never present it as biologically inspired. ❌
- **D:** True, stated word for word on p. 13. ✅

**Final answer: B, D**

> Note on C: The slides do not explicitly say "back-prop is not biological". This conclusion comes from how the slides present it, as a chain-rule algorithm (pp. 36–37).

**Check:** In the LIF equation (p. 11), $C_m\,dV_m/dt = I(t) - V_m/R_m$. With $I=0$, $dV_m/dt = -V_m/(R_mC_m) < 0$, so the potential decays ("leaks"). This confirms D.

---

## Question 3

The Universal Approximation Theorem states that…

A. any continuous function can be approximated by a deep NN given enough **linear layers** · B. … given enough **layers** · C. … by a **single hidden layer** NN with a linear output, given enough neurons

**Lecture material:** p. 17 (Hornik, 1991): "a single hidden layer neural network with a linear output unit can approximate any continuous function arbitrarily well, given enough hidden units."

**Working:** C matches the statement on p. 17. A is wrong because stacking linear layers only ever gives a linear function. B is not what the theorem says: it is about width (one hidden layer), not depth.

**Final answer: C**

**Check:** p. 18: "Although the universal theorem tells us you only need one hidden layer …"

---

## Question 4

Network of operations: $e = (a-1)^2 + (b-0)^2$, $b = \cos(d)$, $a = \cos(c)$. Which is true?

A. BackProp must compute $\partial e/\partial a$ before $\partial e/\partial b$ · B. after · C. in any order · D. none of the above

**Lecture material:** p. 41: "We can evaluate the partial derivatives $\partial e/\partial u_{14}$, $\partial e/\partial u_{13}$, $\partial e/\partial u_{12}$ from the definition of $e$." p. 56: you can compute $\partial e/\partial u_i$ once **all of its outputs** already have their gradients.

**Working:**
1. **Graph:** $c\to a\to e$ and $d\to b\to e$. The two branches are separate.
2. Both $a$ and $b$ have a single output, $e$, so each gradient comes straight from the definition of $e$:
   - $\dfrac{\partial e}{\partial a} = 2(a-1)$
   - $\dfrac{\partial e}{\partial b} = 2b$
3. Neither gradient needs the other, so they can be computed in any order (or in parallel).

**Final answer: C**

**Check:** This is the same situation as $u_{12}, u_{13}, u_{14}$ on p. 42, where each gradient is written directly from $e$.

---

## Question 5

Network of operations: $a = b\cos(c)$, $b = c+2$, $e = a + b + c$. Which is true?

A. BackProp will compute $\partial e/\partial a$ before $\partial e/\partial b$ · B. after · C. at the same time · D. independently

**Lecture material:** p. 44: $\dfrac{\partial e}{\partial u_i} = \sum_{j\in\text{Outputs}(i)} \dfrac{\partial u_j}{\partial u_i}\dfrac{\partial e}{\partial u_j}$. p. 56: a node's gradient can be computed only once the gradients of all of its outputs are known.

**Working:**
1. **Graph edges:**
   - $c\to b$
   - $c\to a$ and $b\to a$
   - $a\to e$, $b\to e$ and $c\to e$
2. **Outputs of each node:**
   - $\text{Outputs}(a) = \{e\}$
   - $\text{Outputs}(b) = \{a, e\}$
3. $\dfrac{\partial e}{\partial a} = 1$. It only needs $e$.
4. $\dfrac{\partial e}{\partial b} = \underbrace{\dfrac{\partial e}{\partial b}\Big|_\text{direct}}_{1} + \dfrac{\partial a}{\partial b}\dfrac{\partial e}{\partial a} = 1 + \cos(c)\cdot\dfrac{\partial e}{\partial a}$. This **uses** $\partial e/\partial a$.
5. So $\partial e/\partial a$ must be computed first.

**Final answer: A**

**Check:** Since $\partial e/\partial a = 1$, we get $\partial e/\partial b = 1 + \cos c$. Directly: substituting $a$ gives $e = b\cos c + b + c$, so $\partial e/\partial b$ (holding $c$ fixed) $= \cos c + 1$ ✓. B, C and D are all incompatible with the dependency $b\to a$.

---

## Question 6

Deeper Neural Networks generalise better than shallower neural networks. True or False?

**Lecture material:** p. 18: "all recent works show that **deeper networks require far fewer parameters and generalise better to the testing set**." p. 26: "even if deeper networks are harder to train, they are more powerful." p. 80: "Deeper networks are known to be more efficient but harder to train."

**Working:** The handout makes this statement directly, as a general finding.

**Final answer: A (True)**

**Check:** This is a *general tendency*, not a guarantee. Question 15 asks whether *adding* hidden layers will **always** improve test accuracy, and the answer there is False.

---

## Question 7

Which statements about vanishing gradients (VG) are true? (select all)

A. VG often happens when training deep NNs. · B. VG happens when the values of the units get stuck near zero. · C. VG happens when the gradients of the units with respect to their inputs get stuck near zero.

**Lecture material:**
- p. 58: "One major challenge when training deeper networks is the problem of vanishing gradients."
- p. 59: $\dfrac{de}{dw} = \dfrac{de}{du_6}\dfrac{du_6}{du_5}\cdots\dfrac{du_1}{dw}$. "It is a product, so if any of $\lvert de/du_6\rvert,\dots,\lvert du_1/dw\rvert$ is near zero, then the resulting gradient will also be near zero."
- p. 60: sigmoid and tanh derivatives are about 0 outside $[-5,5]$.

**Working:**
- **A:** True. It is "a key difficulty when training Deep Neural Networks" (p. 61). ✅
- **B:** False. What matters are the **derivatives** $du_{k}/du_{k-1}$, not the unit values. For example, a sigmoid unit stuck near **1** (large input) has derivative about 0 and causes VG, while a unit near 0 can still have a healthy derivative. ❌
- **C:** True, this is the product argument on p. 59. ✅

**Final answer: A, C**

**Check:** For a sigmoid at input $t=10$: $f(10)\approx1$, not 0, but $f'(10) = f(1-f)\approx4.5\times10^{-5}$. The gradient vanishes even though the unit's value is far from 0.

---

## Question 8

Which activation function is best suited to avoid vanishing gradients? (one)

A. sigmoid · B. tanh · C. linear ($x\mapsto x$) · D. ReLU

**Lecture material:** p. 60: "Except for ReLU, outside of [-5, 5] range, the derivatives are zero or near zero." p. 61: "It is also one of the reasons ReLU is sometimes preferred as at least half of the range has a non-null gradient."

**Working:**
- **A and B:** Sigmoid and tanh saturate, so their derivatives are about 0 for large $|t|$. ❌
- **C:** A linear activation does have derivative 1 everywhere, but it is not a useful activation. A network made only of linear layers collapses into a single linear model, and the universal approximation theorem (p. 17) relies on non-linear hidden activations. ❌
- **D:** ReLU has derivative exactly 1 for all $t>0$, so it does not saturate on the positive side. It is the lecture's recommended choice. ✅

**Final answer: D**

**Check:** p. 60 compares the derivative plots of sigmoid, tanh and ReLU. Only ReLU's stays away from 0 for large inputs.

---

## Question 9

What loss can be used in a Neural Network for a **classification** problem?

A. L1 loss · B. L2 loss · C. cross-entropy · D. Hinge

**Lecture material:**
- [handout-02](<../../Lecture Slides/handout-02-logistic-regression.pdf>) pp. 24 and 38: binary and multinomial cross-entropy are the classification losses.
- handout-02 p. 25: using an L2 (least-squares) loss on sigmoid outputs "is in fact a mistake that the Neural Net community did for a number of years."
- [handout-03](<../../Lecture Slides/handout-03-classic-classifiers.pdf>) p. 12: the hinge loss is used for SVM classification.
- handout-05 p. 3: logistic regression "was your first neural network."

**Working:**
- **C:** The standard classification loss, because it is the maximum-likelihood loss. ✅
- **D:** The hinge loss is a classification loss (SVM) and can be used as the output loss of a network. ✅
- **A and B:** These are regression losses. The lecture explicitly calls L2 on classification outputs a historical mistake (handout-02 p. 25). ❌

**Final answer: C, D**

> ⚠️ Strictly, L2 *can* be applied to class probabilities (handout-02 p. 25 says people did this for years), but it is presented as a poor choice. If the quiz means "can technically be used" rather than "is appropriate", it may also accept B.

**Check:** This pairs with Question 10. Each problem type has its own natural losses.

---

## Question 10

What loss can be used in a Neural Network for a **regression** problem?

A. L1 loss · B. L2 loss · C. cross-entropy · D. Hinge

**Lecture material:**
- [handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) p. 7: MSE (L2) is the loss for linear regression. "Other loss functions are possible (e.g. mean absolute difference)", which is the L1 loss.
- [handout-10](<../../Lecture Slides/handout-10-generative-models.pdf>) p. 15: "for continuous input data, you could use a L2 loss … Alternatively you can use cross-entropy if $x$ is discrete."

**Working:**
- **A and B:** Both measure the distance between a continuous prediction and a continuous target. ✅
- **C:** Cross-entropy needs probabilities over discrete classes. ❌
- **D:** The hinge loss needs a class label and a margin. ❌

**Final answer: A, B**

**Check:** In handout-10 p. 15 the same lecturer uses L2 for continuous outputs and cross-entropy only for discrete ones.

---

## Question 11

For a dataset of 64k observations and batch size 32, how many iterations are needed to process one epoch?

A. 1 · B. 32 · C. 2000 · D. 64,000 · E. it depends

**Lecture material:** p. 67: "After one epoch, the gradient descent will have done $n/\text{BatchSize}$ steps."

**Working:** $64{,}000 / 32 = 2000$ iterations.

**Final answer: C (2000)**

**Check:** $2000\times32 = 64{,}000$. Each observation is used exactly once per epoch, which is the definition on p. 67.

---

## Question 12

Assuming the mini-batch fits in GPU memory, it is faster to process an epoch with a batch size of 1024 than with 12. True or False?

A. False · B. True · C. it depends

**Lecture material:**
- p. 66: "The smaller the batch size, the faster a **step** of the gradient descent can be done."
- p. 67: one epoch $= n/\text{BatchSize}$ steps.

**Working:**
1. With batch 12 an epoch needs $n/12$ steps. With batch 1024 it needs only $n/1024$, which is about 85× fewer steps.
2. Each step on a larger batch is slower (p. 66), but not 85× slower. A GPU processes all samples in a batch **in parallel**, so when the batch fits in memory a step on 1024 samples costs only a little more than a step on 12.
3. Fewer, nearly-as-cheap steps means a faster epoch.

**Final answer: B (True)**

> Note: The GPU-parallelism argument is general background rather than something stated in the slides. The slides only give the step-count formula (p. 67) and the per-step cost trend (p. 66).

**Check:** This is about wall-clock time *per epoch*. Whether training *converges* faster is a separate question (Question 19).

---

## Question 13

While training a NN, we obtain the accuracy graph below. Which are reasonable assessments? (multiple)

![Q13 figure](<image q13.png>)

A. There is underfitting. · B. There is some overfitting. · C. Dropout was applied. · D. Pooling was applied. · E. The learning rate is too small. · F. The learning rate is too high.

**Lecture material:**
- [handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) p. 30: "You know that you are underfitting when the error cannot get low enough."
- p. 79 ("Monitoring for overfitting"): good training and poor validation performance is a sign of overfitting. The figure shows a small train/validation gap labelled "little overfitting".
- p. 78 ("Monitoring the learning rate"): a curve that **zig-zags** is labelled "too high". A slow, smooth decrease is labelled "too low".
- p. 76: dropout randomly switches off units **during training only**.

**Working:**
1. **A:** True. Both curves level off at only about 55–60% accuracy, so the model cannot fit even the training data well. ✅
2. **B:** True. After the curves cross, training accuracy stays a few percent above validation, and the gap slowly grows. That is the "little overfitting" pattern on p. 79. ✅
3. **C:** True. In the early epochs, **validation accuracy is higher than training accuracy**. That is a classic sign of dropout: the training accuracy is measured with units randomly switched off (p. 76), which handicaps it, while validation runs with the full network. ✅
4. **F:** True. In later epochs both curves oscillate in a regular zig-zag, which matches the "too high" curve on p. 78. ✅
5. **E:** False. A learning rate that is too small gives a slow, smooth curve, not oscillations. ❌
6. **D:** False. An accuracy curve tells you nothing about whether pooling layers are in the architecture. ❌

**Final answer: A, B, C, F**

> Note: The "validation above training means dropout" reasoning is a standard practitioner rule that follows from p. 76. The slides do not state it as such.

**Check:** Underfitting (A) and slight overfitting (B) can happen at the same time. A model can be too weak overall and still generalise slightly worse than it trains.

---

## Question 14

For a DNN with $n$ units, what is the worst-case complexity of BackPropagation?

A. $\mathcal{O}(\log n)$ · B. $\mathcal{O}(n)$ · C. $\mathcal{O}(n\log n)$ · D. $\mathcal{O}(n^2)$

**Lecture material:** p. 57: "The worst case complexity of backprop is $\mathcal{O}(\text{number\_of\_units}^2)$ but in practice for most network architectures it is $\mathcal{O}(\text{number\_of\_units})$."

**Final answer: D**

**Check:** In the worst case every unit is connected to every other unit, so the chain-rule sum over $\text{Outputs}(i)$ on p. 56 has up to $n$ terms for each of the $n$ units, giving $n^2$.

---

## Question 15

Increasing the number of hidden layers in a DNN will **always** improve the classification accuracy on your test data. True or False?

**Lecture material:**
- p. 61: deeper networks run into vanishing gradients.
- p. 63: gradient descent "is not guaranteed to converge to a global minimum (or even to converge at all)."
- p. 80: "Deeper networks are known to be more efficient but harder to train."
- [handout-01](<../../Lecture Slides/handout-01-linear-regression.pdf>) pp. 32–33: more capacity can lead to overfitting.

**Working:** More layers *tend* to help (Question 6), but they can also cause vanishing gradients, harder optimisation and overfitting. Any of these can lower test accuracy, so "always" is false.

**Final answer: B (False)**

**Check:** The word "always" is the giveaway. The slides only describe a general tendency, never a guarantee.

---

## Question 16

You obtain this graph for the accuracy on the **training set** over the first 50 epochs. Which statements can reasonably be made?

![Q16 figure](<image q16.png>)

A. There is underfitting. · B. There is overfitting. · C. Accuracy in production will be around 92%. · D. Dropout was applied. · E. None of the above.

**Lecture material:** handout-01 p. 33 and handout-05 p. 79: overfitting is judged by comparing training performance with **validation/test** performance. [handout-04](<../../Lecture Slides/handout-04-evaluating-classifier-performance.pdf>) pp. 34–35: a separate test set is needed to estimate performance on unseen data.

**Working:**
- **A:** Training accuracy reaches about 98–100%, so the model is not underfitting. ❌
- **B:** You cannot detect overfitting without a validation curve to compare against. ❌
- **C:** Production accuracy can only be estimated from held-out data, and nothing in the graph shows 92%. ❌
- **D:** A single smooth training curve gives no evidence about dropout. ❌

**Final answer: E (None of the above)**

**Check:** Only training data is plotted. Every option except A would need validation or test information, and A is contradicted by the near-100% accuracy.

---

## Question 17

Gradient Descent is guaranteed to converge to a local minimum. True or False?

**Lecture material:** p. 63: "gradient descent approaches are **not guaranteed** to converge to a global minimum (**or even to converge at all**)." p. 78: with too high a learning rate, the loss can diverge.

**Final answer: B (False)**

**Check:** p. 78 shows a "too high" learning-rate curve where the loss *increases*, so it does not converge at all.

---

## Question 18

Stochastic Gradient Descent is a form of Gradient Descent where the search direction is randomised. True or False?

A. True · B. False · C. it depends

**Lecture material:** p. 65: "In the edge case where the batch size is 1, the gradient is recomputed for each observation … and the process is called Stochastic Gradient Descent (SGD)." p. 66: small batches mean the computed gradient is "a bit noisier".

**Working:** In SGD the direction is still the (negative) **gradient**, computed on a single observation instead of the whole dataset. The randomness comes from *which observation* is used (the samples are shuffled each epoch, p. 67), not from deliberately randomising the search direction. The direction is a noisy estimate of the true gradient, not a random direction.

**Final answer: B (False)**

**Check:** If the direction were truly random, the method would be random search, not gradient descent.

---

## Question 19

Increasing the batch size speeds up the convergence. True or False?

A. True · B. False · C. it depends

**Lecture material:** p. 66: "The smaller the batch size, the faster a step of the gradient descent can be done. Small batch sizes also mean that the computed gradient is a bit 'noisier' … This randomness can help escape from local minimums but can also lead to poor convergence." p. 63: optimisation requires a lot of trial and error.

**Working:** A larger batch gives a more accurate gradient, so each step is better and there are fewer steps per epoch. However, each step is slower, and you lose the noise that helps escape local minima. Whether overall convergence is faster depends on the problem, the hardware and the learning rate.

**Final answer: C (it depends)**

**Check:** p. 66 lists both advantages and disadvantages for small batches, so there is no universal answer.

---

## Question 20

Which methods could be used to simulate more data? (multiple)

A. adding a Dropout layer · B. adding a Gaussian Noise layer · C. increasing the mini-batch size · D. increasing the L2 regularisation

**Lecture material:**
- p. 75 ("Dropout & Layer Noise"): "One cheap way to obtain more data is to take the original observations and add a bit of random noise to the features … One step further is to add noise, during the training phase, to the hidden units themselves."
- p. 76: "Dropout … can be also seen as adding a (multiplicative) noise to the layers."

**Working:**
- **B:** A Gaussian noise layer adds random noise to the features or units, which is the "cheap way to obtain more data" on p. 75. ✅
- **A:** Dropout is multiplicative noise on the layers (p. 76), the "one step further" version of the same idea. ✅
- **C:** The batch size only changes how the gradient is averaged, not what data the model sees. ❌
- **D:** L2 regularisation penalises large weights (p. 73). It does reduce overfitting, but it does not create new samples. ❌

**Final answer: A, B**

**Check:** Both A and B are presented on pp. 75–76 under one heading as noise-injection substitutes for more data.
