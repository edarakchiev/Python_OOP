class Subscription:
    class_id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_id()

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

    @classmethod
    def get_id(cls):
        cls.class_id = cls.class_id + 1
        return cls.class_id

    @staticmethod
    def get_next_id():
        return Subscription.class_id + 1