from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from uki.gui.application_state import ApplicationState
from uki.orm.base import UkiʔBase


def initialize_database_engine(app_state: ApplicationState) -> Engine:
    engine = create_engine(app_state.sql_alchemy_url, echo=True)
    UkiʔBase.metadata.create_all(engine)
    return engine