import sys

"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


my_precious_logger("error: file not found")
# stderr
'error: file not found'


my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout
"""


def my_precious_logger(text: str):
    list_text = text.strip()
    first_word = list_text[0]
    if first_word == 'error':
        return sys.stderr.write(text)
    else:
        return sys.stdout.write(text)
