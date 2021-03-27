from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship

from db.base_class import Base


class TestManagement(Base):
    id = Column(Integer, primary_key=True, index=True)
    update_time = Column(DATETIME)
    module_name = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    author = Column(String)
    version = Column(String)
    status = Column(String)
    is_delete = Column(BOOLEAN)