class Laptop:
    def __init__(self, CPU_speed_in_GHz, amount_of_RAM, manufacturer_name):
        self.CPU_speed_in_GHz = CPU_speed_in_GHz
        self.amount_of_RAM = amount_of_RAM
        self.manufacturer_name = manufacturer_name

    def __str__(self):
        return "== Manufacturer:" + self.manufacturer_name + "; CPU_speed_in_GHz:" + str(
            self.CPU_speed_in_GHz) + "; amount_of_RAM:" + str(self.amount_of_RAM)


