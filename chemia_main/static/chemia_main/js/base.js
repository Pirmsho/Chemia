// burger functionality
document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.header_flex');
    const burgerMenu = document.querySelector('.burger-menu');
    const navMenu = document.querySelector('.nav_div');

    burgerMenu.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        header.classList.toggle('show_nav');
    });
});

