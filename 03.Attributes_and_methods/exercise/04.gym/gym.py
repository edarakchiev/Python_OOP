class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_subscription(sub_list, sub_id):
        result = [sub for sub in sub_list if sub.id == sub_id][0]
        if result:
            return result

    @staticmethod
    def get_trainer(trainer_list, trainer_id):
        result = [trainer for trainer in trainer_list if trainer.id == trainer_id][0]
        if result:
            return result

    @staticmethod
    def get_customer(customer_list, customer_id):
        result = [customer for customer in customer_list if customer.id == customer_id][0]
        if result:
            return result

    @staticmethod
    def get_plan(plan_list, plan_id):
        result = [plan for plan in plan_list if plan.id == plan_id][0]
        if result:
            return result

    @staticmethod
    def get_equipment(equipment_list, equipment_id):
        result = [e for e in equipment_list if e.id == equipment_id][0]
        if result:
            return result

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, exercise_plan):
        if exercise_plan not in self.plans:
            self.plans.append(exercise_plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_subscription(self.subscriptions, subscription_id)
        trainer_id = subscription.trainer_id
        customer_id = subscription.customer_id
        plan_id = subscription.exercise_id

        trainer = self.get_trainer(self.trainers, trainer_id)
        customer = self.get_customer(self.customers, customer_id)
        plan = self.get_plan(self.plans, plan_id)

        equipment_id = plan.equipment_id
        current_equipment = self.get_equipment(self.equipment, equipment_id)

        return f"{subscription}\n{customer}\n{trainer}\n{current_equipment}\n{plan}"