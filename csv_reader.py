from Laptop import Laptop
import csv


def csv_to_laptops_converter(file_name: str):
    laptops = []
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            laptops.append(Laptop(int(row[0]), int(row[1]), row[2]))
        return laptops
