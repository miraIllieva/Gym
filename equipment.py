from project.subscription import Subscription
class Equipment:
    id = 1

    def __init__(self, name: str):
        self.id = Equipment.id
        self.name = name
        Equipment.id += 1

    @staticmethod
    def get_next_id():
        return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
