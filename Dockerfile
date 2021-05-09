FROM python:3.8-alpine
RUN python3 -m pip install flask prometheus_client requests
ADD app.py /app.py
CMD ["python3", "/app.py"]
