import csv_reader
from Laptop import Laptop, heap_sort_by_CPU_speed_in_GHz_ascending, bubble_sort_by_amount_of_RAM_descending


def main():
    laptops = csv_reader.csv_to_laptops_converter('laptops1.csv')
    bubble_sort_by_amount_of_RAM_descending(laptops)
    heap_sort_by_CPU_speed_in_GHz_ascending(laptops)


if __name__ == '__main__':
    main()
