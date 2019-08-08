FROM python:3

WORKDIR    /predapi
COPY       . /predapi/
RUN        pip install -r requirements.txt
# RUN        chmod a+x /predapi/*.py

CMD        ["python", "./server.py"]