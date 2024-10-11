# Example of a tuple
import boto3
import os
from loguru import logger
import json
my_tuple = (1, 2, 3, 'apple', 'banana')
print("This is a tuple")
print(my_tuple)

print("this is tuple my_tuple[0]")
print(my_tuple[0])  # Output: 1


print("this is tuple my_tuple[0]")
print(my_tuple[0])  # Output: 1

print("this is tuple my_tuple[3]")
print(my_tuple[3])  # Output: 'apple'

local_directory = 'home/Tbone/PYTHONTRASHME'

if not os.path.exists(local_directory):
	os.makedirs(local_directory)
	logger.info("Directory successfully created")
if os.path.exists(local_directory):
	os.rmdir(local_directory)
	logger.error("Directory succesfully removed")
single_tuple = (5,)
logger.info(my_tuple)
print(single_tuple)
