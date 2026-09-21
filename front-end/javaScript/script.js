console.log("Portfólio do Hector carregado!");

const titulo = document.querySelector("#inicio h2");

titulo.textContent = "Hector Dalonso";

const botaoProjetos = document.querySelector("#btnProjetos");

const btnContato = document.querySelector("#btnContato");

botaoProjetos.addEventListener("click", function() {
    console.log("O botão Conheça meu trabalho foi clicado!");

    titulo.classList.toggle("destaque");

    document.querySelector("#projetos").scrollIntoView();
});

btnContato.addEventListener("click", function() {
    console.log("O botão Entrar em contato foi clicado!");
});