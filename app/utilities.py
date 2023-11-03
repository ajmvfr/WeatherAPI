from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, inspect
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def compareFloatNumbers(a : float, b : float):
    retval = False
    try:
        a_float = float(a)
        b_float = float(b)
        retval = (abs(a_float - b_float) < 1e-9)
    except:
        retval = False
    # finally:
    #     retval = False
    return retval


def convert_list_to_model(listobj):
    NewDict = dict()

    for row in listobj:
        NewDict.update(row._asdict())
    
    return NewDict