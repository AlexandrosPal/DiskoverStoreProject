sales_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["order_id", "product_id", "quantity", "price", "revenue", "date"],
        "properties": {
            "order_id": {
                "bsonType": "string",
                "description": "A unique ID for an order",
                # Example: "O001"
            },
            "product_id": {
                "bsonType": "string",
                "description": "A unique ID refrencing a product from the products_collection",
                # Example: "D001"
            },
            "quantity": {
                "bsonType": "int",
                "description": "The quantity of products sold",
                # Example: 5
            },
            "price": {
                "bsonType": "int",
                "description": "The price of the product sold",
                # Example: 50
            },
            "revenue": {
                "bsonType": "int",
                "description": "The revenue from the curret sale/order. It is calculated with price * quantity",
                # Example: 250
            },
            "date": {
                "bsonType": "string",
                "description": "The date in which the sale/order was made",
                # Example: 2023-11-16 22:55:00
            },
        }
    }
}
