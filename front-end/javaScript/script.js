let conexaoEstabelecida = false;

console.log("Portfólio do Hector carregado!");

const titulo = document.querySelector("#titulo-dinamico");

const botaoProjetos = document.querySelector("#btnProjetos");

botaoProjetos.addEventListener("click", function() {

    console.log("O botão Conheça meu trabalho foi clicado!");

    titulo.classList.toggle("destaque");

});

const projetos = [

    {
        nome: "Portfólio Pessoal",

        descricao: "Site desenvolvido para apresentar minha formação, habilidades e projetos na área de tecnologia, utilizando HTML, CSS e JavaScript. O projeto também representa minha evolução prática no desenvolvimento web.",

        tecnologias: "HTML • CSS • JavaScript",

        link: "#"
    },

    {
        nome: "Sistema de Cadastro de Clientes",

        descricao: "Sistema desenvolvido em Python para cadastro e gerenciamento de clientes, utilizando Tkinter para a interface gráfica e JSON para armazenamento dos dados. O projeto foi desenvolvido com foco na aplicação prática de conceitos de programação e orientação a objetos.",
        
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
    `;

    listaProjetos.appendChild(card);

});


const tituloDinamico = document.querySelector("#titulo-dinamico");
const textoTitulo = document.querySelector("#texto-titulo");
const simbolos = document.querySelectorAll(".simbolo");

const textosRolagem = [
    "Hector Dalonso",
    "Dev em formação",
    "Dev de sistemas",
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

const terminalInput = document.querySelector("#terminalInput");
const terminalConteudo = document.querySelector(".terminal-conteudo");

terminalInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        const comando = terminalInput.value.trim().toLowerCase();

        switch (comando) {

    case "help":

        const resposta = document.createElement("p");

        resposta.innerHTML = `
            Comandos disponíveis:<br>
            sobre - informações sobre mim<br>
            skills - minhas habilidades<br>
            projetos - meus projetos<br>
            contato - como entrar em contato
        `;

        terminalConteudo.appendChild(resposta);

        break;

    case "sobre":

    const respostaSobre = document.createElement("p");

    respostaSobre.innerHTML = `
        Nome: Hector Dalonso<br>
        Formação: Ciência da Computação<br>
        Status: Desenvolvedor em formação<br>
        Área: Desenvolvimento de sistemas
    `;

    terminalConteudo.appendChild(respostaSobre);

    break;

    case "skills":

    const respostaSkills = document.createElement("p");

    respostaSkills.innerHTML = `
        Linguagens:<br>
        - Python<br>
        - JavaScript<br><br>

        Web:<br>
        - HTML<br>
        - CSS<br><br>

        Conceitos:<br>
        - Programação Orientada a Objetos
    `;

    terminalConteudo.appendChild(respostaSkills);

    break;

    case "projetos":

    const respostaProjetos = document.createElement("p");

    respostaProjetos.innerHTML = `
        [1] Portfólio Pessoal<br>
        HTML • CSS • JavaScript<br><br>

        [2] Sistema de Cadastro de Clientes<br>
        Python • Tkinter • JSON
    `;

    terminalConteudo.appendChild(respostaProjetos);

    break;

    case "projeto 1":

    window.open(projetos[0].link, "_blank");

    break;

    case "projeto 2":

    window.open(projetos[1].link, "_blank");

    break;

    case "contato":

    const respostaContato = document.createElement("p");

    respostaContato.innerHTML = `
        Canais disponíveis:<br><br>
        [1] WhatsApp<br><br>
        Digite "whatsapp" para iniciar a conexão.
    `;

    terminalConteudo.appendChild(respostaContato);

    break;

    case "whatsapp":

    if (conexaoEstabelecida) {

        window.open("https://wa.me/5511979934334", "_blank");

    } else {

        const respostaConexao = document.createElement("p");

        respostaConexao.textContent =
            "Conexão não estabelecida. Acesse a seção Contato primeiro.";

        terminalConteudo.appendChild(respostaConexao);

}

    break;

    default:

        const respostaErro = document.createElement("p");

        respostaErro.textContent =
            `Comando não encontrado: ${comando}`;

        terminalConteudo.appendChild(respostaErro);

        break;
}

        terminalInput.value = "";
    }
});

const btnConexao = document.querySelector("#btnConexao");
const carregamento = document.querySelector("#carregamento");
const progresso = document.querySelector("#progresso");
const porcentagem = document.querySelector("#porcentagem");
const conexaoSucesso = document.querySelector("#conexaoSucesso");

btnConexao.addEventListener("click", function() {

    btnConexao.style.display = "none";
    carregamento.style.display = "block";
    let valor = 0;

    const intervalo = setInterval(function() {

        valor++;

        progresso.style.width = valor + "%";
        porcentagem.textContent = valor + "%";

        if (valor >= 100) {

            clearInterval(intervalo);

            carregamento.style.display = "none";
            conexaoSucesso.style.display = "block";

            conexaoEstabelecida = true;


}

}, 30);

});