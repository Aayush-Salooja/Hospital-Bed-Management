import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# -----------------------------
# Load Data
# -----------------------------

print("Loading ICU occupancy data...")

df = pd.read_csv(
    "./data/processed/true_icu_occupancy.csv"
)

print(df.head())

# -----------------------------
# Prepare Series
# -----------------------------

values = df["icu_occupancy"].values.reshape(-1, 1)

scaler = MinMaxScaler()

scaled = scaler.fit_transform(values)

# -----------------------------
# Create Sequences
# -----------------------------

WINDOW = 30

X = []
y = []

for i in range(WINDOW, len(scaled)):

    X.append(
        scaled[i-WINDOW:i]
    )

    y.append(
        scaled[i]
    )

X = np.array(X)
y = np.array(y)

print("\nX shape:", X.shape)
print("y shape:", y.shape)

# -----------------------------
# Train/Test Split
# -----------------------------

split = int(
    len(X) * 0.8
)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

# -----------------------------
# Build Model
# -----------------------------

model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(
            X_train.shape[1],
            X_train.shape[2]
        )
    )
)

model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse"
)

# -----------------------------
# Train
# -----------------------------

print("\nTraining LSTM...")

history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_data=(
        X_test,
        y_test
    )
)

# -----------------------------
# Forecast Next 7 Days
# -----------------------------

window = scaled[-WINDOW:]

future_predictions = []

for _ in range(7):

    pred = model.predict(
        window.reshape(
            1,
            WINDOW,
            1
        ),
        verbose=0
    )

    future_predictions.append(
        pred[0][0]
    )

    window = np.vstack(
        [
            window[1:],
            pred
        ]
    )

future_predictions = np.array(
    future_predictions
).reshape(-1, 1)

future_predictions = scaler.inverse_transform(
    future_predictions
)

print("\n===== NEXT 7 DAY ICU FORECAST =====")

for i, value in enumerate(
    future_predictions,
    start=1
):
    print(
        f"Day {i}: "
        f"{value[0]:.2f}"
    )

# -----------------------------
# Save Model
# -----------------------------

model.save(
    "./models/lstm_icu.keras"
)

print(
    "\nSaved:"
)
print(
    "./models/lstm_icu.keras"
)