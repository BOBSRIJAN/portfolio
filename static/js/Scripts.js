document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuOpen = document.getElementById('menu-open');
    const menuClose = document.getElementById('menu-close');

    menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        menuOpen.classList.toggle('hidden');
        menuClose.classList.toggle('hidden');
    });
});
