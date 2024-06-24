import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the Iris dataset from the CSV file
df = pd.read_csv(r'D:\data\iris_dataset.csv')

# Separate features and target
X = df.drop(columns=['target'])
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the SVM model
svm_model = SVC(kernel='linear', C=1.0, random_state=42)
svm_model.fit(X_train, y_train)

# Make predictions
y_pred = svm_model.predict(X_test)

# Calculate accuracy, Confusion matrix, Classification report
accuracy = accuracy_score(y_test, y_pred)

conf_matrix = confusion_matrix(y_test, y_pred)

class_report = classification_report(y_test, y_pred)

# Print the evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

# Inverse transform the standardized test data to original units (cm)
X_test_original = scaler.inverse_transform(X_test)

# Saving the prediction output in a CSV file
output_df = pd.DataFrame(X_test_original, columns=df.columns[:-1])
output_df['Actual Species'] = y_test.values
output_df['Predicted Species'] = y_pred

output_df.to_csv('iris_predictions.csv', index=False)
