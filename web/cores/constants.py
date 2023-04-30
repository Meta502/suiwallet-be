class SwaggerTag:
    TOP_UP = "Top Up"
    TRANSFER = "Transfer"
    INQUIRY = "Inquiry"
    VIRTUAL_ACCOUNT = "Virtual Account"
    AUTHENTICATION = "Authentication"

class DecimalConstant:
    MAX_DIGITS = 32
    DECIMAL_PLACES = 4 

TRANSACTION_TYPE_CHOICES = (
    ("all", "All"),
    ("top_up", "Top Up"),
    ("transfer", "Transfer"),
    ("virtual_account", "Virtual Account")
)
