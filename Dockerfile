FROM flask
FROM python

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .



ENTRYPOINT FLASK_APP=project FLASK_DEBUG=1 flask run