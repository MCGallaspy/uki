from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from uki.gui.application_state import ApplicationState
from uki.orm.base import UkiʔBase


def initialize_database_engine(app_state: ApplicationState) -> Engine:
    engine = create_engine(app_state.sql_alchemy_url, echo=True)
    UkiʔBase.metadata.create_all(engine)
    return engine


def load_lift_data(
        app_state: ApplicationState,
        lift_filename: str,
        flextext_filename: str = None,
    ) -> Engine:
    print(app_state, lift_filename, flextext_filename)