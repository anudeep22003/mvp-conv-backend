from crud.crud_base import CRUDBase
from models.message import Message
from schemas.message import MessageCreate

class CRUDMessage(CRUDBase[Message, MessageCreate]):
    ...

message = CRUDMessage(Message)