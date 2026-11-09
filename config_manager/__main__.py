from .models import ServerConfig
from .exceptions import ValidationError

def main():
    print("=== Запуск демонстрації роботи config_manager ===\n")
    
    # Сценарій 1: Успішне створення конфігурації
    try:
        data = {"host": "127.0.0.1", "port": 8080}
        config = ServerConfig(data)
        print(f"[ОК] Конфігурацію успішно створено! Host: {config.host}, Port: {config.port}")
    except ValidationError as e:
        print(f"[ПОМИЛКА] {e}")

    print("-" * 50)

    # Сценарій 2: Перехоплення помилки валідації
    try:
        invalid_data = {"host": "127.0.0.1", "port": 999999}
        config = ServerConfig(invalid_data)
    except ValidationError as e:
        print(f"[ОК] Помилку валідації успішно перехоплено: {e}")

if __name__ == "__main__":
    main()