users = {
    "123": {
        "name": "John Doe",
        "email": "john@example.com",
        "friends": ["456", "789"],
        "posts": ["101", "102"],
        "activity": {
            "likes": ["201", "202"],
            "comments": ["301", "302"]
        }
    },
    # Additional users with similar complex structure...
}

posts = {
    "101": {
        "title": "My First Post",
        "content": "Hello World!",
        "comments": ["301", "302"],
        "likes": 10,
        "tags": ["adventure", "travel"],
        "updated_at": "2023-12-01T12:00:00Z"
    },
    # Additional posts with similar complex structure...
}

comments = {
    "301": {
        "user_id": "123",
        "content": "Great post!",
        "likes": 3,
        "replies": ["401"],
        "created_at": "2023-12-02T15:30:00Z"
    },
    # Additional comments with similar complex structure...
}