FROM python:3.7.0-alpine3.8
WORKDIR /app
RUN pip install docker
COPY Reaper.py /app
CMD ["python","-u","Reaper.py"]
LABEL maintainer="BetrUG"