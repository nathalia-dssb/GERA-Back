from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from sqlalchemy import text
from app.schemas import schemas
from typing import List
from app.services import crud
from datetime import datetime
from app.models.reportes import Reporte

router = APIRouter()

# --------------------------------------------------------
# Rutas de resguardantess
# ------------------------------------------------------


@router.get("/resguardantes", response_model=List[schemas.ResguardanteBase])
def read_resguardantes_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resguardantes = crud.get_resguardantes(db, skip=skip, limit=limit)
    return resguardantes


@router.get("/resguardantes/{trabajador_id}", response_model=schemas.Resguardante)
def read_resguardante_endpoint(trabajador_id: str, db: Session = Depends(get_db)):
    db_resguardante = crud.get_resguardante(db, trabajador_id=trabajador_id)
    if db_resguardante is None:
        raise HTTPException(
            status_code=404, detail="Resguardante no encontrado")
    return db_resguardante

# --------------------------------------------------------
# Rutas de ubicaciones
# ------------------------------------------------------


@router.get("/ubicaciones", response_model=List[schemas.UbicacionBase])
def read_ubicaciones_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ubicaciones = crud.get_ubicaciones(db, skip=skip, limit=limit)
    return ubicaciones


@router.get("/ubicaciones/{salon_id}", response_model=schemas.UbicacionBase)
def read_ubicacion_endpoint(salon_id: str, db: Session = Depends(get_db)):
    db_ubicacion = crud.get_ubicacion(db, salon_id=salon_id)
    if db_ubicacion is None:
        raise HTTPException(
            status_code=404, detail="Ubicación no encontrada")
    return db_ubicacion


@router.get("/ubicaciones/edificio/{edificio}", response_model=List[str])
def read_salon_ids_by_edificio_endpoint(edificio: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    salon_ids = crud.get_salon_ids_by_edificio(db, edificio=edificio, skip=skip, limit=limit)
    return salon_ids

# --------------------------------------------------------
# Rutas de reportes
# ------------------------------------------------------


@router.post("/", response_model=schemas.Reporte, status_code=status.HTTP_201_CREATED)
def create_reporte(reporte: schemas.ReporteCreate, db: Session = Depends(get_db)):
    reporte_data = reporte.model_dump()

    db_reporte = Reporte(
        **reporte_data,
        reporte_id=datetime.now()
    )

    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)

    return db_reporte


@router.get("/reportes", response_model=List[schemas.Reporte])
def read_reportes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reportes = crud.get_reportes(db, skip=skip, limit=limit)
    return reportes


@router.get("/reporte/{reporte_id}", response_model=schemas.Reporte)
def read_reporte_by_id(reporte_id: datetime, db: Session = Depends(get_db)):
    db_reporte = crud.get_reporte(db, reporte_id=reporte_id)
    if db_reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return db_reporte


@router.put("/reporte/{reporte_id}", response_model=schemas.Reporte)
def update_reporte(
    reporte_id: datetime,
    reporte_update: schemas.ReporteUpdate,
    db: Session = Depends(get_db)
):
    db_reporte = crud.update_reporte(
        db, reporte_id=reporte_id, reporte_update=reporte_update)
    if db_reporte is None:
        raise HTTPException(
            status_code=404, detail="Reporte no encontrado para actualizar")
    return db_reporte


@router.delete("/reporte/{reporte_id}", response_model=schemas.Reporte)
def delete_reporte(reporte_id: datetime, db: Session = Depends(get_db)):
    db_reporte = crud.delete_reporte(db, reporte_id=reporte_id)
    if db_reporte is None:
        raise HTTPException(
            status_code=404, detail="Reporte no encontrado para eliminar")
    return db_reporte
