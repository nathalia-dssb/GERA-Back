from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Activo(Base):
    __tablename__ = "activos"

    equipo_id = Column(Integer, primary_key=True, index=True, nullable=False)
    reguardo_id = Column(Integer, nullable=False)
    no_serie = Column(Integer)
    trabajador_id = Column(Integer, ForeignKey(
        "resguardantes.trabajador_id"), nullable=False)
    descripcion_articulo = Column(String(100))
    caracteristicas = Column(String(100))
    salon_id = Column(String(20), ForeignKey("ubicaciones.salon_id"))

    # relaciones
    resguardante = relationship("Resguardante", back_populates="activos")
    ubicacion = relationship("Ubicacion", back_populates="activos")
    reportes = relationship("Reporte", back_populates="activo")
