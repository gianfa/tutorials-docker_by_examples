# MSSQL Server with Python3.6
This is a ready-to-run example of microservice using a MSSQL Server with Python 3.6.  

### Basic use

0. Set the connection parameters.  
    * *server.py* -> name of the table ('YOUR_TABLE_NAME').
    * *examp_funx.py* -> connection parameters
1. Build the image, by command line
    ```shell
    # from project folder
    docker-compose build
    ```
2. Launch the service, by command line
    ```shell
    # from project folder
    docker-compose up
    ```
3. Open the browser to (http://localhost:5001/db)[http://localhost:5001/db]

4. Enjoy

