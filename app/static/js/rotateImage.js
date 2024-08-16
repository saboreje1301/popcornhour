document.addEventListener('DOMContentLoaded', function() {
    const image = document.querySelector('.rotate-on-hover');

    image.addEventListener('mouseover', function() {
        image.style.transform = 'rotate(180deg)';
    });

    image.addEventListener('mouseout', function() {
        image.style.transform = 'rotate(0deg)';
    });
});