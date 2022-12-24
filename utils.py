from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from livelossplot.tf_keras import PlotLossesCallback
from tensorflow.keras import backend as K

def train_model(X, y, model, numEpoch, nameFile):
    early_stopping = EarlyStopping(monitor='val_loss',
                                   patience=25, verbose=0, mode='min',
                                   restore_best_weights= True)
    callbacks = [PlotLossesCallback(), early_stopping]
    hist = model.fit(X, y, batch_size=32, verbose=1, epochs=numEpoch, validation_split=0.2,
                    callbacks = callbacks)
    model.save_weights(nameFile, save_format='h5')
    return hist

def euc_dist_keras(y_true, y_pred):
    return K.sqrt(K.sum(K.square(y_true - y_pred), axis=-1, keepdims=True))
