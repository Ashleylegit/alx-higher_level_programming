#!/usr/bin/python3
""" A function that prints My name is <first name> <last name> """

def say_my_name(first_name, last_name=""):
    """
    1. first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
    2. You are not allowed to import any module
    """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
