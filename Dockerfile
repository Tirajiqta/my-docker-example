# Dockerfile

# python base image
FROM python:3.9-slim

#set working dir
WORKDIR /app
COPY container-uuid.txt /app/


EXPOSE 8080

COPY application.py .

CMD ["python", "application.py"]

