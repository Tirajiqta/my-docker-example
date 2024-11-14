# Dockerfile

# python base image
FROM python:3.9-slim

#set working dir
WORKDIR /app

EXPOSE 8080

COPY application.py .

CMD ["python", "application.py"]

