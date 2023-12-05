from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

from feature_selection import FeatureSelection

class NeuralNetwork():
    def mlp_regressor(self):
        # Perform the feature selection
        new_features, new_dataset = FeatureSelection.select_features()

        # Separate features and target variable
        X = new_dataset[new_dataset[:, 0] < 2022][:, :-1]
        y = new_dataset[new_dataset[:, 0] < 2022][:, -1]
        self.dataset = new_dataset

        # Standardize the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Split the data into training and testing sets
        # X_train, X_test, y_train, y_test = train_test_split(
        #     X_scaled, y, test_size=0.2, random_state=0
        # )

        # Build and train the neural network model
        model = MLPRegressor(
            hidden_layer_sizes=(100, 100, 100),
            max_iter=1000,
            alpha=0.0001,
            verbose=10,
            solver='adam',
            random_state=21,
            tol=1e-9
        )
        model.fit(X_scaled, y)

        self.model = model
        self.scaler = scaler

    def make_predictions(self):
        X_test = self.dataset[self.dataset[:, 0] == 2022][:, :-1]
        y_test_actual = self.dataset[self.dataset[:, 0] == 2022][:, -1]

        # Standardize the test data using the same scaler
        X_test_scaled = self.scaler.transform(X_test)

        # Make predictions
        y_2022_scaled = self.model.predict(X_test_scaled)

        # Print or return predictions
        print('Predictions for 2022:', y_2022_scaled)
        print('Actual values for 2022:', y_test_actual)
        self.plot_actual_vs_predicted(y_2022_scaled, y_test_actual)
        return y_2022_scaled

    def plot_actual_vs_predicted(self, y_pred_scaled, y_test_actual):
        # Plot the actual vs predicted values
        plt.scatter(y_test_actual, y_pred_scaled, alpha=0.5)
        plt.xlabel("True Labels")
        plt.ylabel("Predicted Labels")
        plt.title("Actual vs. Predicted Values")
        plt.show()

        # Print the MSE
        mse = mean_squared_error(y_test_actual, y_pred_scaled)
        print('MSE:', mse)
