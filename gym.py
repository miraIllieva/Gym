
from project.customer import Customer
from project.equipment import Equipment
from project.trainer import Trainer
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        """
        Retrieves and formats subscription details by ID.
        """

        # Find the subscription by ID
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        if not subscription:
            return f"Subscription with ID {subscription_id} not found."

        # Find the related customer, trainer, equipment, and plan using the subscription data
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        equipment = next((e for e in self.equipment if e.id == subscription.exercise_id), None)
        plan = next((p for p in self.plans if p.trainer_id == subscription.trainer_id and p.equipment_id == subscription.exercise_id), None)

        if not all([customer, trainer, equipment, plan]):
            return f"Some details are missing for subscription ID {subscription_id}."

        # Return formatted information
        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"


