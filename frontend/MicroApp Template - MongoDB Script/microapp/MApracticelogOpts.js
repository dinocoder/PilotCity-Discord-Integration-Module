use microapp;

db.createCollection( "MApracticelogOpts",{
    "storageEngine": {
        "wiredTiger": {}
    },
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "MApracticelogOpts",
            "additionalProperties": false,
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "instructions": {
                    "bsonType": "array",
                    "additionalItems": true,
                    "minItems": 1,
                    "maxItems": 5,
                    "uniqueItems": false,
                    "items": {
                        "bsonType": "string"
                    }
                },
                "minReq": {
                    "bsonType": "int",
                    "description": "minimum requirement to complete this microapp\n",
                    "minimum": -1
                },
                "goal": {
                    "bsonType": "int"
                }
            },
            "required": [
                "_id",
                "instructions",
                "minReq",
                "goal"
            ]
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});