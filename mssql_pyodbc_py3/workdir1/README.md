# MSSQL Server with Python3.6
This is a ready-to-run example of microservice using a MSSQL Server with Python 3.6.  
### Why
Because I lost my mind trying to make a simple connection to MSSQL DB through python3, not finding any docker images ready to be used.

### Content
The image mounts a Ubuntu 16.04 OS, and it comes with pyodbc, pandas and flask.  
The file *examp_funx.py* has a function as example, ran by a flask server, by *server.py*.

### Basic use

0. Set the connection parameters.  
    * *server.py* -> name of the table ('YOUR_TABLE_NAME').
    * *examp_funx.py* -> connection parameters
1. Build the image, by command line
    ```shell
    # from workdir1/
    docker-compose build
    ```
2. Launch the service, by command line
    ```shell
    # from workdir1/
    docker-compose up
    ```
3. Open the browser to (http://localhost:5001/db)[http://localhost:5001/db]

4. Enjoy

