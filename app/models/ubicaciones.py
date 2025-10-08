from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    salon_id = Column(String(20), primary_key=True, index=True, nullable=False)
    edificio = Column(String(100), nullable=False)

    # relaciones
    activos = relationship("Activo", back_populates="ubicacion")
