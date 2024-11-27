from fastapi import FastAPI, HTTPException, status
from fastapi import File, UploadFile, Form
import numpy as np
import cv2
from keras.models import load_model

app = FastAPI()

model = load_model('best.keras')

def predict(file, predicting_model):
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    arr = np.fromstring(file, 'uint8')
    img = cv2.imdecode(arr, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (32, 32), interpolation = cv2.INTER_AREA)
    img = (img / 255).astype("float64")
    tmp = predicting_model.predict(np.expand_dims(img, axis=0))
    return letters[tmp.argmax()]


# just check the connection
@app.get('/')
def root():
    return {'message': 'Hello World'}


# upload the file and return the letter
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        res = predict(contents, model)
    except Exception as e:
        print(e)
        return {"message": f"{e}"}
    finally:
        file.file.close()
    return {"message": f"{res}"}
