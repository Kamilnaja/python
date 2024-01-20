import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from keras.layers import LSTM, Dense, Embedding, Flatten
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from tensorflow import keras

zdania = {
    "Kobiety są równe w stosunku do mężczyzn": 1,
    "Kobiety są gorsze od mężczyzn": 0,
    "Mężczyźni są gorsi od kobiet": 0,
    "Mężczyźni powinni być szefami": 0,
    "Kobiety powinny zajmować się domem": 0,
    "Mężczyźni są agresywni": 0,
    "Zarówno kobiety jak i mężczyźni są czsem agresywni": 1,
    "Kobiety są słabe": 0,
    "Mężczyźni dużo piją": 0,
    "Miejsce kobiety jest w kuchni": 0,
    "Miejsce mężczyzny jest w pracy": 0,
    "Kobiety i mężczyźni są równi": 1,
    "Kobiety mogą być szefami": 1,
    "Mężczyźni mogą zajmować się domem": 1,
    "Mężczyźni i kobiety mogą być agresywni": 1,
    "Mężczyźni i kobiety mogą być silni": 1,
    "Mężczyźni są słabi": 0,
    "Tylko kobiety są silne": 0,
    "Kobiety powinny być szefami": 0,
    "Mężczyźni powinni zajmować się domem": 0,
    "Kobiety są agresywne": 0,
    "Mężczyźni są silni": 0,
    "Mężczyźni są słabi": 0,
    "Mężczyzna powinien płacić za kobietę": 0,
    "Mężczyzna powinien mieć samochód": 0,
    "Kobieta powinna mieć dzieci": 0,
    "Kobieta powinna być matką": 0,
    "Kobieta powinna być żoną": 0,
    "Kobieta powinna być kobietą": 1,
    "Mężczyzna powinien być mężczyzną": 1,
    "Mężczyzna powinien być ojcem": 0,
    "Mężczyzna powinien być mężem": 0,
    "Mężczyzna powinien być silny": 0,
    "Kobieta powinna być słaba": 0,
    "Chłopcy nie płaczą": 0,
    "Kobiety muszą zarabiać mniej bo są mniej inteligentne": 0,
    "Równość szans kobiet i mężczyzn jest ważnym elementem szerszej kwestii równości szans": 1,
    "Kobiety są zdolne do wielu rzeczy": 1,
    "Mężczyźni są zdolni do wielu rzeczy": 1,
    "Kobiety i mężczyźni są zdolni do wielu rzeczy": 1,
    "Równość szans kobiet i mężczyzn jest ważna": 1,
    "Równość płci jest ważna": 1,
}

# Separate sentences and labels
sentences = list(zdania.keys())
labels = list(zdania.values())

# Convert labels to numpy array
labels = np.array(labels)

# Tokenize the sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

# Convert sentences to sequences
sequences = tokenizer.texts_to_sequences(sentences)

# Pad sequences to have consistent length
padded_sequences = pad_sequences(sequences)

model = Sequential(
    [
        Embedding(
            input_dim=len(tokenizer.word_index) + 1,
            output_dim=32,
            input_length=padded_sequences.shape[1],
        ),
        LSTM(32, return_sequences=True),
        Flatten(),
        Dense(1, activation="sigmoid"),
    ]
)

model.compile(optimizer="adam", loss="binary_crossentropy",
              metrics=["accuracy"])
epochs = 10
history = model.fit(padded_sequences, labels,
                    epochs=epochs, validation_split=0.2)

# Example new sentences
new_sentences = [
    "Kobiety i mężczyźni są zdolni do wielu rzeczy",
    "Kobiety i mężczyźni są równi",
    "Kobiety mogą być szefami",
]

# Convert new sentences to sequences
new_sequences = tokenizer.texts_to_sequences(new_sentences)

# Pad sequences to have consistent length
padded_new_sequences = pad_sequences(
    new_sequences, maxlen=padded_sequences.shape[1])

# Make predictions
predictions = model.predict(padded_new_sequences)

# Convert probabilities to classes (0 or 1)
predicted_classes = (predictions > 0.5).astype(int)

# Display predictions
for i, sentence in enumerate(new_sentences):

    print(f"Sentence: {sentence}")
    print(f"Predicted Class: {predictions} {predicted_classes[i][0]}")

# show plot
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs_range = range(epochs)

# plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label="Training Accuracy")
# plt.plot(epochs_range, val_acc, label="Validation Accuracy")
# plt.legend(loc="lower right")
# plt.title("Training and Validation Accuracy")
# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label="Training Loss")
# plt.plot(epochs_range, val_loss, label="Validation Loss")
# plt.legend(loc="upper right")
# plt.title("Training and Validation Loss")
# plt.show()
