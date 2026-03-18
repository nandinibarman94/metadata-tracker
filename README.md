# Metadata Management System

## Database Schema Overview

Three tables have been created: `sourcesystems`, `datasets`, and `dataelements`.

### Relationships (Cardinality)

- `sourcesystems` → `datasets`: One to Many (Each combination of sourceSystem and owner can have multiple datasets, but each dataset belongs to exactly one combination)
- `datasets` → `dataelements`: One to Many (Each dataset can have multiple data elements, but each data element belongs to exactly one dataset)

### Constraints and Considerations

- `name` and `owningApplication` in `sourcesystems` form a composite unique key
- `name` and `sourceSystemId` in `datasets` form a composite unique key (tables can be duplicate across databases, but not within)
- `name` and `datasetId` in `dataelements` form a composite unique key (columns can be duplicate across tables, but not within the same table)

## API Details

### Dataset APIs

| Endpoint | Method | Params | Status Codes | Description |
|----------|--------|--------|--------------|-------------|
| `/datasets` | POST | - | 200, 404,422, 500 | Create a new dataset in the metadata catalog |
| `/datasets` | GET | - | 200, 500 | Retrieve all datasets |
| `/datasets/{datasetId}` | GET | `datasetId` (int) | 200, 404, 422 | Retrieve a dataset and its associated data elements by ID |

### Data Elements APIs

| Endpoint | Method | Params | Status Codes | Description |
|----------|--------|--------|--------------|-------------|
| `/elements` | POST | `datasetId` (int) | 200, 404, 422, 500 | Create a new data element and associate it with a dataset |
| `/elements` | GET | `datasetId` (int), `pii` (bool), `datatype` (str) | 200, 422 | Retrieve data elements with optional filters |

### Source Systems API
| Endpoint | Method | Params | Status Codes | Description |
|----------|--------|--------|--------------|-------------|
| `/sourcesystems` | GET | - | 200, 500 | Retrieve all sourcesystems |

### Request/Response Models

- **Request Models**: `CreateDataset` (for POST /datasets), `CreateDataElement` (for POST /elements)
- **Response Models**: `GetDataset`, `GetDatasetWithElements`, `GetDataElement`, `GetSourceSystem`

## Validation Rules

* Validation rules enforce data integrity for primary key columns in the `dataelements` entity:

- When `isPrimary = True`:
  - `isUnique` is automatically set to True if not explicitly provided
  - `isNullable` is automatically set to False if not explicitly provided
  - Raises validation error if `isUnique` is explicitly set to False
  - Raises validation error if `isNullable` is explicitly set to True

* The `datatype` column for the data elements must be one of the predefined enum values (char, varchar, integer, decimal, numeric, float, double, boolean, date, time, timestamp or uuid)

## Steps to Run the Application

### Without Docker

**Prerequisites**: Python ≥3.14, Poetry, SQLite

```bash
git clone https://github.com/nandinibarman94/metadata-tracker.git
cd metadata-tracker
poetry install
poetry run alembic upgrade head
poetry run uvicorn src.main:app --reload
```
--`poetry run alembic upgrade head` - This will create the database(MetadataTracker.db) and the tables in the database for you. Additionally, it will create a row in the sourcesystem table as master data. You can use the `GET /sourcesystems/` endpoint to view the sourcesystem inserted.
-- Navigate to `http://localhost:8000/docs` for Swagger UI. 
-- Run tests with `poetry run pytest -v`.

### With Docker

```bash
git clone https://github.com/nandinibarman94/metadata-tracker.git
docker compose up
```
-- You can provide a different DB name of your choice in the docker compose file,  default : MetadataTracker.db.
-- No need to run migrations manually. The database and tables are created as part of the migration. A default row is inserted into the sourcesystems table as master data during initialization. Use the `GET /sourcesystems` endpoint to view the sourcesystem inserted.
-- Navigate to `http://localhost:8000/docs` for Swagger UI. 

## Enhancements and Improvements

 * Authorization & Authentication
 * Relationships between datasets
 * Considering unique data elements.
 