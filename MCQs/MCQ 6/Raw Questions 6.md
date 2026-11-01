Question 1
1
 Point
Question 1
A convolutional neural network (CNN) has three consecutive \(5 \times 5\) convolutional layers, each with a stride of 1 and no pooling. What is the size of the area of the input image, known as the receptive field, which is used in the computation of a single output unit (pixel) in the third convolutional layer?

Option A
\({\tt 5}\times {\tt 5}\)

Option B
\({\tt 7}\times {\tt 7}\)

Option C
\({\tt 9}\times {\tt 9}\)

Option D
\({\tt 13}\times {\tt 13}\)

Option E
\({\tt 15}\times {\tt 15}\)

Option F
\({\tt 125}\times {\tt 125}\)

Question 2
1
 Point
Question 2
A convolutional neural network (CNN) has three consecutive \(3 \times 3\) convolutional layers, each with a stride of 1 and no pooling. What is the size of the area of the input image, known as the receptive field, which is used in the computation of a single output unit (pixel) in the third convolutional layer?

Option A
\({\tt 3}\times {\tt 3}\)

Option B
\({\tt 4}\times {\tt 4}\)

Option C
\({\tt 5}\times {\tt 5}\)

Option D
\({\tt 7}\times {\tt 7}\)

Option E
\({\tt 9}\times {\tt 9}\)

Question 3
Question 3
1
 Point
Question 3
Is a network made of convolutional neural layers a feed forward neural network?

Option A
False

Option B
True

Question 4
1
 Point
Question 4
Based on the following code, what is the shape of the output?

conv = nn.Conv2d(in_channels=5, out_channels=4, kernel_size=5,
                 stride=2, padding="valid")
x = torch.randn(5, 22, 8)
x = conv(x)
Option A
\(4\times 8 \times 1\)

Option B
\(4\times 9 \times 2\)

Option C
\(4\times 10 \times 3\)

Option D
\(4\times 18 \times 4\)

Option E
\(4\times 20 \times 6\)

Option F
\(4\times 22 \times 8\)

Question 5
Question 5
1
 Point
Question 5
Based on the same code as in previous question, what is the number of trainable parameters of the model?

conv = nn.Conv2d(in_channels=5, out_channels=4, kernel_size=5,
                 stride=2, padding="valid")
x = torch.randn(5, 22, 8)
x = conv(x)
Option A
25

Option B
29

Option C
125

Option D
129

Option E
500

Option F
504





Question 6
Question 6
1
 Point
Question 6
For which purpose a Convolutional Neural Network is used? (select all possible answers)

Option A
It is a multi purpose alghorithm that can be used for Unsupervised Learning.

Option B
Mainly to process and analyse financial models, predicting future trends.

Option C
Mainly to process and analyse digital images, with some success cases involving processing voice and natural language.

Option D
It is a multi purpose alghorithm that can be used for Supervised Learning.

Question 7
Question 7
1
 Point
Question 7
Which answer explains best Flattening?

Option A
It transforms the input dataset into a tensor.

Option B
It is the last step of CNN.

Option C
It transforms the input image into a vector

Option D
It transforms a tensor into a vector.

Question 8
Question 8
1
 Point
Question 8
What computes the average of the elements in blocks of feature map covered by the filter?

Option A
Stride

Option B
Max pooling

Option C
Average pooling

Option D
Global pooling

Option E
none of these

Question 9
Question 9
1
 Point
Question 9
Can softmax be used in a Convolutional Neural Network?

Option A
True

Option B
False

Question 10
Question 10
1
 Point
Question 10
Where does weight sharing occurs?

Option A
Weight sharing occurs in Convolutional Layers

Option B
Weight sharing occurs in Fully Connected Layers

Option C
Weight sharing occurs in MaxPooling

Question 11
Question 11
1
 Point
Question 11
In what year was LeNet-5, the network that pioneered the use of convolutional layers in neural nets, published? (one answer is correct)

Option A
1986

Option B
1998

Option C
2012

Option D
2014

