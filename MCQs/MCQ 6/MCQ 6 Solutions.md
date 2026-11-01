# MCQ 6 — Convolutional Neural Networks: Worked Solutions

**Main source:** [handout-06-convolutional-neural-networks.pdf](<../../Lecture Slides/handout-06-convolutional-neural-networks.pdf>)

> Page references are **PDF page numbers**, as shown in a PDF viewer. The slide number printed in the corner differs because of animation builds. For example, PDF p. 25 is printed slide 15.

## Answer summary

| Q | Answer |
|---|--------|
| 1 | D ($13\times13$) |
| 2 | D ($7\times7$) |
| 3 | B (True) |
| 4 | B ($4\times9\times2$) |
| 5 | F (504) |
| 6 | A, C, D |
| 7 | D |
| 8 | C |
| 9 | A (True) |
| 10 | A |
| 11 | B (1998) |

---

## Question 1

A CNN has three consecutive $5\times5$ convolutional layers, each with stride 1 and no pooling. What is the receptive field of a single output pixel of the third layer?

A. $5\times5$ · B. $7\times7$ · C. $9\times9$ · D. $13\times13$ · E. $15\times15$ · F. $125\times125$

**Lecture material:** p. 8: "In convolutional layers, the units in the next layer are only connected to their neighbours in the input layer … the neighbourhood is defined as a $5\times5$ window." p. 10: $\text{logit}_{i,j} = \sum_{a=-h_1}^{h_1}\sum_{b=-h_2}^{h_2}\dots\,u_{a+i,\,b+j}$, so each output depends on input pixels within $\pm h$ of its position. Here $h = (5-1)/2 = 2$. The term "receptive field" itself only appears on p. 48. The layer-by-layer growth rule below follows from p. 10 and is not stated on the slides.

**Working:**
Each $5\times5$ layer with stride 1 widens the dependency by $h=2$ pixels on each side, so the width grows by $k-1 = 4$:

| After layer | Receptive field |
|---|---|
| 1 | $5$ |
| 2 | $5 + 4 = 9$ |
| 3 | $9 + 4 = 13$ |

In general: $\text{RF} = 1 + L(k-1) = 1 + 3\times4 = 13$.

**Final answer: D ($13\times13$)**

**Check:**
- **Numerical check:** I verified this in PyTorch by back-propagating from a single output pixel through three `Conv2d(1,1,5)` layers. Exactly 13 input rows and columns get a non-zero gradient.
- **Option F:** $125 = 5^3$ is a trap from multiplying the kernel sizes together.

---

## Question 2

Same as Question 1, but with three $3\times3$ layers. What is the receptive field?

A. $3\times3$ · B. $4\times4$ · C. $5\times5$ · D. $7\times7$ · E. $9\times9$

**Lecture material:** pp. 8 and 10, as in Question 1, with $h = 1$.

**Working:** Each layer adds $k-1 = 2$:

| After layer | Receptive field |
|---|---|
| 1 | $3$ |
| 2 | $5$ |
| 3 | $7$ |

$\text{RF} = 1 + 3\times2 = 7$.

**Final answer: D ($7\times7$)**

**Check:**
- **Numerical check:** The same PyTorch gradient check gives exactly 7.
- **Option E:** $9 = 3\times3$ is the trap from multiplying the kernel sizes.

---

## Question 3

Is a network made of convolutional layers a feedforward neural network?

A. False · B. True

**Lecture material:**
- [handout-05](<../../Lecture Slides/handout-05-deep-feedforward-networks.pdf>) p. 6: "Neural Networks based on directed acyclic graphs are called **FeedForward Neural Networks**."
- handout-06 p. 8: in conv layers, each unit is connected to its neighbourhood in the *previous* layer only.
- handout-06 p. 40: a typical convnet goes conv, then pool, then FC, then softmax.

**Working:** A conv layer is just a dense layer with most connections removed and the remaining weights shared (pp. 8–9). Information still flows in one direction only, from input to output, with no cycles. The computation graph is therefore a DAG, which is the definition of a feedforward network.

**Final answer: B (True)**

**Check:** Back-propagation works on convnets exactly as in handout-05. The filter-visualisation method on p. 50 back-propagates through VGG16, which requires an acyclic graph.

---

## Question 4

```python
conv = nn.Conv2d(in_channels=5, out_channels=4, kernel_size=5,
                 stride=2, padding="valid")
x = torch.randn(5, 22, 8)
x = conv(x)
```

What is the shape of the output?

