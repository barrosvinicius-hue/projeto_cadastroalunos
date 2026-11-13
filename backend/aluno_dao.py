import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BANCO = BASE_DIR / "escola.db"

class AlunoDAO:
    def conectar(self):
        return sqlite3.connect(BANCO)

    def adicionar(self, aluno):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome, email) VALUES (?, ?)",
            (aluno.nome, aluno.email)
        )
        aluno_id = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return aluno_id

    def listar_todos(self):
        conexao = self.conectar()
        conexao.row_factory = sqlite3.Row
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM alunos ORDER BY id DESC")
        alunos = [dict(linha) for linha in cursor.fetchall()]
        conexao.close()
        return alunos

    def excluir(self, aluno_id):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
        excluiu = cursor.rowcount > 0
        conexao.commit()
        conexao.close()
        return excluiu
