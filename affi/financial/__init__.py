
class TransactionType:
    DEPOSIT = 'deposit'
    RECEIVED = 'RECEIVED'

    CHOICES = [
        (DEPOSIT, 'deposit'),
        (RECEIVED, 'RECEIVED')
    ]


class TransactionState:
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'

    CHOICES = [
        (PENDING, 'pending'),
        (SUCCESS, 'success'),
        (FAILED, 'failed')
    ]