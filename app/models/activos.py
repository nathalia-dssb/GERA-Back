from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.database import Base

class Activo(Base):
    __tablename__ = "activos"

    id_activo = Column(Integer, primary_key=True, nullable=False)
    folio_resguardo = Column(Integer, nullable=False)
    clave_activo = Column(Integer)
    num_serie = Column(Integer)
    clave_resguardante = Column(Integer, ForeignKey("resguardantes.clave"), nullable=False)
    caracteristicas = Column(String(100))
    factura = Column(String(100))
    ubicacion = Column(String(100))
    condiciones = Column(String(100))
    estatus = Column(Boolean)