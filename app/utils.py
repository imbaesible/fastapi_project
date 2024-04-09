from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    plain_password_encoded = plain_password.encode('utf-8')
    return pwd_context.verify(plain_password_encoded, hashed_password)