from sqlalchemy.orm import Session
from datetime import datetime

# ===================================================================
# Importación Correcta
# ===================================================================
from app.models.resguardantes import Resguardante
from app.models.reportes import Reporte
from app.schemas import schemas

# ===================================================================
# Funciones CRUD para Resguardante (Solo Lectura)
# ===================================================================


def get_resguardante(db: Session, trabajador_id: str):
    return db.query(Resguardante).filter(Resguardante.trabajador_id == trabajador_id).first()


def get_resguardantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Resguardante).offset(skip).limit(limit).all()

# ===================================================================
# Funciones CRUD para Reporte (Lectura y Escritura)
# ===================================================================


def get_reporte(db: Session, reporte_id: datetime):
    return db.query(Reporte).filter(Reporte.reporte_id == reporte_id).first()


def get_reportes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Reporte).offset(skip).limit(limit).all()


def create_reporte(db: Session, reporte: schemas.ReporteCreate):
    db_reporte = Reporte(
        **reporte.model_dump()
    )
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte


def update_reporte(db: Session, reporte_id: datetime, reporte_update: schemas.ReporteUpdate):
    db_reporte = get_reporte(db, reporte_id=reporte_id)
    if not db_reporte:
        return None

    update_data = reporte_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_reporte, key, value)

    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte


def delete_reporte(db: Session, reporte_id: datetime):
    db_reporte = get_reporte(db, reporte_id=reporte_id)
    if not db_reporte:
        return None

    db.delete(db_reporte)
    db.commit()
    return db_reporte
