from feature_selection import FeatureSelection
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
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
        print(y_test_predicted)
        mse = mean_squared_error(y_test_actual, y_test_predicted)

        return y_test_predicted 

    def logistic_regression():
        dataframe = FeatureSelection.create_mvp_column()

        mvp_column = dataframe['was_mvp']
        dataframe.drop('was_mvp', axis=1)

        # Create modeling and test datasets
        test_data = dataframe[dataframe['season'] > 2017]
        players = test_data['player']
        test_data.drop(['player', 'pos', 'team_id'], axis=1, inplace=True)
        predict_data = dataframe[dataframe['season'] <= 2017]
        predict_data.drop(['player', 'pos', 'team_id'], axis=1, inplace=True)
        predict_labels = mvp_column[dataframe['season'] <= 2017]

        # Train model and print results
        model = RandomForestClassifier()
        model.fit(predict_data, predict_labels)
        predictions = model.predict(test_data)
        mvps = players[predictions == 1]
        print(mvps)

        
