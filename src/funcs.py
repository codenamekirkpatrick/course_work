import os
import json
from datetime import datetime


def get_list_from_json():
    path_operations = os.path.join("..", "operations", "operations.json")
    with open(path_operations, encoding="utf-8") as file:
        operations = json.load(file)
    return operations

get_list_from_json()

def show_five_last_transactions(operations):
    if len(operations) < 5:
        last_five_operations = operations
    else:
        last_five_operations = operations[-5:]

    for transaction in last_five_operations:
        print(f"{transaction['date']} {transaction['description']}")
        print(f"{transaction['from']} {transaction['to']}")
        print(f"{transaction['from']} {transaction['to']}")
        print(f"{transaction['amount']}")
