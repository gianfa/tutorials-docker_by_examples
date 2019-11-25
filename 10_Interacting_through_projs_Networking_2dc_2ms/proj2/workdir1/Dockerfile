FROM python:3

WORKDIR    /home/python/app/
COPY       . /home/python/app/
RUN        pip install -r requirements.txt
RUN        chmod a+x *.py

CMD        ["python", "./server.py"]