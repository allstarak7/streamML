import numpy as np
import sklearn.feature_selection
import pandas as pd
import sklearn.impute


data = np.genfromtxt('Dataset_Numbers_Only.csv', delimiter=',', dtype=float, skip_header=1)
features = np.genfromtxt('Dataset_Features.csv', delimiter=',', dtype=str)

# Remove feature names that correlate to string data types
features = np.delete(features, [1, 2, 4])

# Remove players with under 10 minutes of playing time per game
low_playing_time = list(np.where(data[:, 4] < 10)[0])
data = np.delete(data, low_playing_time, axis=0)

# Remove inconsequential features season, age
data = np.delete(data, [0, 1], axis=1)
features = np.delete(features, [0, 1])

# Remove redundant stats (example: fg_made can be derived from fg_pct and fg_attempted)
data = np.delete(data, [3, 6, 9, 13], axis=1)
features = np.delete(features, [3, 6, 9, 13])


imputer = sklearn.impute.SimpleImputer(missing_values=np.nan, strategy='mean')
imputed_data = imputer.fit_transform(data)


# Specify features that need to be included (pts, reb, ast, etc.) and remove them before variance threshold is examined
essential_features = [4, 6, 8, 14, 15, 16, 17, 18, 20, 45]
non_essential_data = np.delete(imputed_data, essential_features, axis=1)
non_essential_features = np.delete(features, essential_features)

# Convert to dataframe because it lets you see selected column names
df = pd.DataFrame(non_essential_data, columns=non_essential_features)

# Select features with a variance greater than 0.8
feature_selector = sklearn.feature_selection.VarianceThreshold(threshold=1)
reduced_data = feature_selector.fit_transform(df)
selected_features = feature_selector.get_feature_names_out()


new_features = np.append(features[essential_features], np.array(selected_features))
new_dataset = np.hstack((imputed_data[:, essential_features], np.array(reduced_data)))

print(selected_features)
print(new_features)
print(new_features.shape)
print(new_dataset.shape)

