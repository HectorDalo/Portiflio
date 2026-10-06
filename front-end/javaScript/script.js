console.log("Portfólio do Hector carregado!");

const titulo = document.querySelector("#inicio h2");

titulo.textContent = "Hector Dalonso";

const botaoProjetos = document.querySelector("#btnProjetos");

const btnContato = document.querySelector("#btnContato");

botaoProjetos.addEventListener("click", function() {

    console.log("O botão Conheça meu trabalho foi clicado!");

    titulo.classList.toggle("destaque");

});

const projetos = [

    {
        nome: "Portfólio Pessoal",

        descricao: "Site desenvolvido para apresentar minha trajetória, habilidades, projetos e evolução na área de tecnologia.",

        tecnologias: "HTML • CSS • JavaScript",

        link: "#"
    },

    {
        nome: "Sistema de Cadastro de Clientes",

        descricao: "Sistema de cadastro e gerenciamento de clientes desenvolvido em Python, utilizando interface gráfica com Tkinter e armazenamento de dados em JSON.",
        
        tecnologias: "Python • Tkinter • JSON",
        
        link: "https://github.com/HectorDalo/Portiflio/tree/main/Projetos/Cadastro-Clientes"
    }

];

const listaProjetos = document.querySelector("#listaProjetos");

projetos.forEach(function(projeto) {

    const card = document.createElement("div");

    card.classList.add("projeto");

    card.innerHTML = `
        <h3>${projeto.nome}</h3>

        <p>${projeto.descricao}</p>

        <span>${projeto.tecnologias}</span>

        <a href="${projeto.link}" class="btn-projeto" target="_blank">Ver projeto</a>
    `;

    listaProjetos.appendChild(card);

});

btnContato.addEventListener("click", function() {

    console.log("O botão Entrar em contato foi clicado!");

});