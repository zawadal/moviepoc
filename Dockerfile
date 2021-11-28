FROM python:3.9-slim
ADD rotten.py /app/rotten.py
ENTRYPOINT ["python", "/app/rotten.py"]