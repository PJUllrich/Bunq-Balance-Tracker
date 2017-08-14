import random

from model import Key, User
from tests.rules.base import BaseRule


class UserRule(BaseRule):
    @classmethod
    def create(cls):
        rand_env = random.choice(['Sandbox', 'Production'])
        rand_chat_id = random.randint(1000, 1000000)
        rand_key_auth = Key(cls.faker.sha256().encode(), cls.faker.sha256().encode())
        rand_key_api = Key(cls.faker.sha256().encode(), cls.faker.sha256().encode())

        return User(rand_env, rand_chat_id, rand_key_auth, rand_key_api)