from typing import Dict, Any
from ..exceptions import ValidationError, BusinessLogicError

class ServerConfig:
    """Клас моделі конфігурації сервера з перевіркою параметрів."""
    
    def __init__(self, raw_data: Dict[str, Any]) -> None:
        self.host = self._validate_host(raw_data.get("host"))
        self.port = self._validate_port(raw_data.get("port"))

    def _validate_host(self, host: Any) -> str:
        if not host or not isinstance(host, str):
            raise ValidationError("Параметр host повинен бути непорожнім рядком!")
        return host

    def _validate_port(self, port: Any) -> int:
        if not isinstance(port, int) or not (1 <= port <= 65535):
            raise ValidationError("Параметр port повинен бути цілим числом від 1 до 65535!")
        return port