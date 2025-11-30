from database import get_connection
from models.flashcard import Flashcard
from datetime import datetime, timedelta

class FlashcardService:

    @staticmethod
    def criar(pergunta, resposta, categoria):
        conn = get_connection()
        cur = conn.cursor()

        proxima = datetime.now().strftime("%Y-%m-%d")

        cur.execute("""
            INSERT INTO flashcards (pergunta, resposta, proxima_revisao, categoria)
            VALUES (?, ?, ?, ?)
        """, (pergunta, resposta, proxima, categoria))

        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM flashcards")
        dados = cur.fetchall()

        conn.close()

        return [Flashcard(*d) for d in dados]
    
    @staticmethod 
    def pegar_para_revisao():
        conn = get_connection()
        cur = conn.cursor()

        hoje = datetime.now().strftime("%Y-%m-%d")

        cur.execute("""
            SELECT * FROM flashcards
            WHERE proxima_revisao <= ?
            ORDER BY proxima_revisao ASC
        """, (hoje,))

        dados = cur.fetchall()
        conn.close()

        return [Flashcard(*d) for d in dados]
    
    @staticmethod 
    def revisar(id, dificuldade):
        """
        dificuldade:
        1 = facil(+3 dias)
        2 = medio(+2 dias)
        3 = dificil(+1dia)
        """
        conn = get_connection()
        cur = conn.cursor()

        dias = {1: 3, 2: 2, 3: 1}[dificuldade]

        proxima = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d")
        ultima = datetime.now().strftime("%Y-%m-%d")

        cur.execute("""
            UPDATE flashcards
            SET nivel = ?, ultima_revisao = ?, proxima_revisao = ?
            WHERE id = ?
        """, (dificuldade, ultima, proxima, id))

        conn.commit()
        conn.close()

    @staticmethod
    def listar_categorias():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT DISTINCT categoria FROM flashcards WHERE categoria IS NOT NULL")
        categorias_bd = [row[0] for row in cur.fetchall()]

        conn.close()

        categorias_padrao = ["Matemática", "Programação", "Inglês", "Biologia", "Gramática", "História"]

        todas = list(dict.fromkeys(categorias_padrao + categorias_bd))

        return todas