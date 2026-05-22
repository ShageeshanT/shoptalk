from dataclasses import dataclass


@dataclass(frozen=True)
class DemoScenario:
    name: str
    customer_message: str
    expected_intent: str


HOME_BAKER_SCENARIOS = [
    DemoScenario('birthday cake inquiry', 'Can I order a 1kg chocolate cake for Saturday?', 'new_order'),
    DemoScenario('payment check', 'Did you receive my deposit payment?', 'payment_question'),
    DemoScenario('delivery question', 'Can you deliver to Malabe?', 'delivery_question'),
]
