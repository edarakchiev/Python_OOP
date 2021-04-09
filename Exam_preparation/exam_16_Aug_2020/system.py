from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as context:
            return str(context)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_used_memory = sum(s.memory_consumption for s in System._software)
        total_memory = sum(h.memory for h in System._hardware)
        total_used_space = sum(s.capacity_consumption for s in System._software)
        total_capacity = sum(h.capacity for h in System._hardware)



        result = [f"System Analysis"]
        result.append(f"Hardware Components: {len(System._hardware)}")
        result.append(f"Software Components: {len(System._software)}")
        result.append(f"Total Operational Memory: {total_used_memory} / {total_memory}")
        result.append(f"Total Capacity Taken: {total_used_space} / {total_capacity}")

        return "\n".join(result)

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            result += f"Express Software Components: {len(System.get_express_software(hardware.software_components))}\n"
            result += f"Light Software Components: {len(System.get_light_software(hardware.software_components))}\n"
            result += f"Memory Usage: {hardware.memory - hardware.free_memory} / {hardware.memory}\n"
            result += f"Capacity Usage: {hardware.capacity - hardware.free_capacity} / {hardware.capacity}\n"
            result += f"Type: {hardware.type}\n"
            soft_comps = [s.name for s in hardware.software_components]
            if not soft_comps:
                result += "None"
            else:
                result += f"Software Components: {', '.join(soft_comps)}"
        return result

    @staticmethod
    def get_light_software(soft_list):
        return [s for s in soft_list if s.type == "Light"]

    @staticmethod
    def get_express_software(soft_list):
        return [s for s in soft_list if s.type == "Express"]

