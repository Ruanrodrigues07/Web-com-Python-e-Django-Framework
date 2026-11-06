function gritar() {
    alert("AAAAAAAAHHHHHHHHHHHHHHHHH");
}

function perguntar() {
    var nome;
    nome = prompt("Qual é o seu nome?");
    alert("Olá, " + nome + "! Prazer em te conhecer!");
}

function mudar_texto() {
    var h1 = document.getElementsByTagName("h1");

    if(h1[0].innerText == "Geek University") {
        
        h1[0].innerText = "Evolua o seu lado Geek!";
    } else {
        h1[0].innerText = "Geek University";
    }

}

function Incrementar() {
    var p1 = document.getElementById("p1");
    for(var i = 0; i < 1000; i++) {
        p1.innerText = parseInt(p1.innerText) + 1;
    }
}