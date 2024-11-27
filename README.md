# Optical Character Recognition for Handwritten Russian Letters
Optical Character Recognition (OCR) for Russian letters
involves converting images of handwritten or printed Cyrillic
text into machine-readable formats. In our project we will focus on developing CNN-like model
for Russian OCR.

# Model 
![image](https://github.com/EgorLeb/CV_Priject_IU_FALL_2024/blob/main/assets/madel_desc.jpg)

# Deployment

This project uses **Fastapi**, **Streamlit**. 

Inside there is a loaded model with weights that will determine the letter in the image.

The build is done by running the **Docker-compose** file.

## build.

```sudo docker compose build```

```sudo docker compose up```

The final web application will be located at ```http://localhost:8502/``.

## Folders

```./api```.

Fastapi application. Handles one basic request to check connectivity and one request to upload a photo via post request.

```./app```

Streamlit application. Receives a photo and sends it to a neighboring container on Fastapi, then receives and outputs the result.

Also vilidates the input file and handles errors.

**Important, when running the application access is via port 8502.** Fastapi access is standard, on port 8000.
![image](https://github.com/user-attachments/assets/867d4e91-1f41-4d28-9dad-ccb34f4d07e2)

![image](https://github.com/user-attachments/assets/63672df4-5794-49cd-9d2d-2c5bc402de69)

Case with wrong file format

![image](https://github.com/user-attachments/assets/1882361f-d318-40b1-b9e2-6abcd2106cae)

# Results and Evaluation
After training the model, the following accuracy metrics
were achieved:

- Training Accuracy: 0.9096
- Validation Accuracy: 0.9056
- Test Accuracy: 0.8843
