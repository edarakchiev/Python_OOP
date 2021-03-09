class Trainer:
    class_id = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def get_id(cls):
        cls.class_id = cls.class_id + 1
        return cls.class_id

    @staticmethod
    def get_next_id():
        return Trainer.class_id + 1