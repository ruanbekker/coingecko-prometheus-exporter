FROM python:3.11-alpine
RUN python3 -m pip install flask prometheus_client requests
ENV CRYPTO_COINS=bitcoin,kaspa
ENV CURRENCY=eur
ADD app.py /app.py
CMD ["python3", "/app.py"]
