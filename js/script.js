function toggleMenu(event) {
    var menu = document.getElementById('nav-menu');
    if (menu.classList.contains('hidden')) {
        menu.classList.remove('hidden');
        menu.style.maxHeight = menu.scrollHeight + 'px';
        document.addEventListener('click', closeMenuOnClickOutside);
    } else {
        menu.style.maxHeight = '0';
        menu.addEventListener('transitionend', function() {
            menu.classList.add('hidden');
            document.removeEventListener('click', closeMenuOnClickOutside);
        }, { once: true });
    }
    event.stopPropagation(); 
}

function closeMenuOnClickOutside(event) {
    var menu = document.getElementById('nav-menu');
    var menuIcon = document.querySelector('.menu-icon');
    if (!menu.contains(event.target) && !menuIcon.contains(event.target)) {
        menu.style.maxHeight = '0';
        menu.addEventListener('transitionend', function() {
            menu.classList.add('hidden');
            document.removeEventListener('click', closeMenuOnClickOutside);
        }, { once: true });
    }
}
