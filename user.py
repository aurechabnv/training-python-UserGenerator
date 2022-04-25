import logging
import faker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(level=logging.INFO,
                    filename= BASE_DIR / "user.log",
                    filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

fake = faker.Faker()

def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(n: int):
    """Generate multiple users

    Args:
        n (int): Total of users to generate

    Returns:
        list[str]: List of users
    """
    logging.info(f"Generating a list of {n} users")
    return [get_user() for _ in range(n)]

if __name__ == "__main__":
    print(get_users(n=3))