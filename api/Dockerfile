FROM python:3.8-slim

# Install netcat
#RUN apt-get update && \
#    apt-get -y install netcat && \
#    apt-get clean

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN python -m pip install dask[array]
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# run server
CMD python manage.py run -h 0.0.0.0
