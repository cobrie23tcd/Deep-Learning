Question 1
If vectors \({\bf w}\) and \({\bf x}\) are of dimensions \(3 \times 1\), which of the following statements are correct (mark all correct statements)

Option A
\({\bf w}^{\top}{\bf x} = {\bf x}^{\top}{\bf w}\)

Selected
Option B
\({\bf w}{\bf x}^{\top} = {\bf x}{\bf w}^{\top}\)

Option C 
size of \({\bf w}^{\top}{\bf x}\) is \(3 \times 3\)


Question 2
If vector \({\bf w}\) is of dimension \(3 \times 1\) and matrix \({\bf A}\) of dimension \(5 \times 3\), then what is the dimension of \(\left({\bf w}^{\top}{\bf A}^{\top}{\bf A}{\bf w}\right)^{\top}\)?

Option A
\({\tt 5}\times {\tt 5}\)

Option B
\({\tt 3}\times {\tt 3}\)

Option C
\({\tt 3}\times {\tt 1}\)

Option D
\({\tt 1}\times {\tt 1}\)

Option E
\({\tt 1}\times {\tt 5}\)

Option F
\({\tt 1}\times {\tt 3}\)

Option G
incorrect dimensions for matrix multiplication

Question 3
If vector \({\bf w}\) is of dimension \(3 \times 1\) and matrix \({\bf A}\) of dimension \(5 \times 3\), then what is the dimension of \({\bf A}{\bf w}{\bf w}^{\top}{\bf A}^{\top}\)?

Option A
\({\tt 5}\times {\tt 5}\)

Option B
\({\tt 3}\times {\tt 3}\)

Option C
\({\tt 3}\times {\tt 1}\)

Option D
\({\tt 1}\times {\tt 1}\)

Option E
\({\tt 1}\times {\tt 5}\)

Option F
\({\tt 1}\times {\tt 3}\)

Option G
incorrect dimensions for matrix multiplication

Question 4
Consider the following loss function:



\[ E({\bf w}) = \frac{1}{1 + {\bf w}^{\top}{\bf x} + {\bf w}^{\top}{\bf w}} \]What is the expression of its gradient \(\frac{\partial E}{\partial {\bf w}}\)?

Option A
\(-\frac{ {\bf x} + 2 {\bf w} }{\left(1 + {\bf w}^{\top}{\bf x} + {\bf w}^{\top}{\bf w}\right)^2}\)

Option B
\(-\frac{ {\bf x}^{\top} + 2 {\bf w}^{\top}}{\left(1 + {\bf w}^{\top}{\bf x} + {\bf w}^{\top}{\bf w}\right)^2}\)

Option C
\(-\frac{ {\bf w} }{\left(1 + {\bf w}^{\top}{\bf x} + {\bf w}^{\top}{\bf w}\right)^2}\)

Option D
\(-\frac{ {\bf x} }{\left(1 + {\bf w}^{\top}{\bf x} + {\bf w}^{\top}{\bf w}\right)^2}\)

Question 5
Which of the following models with input \(x_1,x_2\), parameters \(w_1,w_2\) and noise \(\epsilon\sim \mathcal{N}(0,\sigma^2)\), are linear in the parameters and follow the Least Squares assumptions? (mark all models that are linear):

Option A
\(y = \log(x_1)w_1 + \log(x_2+1)(w_2+1) + \epsilon\)

Option B
\(y = \sin(x_1 w_1 + w_2) + \epsilon\)

Option C
\(y = {w_1}x_1^2 + {w_2}x_2^2 + 3 \epsilon\)

Option D
\(y = {w_1}^2x_1 + {w_2}^2x_1 + 3 \epsilon\)

Question 6
Which of the following models with input \(x_1,x_2\), parameters \(w_1,w_2\) and noise \(\epsilon\sim \mathcal{N}(0,\sigma^2)\), are linear in the parameters and follow the Least Squares assumptions? (mark all models that are linear):

Option A
\(y = {w_1}x_1 + {w_2}x_2 + \epsilon\)

