import json
import random
from typing import List

import faker

fake = faker.Faker()


def generate_users_pool(size: int):
    user_pool = []
    current_size = 0
    while current_size < size:
        user = {
            "id": current_size,
            "name": fake.name(),
            "age": random.randint(18, 35),
        }
        user_pool.append(user)
        current_size += 1
    return user_pool


def save_pool(pool: List[dict], filename: str):
    with open(filename, "w") as file:
        json.dump(pool, file, indent=4)


def __main():
    res = generate_users_pool(100)
    save_pool(res, "users.json")
    print(res)


if __name__ == "__main__":
    __main()
