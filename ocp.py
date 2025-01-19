## Exemplo ruim


class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processando pagamento de {amount} com cartão de crédito.")
        elif payment_type == "paypal":
            print(f"Processando pagamento de {amount} com PayPal.")


## Exemplo bom

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount): ...


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return super().process_payment(amount)


class MercadoPagoPayment(PaymentProcessor):
    def process_payment(self, amount):
        return super().process_payment(amount)
