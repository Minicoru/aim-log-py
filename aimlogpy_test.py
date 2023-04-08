from aimlogpy import *
import os

# Test case for aimlog with a boolean log_message


def test_aimlog_with_boolean():
    log_message = True
    assert aimlog(log_message) == True
    # Assert that the log file was created
    assert os.path.exists(
        f"{datetime.now().isoformat().split('T')[0]}.log") == True

# Test case for aimlog with a float log_message


def test_aimlog_with_float():
    log_message = 3.14
    assert aimlog(log_message) == True
    # Assert that the log file was created
    assert os.path.exists(
        f"{datetime.now().isoformat().split('T')[0]}.log") == True

# Test case for aimlog with a complex log_message


def test_aimlog_with_complex():
    log_message = complex(2, 3)
    assert aimlog(log_message) == True
    # Assert that the log file was created
    assert os.path.exists(
        f"{datetime.now().isoformat().split('T')[0]}.log") == True

# Test case for aimlog with a custom object log_message


def test_aimlog_with_custom_object():
    class CustomObject:
        def __str__(self):
            return "CustomObject"
    log_message = CustomObject()
    assert aimlog(log_message) == True
    # Assert that the log file was created
    assert os.path.exists(
        f"{datetime.now().isoformat().split('T')[0]}.log") == True

# Test case for aimlog with an empty log_message


def test_aimlog_with_empty():
    log_message = ""
    assert aimlog(log_message) == True
    # Assert that the log file was created
    assert os.path.exists(
        f"{datetime.now().isoformat().split('T')[0]}.log") == True
