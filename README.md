Metadata Management System

## Database Schema Overview

#Three tables have been created (sourcesystems, datasets, dataelements)

#Relationships (Cardinality)
-- `sourcesystems`-> `datasets` - One to Many (Each combination of sourceSystem and owner can have multiple datasets, but each dataset belongs to exactly one combination of sourceSystem and owner)
-- `datasets`-> `dataelements`- One to Many (Each dataset can have multiple data elements, but each data element belongs to exactly one dataset)

#Constraints and Considerations
-- `name` and `owningApplication` in `sourcesystems` is a composite unique key.
-- `name` and `sourceSystemId` in `datasets` is a composite unique key as tables can be duplicate across databases, but not within databases
-- `name` and `datasetId` in `dataelements` is a composite unique key as columns can be duplicate across tables, but not within the same table.

## API Details
===============================================
            Dataset APIs
===============================================
API Endpoint         | Method | Params          | Status codes  | Description
--------------------------------------------------------------------------------------------------------------------------------
/datasets            | POST   | -                | 200,422,500  | Create a new dataset in the metadata catalog.
/datasets            | GET    | -                | 200,500      | Retrieve all datasets.
/datasets/{datasetId}| GET    | datasetId (int)  | 200,402,422  | Retrieve a dataset and its associated data elements by ID.

===========================================================
            Data elements APIs
===========================================================
API Endpoint| Method | Params                                      | Status Codes   |Description
-----------------------------------------------------------------------------------------------------------------------------------------
/elements   | POST   | datasetId (int)                             | 200,404,422,500| Create a new data element and associate it with a dataset.
/elements   | GET    | datasetId (int), pii (bool), datatype (str) | 200,422        | Retrieve data elements with optional filters.

===========================================================
NOTES:
- Request Body Models:
    * CreateDataset – for /datasets POST
    * CreateDataElement – for /elements POST

- Response Models:
    * GetDataset – Dataset details
    * GetDatasetWithElements – Dataset details with all associated data elements
    * GetDataElement – Data element details
===========================================================

## Validation Rules

Validation rules have been implemented to enforce data integrity for primary key column in the `dataelements` entity.

- When a data element is marked as a primary key (`isPrimary = True`):
  - `isUnique` is automatically set to True if it is not explicitly provided.
  - `isNullable` is automatically set to False if it is not explicitly provided.

- Additional validations ensure consistency:
  - If `isPrimary = True` and `isUnique` is explicitly set to False, a validation error is raised.
  - If `isPrimary = True` and `isNullable` is explicitly set to True, a validation error is raised.

These rules ensure that all primary key columns remain **unique and non-nullable**, maintaining consistency with standard database primary key constraints.

## Improvement and Enhancement Areas
## Steps to run the application 

   **Follow these steps if you do not want to use Docker**
     -- Pre-requisites : python >=3.14, poetry and sqlite
     -- Clone the repository https://github.com/nandinibarman94/metadata-tracker.git
     -- Inside project root folder run `poetry install`
     -- Run `poetry run alembic upgrade head`- This will create the database(MetadataTracker.db) and the tables in the database for you. Additionally, it will create a row in the sourcesystem table as master data. You can run the select statement to see the row created. You can either use the 'DB browser for SQLite' or run the below commands in sqlite CLI
     =====================================================================
        PS C:\assignment\metadata-tracker> sqlite3 MetadataTracker.db
        SQLite version 3.51.2 2026-01-09 17:27:48
        Enter ".help" for usage hints.
        sqlite> .databases
        main: C:\assignment\metadata-tracker\MetadataTracker.db r/w
        sqlite> .tables
        alembic_version  dataelements     datasets         sourcesystems  
        sqlite> select * from sourcesystems;
        1|OrderDB|data-team|2026-03-17 18:57:33|admin|2026-03-17 18:57:33|admin
        sqlite> .exit
        PS C:\assignment\metadata-tracker>  
     ===============================================================================
     -- Run `poetry run uvicorn src.main:app --reload` to start the application
     -- Navigate to /docs to access the Swagger UI.
     -- Run `poetry run pytest -v` if you want to run the test cases.

   **Follow these steps if you want to use Docker**
     -- Clone the repository https://github.com/nandinibarman94/metadata-tracker.git
     -- Build the docker file using `docker build -t metadata-tracker-image:1.0 .`
     --Run the container using `docker run -it -p 8000:8080 metadata-tracker-image:1.0`.
     You can also pass an environment variable DB_FILE in your docker run command like `docker run -it -e DB_FILE=<yourDBName.db> -p 8000:8080 metadata-tracker-image:1.0`. If you do not pass any env variable, MetadataTracker.db would be created as your default DB.
     -- Run `poetry run alembic upgrade head`- This will create the database and tables in the database for you. Additionally, it will create a row in the sourcesystem table as master data. You can run the below commands in sqlite CLI to verify the same. I passed 'MDTracker.db' in DB_FILE env variable.
    ==============================================================================================
        PS C:\assignment\metadata-tracker> docker run -it -e DB_FILE=MDTracker.db  -p 8000:8080 metadata-tracker-image:1.0
        root@f71cac56e9ed:/metadata-tracker# poetry run alembic upgrade head
        Skipping virtualenv creation, as specified in config file.
        INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
        INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
        INFO  [alembic.runtime.migration] Running upgrade  -> efb5de449e26, database setup
        INFO  [alembic.runtime.migration] Running upgrade efb5de449e26 -> 40f463d0dd64, insert default source system
        root@f71cac56e9ed:/metadata-tracker# sqlite3 MDTracker.db
        SQLite version 3.46.1 2024-08-13 09:16:08
        Enter ".help" for usage hints.
        sqlite> .databases
        main: /metadata-tracker/MDTracker.db r/w
        sqlite> .tables
        alembic_version  dataelements     datasets         sourcesystems  
        sqlite> select * from sourcesystems;
        1|OrderDB|data-team|2026-03-17 19:39:38|admin|2026-03-17 19:39:38|admin
        sqlite> .exit
        root@f71cac56e9ed:/metadata-tracker# 
   ==============================================================================================
    -- Run `poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8080` to start the application 
    -- Navigate to `http://localhost:8000/docs` to see the Swagger UI.
    --  Run `poetry run pytest -v` if you want to run the test cases.
    

