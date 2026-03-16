from unittest.mock import patch, MagicMock

def testGetElements(client):
    mockResponse = [
        {
            "id": 1,
            "name": "customer_id",
            "datatype": "int",
            "datasetName": "customers",
            "pii": False,
            "isActive": True,
            "isPrimary": True,
            "isUnique": True,
            "isNullable": False,
            "createdOn": "2026-01-01T00:00:00",
            "createdBy": "admin",
            "updatedOn": "2026-01-01T00:00:00",
            "updatedBy": "admin"
        }
    ]
    mockGet = MagicMock(return_value=mockResponse)

    with patch("repository.getDataElements", mockGet):
        response = client.get("/elements")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "customer_id"