from passlib.hash import sha256_crypt


class HashService:

    def hash(self, string: str) -> str:
        return sha256_crypt.hash(string)

