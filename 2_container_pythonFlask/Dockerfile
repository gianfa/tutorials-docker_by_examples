FROM python:3

WORKDIR    /dock2
COPY       requirements.txt /dock2/
RUN        pip install -r requirements.txt

COPY       *.py /dock2/
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]