import re
import pytest

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if re.match(pattern, email):
        return True
    else:
        return False

def test_validate_email_positive_1():
    assert validate_email("example@example.com") == True

def test_validate_email_positive_2():
    assert validate_email("first.last@example.co.uk") == True

def test_validate_email_positive_3():
    assert validate_email("first_last@example.io") == True

def test_validate_email_positive_4():
    assert validate_email("123456@example.com") == True

def test_validate_email_positive_5():
    assert validate_email("user.name+tag+sorting@example.com") == True


def test_validate_email_negative_1():
    assert validate_email("plainaddress") == False

def test_validate_email_negative_2():
    assert validate_email("@no-local-part.com") == False

def test_validate_email_negative_3():
    assert validate_email("Outlook User<outlook_user@example.com>") == False

def test_validate_email_negative_4():
    assert validate_email("no-at-domain.com") == False

def test_validate_email_negative_5():
    assert validate_email("user@.com") == False
