from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.free_capacity = capacity
        self.free_memory = memory

    def install(self, software: Software):
        if software.capacity_consumption > self.free_capacity or software.memory_consumption > self.free_memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)
        self.free_capacity -= software.capacity_consumption
        self.free_memory -= software.memory_consumption

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.free_capacity += software.capacity_consumption
        self.free_memory += software.memory_consumption