A. $4\times8\times1$ · B. $4\times9\times2$ · C. $4\times10\times3$ · D. $4\times18\times4$ · E. $4\times20\times6$ · F. $4\times22\times8$

**Lecture material:**
- p. 22: `padding='valid'` means "we don't compute the pixels that need neighbours outside of the image domain", so the output is cropped.
- p. 25: PyTorch's NCHW layout. A $5\times5$ valid convolution loses 2 pixels on each side, so $592\times443$ becomes $588\times439$.
- pp. 29–30: stride $s$ keeps only every $s$-th pixel. Worked example: a $16\times16$ input with a $3\times3$ kernel and stride 2 gives $7\times7$.

**Working:**
1. **Read the input shape.** `x` has 3 dimensions, so PyTorch treats it as an *unbatched* $C\times H\times W$ tensor: $C=5$, $H=22$, $W=8$. $C=5$ matches `in_channels=5`.
2. **Valid output positions.** With valid padding a $k=5$ kernel fits at $H-k+1$ positions in each direction:
   - Height: $22-5+1 = 18$
   - Width: $8-5+1 = 4$
3. **Apply the stride.** Stride 2 keeps every second one of those positions, i.e. $\lfloor (N-k)/s \rfloor + 1$:
   - Height: $\lfloor 17/2\rfloor + 1 = 8 + 1 = 9$
   - Width: $\lfloor 3/2\rfloor + 1 = 1 + 1 = 2$
4. **Channels.** The number of output channels is `out_channels = 4`.

Output shape $= 4\times9\times2$.

**Final answer: B ($4\times9\times2$)**

**Check:**
- **Slide example:** The same formula gives the lecture's result on p. 30: $\lfloor(16-3)/2\rfloor+1 = 7$ ✓.
- **Run in PyTorch:** Running the exact code prints `torch.Size([4, 9, 2])` ✓.
- **Distractors:** Option D, $4\times18\times4$, is what you get if you forget the stride.

---

## Question 5

Same code. What is the number of trainable parameters?

A. 25 · B. 29 · C. 125 · D. 129 · E. 500 · F. 504

**Lecture material:**
- p. 10: each output channel $k$ has its own weights $w_{a,b,c,k}$ over a $(2h_1+1)\times(2h_2+1)\times h_3$ window across **all input channels**, plus a bias $w_{0,k}$.
- p. 25: "This convolution layer is defined by $3\times6\times5\times5 = 450$ weights", calculated as in_channels × out_channels × kernel area.

**Working:**
- Weights: $\text{in}\times\text{out}\times k\times k = 5\times4\times5\times5 = 500$
- Biases: one per output channel, $w_{0,k}$ on p. 10, so 4. `nn.Conv2d` has `bias=True` by default.
- Total: $500 + 4 = 504$

**Final answer: F (504)**

**Check:**
- **Run in PyTorch:** `sum(p.numel() for p in conv.parameters())` returns **504** ✓.
- **Stride and padding:** These do not change the parameter count. They only affect the output shape.
- **Distractors:**
  - Option E (500) is the weight count without biases, the same convention as the 450 on p. 25.
  - Options A–D come from forgetting the channels.

---

## Question 6

For which purpose is a Convolutional Neural Network used? (select all)

A. A multi-purpose algorithm that can be used for Unsupervised Learning. · B. Mainly to process and analyse financial models, predicting future trends. · C. Mainly to process and analyse digital images, with some success in voice and natural language. · D. A multi-purpose algorithm that can be used for Supervised Learning.

**Lecture material:**
- handout-06 p. 2: "Convolutional Neural Networks … are a type of neural net **especially used for processing image data**."
- handout-06 pp. 40–44: classification networks (LeNet, AlexNet, VGG) trained on labelled data, which is supervised learning.
- [handout-10](<../../Lecture Slides/handout-10-generative-models.pdf>) p. 3: generative modelling "is a form of **unsupervised** learning".
- handout-10 p. 15: "The autoencoder architecture applies to **any kind of neural net**", which includes convolutional encoders and decoders.
- handout-06 p. 37: transposed convolutions for up-sampling, which are typically used in decoders.

**Working:**
- **C:** True, images are the main use (p. 2). ✅
- **D:** True. Image classification with labels is supervised (pp. 40–44). ✅
- **A:** True. Convnets can be the encoder or decoder of an autoencoder or generative model, which is unsupervised (handout-10 pp. 3 and 15). ✅
- **B:** False. Financial time-series forecasting is not the *main* purpose of CNNs. ❌

**Final answer: A, C, D**

