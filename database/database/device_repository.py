import sqlite3

from database.event_repository import DB_PATH


class DeviceRepository:

    def __init__(self):
        self.crear_tabla()

    def conectar(self):
        """Establece la conexión con SQLite."""
        return sqlite3.connect(DB_PATH)

    def crear_tabla(self):
        """Crea la tabla de dispositivos."""

        with self.conectar() as conexion:
            conexion.execute("""
                CREATE TABLE IF NOT EXISTS dispositivos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    zona TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    estado TEXT NOT NULL
                )
            """)

    def registrar_dispositivo(
        self,
        nombre,
        zona,
        tipo="INTERRUPTOR"
    ):
        """Registra un nuevo dispositivo."""

        with self.conectar() as conexion:
            conexion.execute("""
                INSERT INTO dispositivos (
                    nombre,
                    zona,
                    tipo,
                    estado
                )
                VALUES (?, ?, ?, ?)
            """, (
                nombre,
                zona,
                tipo,
                "ACTIVO"
            ))

    def consultar_dispositivos(self):
        """Obtiene los dispositivos registrados."""

        with self.conectar() as conexion:
            conexion.row_factory = sqlite3.Row

            filas = conexion.execute("""
                SELECT *
                FROM dispositivos
                ORDER BY id DESC
            """).fetchall()

            return [dict(fila) for fila in filas]
