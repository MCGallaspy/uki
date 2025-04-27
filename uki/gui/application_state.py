from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.pool import StaticPool, SingletonThreadPool

from uki.orm.base import UkiʔBase


class ApplicationState:
    
    def __init__(
        self,
        sql_alchemy_url: str = "sqlite:///:memory:"
    ):
        """
        Represents the state of the GUI application.
        
        sql_alchemy_url: A SQLAlchemy URL that will be used to establish
                         a database connection.
        """
        self.sql_alchemy_url = sql_alchemy_url
        engine = create_engine(sql_alchemy_url, echo=True)
        UkiʔBase.metadata.create_all(engine)
        self._engine = engine
    
    @property
    def engine(self):
        return self._engine