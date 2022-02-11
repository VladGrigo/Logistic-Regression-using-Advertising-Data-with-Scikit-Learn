FROM python:3.10.2-bullseye
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install Cython
RUN pip install -r requirements.txt
CMD python ./script.py