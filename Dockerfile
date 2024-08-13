FROM python:alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main_score.py .
COPY score.txt .
EXPOSE 8777
EXPOSE 5254
CMD python main_score.py