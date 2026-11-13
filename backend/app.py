from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from banco import criar_banco
from aluno_dao import AlunoDAO
from aluno import Aluno

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIR),
    static_url_path="/static"
)

criar_banco()
dao = AlunoDAO()

@app.route("/")
def inicio():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/api/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(dao.listar_todos())

@app.route("/api/alunos", methods=["POST"])
def cadastrar_aluno():
    dados = request.get_json(silent=True) or {}
    nome = (dados.get("nome") or "").strip()
    email = (dados.get("email") or "").strip()

    if not nome or not email:
        return jsonify({"erro": "Preencha nome e e-mail."}), 400

    aluno = Aluno(nome, email)
    novo_id = dao.adicionar(aluno)
    return jsonify({"mensagem": "Aluno cadastrado com sucesso!", "id": novo_id}), 201

@app.route("/api/alunos/<int:aluno_id>", methods=["DELETE"])
def excluir_aluno(aluno_id):
    if dao.excluir(aluno_id):
        return jsonify({"mensagem": "Aluno excluído com sucesso."})
    return jsonify({"erro": "Aluno não encontrado."}), 404

if __name__ == "__main__":
    app.run(debug=True)
