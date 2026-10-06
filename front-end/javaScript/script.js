console.log("Portfólio do Hector carregado!");

const titulo = document.querySelector("#titulo-dinamico");

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

const tituloDinamico = document.querySelector("#titulo-dinamico");
const textoTitulo = document.querySelector("#texto-titulo");
const simbolos = document.querySelectorAll(".simbolo");

const textosRolagem = [
    "Hector Dalonso",
    "Dev em formação",
    "Foco em Programação",
    "Dev de Sistemas"
];

let indiceRolagem = 0;

textoTitulo.textContent = textosRolagem[indiceRolagem];

setInterval(function() {

    // Saída do texto atual
    tituloDinamico.style.transform = "translateY(-67px)";
    tituloDinamico.style.opacity = "0";

    setTimeout(function() {

        // Próximo texto
        indiceRolagem =
            (indiceRolagem + 1) % textosRolagem.length;

        textoTitulo.textContent =
            textosRolagem[indiceRolagem];

        // Prepara o novo texto para entrar por baixo
        tituloDinamico.style.transition = "none";
        tituloDinamico.style.transform = "translateY(67px)";

        setTimeout(function() {

            // Entrada do novo texto
            tituloDinamico.style.transition =
                "transform 0.6s ease, opacity 0.6s ease";

            tituloDinamico.style.transform =
                "translateY(0)";

            tituloDinamico.style.opacity = "1";

            // Espera o texto terminar de aparecer
            setTimeout(function() {

                // Reinicia a animação dos dois símbolos
                simbolos.forEach(function(simbolo) {
                    simbolo.classList.remove("carregando");
                });

                void tituloDinamico.offsetWidth;

                simbolos.forEach(function(simbolo) {
                    simbolo.classList.add("carregando");
                });

            }, 600);

        }, 50);

    }, 600);

}, 2500);