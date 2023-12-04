import numpy as np
import sklearn.feature_selection
import pandas as pd
import sklearn.impute


class FeatureSelection():
    def select_features():
        data = np.genfromtxt('New_Dataset_Numbers_Only.csv',
                             delimiter=',', dtype=float, skip_header=1)
        features = np.genfromtxt(
            'New_Dataset_Features.csv', delimiter=',', dtype=str)

        award_share = features[30]  # this is the column titled 'award_share'
        seasons = features[0]

        # Remove feature names that correlate to string data types
        features = np.delete(features, [1, 2, 4])

        # Remove players with under 10 minutes of playing time per game
        low_playing_time = list(np.where(data[:, 4] < 10)[0])
        data = np.delete(data, low_playing_time, axis=0)

        # Remove inconsequential features season, age
        data = np.delete(data, [1], axis=1)
        features = np.delete(features, [1])

        # Remove redundant stats (example: fg_made can be derived from fg_pct and fg_attempted)
        # was data = np.delete(data, [3, 6, 9, 13], axis=1)
        data = np.delete(data, [4, 7, 10, 14], axis=1)
        # was data = features = np.delete(features, [3, 6, 9, 13])
        features = np.delete(features, [4, 7, 10, 14])

        imputer = sklearn.impute.SimpleImputer(
            missing_values=np.nan, strategy='mean')
        imputed_data = imputer.fit_transform(data)

        # this is the imputed award share data
        award_share_data = imputed_data[:, 21]
        # seasons
        seasons_data = imputed_data[:, 0]

        # now we can delete the seasons data before feature selection now that we have it saved
        features = np.delete(features, [0])
        imputed_data = np.delete(imputed_data, [0], axis=1)

        # Specify features that need to be included (pts, reb, ast, etc.) and remove them before variance threshold is examined
        essential_features = [4, 6, 8, 14, 15, 16, 17, 18, 20]
        non_essential_data = np.delete(
            imputed_data, essential_features, axis=1)
        non_essential_features = np.delete(features, essential_features)

        # Convert to dataframe because it lets you see selected column names
        df = pd.DataFrame(non_essential_data, columns=non_essential_features)

        # Select features with a variance greater than 0.8
        feature_selector = sklearn.feature_selection.VarianceThreshold(
            threshold=1)
        reduced_data = feature_selector.fit_transform(df)
        selected_features = feature_selector.get_feature_names_out()

        new_features = np.append(
            features[essential_features], np.array(selected_features))
        # need to reappend award_share
        new_features = np.append(new_features, np.array(award_share))
        # need to append the seasons back
        new_features = np.append(np.array(seasons), new_features)

        new_dataset = np.hstack(
            (imputed_data[:, essential_features], np.array(reduced_data)))

        # need to reappend award_share data
        new_dataset = np.hstack((new_dataset, award_share_data[:, np.newaxis]))

        # need to reappend seasons to the front
        new_dataset = np.hstack((seasons_data[:, np.newaxis], new_dataset))

        # print(selected_features)
        # print(new_features)
        # print(new_features.shape)
        # print(new_dataset.shape)

        return new_features, new_dataset
