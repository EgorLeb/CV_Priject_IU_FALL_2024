# CV_Priject_IU_FALL_2024

В этом проекте использованы **Fastapi**, **Streamlit**. 

Внутри есть загруженная модель с весами, которая определит букву на изображении.

Сборка происходит через запуск **Docker-compose** файла.

./api

Fastapi приложение. Обрабатывает один базовый запрос для проверки подключения и один запрос на выгрузку фото через post запрос.

./app

Streamlit приложение. Принимает фото и отправляет в соседний контейнер на Fastapi, после принимает и выводит результат.

Также вилидирует входной файл и обрабатывает ошибки.

**Важно, при запусте приложения доступ осуществляется через порт 8502.** К Fastapi доступ стандартный, по 8000 порту.


![image](https://github.com/user-attachments/assets/9f3d2e27-dc70-41b9-bd42-650e8cc2ed7f)

![image](https://github.com/user-attachments/assets/ecfc755f-4bf6-4a21-a57d-a6d22870202c)


Кейс с неверным форматом

![image](https://github.com/user-attachments/assets/0ad25778-f6cc-4323-8717-0401cb6882fa)


