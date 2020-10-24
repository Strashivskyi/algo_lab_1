class Laptop:
    def __init__(self, CPU_speed_in_GHz, amount_of_RAM, manufacturer_name):
        self.CPU_speed_in_GHz = CPU_speed_in_GHz
        self.amount_of_RAM = amount_of_RAM
        self.manufacturer_name = manufacturer_name

    def __str__(self):
        return "[Manufacturer:" + self.manufacturer_name + "; CPU_speed_in_GHz:" + str(self.CPU_speed_in_GHz) + "; amount_of_RAM:" + str(self.amount_of_RAM) + ";]"

    @staticmethod
    def bubble_sort_by_amount_of_RAM_descending(laptops):
        print("\nBUBBLESORT:\n")
        n = len(laptops)
        for i in range(n - 1):
            has_swapped = 0
            for j in range(n - 1):
                if laptops[j].amount_of_RAM < laptops[j + 1].amount_of_RAM:
                    laptops[j], laptops[j + 1] = laptops[j + 1], laptops[j]
                    has_swapped = 1
                if has_swapped == 0:
                    break


def heap_sort_by_CPU_speed_in_GHz_ascending(laptops):
    print("\nHEAPSORT:\n")
    n = len(laptops)
    i = n // 2
    for i in range(n, -1, -1):
        heapify(laptops, n, i)
    i = n
    for i in range(n - 1, 0, -1):
        laptops[i], laptops[0] = laptops[0], laptops[i]
        heapify(laptops, i, 0)


def heapify(laptops, n, i):
    largest = i
    l = 2 * i
    r = 2 * i + 1
    if l < n and laptops[l].CPU_speed_in_GHz > laptops[largest].CPU_speed_in_GHz:
        largest = l
    if r < n and laptops[r].CPU_speed_in_GHz > laptops[largest].CPU_speed_in_GHz:
        largest = r
    if largest != i:
        laptops[largest], laptops[i] = laptops[i], laptops[largest]
        heapify(laptops, n, largest)
