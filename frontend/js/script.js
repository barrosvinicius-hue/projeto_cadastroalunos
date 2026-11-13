const formulario = document.getElementById("form-aluno");
const lista = document.getElementById("lista");
const mensagem = document.getElementById("mensagem");

async function carregarAlunos() {
    lista.textContent = "Carregando...";

    try {
        const resposta = await fetch("/api/alunos");
        const alunos = await resposta.json();
        lista.innerHTML = "";

        if (alunos.length === 0) {
            lista.textContent = "Nenhum aluno cadastrado ainda.";
            return;
        }

        alunos.forEach((aluno) => {
            const item = document.createElement("div");
            item.className = "aluno";

            const informacoes = document.createElement("div");
            const nome = document.createElement("strong");
            nome.textContent = aluno.nome;

            const email = document.createElement("p");
            email.textContent = aluno.email;
            informacoes.append(nome, email);

            const botao = document.createElement("button");
            botao.className = "excluir";
            botao.textContent = "Excluir";
            botao.addEventListener("click", () => excluirAluno(aluno.id));

            item.append(informacoes, botao);
            lista.appendChild(item);
        });
    } catch (erro) {
        lista.textContent = "Erro ao conectar. Confira se o Flask está ligado.";
    }
}

formulario.addEventListener("submit", async (evento) => {
    evento.preventDefault();
    mensagem.textContent = "";

    const dados = {
        nome: document.getElementById("nome").value,
        email: document.getElementById("email").value
    };

    try {
        const resposta = await fetch("/api/alunos", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });

        const resultado = await resposta.json();
        if (!resposta.ok) {
            throw new Error(resultado.erro || "Erro ao cadastrar.");
        }

        mensagem.textContent = resultado.mensagem;
        formulario.reset();
        carregarAlunos();
    } catch (erro) {
        mensagem.textContent = erro.message;
    }
});

async function excluirAluno(id) {
    if (!confirm("Deseja excluir este aluno?")) return;

    const resposta = await fetch(`/api/alunos/${id}`, {
        method: "DELETE"
    });
    const resultado = await resposta.json();
    mensagem.textContent = resultado.mensagem || resultado.erro;
    carregarAlunos();
}

document.getElementById("atualizar")
    .addEventListener("click", carregarAlunos);

carregarAlunos();
