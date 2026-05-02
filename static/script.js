function toggleTheme() {
    document.body.classList.toggle("light");

    // guardar preferência no browser
    if (document.body.classList.contains("light")) {
        localStorage.setItem("theme", "light");
    } else {
        localStorage.setItem("theme", "dark");
    }
}

// aplicar tema ao carregar a página
window.addEventListener("DOMContentLoaded", () => {
    const theme = localStorage.getItem("theme");

    if (theme === "light") {
        document.body.classList.add("light");
    }
});

// Menu
function toggleMenu(btn) {
    const menu = btn.nextElementSibling;

    // fecha todos os outros
    document.querySelectorAll(".menu-dropdown").forEach(m => {
        if (m !== menu) m.style.display = "none";
    });

    // alterna este
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}

// fechar ao clicar fora
document.addEventListener("click", function (e) {
    if (!e.target.closest(".menu-wrapper")) {
        document.querySelectorAll(".menu-dropdown").forEach(m => {
            m.style.display = "none";
        });
    }
});