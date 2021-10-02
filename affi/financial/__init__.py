
class TransactionType:
    DEPOSIT = 'deposit'
    RECEIVED = 'received'

    CHOICES = [
        (DEPOSIT, 'deposit'),
        (RECEIVED, 'received')
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