import json
import os

from config import DATA_DIR
from models.calendario import Calendario

FILE_PATH = os.path.join(DATA_DIR, "calendario.json")

class CalendarioService:

    @staticmethod
    def load():
        if not os.path.exists(FILE_PATH):
            cal = Calendario("01-01-2025", "31-12-1025")
            CalendarioService.save(cal)
            return cal
        
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.loaf(f)
            return Calendario.from_dict(data)
        
    @staticmethod
    def save(calendario):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
               json.dump(calendario.to_dict(), f, indent=4)