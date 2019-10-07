import tensorflow
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Reshape

classifier =  Sequential()

classifier.add(Convolution2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Convolution2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Convolution2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())
classifier.add(Dense(units=128,activation='relu'))
classifier.add(Dense(units=1,activation='sigmoid'))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen=ImageDataGenerator(rescale=1/1.255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        'chest_xray/train',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = train_datagen.flow_from_directory(
        'chest_xray/test',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

val_set = train_datagen.flow_from_directory(
        'chest_xray/val',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

cl=classifier.fit_generator(
        training_set,
        steps_per_epoch=16,
        epochs=20,
        validation_data=test_set,
        validation_steps=16)


from sklearn.metrics import classification_report, confusion_matrix

y_pred = classifier.predict_generator(test_set)
y_pred =(y_pred>0.5)
class_labels = test_set.class_indices
class_labels = {v: k for k, v in class_labels.items()}
classes = list(class_labels.values())
print('Confusion Matrix')
print(confusion_matrix(test_set.classes, y_pred))
print('Classification Report')
print(classification_report(test_set.classes, y_pred, target_names=classes))


import matplotlib.pyplot as plt

plt.plot(cl.history['acc'])
plt.plot(cl.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['training_set', 'test_set'], loc='upper left')
plt.show()

#Loss
plt.plot(cl.history['loss'])
plt.plot(cl.history['val_loss'])
plt.title('Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['training_set', 'test_set'], loc='upper left')
plt.show()
