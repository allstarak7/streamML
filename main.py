from neuralNetwork import NeuralNetwork
from regression import Regression


def main():
    # mse = Regression.linear_regression()
    #Regression.logistic_regression()
    nn = NeuralNetwork()
    nn.mlp_regressor()
    nn.make_predictions()
    # print('mse:', mse)


if __name__ == "__main__":
    main()
