FROM python:alpine3.7
RUN apk update && apk add --no-cache gcc g++ python3-dev unixodbc-dev
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python ./script.py