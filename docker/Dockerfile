FROM python:3.8.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ../src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s CMD curl --fail http://localhost:5000/health || exit 1
ENTRYPOINT ["python","./src/app.py"]