Option B
\(y = {w_1}x_1 + {w_2}x_1^2 + 3{w_1}x_2 + 2{w_2}x_1^2x_2^2  + \epsilon\)

Option C
\(y = {w_1}x_1 + {w_2}x_2 + (x_1 + x_2) \epsilon\)

Option D
\(y = x_1 w_1 + x_1 w_1^2 + x_2 w_1^3 + w_2 + \epsilon\)

Question 7

Which of the following models with input \(x_1,x_2\), parameters \(w_1,w_2\) and noise \(\epsilon\sim \mathcal{N}(0,\sigma^2)\), are linear in the parameters and follow the Least Squares assumptions? (mark all models that are linear):

Option A
\(y = w_1 x_1^2 + x_2 w_2^2 + \epsilon\)

Option B
\(y = {w_1}{w_2} + {x_1}{x_2} + \epsilon\)

Option C
\(y = \left( w_1 x_1 + x_2\right)/\left( w_2 x_2 + x_3\right) + \epsilon\)

Option D
\(y = {x_1}{x_1} + w_1 + \exp(-0.7) \epsilon\)

Question 8
We are trying to fit a polynomial model to a dataset using Least Squares. We have a very large training set but the estimated model predictions are quite poor? Which strategy/strategies could help us improve the predictions?

Option A
decreasing the size of the training set

Option B
increasing the size of the training set

Option C
increasing the size of the test set

Option D
descreasing the size of the test set

Option E
increasing the Tikhonov regularisation

Option F
increasing the polynomial order of the model

Question 9
We are trying to fit a 3rd degree polynomial to a dataset using Least Squares. We know that the underlying model is indeed a 3rd degree polynomial and we are trying to estimate the polynomial coefficients. However, we are having issues with overfitting. Which strategy/strategies will give us the best chance of finding the best estimate of the true polynomial coefficients?

Option A
decreasing the size of the training set

Option B
increasing the size of the training set

Option C
increasing the size of the test set

Option D
descreasing the size of the test set

Option E
increasing the Tikhonov regularisation

Option F
increasing the polynomial order of the model

Question 10
Which of the following facts are true (mark all statements that are true):

Option A
Regularisation biases the parameters towards the value 0.

Option B
Regularisation is usually used to reduce underfitting.

Option C
Regularisation is usually used to reduce overfitting.

Option D
Tikhonov Regularisation does add significant numerical complexity to Least Squares.

Question 11
Given a loss function \(E({\bf w})\), we also want to want to have \(\sum_{j=0}^p w_j b_j\) to be close to zero. What new loss function can achieve this?

Option A
\(E'({\bf w}) = E({\bf w}) + \lambda \left({\bf b}-{\bf w}\right)^{\top}\left({\bf b}-{\bf w}\right)\)

Option B
\(E'({\bf w}) = E({\bf w}) + \lambda {\bf w}^{\top}{\bf b}\)

Option C
\(E'({\bf w}) = E({\bf w}) + \lambda {\bf w}^{\top}{\bf b}{\bf b}^{\top}{\bf w}\)

Option D
\(E'({\bf w}) = E({\bf w}) + \lambda {\bf b}^{\top}{\bf b}\)

Q12
Consider the Least Square model prediction in the Figure below.



Which of the following statements are correct? (mark all correct)

Option A
increasing the size of the test set will improve the overall prediction error.

Option B
increasing the size of the training set will improve the overall prediction error.

Option C
increasing the Tikhonov regularisation will improve the overall prediction error.

Option D
decreasing the Tikhonov regularisation will improve the overall prediction error.

Option E
this is a case of overfitting

Option F
this is a case of underfitting

Question 13

We have a dataset and we want to fit a polynomial model of order 7 using Least Squares.



What are (is) the possible reason(s) why the estimated prediction model seems so poor? (mark all correct answers)

Option A
The dataset is too small.

Option B
We should use regularisation.

Option C
The error is not independent and Gaussian.

Option D
The model order is too high.