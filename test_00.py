import os

def bar():
  user_input = input("Enter filename: ")
  with open(user_input, 'r') as file:  # Vulnerable to directory traversal
    content = file.read()

def foo():
  directory = input("Enter the directory to list: ")
  command = f"ls {directory}"
  os.system(command)
