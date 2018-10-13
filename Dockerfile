FROM python:3.7.0-alpine3.8
COPY . /app
WORKDIR /app
RUN pip install docker
CMD python ./Reaper.py