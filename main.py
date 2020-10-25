import timeit
from datetime import timedelta

from Laptop import Laptop, heap_sort_by_CPU_speed_in_GHz_ascending


def main():
    first_laptop = Laptop(14, 16, "Glucklich")
    second_laptop = Laptop(200, 40, "Henry")
    third_laptop = Laptop(100, 50, "Kless")
    laptops = [first_laptop, second_laptop, third_laptop]
    Laptop.bubble_sort_by_amount_of_RAM_descending(laptops)
    heap_sort_by_CPU_speed_in_GHz_ascending(laptops)


if __name__ == '__main__':
    main()
