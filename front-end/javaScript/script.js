let conexaoEstabelecida = false;
let acessoLiberado = false;

const statusSistema = document.querySelector(".status-sistema");

console.log("Portfólio do Hector carregado!");

const titulo = document.querySelector("#titulo-dinamico");

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
const historicoTerminal =
    document.querySelector("#historicoTerminal");

terminalInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        const comando = terminalInput.value.trim().toLowerCase();

        const comandoDigitado = document.createElement("p");

        comandoDigitado.classList.add("comando-digitado");

        comandoDigitado.textContent =
            "hector@portfolio:~$ " + comando;

        historicoTerminal.appendChild(comandoDigitado);

        switch (comando) {

    case "help":

        const resposta = document.createElement("p");

        resposta.innerHTML = `
            Comandos disponíveis:<br>
            sobre - informações sobre mim<br>
            skills - minhas habilidades<br>
            projetos - meus projetos<br>
            Contato - como entrar em contato<br>
            Clear - limpar o terminal<br>
            status - status do sistema
        `;

        historicoTerminal.appendChild(resposta);

    break;

    case "sobre":

        const respostaSobre = document.createElement("p");

        respostaSobre.innerHTML = `
            Nome: Hector Dalonso<br>
            Formação: Ciência da Computação<br>
            Status: Desenvolvedor em formação<br>
            Área: Desenvolvimento de sistemas
        `;

        historicoTerminal.appendChild(respostaSobre);

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

        historicoTerminal.appendChild(respostaSkills);

    break;

    case "projetos":

        const respostaProjetos = document.createElement("p");

        respostaProjetos.innerHTML = `
            Projetos disponíveis:<br><br>
            [1] Portfólio Pessoal<br>
            Digite: projeto portfolio<br><br>
            [2] Sistema de Cadastro de Clientes<br>
            Digite: projeto cadastro
        `;

        historicoTerminal.appendChild(respostaProjetos);

    break;

    case "projeto 1":

        const respostaProjeto1 = document.createElement("p");

        respostaProjeto1.textContent =
            "Abrindo " + projetos[0].nome + "...";

        historicoTerminal.appendChild(respostaProjeto1);

        setTimeout(function() {
            window.open(projetos[0].link, "_blank");
        }, 1000);

    break;

    case "projeto 2":

        case "projeto cadastro":

            const respostaCadastro = document.createElement("p");

            respostaCadastro.textContent =
                "Abrindo " + projetos[1].nome + "...";

            historicoTerminal.appendChild(respostaCadastro);

            setTimeout(function() {
                window.open(projetos[1].link, "_blank");
        }, 1000);

    break;

    case "contato":

        const respostaContato = document.createElement("p");

        respostaContato.innerHTML = `
            Canais disponíveis:<br><br>
            [1] WhatsApp<br><br>
            Digite "whatsapp" para iniciar a conexão.
        `;

        historicoTerminal.appendChild(respostaContato);

    break;

    case "whatsapp":

        if (conexaoEstabelecida) {

            const respostaWhatsApp = document.createElement("p");

            respostaWhatsApp.classList.add("sucesso-terminal");

            respostaWhatsApp.textContent =
                "CANAL WHATSAPP AUTORIZADO. INICIANDO CONEXÃO...";

            historicoTerminal.appendChild(respostaWhatsApp);

            setTimeout(function() {
                window.open("https://wa.me/5511979934334", "_blank");
            }, 3000);

        }else{

            const respostaConexao = document.createElement("p");

            respostaConexao.classList.add("erro-terminal");

             respostaConexao.textContent =
                "ERRO: conexão não estabelecida. Acesse a seção Contato para liberar o canal.";

            historicoTerminal.appendChild(respostaConexao);
        }
    break;

    case "clear":

        historicoTerminal.innerHTML = "";

    break;

    case "status":

        const respostaStatus = document.createElement("p");

            respostaStatus.innerHTML = `
                SYSTEM STATUS<br><br>
                ${acessoLiberado
                    ? "[✓] Sistema ........ ONLINE"
                    : "[!] Sistema ........ BLOQUEADO"}<br>
                [✓] Terminal ........ ONLINE<br>
                [✓] Projetos ........ ONLINE<br>
                ${conexaoEstabelecida
                    ? "[✓] WhatsApp ........ CONECTADO"
                    : "[!] WhatsApp ........ BLOQUEADO"}
            `;

            historicoTerminal.appendChild(respostaStatus);

    break;

    default:

        const respostaErro = document.createElement("p");

        respostaErro.textContent =
            `Comando não encontrado: ${comando}`;

        historicoTerminal.appendChild(respostaErro);

    break;
}
        terminalConteudo.appendChild(document.querySelector(".terminal-linha"));

        terminalInput.value = "";

        terminalInput.focus();

        terminalConteudo.scrollTop = terminalConteudo.scrollHeight;
    }
});

const statusModulo = document.querySelector("#statusModulo");

const btnAcesso = document.querySelector("#btnAcesso");
const progressoAcesso = document.querySelector("#progressoAcesso");
const porcentagemAcesso = document.querySelector("#porcentagemAcesso");

btnAcesso.addEventListener("click", function() {

    let progresso = 0;

    const animacaoProgresso = setInterval(function() {

        progresso += 1;

        progressoAcesso.style.width = progresso + "%";
        porcentagemAcesso.textContent = progresso + "%";

        if (progresso >= 100) {
        clearInterval(animacaoProgresso);
        }

    }, 90);

    setTimeout(function() {

        statusModulo.textContent =
            "Carregando módulo Sobre. . .";

    }, 1000);
        

    setTimeout(function() {

        statusModulo.textContent =
            "Carregando módulo Habilidades. . .";

    }, 3000);

    setTimeout(function() {

        statusModulo.textContent =
            "Carregando módulo Projetos. . .";

    }, 5000);

    setTimeout(function() {

        statusModulo.textContent =
            "Carregando módulo Terminal. . .";

    }, 7000);

    setTimeout(function() {

    statusModulo.textContent =
            "Carregando módulo Contato. . .";

    statusSistema.textContent =
    "● SYSTEM ONLINE";

    statusModulo.textContent =
    "";

    document.querySelector("#acessoPermitido").style.display = "block";

    btnAcesso.style.opacity = "0";
    btnAcesso.style.transform = "translateY(-10px)";

    setTimeout(function() {
        btnAcesso.style.visibility = "hidden";
    }, 500);

    porcentagemAcesso.style.opacity = "0";
    porcentagemAcesso.style.transform = "translateY(-10px)";

    setTimeout(function() {
        porcentagemAcesso.style.visibility = "hidden";
    }, 500);


        if (porcentagemAcesso.textContent === "100%") {

        acessoLiberado = true;

        const body = document.querySelector("body");

        body.classList.add("acesso-liberado");

        console.log("ACESSO LIBERADO!");

        const secoes = document.querySelectorAll(
            "#sobre, #habilidades, #projetos, #terminal, #contato"
        );

        secoes.forEach(function(secao) {
            secao.classList.add("secao-animada");
        });

        const observadorSecoes = new IntersectionObserver(function(entradas) {

            entradas.forEach(function(entrada) {

                if (entrada.isIntersecting) {
                    entrada.target.classList.add("visivel");
                }

            });

        }, {
            threshold: 0.2
        });

        secoes.forEach(function(secao) {
            observadorSecoes.observe(secao);
        });

    }

}, 9000);

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
