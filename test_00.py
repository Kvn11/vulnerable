import os


def main():
  directory = input("Enter the directory to list: ")
  command = f"ls {directory}"
  os.system(command)
