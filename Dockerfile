FROM python:3.7-alpine
RUN mkdir /app
COPY . /app
ADD geckodriver /usr/local/bin/geckodriver 
RUN apk add --update firefox
WORKDIR /app
RUN chmod 777 /usr/local/bin/geckodriver
RUN chmod 777 *
RUN pip install -r requiriments
CMD ["python3", "/app/init.py"]