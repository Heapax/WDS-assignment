FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY nasa_script.py .

CMD ["python", "nasa_script.py"]
