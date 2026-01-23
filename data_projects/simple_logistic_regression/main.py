from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("./data/titanic.csv")
X = df[['Pclass', 'Fare']]
y = df['Survived']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12)

# Train Logistic Regression model
model = LogisticRegression(max_iter=100)
model.fit(X_train, y_train)

# predict and evaluate
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)
print(f"Accuracy: {score:.2f}")
