import hashlib
import subprocess

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def greet(name):
    return f"Hello, {name}!"

def run_command(user_input):
    return subprocess.run(user_input, shell=True)


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def calculate(expression):
    return eval(expression)