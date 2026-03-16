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

