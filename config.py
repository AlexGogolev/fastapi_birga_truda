"""тут храняться переменные, связанные с конфигурацией приложения"""

from starlette.config import Config  # класс Config нужен для работы с переменными окружения ОС

config = Config(".env")  # env_file

DATABASE_URL = config("EE_DATABASE")  # EE_DATABASE - переменная окружения





