from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import BaseModel

BASE_URL = 'sqlite:///db.db'


class DB:
    """
        Основной класс инициализирования базы данных. Если класс не получает
        требуемых для запуска MySql движка, то запускается sqllite3 база
        данных db.db
        Атрибуты:
            
            1) для подключения к MySql базе данных с использованием
            драйвера pymysql
        
            __db_user: str - имя пользователя для подключения к базе
            __db_host: str - хост расположения базы
            __db_password: str - пароль доступа к базе
            __db_basename: str - имя базы
        
            2) для вывода в лога работы движка с базой данных

            _echo: bool = True

            3) служебные:
            engine - движок обращения к базе данных
            session - экземпляр класса sqlalchemy.orm.Session
    """

    __db_user: str
    __db_host: str
    __db_password: str
    __db_basename: str
    _echo: bool = True

    def __init__(self, config=None):

        self.url = self.__create_url(config)

        if config:
            self._echo = False

        self.engine = create_engine(self.url, echo=self._echo)
        BaseModel.metadata.create_all(bind=self.engine)
        self.session = Session(self.engine)

    def __create_url(self, config) -> str:
        """
            Метод формирования url для для запуска движка базы данных
        """

        if config is None:
            return BASE_URL

        self.__db_user = config.db.db_user
        self.__db_host = config.db.db_host
        self.__db_password = config.db.db_password
        self.__db_basename = config.db.database

        return f'mysql+pymysql://{self.__db_user}:\
                                 {self.__db_password}@\
                                 {self.__db_host}/\
                                 {self.__db_basename}'


if __name__ == '__main__':
    db = DB()
