FROM python:3

WORKDIR    /dock3
COPY       requirements.txt /dock3/
RUN        pip install -r requirements.txt

COPY       *.py /dock3/
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]