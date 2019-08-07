FROM python:3

WORKDIR    /dock5
COPY       requirements.txt /dock5/
RUN        pip install -r requirements.txt

COPY       *.py /dock5/
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]