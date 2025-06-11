from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Resguardante(Base):
    __tablename__ = "resguardantes"

    clave = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(200))