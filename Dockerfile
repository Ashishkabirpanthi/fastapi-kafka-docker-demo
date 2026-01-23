FROM python:3.12-slim

WORKDIR /app

COPY  pyproject.toml ./

RUN pip install --no-cache-dir -e .

COPY . .

EXPOSE 8000

CMD ["uvicorn","app.server:app","--port","8000"]

