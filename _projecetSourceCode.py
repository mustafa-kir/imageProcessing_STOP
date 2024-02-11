import cv2
import os
import numpy as np


DATADIR = ""  # Görüntülerin bulunduğu dizin
CATEGORIES = ["stop", "not_stop"] # klasörler

IMG_SIZE = 50  # Görüntüleri yeniden boyutlandırma

data = []
labels = []

# Klasörlerdiki değerleri tek tek okuma
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    class_num = CATEGORIES.index(category)
    for img in os.listdir(path):
        # klasörlerdeki değerleri tek tek okuma ama eğer hata olursa bir sonrakine atla
        try:
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            data.append(new_array)
            labels.append(class_num)
        except Exception as e:
            pass


data = np.array(data).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
data = data / 255.0  # Normalize the data

labels = np.array(labels)

from sklearn.model_selection import train_test_split
# Veriyi eğitim ve test seti olarak ayır
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Yapay sinir ağı
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout

model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=data.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))

model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, epochs=30, validation_split=0.1)
val_loss, val_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {val_accuracy}")

test_image_path = "not_stop_1.jpg"
# Resmi oku ve boyutlandır 
test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
test_image = cv2.resize(test_image, (IMG_SIZE, IMG_SIZE))
test_image = np.array(test_image).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
test_image = test_image / 255.0

# Modelden tahmin al
prediction = model.predict(test_image)

# Tahmin sonucunu yazdır
if prediction[0][0] < 0.5:
    print("STOP")
else:
    print("STOP No Sraffic Sign")