> Note: The slides do not show a "convolutional autoencoder" explicitly. Option A follows from handout-10 p. 15, which says the autoencoder architecture applies to any kind of neural net.

**Check:** "Mainly … images" (C) and "mainly … financial" (B) cannot both be true, and p. 2 settles it in favour of C.

---

## Question 7

Which answer best explains Flattening?

A. It transforms the input dataset into a tensor. · B. It is the last step of a CNN. · C. It transforms the input image into a vector. · D. It transforms a tensor into a vector.

**Lecture material:**
- p. 40: "At some point the picture is so small (eg. $7\times7$) … You can then connect it to fully connected layers."
- p. 45: in the VGG16 code, `x = torch.flatten(x, 1)` turns the $512\times7\times7$ feature tensor into a vector of length $512\cdot7\cdot7 = 25088$ for `nn.Linear(512 * 7 * 7, 4096)`.

**Working:**
- **D:** Flattening reshapes a multi-dimensional tensor (channels × height × width) into a 1-D vector so it can feed a dense layer. ✅
- **C:** Too narrow. Flattening is usually applied to *feature maps* deep inside the network, not to the input image. ❌
- **B:** False. The last step is the classifier (FC layers and softmax, p. 40), which comes after flattening. ❌
- **A:** False. The data is already a tensor (p. 25). ❌

**Final answer: D**

**Check:** In the VGG16 code, flatten sits between the conv/pool feature extractor and the fully connected classifier, operating on the $512\times7\times7$ feature tensor.

---

## Question 8

What computes the **average** of the elements in the blocks of a feature map covered by the filter?

A. Stride · B. Max pooling · C. Average pooling · D. Global pooling · E. none of these

**Lecture material:** p. 33: "The Pooling layer operates a sub-sampling of the picture. Different sub-sampling strategies are possible: **average pooling**, max pooling, stochastic pooling." p. 34: max pooling keeps the *maximum* of each block. pp. 29–32: stride skips pixels and does no averaging.

**Working:** Average pooling replaces each block with its mean. Max pooling keeps the maximum, and stride just skips positions. Global pooling averages (or takes the max over) the *entire* feature map at once, not filter-sized blocks.

**Final answer: C**

**Check:** On the $4\times4$ example on p. 34, average pooling of the top-left block $\{0,10,4,3\}$ gives $17/4 = 4.25$, whereas max pooling gives $10$ (as shown on the slide).

---

## Question 9

Can softmax be used in a Convolutional Neural Network?

A. True · B. False

**Lecture material:** p. 40: "You can then connect it to fully connected layers and **terminate by a last softmax layer for classification**." [handout-02](<../../Lecture Slides/handout-02-logistic-regression.pdf>) p. 35 defines softmax.

**Final answer: A (True)**

**Check:** LeNet, AlexNet and VGG (pp. 42–44) all end in a multi-class output. VGG's final `nn.Linear(4096, num_classes)` (p. 45) produces the logits that softmax turns into class probabilities.

---

## Question 10

Where does weight sharing occur?

A. In Convolutional Layers · B. In Fully Connected Layers · C. In MaxPooling

**Lecture material:** p. 9: "Moreover the weights are **shared across all the pixels**." p. 10: "in convnets, the weights are associated to the relative positions of the neighbours and shared across all pixel locations."

**Working:**
- **A:** The same filter weights are applied at every pixel position. ✅
- **B:** In fully connected layers every connection has its own weight (p. 4). ❌
- **C:** Max pooling has no trainable weights at all. ❌

**Final answer: A**

**Check:** Weight sharing is why a conv layer has only $3\times6\times5\times5 = 450$ weights (p. 25), regardless of image size. A dense layer would need up to $(3\times H\times W)^2$ weights (p. 5).

---

## Question 11

In what year was LeNet-5, the network that pioneered the use of convolutional layers, published?

A. 1986 · B. 1998 · C. 2012 · D. 2014

**Lecture material:** p. 2: "Convnets gained popularity with LeNet-5, a pioneering 7-level convolutional network by LeCun et al. (**1998**)." p. 42: "LeNet-5 (LeCun, 1998). The network pioneered the use of convolutional layers in neural nets."

**Final answer: B (1998)**

**Check:** The distractors are other dates from the course:
- 1986 is back-propagation by Rumelhart, Hinton and Williams ([handout-05](<../../Lecture Slides/handout-05-deep-feedforward-networks.pdf>) p. 34).
- 2012 is AlexNet (p. 43).
- 2014 is VGG's ILSVRC entry (p. 44).
