from fastapi import FastAPI, HTTPException, status
from fastapi import File, UploadFile, Form
import numpy as np
import cv2
import model as mdl


app = FastAPI()

# model = mdl.get_model()
# model.load_weights("best.keras")
#
#
# def predict(file, predicting_model):
#     letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#     arr = np.fromstring(file, 'uint8')
#     img = cv2.imdecode(arr, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img, (32, 32), interpolation = cv2.INTER_AREA)
#     img = (img / 255).astype("float64")
#     tmp = predicting_model.predict(np.expand_dims(img, axis=0))
#     return letters[tmp.argmax()]
#
#
# @app.get('/')
# def root():
#     return {'message': 'Hello World'}
#
#
# @app.post("/upload")
# def upload(filename: str = Form(...), file: UploadFile = File(...)):
#     try:
#         contents = file.file.read()
#         res = predict(contents, model)
#     except Exception as e:
#         print(e)
#         return {"message": f"{e}"}
#     finally:
#         file.file.close()
#     return {"message": f"{res}"}
