FROM python:3

WORKDIR    /dock4
COPY       requirements.txt /dock4/
RUN        pip install -r requirements.txt

COPY       *.py /dock4/
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]