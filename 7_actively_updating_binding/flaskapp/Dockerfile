FROM python:3

WORKDIR    /dock7
COPY       . /dock7/
RUN        pip install -r requirements.txt
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]