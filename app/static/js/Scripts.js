document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuOpen = document.getElementById('menu-open');
    const menuClose = document.getElementById('menu-close');

    if (menuToggle && mobileMenu && menuOpen && menuClose) {
        menuToggle.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            menuOpen.classList.toggle('hidden');
            menuClose.classList.toggle('hidden');
        });
    }

    // Edit project function (only for adminproject.html)
    const projectForm = document.getElementById('project_id');
    if (projectForm) {
        window.editProject = function(id, title, description, image, github_link) {
            document.getElementById('project_id').value = id;
            document.getElementById('title').value = title;
            document.getElementById('description').value = description;
            document.getElementById('image').value = image;
            document.getElementById('github_link').value = github_link;
            const formHeader = document.querySelector('h2');
            if (formHeader) {
                formHeader.textContent = 'Edit Project';
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        };
    }
});