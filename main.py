import csv_reader
from Laptop import Laptop
from sort_functions import bubble_sort_by_amount_of_RAM_descending, heap_sort_by_CPU_speed_in_GHz_ascending


def main():
    laptops = csv_reader.csv_to_laptops_converter('laptops1.csv')
    bubble_sort_by_amount_of_RAM_descending(laptops)
    heap_sort_by_CPU_speed_in_GHz_ascending(laptops)


if __name__ == '__main__':
    main()
