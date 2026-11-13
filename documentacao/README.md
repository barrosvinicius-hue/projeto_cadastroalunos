# Projeto Integrado — Cadastro de Alunos

## Funcionalidades
- Cadastrar alunos com nome e e-mail.
- Consultar a lista de alunos.
- Excluir alunos.
- Salvar os dados em SQLite.

## Tecnologias
- DWS: HTML, CSS e JavaScript.
- POO: classe Python `Aluno`.
- DAO: classe `AlunoDAO`.
- Back-end: Python e Flask.
- Banco de dados: SQLite.
- Integração: Fetch API.

## Como executar
1. Instale Python 3.
2. Abra o terminal na pasta principal do projeto.
3. Instale as dependências:

   `pip install -r backend/requirements.txt`

4. Entre na pasta backend:

   `cd backend`

5. Inicie o servidor:

   `python app.py`

6. Abra `http://127.0.0.1:5000` no navegador.

O banco `escola.db` é criado automaticamente dentro de `backend/`.

## Rotas
| Método | Rota | Função |
|---|---|---|
| GET | `/api/alunos` | Lista alunos |
| POST | `/api/alunos` | Cadastra aluno |
| DELETE | `/api/alunos/<id>` | Exclui aluno |

## Estrutura
- `backend/`: Python, Flask, POO e DAO.
- `frontend/`: HTML.
- `frontend/css/`: estilos CSS.
- `frontend/js/`: JavaScript e Fetch.
- `database/`: script SQL.
- `documentacao/`: instruções e documentação.

## GitHub
Envie a pasta inteira ao repositório. Em Settings > Collaborators, adicione `leonardo.stephan@eaportal.org` e envie o convite para a conta correspondente.

Faça commits ao longo do desenvolvimento. O GitHub Pages sozinho não executa o back-end Flask; para testar o sistema completo, inicie o servidor Python ou hospede o back-end em serviço compatível.
