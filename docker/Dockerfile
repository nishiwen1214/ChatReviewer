FROM python:3.10-slim
LABEL maintainer="hanhongyong"
RUN apt-get update \
    && apt-get install -y libpq-dev build-essential \
    && apt-get clean 
RUN mkdir /app
RUN mkdir -p /app/ChatResponse && mkdir -p /app/ChatReviewer
COPY requirements.txt /app/
COPY ChatResponse/* /app/ChatResponse
COPY ChatReviewer/* /app/ChatReviewer
COPY entrypoint.sh /app/
RUN pip install --user --no-cache-dir -r /app/requirements.txt
WORKDIR /app
EXPOSE 7000
EXPOSE 8000
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh","./entrypoint.sh"]



