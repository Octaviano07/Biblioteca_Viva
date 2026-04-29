// =====================
// WHATSAPP
// =====================
const btn = document.getElementById("whatsappBtn");

if (btn) {
    btn.href = "https://wa.me/" + dados.whatsapp;
    btn.target = "_blank";
}

// =====================
// Perfil foto
//======================
window.onload = () => {
    document.getElementById("autorImg").src =
        "img/" + dados.imagemAutor;
};


// =====================
// FRASES ALEATÓRIAS
// =====================
const fraseEl = document.getElementById("frase");

if (fraseEl) {
    let i = 0;
    fraseEl.textContent = dados.frases[0];

    setInterval(() => {
        i = (i + 1) % dados.frases.length;
        fraseEl.textContent = dados.frases[i];
    }, 3000);
}

// =====================
// LISTA DE POSTS
// =====================
const container = document.getElementById("posts");

if (container) {
    dados.posts.forEach(p => {

        const div = document.createElement("div");
        div.classList.add("card");

        div.innerHTML = `
            <h3>${p.titulo}</h3>
            <small>${p.categoria}</small>
            <p>${p.resumo}</p>
            <a href="post.html?id=${p.id}">Ler mais</a>
        `;

        container.appendChild(div);
    });
}

// =====================
// POST INDIVIDUAL
// =====================
const postContainer = document.getElementById("post");

if (postContainer) {

    const url = new URLSearchParams(window.location.search);
    const id = url.get("id");

    const post = dados.posts.find(p => p.id == id);

    if (post) {
        postContainer.innerHTML = `
            <h1>${post.titulo}</h1>
            <h4>${post.categoria}</h4>
            <p>${post.conteudo}</p>
        `;
}
} 