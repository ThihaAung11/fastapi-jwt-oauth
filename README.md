## Description
A simple fasta pi app with jwt, auth and oauth


### Prerequisite
1. Python 3.10+
2. FastAPI
3. Sqlite

### Initialization DB *(not important)*
#### Database Initialization with alembic
1. Edit sqlalchemy.url in alembic.ini file
2. Edit target_metadata in alembic/env file 
3. 
    ```
    alembic revision --autogenerate -m "Initial migration
    ```
4.
    ```
    alembic upgrade head
    ```