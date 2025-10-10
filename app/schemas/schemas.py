from pydantic import BaseModel
from typing import List
from datetime import datetime

# ===================================================================
# Ubicacion Schemas
# ===================================================================


class UbicacionBase(BaseModel):
    salon_id: str
    edificio: str


class Ubicacion(UbicacionBase):
    activos: List["Activo"] = []

    class Config:
        from_attributes = True


# ===================================================================
# Resguardante Schemas
# ===================================================================

class ResguardanteBase(BaseModel):
    trabajador_id: str
    nombre_completo: str


class Resguardante(ResguardanteBase):
    activos: List["Activo"] = []

    class Config:
        from_attributes = True


# ===================================================================
# Reporte Schemas (Full CRUD)
# ===================================================================

class ReporteBase(BaseModel):
    estado: str
    observaciones: str
    equipo_id: int


class ReporteCreate(ReporteBase):
    pass


class ReporteUpdate(BaseModel):
    estado: str
    observaciones: str


class Reporte(ReporteBase):
    reporte_id: datetime

    class Config:
        from_attributes = True


# ===================================================================
# Activo Schemas
# ===================================================================

class ActivoBase(BaseModel):
    reguardo_id: int
    no_serie: int
    trabajador_id: str
    descripcion_articulo: str
    caracteristicas: str
    salon_id: str


class Activo(ActivoBase):
    equipo_id: int
    resguardante: ResguardanteBase
    ubicacion: UbicacionBase
    reportes: List[ReporteBase] = []

    class Config:
        from_attributes = True


Ubicacion.model_rebuild()
Resguardante.model_rebuild()
