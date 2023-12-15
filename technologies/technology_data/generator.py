import json
import random
from typing import List

import faker

fake = faker.Faker()


def save_pool(pool: List[dict], filename: str):
    with open(filename, "w") as file:
        json.dump(pool, file, indent=4)


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


def generate_song_title(min_length: int = 3, max_length: int = 7):
    music_words = [
        "melodia", "harmonia", "ritmo", "batida", "acorde", "canção", "voz", "instrumento",
        "dança", "emoção", "alma", "sonho", "viagem", "liberdade", "amor", "dor", "esperança"
    ]
    num_words = random.randint(min_length, max_length)
    words = random.sample(music_words, num_words)
    title = " ".join(words)
    if random.random() > 0.5:
        title = title.upper()
    elif random.random() > 0.75:
        title = title[::-1]
    return title


def generate_song_pool(size: int):
    song_pool = []
    current_size = 0
    while current_size < size:
        song = {
            "id": current_size,
            "nome": generate_song_title(),
            "artista": fake.name(),
            "categoria": random.choice(["rock", "pop", "samba", "funk", "sertanejo", "rap", "indie", "metal"]),
            "data_lancamento": fake.date_between(start_date='-10y', end_date='today')
        }
        song_pool.append(song)
        current_size += 1
    return song_pool


def __main():
    # res = generate_users_pool(100)
    # save_pool(res, "users.json")
    # print(res)
    title = generate_song_title()
    return


if __name__ == "__main__":
    __main()
