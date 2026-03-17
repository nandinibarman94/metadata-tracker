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
  - Clone the repository https://github.com/nandinibarman94/metadata-tracker.git
  - Build the docker file using `docker build -t metadata-tracker-image:1.0 .`
  - Run the container, do not miss setting up the ENV variable `DB_FILE` using `docker run -it  -e DB_FILE=<your db filepath.db> -p 8000:8080 metadata-tracker-image:1.0`.
    Below is an example of docker run command- `docker run -it  -e DB_FILE=sqlite/MDTracker.db -p 8000:8080 metadata-tracker-image:1.0`
  - Create a database using `sqlite3 <dbname.db>`. 
  - Check if your database is created using `.databases`
  - Type .exit to move out of the sqlite environment
  - If you want to double check, then run the `ls` command to make sure your db is created in the right place.
    *Below is a step by step illustration of creating the db:*
    ----------------------------------------------------------
    root@8878073208e1:/metadata-tracker# mkdir sqlite
    root@8878073208e1:/metadata-tracker# cd sqlite
    root@8878073208e1:/metadata-tracker/sqlite# sqlite3 MDTracker.db
    SQLite version 3.46.1 2024-08-13 09:16:08
    Enter ".help" for usage hints.
    sqlite> .databases
    main: /metadata-tracker/sqlite/MDTracker.db r/w
    sqlite> .exit
    root@8878073208e1:/metadata-tracker/sqlite# ls
    MDTracker.db
    ----------------------------------------------------
  - Move to the root folder metadata-tracker and run the alembic upgrade command to create the three tables.
    `poetry run alembic upgrade head`
  - You can verify if your tables are created using the `.tables` command inside the sqlite environment.
  - The sourcesystem is already populated with one entry. Use the select statement to check the row.
    *Below is a step by step illustration of the above points.*
   ------------------------------------------------------------
    root@85ac74f5cf9f:/metadata-tracker/sqlite# cd ..
    root@85ac74f5cf9f:/metadata-tracker# poetry run alembic upgrade head
    Skipping virtualenv creation, as specified in config file.
    INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.runtime.migration] Running upgrade  -> efb5de449e26, database setup
    INFO  [alembic.runtime.migration] Running upgrade efb5de449e26 -> 40f463d0dd64, insert default source system
    root@85ac74f5cf9f:/metadata-tracker# cd sqlite
    root@85ac74f5cf9f:/metadata-tracker/sqlite# sqlite MDTracker.db
    bash: sqlite: command not found
    root@85ac74f5cf9f:/metadata-tracker/sqlite# sqlite3 MDTracker.db
    SQLite version 3.46.1 2024-08-13 09:16:08
    Enter ".help" for usage hints.
    sqlite> .tables
    alembic_version  dataelements     datasets         sourcesystems  
    sqlite> select * from sourcesystems;
    1|OrderDB|data-team|2026-03-17 14:48:40|admin|2026-03-17 14:48:40|admin
    sqlite> .exit
    root@85ac74f5cf9f:/metadata-tracker/sqlite#
   ----------------------------------------------------------
   - Go to the root folder metadata-tracker and run the uvicorn command `poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8080`
   - You can navigate to `http://localhost:8000/docs` to see the Swagger UI.
    

