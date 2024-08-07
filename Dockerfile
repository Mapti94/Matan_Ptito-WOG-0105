FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8777
CMD python main_score.py