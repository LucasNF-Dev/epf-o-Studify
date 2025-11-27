import json
import os

from config import DATA_DIR
from models.calendario import Calendario

FILE_PATH = os.path.join(DATA_DIR, "calendario.json")

class CalendarioService:

    @staticmethod
    def load():
        if not os.path.exists(FILE_PATH):
            cal = Calendario("01-01-2025", "31-12-2025")
            CalendarioService.save(cal)
            return cal
        
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Calendario.from_dict(data)
        
    @staticmethod
    def save(calendario):
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        with open(FILE_PATH, "w", encoding="utf-8") as f:
               json.dump(calendario.to_dict(), f, indent=4)