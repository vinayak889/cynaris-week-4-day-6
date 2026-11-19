# Stage 1: dependency builder
FROM python:3.12-slim AS builder
WORKDIR /build
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: lean runtime image
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 8000
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
