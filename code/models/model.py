from keras.metrics import categorical_accuracy
from keras.models import Sequential
from keras.layers import Dense, LeakyReLU, Conv2D, MaxPooling2D, GlobalMaxPooling2D, Activation, Dropout
import warnings; warnings.filterwarnings('ignore')

def get_model():
    model = Sequential()

    model.add(Conv2D(8, (5, 5), padding='same', input_shape=(32, 32, 3)))
    model.add(LeakyReLU(alpha=.025))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(.1))

    model.add(Conv2D(16, (5, 5), padding='same'))
    model.add(LeakyReLU(alpha=.025))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(.1))

    model.add(Conv2D(32, (5, 5), padding='same'))
    model.add(LeakyReLU(alpha=.025))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(.1))

    model.add(GlobalMaxPooling2D())
    model.add(Dense(128))
    model.add(Dense(33))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=[categorical_accuracy])
    return model
