import pytest
from ApiModels.dataElementModel import CreateDataElement

def testPrimaryKeyValidationError():
    payload = {
        "name": "id",
        "datatype": "int",
        "isPrimary": True,
        "isUnique": False,
        "createdBy": "admin",
        "updatedBy": "admin"
    }

    with pytest.raises(ValueError):
        CreateDataElement(**payload)