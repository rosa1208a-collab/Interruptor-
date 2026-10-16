import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "interruptor.db"


class EventRepository:

    def __init__(self):
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(DB_PATH)

    def crear_tabla(self):
        """Crea la tabla de eventos si no existe."""

        with self.conectar() as conexion:
            conexion.execute("""
                CREATE TABLE IF NOT EXISTS eventos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT,
                    gesto TEXT,
                    aceptado INTEGER,
                    motivo TEXT,
                    accion TEXT,
                    modo_prueba INTEGER,
                    confianza REAL,
                    distancia REAL,
                    estado_luz TEXT
                )
            """)

    def guardar_evento(self, evento):
        """Guarda una interacción en la base de datos."""

        with self.conectar() as conexion:
            conexion.execute("""
                INSERT INTO eventos (
                    fecha,
                    gesto,
                    aceptado,
                    motivo,
                    accion,
                    modo_prueba,
                    confianza,
                    distancia,
                    estado_luz
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                evento["fecha"],
                evento["gesto"],
                int(evento["aceptado"]),
                evento["motivo"],
                evento["accion"],
                int(evento["modo_prueba"]),
                evento["confianza"],
                evento["distancia"],
                evento["estado_luz"]
            ))

    def consultar_historial(self, limite=100):
        """Consulta los eventos más recientes."""

        with self.conectar() as conexion:
            conexion.row_factory = sqlite3.Row

            filas = conexion.execute("""
                SELECT *
                FROM eventos
                ORDER BY id DESC
                LIMIT ?
            """, (limite,)).fetchall()

            return [dict(fila) for fila in filas]
