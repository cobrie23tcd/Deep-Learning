Question 1
1
 Point
Question 1
In a Neural Network, what is a unit? (only one answer)

Option A
a linear combination of inputs followed by an activation function

Option B
a differentiable function

Option C
the loss function

Option D
a set of neurons

Question 2
1
 Point
Question 2
Which of the following statements are true? (select all answers that are correct)

Option A
In the LIF neuron model, LIF stands for Leaky Intensity-and-Fire.

Option B
The relationship between the input intensity and the output firing rate of neurons resembles that of an activation function.

Option C
Both the mathematical model of artifical neurons and their training method have been inspired by biology.

Option D
The membrane potential drops in the absence of stimulus.

Select up to 4 options

Question 3
1
 Point
Question 3
The Universal Approximation Theorem states that

Option A
any continuous function can be arbitrarily well approximated by a deep neural network, given enough linear layers.

Option B
any continuous function can be arbitrarily well approximated by a deep neural network, given enough layers.

Option C
any continuous function can be arbitrarily well approximated by a single hidden layer neural network with a linear neuron output, given enough neurons.

Question 4
1
 Point
Question 4
Consider the network of operations:

\[ e=(a-1)^2+(b-0)^2,\; b=\cos(d),\; a=\cos(c) \]

Which of the following statements is true?

Option A
BackPropagation has to compute \(\frac{\partial e}{\partial a}\) before \(\frac{\partial e}{\partial b}\)

Option B
BackPropagation has to compute \(\frac{\partial e}{\partial a}\) after \(\frac{\partial e}{\partial b}\)

Option C
BackPropagation can compute \(\frac{\partial e}{\partial a}\) and \(\frac{\partial e}{\partial b}\) in any order.

Option D
none of the above.

Question 5
1
 Point
Question 5
Consider the network of operations:

\[ a=b\cos(c),\; b=c+2,\; e=a+b+c \]

Which of the following statements is true?

Option A
BackPropagation will compute \(\frac{\partial e}{\partial a}\) before \(\frac{\partial e}{\partial b}\)

Option B
BackPropagation will compute \(\frac{\partial e}{\partial a}\) after \(\frac{\partial e}{\partial b}\)

Option C
BackPropagation will compute \(\frac{\partial e}{\partial a}\) at the same time as \(\frac{\partial e}{\partial b}\)

Option D
BackPropagation can compute \(\frac{\partial e}{\partial a}\) and \(\frac{\partial e}{\partial b}\) independently

Question 6
1
 Point
Question 6
Deeper Neural Networks generalise better than shallower neural networks.

Option A
True

Option B
False



Question 7
1
 Point
Question 7
Which of the following statements about the problem of vanishing gradients (VG) are true? (select all correct answers)

Option A
VG often happens when training deep neural networks.

Option B
VG happens when the values of the units get stuck near zero.

Option C
VG happens when the values of the gradient of the units with respect to their inputs get stuck near zero.

Select up to 3 options

Question 8
1
 Point
Question 8
Which of the following activation functions is best suited to avoid the problem of vanishing gradients? (select one)

Option A
sigmoid

Option B
tanh

Option C
linear (\(x \mapsto x\))

Option D
ReLU

Continu

Question 9
1
 Point
Question 9
What loss can be used in a Neural Network for a classification problem?

Option A
L1 loss

Option B
L2 loss

Option C
cross-entropy

Option D
Hinge

Select up to 4 options

Question 10
Question 10
1
 Point
Question 10
What loss can be used in a Neural Network for a regression problem?

Option A
L1 loss

Option B
L2 loss

Option C
cross-entropy

Option D
Hinge

Select up to 4 options

Question 11
Question 11
1
 Point
Question 11
For dataset of 64k observations and batch size of 32, how many iterations are needed to process an epoch?

Option A
1

Option B
32

Option C
2000

Option D
64,000

Option E
it depends

Question 12
Question 12
1
 Point
Question 12
Assuming that the mini-batch fits in the GPU memory, it is faster to process an epoch with a batch size of 1024 than a batch size of 12.

Option A
False

Option B
True

Option C
it depends

Question 13
Question 13
1
 Point
Question 13
While training a neural net, we obtain an accuracy graph similar to the one below.



Which of the following statements are reasonable assessment of the situation. (multiple choices possible)

Option A
There is underfitting.

Option B
There some overfitting

Option C
Dropout was applied.

Option D
Pooling was applied.

Option E
The learning rate is too small.

Option F
The learning rate is too high.

Select up to 6 options

Question 14
1
 Point
Question 14
For a DNN with \(n\) units, what is the worst case complexity of BackPropagation?

Option A
\(\mathcal{O}(\log(n))\)

Option B
\(\mathcal{O}(n)\)

Option C
\(\mathcal{O}(n\log(n))\)

Option D
\(\mathcal{O}(n^2)\)

Question 15
1
 Point
Question 15
Increasing the number of hidden layers in a Deep Neural Network will always improve the classification accuracy on your test data.

Option A
True

Option B
False

Question 16
1
 Point
Question 16
You obtain the following graph for the accuracy on the training set (over the first 50 epochs).



Which of the following statements can be reasonably made from this graph. (multiple choices possible)

Option A
There is underfitting.

Option B
There is overfitting

Option C
Accuracy in production will be around 92%

Option D
Dropout was applied.

Option E
None of the above

Question 17
1
 Point
Question 17
Gradient Descent is guaranteed to converge to a local minimum.

Option A
True

Option B
False

Question 18
1
 Point
Question 18
Stochastic Gradient Descent is a form of Gradient Descent where the search direction is randomised.

Option A
True

Option B
False

Option C
it depends

Question 19
1
 Point
Question 19
Increasing the batch size speeds up the convergence.

Option A
True

Option B
False

Option C
it depends

Question 20
1
 Point
Question 20
Which of the following methods could be used to simulate more data? (multiple choices possible)

Option A
adding a Dropout layer

Option B
adding a Gaussian Noise layer

Option C
increasing the mini-batch size

Option D
increasing the L2 regularisation