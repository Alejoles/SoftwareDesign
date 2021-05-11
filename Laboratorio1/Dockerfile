FROM python:3.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8001
COPY app.py app.py
CMD ["gunicorn", "app:api", "--bind", ":8001"]
