from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    status = Column(String, default="todo")

    assigned_to = Column(Integer, ForeignKey("users.id"))

    project_id = Column(Integer, ForeignKey("projects.id"))