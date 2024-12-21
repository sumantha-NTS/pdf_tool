FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr libgl1-mesa-glx poppler-utils ghostscript

COPY requirements.txt ./app/
RUN pip install -r /app/requirements.txt

COPY . .

CMD ["python","Welcome.py"]