from enum import Enum

class PaymentType(Enum):

    CREDIT_CARD = 'Credit Card'
    CASH = 'Cash'
    CHECK = 'Check'
    OTHER = 'Other'