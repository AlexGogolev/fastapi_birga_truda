"""тут всё связано с подключением к БД"""

# для подключения к БД используем sqlalchemy + допом ставим databases (pip install)
# +++ установим обёртки для postgresql для databases: pip install "databases[postgresql]"
# +++ pip install psycopg2-binary

from databases import Database
from sqlalchemy import create_engine, MetaData  # create_engine - для подключения к БД; MetaData - объект-контейнер, который содержит всю необходимую информацию для работы ORM (таблицы, ...)

from core.config import DATABASE_URL  # импортируем переменную (видимо окружения)


database = Database(DATABASE_URL)
metadata = MetaData()  # создаём экземпляр класса MetaData, который будем использовать для создания таблиц
engine = create_engine(
    DATABASE_URL,    
)  # используем ТОЛЬКО для синхронных запросов к БД + используем это в самом начале - для создания таблиц нашего приложения



