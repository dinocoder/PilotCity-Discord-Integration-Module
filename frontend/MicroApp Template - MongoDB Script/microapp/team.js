use microapp;

db.createCollection( "team",{
    "storageEngine": {
        "wiredTiger": {}
    },
    "capped": false,
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "title": "team",
            "additionalProperties": false,
            "properties": {
                "_id": {
                    "bsonType": "objectId"
                },
                "teamName": {
                    "bsonType": "string"
                },
                "user_ids": {
                    "bsonType": "array",
                    "additionalItems": true,
                    "uniqueItems": true,
                    "items": {
                        "bsonType": "objectId"
                    }
                }
            },
            "required": [
                "_id",
                "teamName",
                "user_ids"
            ]
        }
    },
    "validationLevel": "off",
    "validationAction": "warn"
});