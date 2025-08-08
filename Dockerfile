# Dockerfile - small, production-ready
FROM python:3.11-slim

# create non-root user for security (best practice)
RUN useradd --create-home appuser
WORKDIR /home/appuser/app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY . .

# switch to non-root user
USER appuser

# run via gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "--workers=2", "--timeout=120"]
