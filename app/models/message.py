from sqlalchemy import Column, String, Text, Integer, DateTime

# from ..db.base_class import Base, IMPORT_PATH
# from ..db.session import SQL_DATABASE_URL
from .base_class import Base


class Message(Base):
    conv_id = Column(Integer, nullable=False)
    content = Column(Text)
    sender = Column(String, nullable=False)  # human
    receiver = Column(String, nullable=False)  # agent
    sources = Column(String)
    ts_created = Column(DateTime)


if __name__ == "__main__":
    ...
