

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
