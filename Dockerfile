FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip3 install -r requisitos.txt
EXPOSE 5000
CMD python ./main.py
