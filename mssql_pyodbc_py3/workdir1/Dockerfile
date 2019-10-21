############################# MSSQL SERVER with Python 3.6 ############################
# MSSQL SERVER
# on UBUNTU 16.04
# with Python 3.6, Python2.7
# and pyodbc, pandas, fflask


## 1. LOAD THE MICROSOFT MSSQL SERVER IMAGE ##
FROM mcr.microsoft.com/mssql/server:2019-CTP3.2-ubuntu

WORKDIR    /home/python/app/
COPY       . /home/python/app/

## 2. INSTALLING PYTHON3 & PIP ##
# RUN apt-get update
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install software-properties-common python-software-properties -y
# install python3
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update
RUN apt-get install python3.6 -y
# update deafult python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
# install pip
RUN apt-get install curl -y
RUN curl -sS https://bootstrap.pypa.io/get-pip.py >>setup.py
RUN python3 setup.py


### 3. ODBC ###
RUN apt-get install python3.6-dev -y
RUN apt-get install git-core -y

RUN apt-get install unixodbc-dev -y
RUN apt-get update
RUN apt-get install build-essential -y
RUN pip3 install pyodbc

### 4. UTILS ###
RUN apt install --assume-yes vim

### 5. PREPARE WORKSPACE ###
RUN pip3 install -r requirements.txt
RUN chmod a+x *.py

### LAUNCH SERVER ###
CMD ["python3", "./server.py"]