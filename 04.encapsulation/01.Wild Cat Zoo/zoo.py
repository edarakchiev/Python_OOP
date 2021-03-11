class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @staticmethod
    def get_worker(worker_list, worker_name):
        if worker_list:
            worker = [worker for worker in worker_list if worker.name == worker_name][0]
            return worker

    @staticmethod
    def get_salary_all_workers(workers_list):
        return sum([float(worker.salary) for worker in workers_list])

    @staticmethod
    def needed_money_for_animals(animals_list):
        return sum([animal.get_needs() for animal in animals_list])

    @staticmethod
    def get_lions(animals_list):
        return [lion for lion in animals_list if lion.type == "Lion"]

    @staticmethod
    def get_tigers(animals_list):
        return [tiger for tiger in animals_list if tiger.type == "Tiger"]

    @staticmethod
    def get_cheetahs(animals_list):
        return [cheetah for cheetah in animals_list if cheetah.type == "Cheetah"]

    @staticmethod
    def get_keepers(workers_list):
        return [keeper for keeper in workers_list if keeper.type == "Keeper"]

    @staticmethod
    def get_caretaker(workers_list):
        return [caretaker for caretaker in workers_list if caretaker.type == "Caretaker"]

    @staticmethod
    def get_vet(workers_list):
        return [vet for vet in workers_list if vet.type == "Vet"]

    def add_animal(self, animal, price):
        if price > self.__budget:
            return "Not enough budget"
        elif len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        # self.__animal_capacity -= 1
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.type} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        # self.__workers_capacity -= 1
        self.workers.append(worker)
        return f"{worker.name} the {worker.type} hired successfully"

    def fire_worker(self, worker_name):
        worker = self.get_worker(self.workers, worker_name)
        if not worker:
            return f"There is no {worker_name} in the zoo"
        # self.__workers_capacity += 1
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = self.get_salary_all_workers(self.workers)
        if salaries > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {int(self.__budget)}"

    def tend_animals(self):
        need_money = self.needed_money_for_animals(self.animals)
        if need_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= need_money
        return f"You tended all the animals. They are happy. Budget left: {int(self.__budget)}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = self.get_lions(self.animals)
        tigers = self.get_tigers(self.animals)
        cheetah = self.get_cheetahs(self.animals)
        result = f"You have {len(self.animals)} animals\n"
        if lions:
            result += f"----- {len(lions)} Lions:\n"
            result += '\n'.join([f'{lion}' for lion in lions])
            result += "\n"
        if tigers:
            result += f"----- {len(tigers)} Tigers:\n"
            result += '\n'.join([f'{tiger}' for tiger in tigers])
            result += "\n"
        if cheetah:
            result += f"----- {len(cheetah)} Cheetahs:\n"
            result += '\n'.join([f'{cheet}' for cheet in cheetah])
            #result += "\n"
        return result

    def workers_status(self):
        keepers = self.get_keepers(self.workers)
        caretakers = self.get_caretaker(self.workers)
        vets = self.get_vet(self.workers)
        result = f"You have {len(self.workers)} workers\n"
        if keepers:
            result += f"----- {len(keepers)} Keepers:\n"
            result += '\n'.join([f'{keeper}' for keeper in keepers])
            result += "\n"
        if caretakers:
            result += f"----- {len(caretakers)} Caretakers:\n"
            result += '\n'.join([f'{caretaker}' for caretaker in caretakers])
            result += "\n"
        if vets:
            result += f"----- {len(vets)} Vets:\n"
            result += '\n'.join([f'{vet}' for vet in vets])
            # result += "\n"
        return result
