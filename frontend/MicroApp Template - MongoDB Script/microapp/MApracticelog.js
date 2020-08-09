use microapp;

db.createCollection( "MApracticelog",{
    "storageEngine": {
        "wiredTiger": {}
    },
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "MApracticelog",
            "additionalProperties": false,
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "team_id": {
                    "bsonType": "objectId"
                },
                "log": {
                    "bsonType": "object",
                    "properties": {
                        "lastModified": {
                            "bsonType": "timestamp"
                        }
                    },
                    "additionalProperties": true,
                    "patternProperties": {
                        "^[a-zA-Z0-9_.-]+$": {
                            "bsonType": "int"
                        }
                    }
                }
            },
            "required": [
                "_id",
                "team_id"
            ]
        }
    },
    "validationLevel": "moderate",
    "validationAction": "error"
});