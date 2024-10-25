FROM python:3.8.10
WORKDIR /app
COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install fastapi[all]
RUN pip install opencv-python
RUN pip install keras
RUN pip install tensorflow
RUN pip install jiwer gradio typing-extensions

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
