from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class Reporte(Base):
    __tablename__ = "reportes"

    reporte_id = Column(DateTime, primary_key=True, nullable=False, index=True)
    estado = Column(String(20))
    observaciones = Column(Text)
    equipo_id = Column(Integer, ForeignKey(
        "activos.equipo_id"), nullable=False)

    # relaciones
    activo = relationship("Activo", back_populates="reportes")
