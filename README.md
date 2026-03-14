Metadata Management System

## Database Schema Overview
#Three tables have been created (databases, datasets, dataelements)

#Relationships (Cardinality)
-- 'databases'-> 'datasets' - One to Many (Each database can have multiple datasets, but each dataset belongs to exactly one database)
-- 'datasets'-> 'dataelements '- One to Many (Each dataset can have multiple data elements, but each data element belongs to exactly one dataset)

#Constraints and Considerations
-- Same server instance has a unique database name
-- 'name' and 'dbId' in 'datasets' is a composite unique key as tables can be duplicate across databases, but not within databases
-- 'name' and 'datasetId' in 'dataelements' is a composite unique key as columns can be duplicate across tables, but not within the same table.

