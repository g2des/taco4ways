# Intro to ANN

## Perceptron and more

- McCulloch and Pitt presented simplified computational model of biological neuron.
- May perform complex computations using propositional logic

### Perceptron
- a form of threshold logic unit
- performs weighted sum of the inputs and applies a step funciton to this sum and outputs the result
- the model learns using hebbian learning $\hat{w} = w_{i} + \eta (\hat{y}- y_{i}) x_{i}
- learns a linear boundary
- produces result based on a hard threshold, hence logistic regression is more preferred
- can't classify XOR output, problem solved by MLP

## MLP
- feed forward networks with dense layers
- learns using backprop
- has non linear equations to learn more complex boundaries
- cannot use linear functions as activation functions as $f(g(x))$ will still be linear if $f$ and $g$ are linear fuctions
- weights and biases are initialzed randomly or with a initialization method
- symmetric weights will be affected similarly by backprop thus still act as having single neuron

## Regression MLP
- requires one output neuron per output dimension
- use of activation functions
  - relu if you want output to be positive
  - logistic or tanh if you want output to be in range
- mean squared error normally, absolute error if many outliers, or huber loss

## Classification MLP
- binary classification, single o/p neuron with logistic activation
- multilable classification, one o/p neuron per label with logistic activation
- multiclass classification, one o/p neuron per class with softmax activation

## Challenges of model tuning : TODO

## Keras
- Building a classification model and training it on fashion mnist database
- Building a regression model and training it on california housing price database
- Use of functional API to build wide deep network/ network with auxilary outputs
- callbacks
- using tensorboard from saving history


## References
- [wide and deep network](https://arxiv.org/pdf/1606.07792.pdf)
- [Backprop]
- 