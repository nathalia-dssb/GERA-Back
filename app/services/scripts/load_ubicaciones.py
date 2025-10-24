import pandas as pd
from pathlib import Path

from app.models.ubicaciones import Ubicacion
from app.db.database import SessionLocal


def load_ubicaciones():
    BASE_DIR = Path(__file__).parent / "../../data/"

    # cargar el exel de ubicaciones
    file_path = BASE_DIR / "UBICACIONES_INVENTARIO.xlsx"
    ubicaciones_df = pd.read_excel(
        file_path, header=None, usecols='A,B',
        skiprows=1, names=['edificio', 'salon_id'], dtype={'salon_id': str})

    # Limpieza de nulos
    ubicaciones_df = ubicaciones_df.dropna(
        how='all').dropna(axis=1, how='all')

    # Si no se pueden hacer conversiones de id la ubicación no se registrara en la BD por seguridad
    ubicaciones_df = ubicaciones_df.dropna(subset=['salon_id'])
    ubicaciones_df['salon_id'] = ubicaciones_df['salon_id'].astype(
        str)
    ubicaciones_df = ubicaciones_df.drop_duplicates(
        subset=['salon_id'],
        keep='first'
    )

    # Limpieza en el edificio en caso de haber espacios
    ubicaciones_df['edificio'] = ubicaciones_df['edificio'].astype(
        str).str.strip()

    return ubicaciones_df


def insert_ubicaciones_to_db():

    ubicaciones_df = load_ubicaciones()
    # esta linea estará en otro lado es para inicializar la db init_db()
    db = SessionLocal()

    try:
        existing_ids = {result[0] for result in db.query(
            Ubicacion.salon_id).all()}

        new_records = []
        for _, row in ubicaciones_df.iterrows():
            if row['salon_id'] not in existing_ids:
                ubicacion = Ubicacion(
                    salon_id=row['salon_id'],
                    edificio=row['edificio']
                )
                new_records.append(ubicacion)

        if new_records:
            db.bulk_save_objects(new_records)
            db.commit()
            print(f"Se han insertado {len(new_records)} nuevas ubicaciones")
        else:
            print("No hay nuevas inserciones")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    insert_ubicaciones_to_db()