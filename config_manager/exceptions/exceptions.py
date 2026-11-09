class ConfigError(Exception):
    """Базовий виняток для помилок конфігурації."""
    pass

class ValidationError(ConfigError):
    """Помилка валідації даних."""
    pass

class BusinessLogicError(ConfigError):
    """Помилка бізнес-логіки."""
    pass