import random


def generate_random_ip_address():
    """
    Generates a random IP address.
    :return: A string representing an IP address.
    """
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))


def __main():
    random_ip = generate_random_ip_address()
    return


if __name__ == "__main__":
    __main()
