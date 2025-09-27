from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class Resguardante(Base):
    __tablename__ = "resguardantes"

    trabajador_id = Column(Integer, primary_key=True,
                           index=True, nullable=False)
    nombre_completo = Column(String(200))

    # relaciones
    activos = relationship("Activo", back_populates="resguardante")
