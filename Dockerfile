FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
RUN git clone https://github.com/Mapti94/Matan_Ptito-WOG-0105.git .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8777
CMD python main_score.py