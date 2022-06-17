FROM python:3.8
FROM mcr.microsoft.com/playwright/python:v1.22.0-focal
RUN pip install --upgrade pip
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "src/main.py"]