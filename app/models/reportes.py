from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.db.database import Base

class Reporte(Base):
    __tablename__ = "reportes"

    id_reporte = Column(DateTime, primary_key=True, nullable=False)
    estado = Column(String(20))
    observaciones = Column(String)
    id_activo = Column(Integer, ForeignKey("activos.id_activo"), nullable=False)
