import uuid
import random
from dataclasses import dataclass
from Locations import locations
from faker import Faker
import time
import datetime
import csv
from kafka import KafkaProducer

@dataclass
class Transaction:
    transaction_id:str
    transaction_type:str
    location:dict #categorized into city,state and coast
    gender:str
    sale_amount:int


def transaction_generator()->Transaction:
    gender = ['male','female','rather not say']
    sale = round(random.uniform(1.00, 100.00), 2)
    trasaction_type = ['Credit','Debit','Cash','Refund_Credit','Gift_Card']
    transaction:Transaction = Transaction(
        transaction_id=uuid.uuid4(), #transaction id
        transaction_type=random.choice(trasaction_type), #Random trasaction type
        location= random.choice(locations), #choose random location
        gender= random.choice(gender),
        sale_amount=  sale #choose a random sale amount
        )
    return transaction


def create_csv_file():
    # Get current timestamp in a string format to be used in the file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"transactions_{timestamp}.csv"
    
    # Open the file in write mode and create the CSV writer
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers
        writer.writerow([
                          'transaction_id',
                          'transaction_type', 
                          'gender',
                          'city',
                          'state',
                          'coast',
                          'sale_amount'
                          ])
        
    return filename



if __name__ == '__main__':
    filename = create_csv_file()
    while True:
        transaction = transaction_generator()
        print(transaction)
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                transaction.transaction_id,
                transaction.transaction_type,
                transaction.gender,
                transaction.location["city"],
                transaction.location["state"],
                transaction.location["coast"],
                transaction.sale_amount
            ])
        time.sleep(1)

