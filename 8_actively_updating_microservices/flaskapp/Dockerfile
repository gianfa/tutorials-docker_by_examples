FROM python:3

WORKDIR    /dock8
COPY       . /dock8/
RUN        pip install -r requirements.txt
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]