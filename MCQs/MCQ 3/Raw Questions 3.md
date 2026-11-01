q1. What datasets are best suited for kernel methods?

Option A
datasets with large \(n\) and large \(p\)

Option B
datasets with large \(n\) and small \(p\)

Option C
datasets with small \(n\) and large \(p\)

Option D
datasets with small \(n\) and small \(p\)

Option E
size doesn't matter

Question 2
When are Machine Learning methods usually less effective? (select all correct answers)

Option A
When the data is linearly separable.

Option B
When the observations are linearly dependent.

Option C
When the classes are linearly dependent.

Option D
When the classes do mix (ie. point clouds for both classes overlap).

q3
Suppose you are using SVM with linear kernel of polynomial degree 2. You find that the corresponding training and testing accuracy is 100% (ie. all the observations in the dataset are correctly classified). You now increase the polynomial degree \(d\) of this kernel.

What would you think will happen? (select all correct answers)

Option A
increasing \(d\) may underfit the data

Option B
increasing \(d\) may overfit the data

Option C
nothing will happen because the model is already 100% accurate on the training set

Option D
nothing will happen because the model is already 100% accurate on the test set

Option E
none of the above

q4
Which of these following statements about kernel functions are true? (select all correct answers)

Option A
The kernel function maps low dimensional data into a high dimensional space.

Option B
The kernel function is a similarity function

Option C
The computational complexity of the kernel function is independent of the corresponding mapped feature space.

Option D
Kernel functions are specific to SVM.

q5
Which of the following facts about SVM and the kernel trick are true (multiple choices possible):

Option A
The kernel trick can be used for both SVM and Logistic Regression.

Option B
The Loss for both Linear SVM and Logitstic Regression are the same.

Option C
Linear SVM is a priori more performant than Logistic Regression

Question 6
Consider the binary class dataset below (with 2 features \((x_1, x_2)\) and 2 classes (cross and circle). Which of the following classification techniques will be suitable for this dataset? (choose all that can give good results, using the model straight as, without any prior feature recombination).



Option A
Decision Tree

Option B
Logistic Regression

Option C
Random Forest

Option D
SVM with RBF kernel


q7
Which of the following binary classifiers produced the following decision boundary map?



Option A
3-nearest neighbours

Option B
5-nearest neighbours

Option C
1-nearest neighbours

Option D
Decision Tree

Option E
Adaboost or Random Forest

Option F
SVM with RBF kernel

Question 8

Consider the binary class dataset below (with 2 features \((x_1, x_2)\) and 2 classes (cross and circle). Which classifier is least likely to overfit? (mark one answer)



Option A
Logistic Regression

Option B
SVM with RBF kernel

Option C
Decision Tree

Option D
\(k\)-nearest neighbours

Option E
Random Forest

Option F
Least Squares

q9
What are the effects of increasing \(k\) in \(k\)-Nearest Neighbours? (select all answers that are true in general)

Option A
increase the area in the boundary decision where the prediction is \(0<p<1\)

Option B
increase the computational time when evaluating the prediction

Option C
increase the overall accuracy of the predictions.

Option D
decrease the overall accuracy of the predictions.

Select up to 4 options

Question 10

Which of these statements about Decision Tress are true? (select all answers that are correct)

Option A
ML methods based on Decision Trees (eg. AdapBoost) only predict the most likely class, not the probability to belong to a class.

Option B
Decisions Trees are computationally more efficient than kernel SVMs.

Option C
Decisions Trees take their decisions based on binary decisions such as \({\bf x}^{\top}{\bf w} > 0\).

Option D
Decisions Trees are robust to a rotation of the feature space.


