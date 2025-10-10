import pandas as pd
from pathlib import Path

from app.models.resguardantes import Resguardante
from app.db.database import SessionLocal


def load_resguardantes():
    BASE_DIR = Path(__file__).parent / "../../data/"

    # cargar el exel de reguardantes
    file_path = BASE_DIR / "INVENTARIO_SEPTIEMBRE_2025.xlsx"
    resguardantes_df = pd.read_excel(
        file_path, header=None, usecols='P,Q',
        skiprows=5, names=['trabajador_id', 'nombre_completo'], dtype={'trabajador_id': str})

    # Limpieza de nulos
    resguardantes_df = resguardantes_df.dropna(
        how='all').dropna(axis=1, how='all')

    # Si no se pueden hacer conversiones de id el resguardante no se registrara en la BD por seguridad
    resguardantes_df = resguardantes_df.dropna(subset=['trabajador_id'])
    resguardantes_df['trabajador_id'] = resguardantes_df['trabajador_id'].astype(
        str)
    resguardantes_df = resguardantes_df.drop_duplicates(
        subset=['trabajador_id'],
        keep='first'
    )

    # Limpieza en el nombre en caso de haber espacios
    resguardantes_df['nombre_completo'] = resguardantes_df['nombre_completo'].astype(
        str).str.strip().str.replace('.', '', regex=False)

    return resguardantes_df


def insert_resguardantes_to_db():

    resguardantes_df = load_resguardantes()
    # esta linea estará en otro lado es para inicializar la db init_db()
    db = SessionLocal()

    try:
        existing_ids = {result[0] for result in db.query(
            Resguardante.trabajador_id).all()}

        new_records = []
        for _, row in resguardantes_df.iterrows():
            if row['trabajador_id'] not in existing_ids:
                resguardante = Resguardante(
                    trabajador_id=row['trabajador_id'],
                    nombre_completo=row['nombre_completo']
                )
                new_records.append(resguardante)

        if new_records:
            db.bulk_save_objects(new_records)
            db.commit()
            print(f"Se han insertado {len(new_records)} nuevos resguardantes")
        else:
            print("No hay nuevas inserciones")

    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    insert_resguardantes_to_db()
