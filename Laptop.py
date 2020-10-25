import timeit
from datetime import timedelta
from timeit import default_timer as timer
import counters


class Laptop:
    def __init__(self, CPU_speed_in_GHz, amount_of_RAM, manufacturer_name):
        self.CPU_speed_in_GHz = CPU_speed_in_GHz
        self.amount_of_RAM = amount_of_RAM
        self.manufacturer_name = manufacturer_name

    def __str__(self):
        return "== Manufacturer:" + self.manufacturer_name + "; CPU_speed_in_GHz:" + str(
            self.CPU_speed_in_GHz) + "; amount_of_RAM:" + str(self.amount_of_RAM)

    @staticmethod
    def bubble_sort_by_amount_of_RAM_descending(laptops):
        start_time = timer()
        print("---------------------------------------------------")
        print("BUBBLESORT:\n")
        n = len(laptops)
        for i in range(n - 1):
            has_swapped = 0
            for j in range(n - 1):
                counters.bubble_comparison_number = counters.bubble_comparison_number + 2
                if laptops[j].amount_of_RAM < laptops[j + 1].amount_of_RAM:
                    laptops[j], laptops[j + 1] = laptops[j + 1], laptops[j]
                    counters.bubble_swap_number = counters.bubble_swap_number + 1
                    has_swapped = 1
                if has_swapped == 0:
                    break
        elapsed_time = timedelta(seconds=timer() - start_time)
        for x in range(len(laptops)):
            print(laptops[x])
        print("\nExecution duration:")
        print(str(elapsed_time)[6:] + "s")
        print("\nComparisons number:")
        print(counters.bubble_comparison_number)
        print("\nSwaps number:")
        print(counters.bubble_swap_number)


def heap_sort_by_CPU_speed_in_GHz_ascending(laptops):
    start_time = timer()
    print("---------------------------------------------------")
    print("HEAPSORT:\n")
    n = len(laptops)
    i = n // 2
    for i in range(n, -1, -1):
        heapify(laptops, n, i)

    i = n
    for i in range(n - 1, 0, -1):
        laptops[i], laptops[0] = laptops[0], laptops[i]
        counters.heap_swap_number = counters.heap_swap_number + 1
        heapify(laptops, i, 0)
    elapsed_time = timedelta(seconds=timer() - start_time)
    for x in range(len(laptops)):
        print(laptops[x])
    print("\nExecution duration:")
    print(str(elapsed_time)[6:] + "s")
    print("\nComparisons number:")
    print(counters.heap_comparison_number)
    print("\nSwaps number:")
    print(counters.heap_swap_number)


def heapify(laptops, n, i):
    largest = i
    l = 2 * i
    r = 2 * i + 1
    counters.heap_comparison_number = counters.heap_comparison_number + 3
    if l < n and laptops[l].CPU_speed_in_GHz > laptops[largest].CPU_speed_in_GHz:
        largest = l
    if r < n and laptops[r].CPU_speed_in_GHz > laptops[largest].CPU_speed_in_GHz:
        largest = r
    if largest != i:
        laptops[largest], laptops[i] = laptops[i], laptops[largest]
        counters.heap_swap_number = counters.heap_swap_number + 1
        heapify(laptops, n, largest)
