import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

df = pd.read_csv('obl.csv', parse_dates=["date"])


# Convert date to numeric representation
df['date'] = pd.to_datetime(df['date'])

# Split data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    df['date'], df['amount'], test_size=0.2, random_state=42)

# Create the model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,), name='date'),
    tf.keras.layers.Dense(units=1, name='amount')
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
history = model.fit(train_data, train_labels, epochs=100,
                    validation_split=0.2, verbose=0)

# Evaluate the model
loss, mae = model.evaluate(test_data, test_labels, verbose=2)
print("Mean Absolute Error on Test Data:", mae)

# Make predictions
predictions = model.predict(test_data)

# Plot the results
plt.scatter(test_data, test_labels, label='Actual')
plt.scatter(test_data, predictions, label='Predicted')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend()
plt.show()
# print(df.columns)

# features = df["date"]
# target = df["amount"]

# features = tf.keras.utils.normalize(features, axis=0)
# features_unix = features.dt.timestamp.to_numpy().reshape(-1, 1)
# features_normalized = tf.keras.utils.normalize(features_unix, axis=0)

# plt.plot(df["date"], df["amount"])
# plt.show()

# features = tf.keras.utils.normalize(features, axis=0)

# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(1, use_bias=True, activation="linear")
# ])

# model.compile(loss="mse", optimizer="adam")

# history = model.fit(features, labels, epochs=100)
# loss, accuracy = model.evaluate(features, labels)

# new_features = pd.DataFrame({"date": ["2023-11-16"]})
# prediction = model.predict(new_features)

# print(prediction)
