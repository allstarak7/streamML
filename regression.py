from feature_selection import FeatureSelection
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


class Regression():
    def linear_regression():
        # perform the feature selection
        new_features, new_dataset = FeatureSelection.select_features()

        # perform the regression on the new dataset obtained from feature selection

        # print(new_features)
        # print(new_dataset)

        # features for up to 2021, every column except last
        X = new_dataset[new_dataset[:, 0] < 2022][:, :-1]
        # target variable, last column
        y = new_dataset[new_dataset[:, 0] < 2022][:, -1]

        X_test = new_dataset[new_dataset[:, 0] == 2022][:, :-1]
        y_test_actual = new_dataset[new_dataset[:, 0] == 2022][:, -1]

        model = LinearRegression()
        model.fit(X, y)

        y_test_predicted = model.predict(X_test)
        mse = mean_squared_error(y_test_actual, y_test_predicted)

        return mse
