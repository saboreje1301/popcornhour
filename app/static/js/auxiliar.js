document.getElementById('menu-button').addEventListener('click', function () {
    var menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
});


const carouselInner = document.getElementById('carouselInner');
const prevButton = document.getElementById('prevButton');
const nextButton = document.getElementById('nextButton');

let currentIndex = 0;
const totalItems = 20;
const visibleItems = 6;

function updateCarousel() {
    const translateX = -100 * (currentIndex / visibleItems);
    carouselInner.style.transform = `translateX(${translateX}%)`;
}

prevButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
});

nextButton.addEventListener('click', () => {
    if (currentIndex < totalItems - visibleItems) {
        currentIndex++;
        updateCarousel();
    }
});

updateCarousel();


const form = document.getElementById('login-form');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Send the data to Flask using an AJAX request
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/login', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Login successful, do something
                console.log('Login successful');
            } else {
                // Login failed, do something
                console.log('Login failed');
            }
        }
    };
    xhr.send(JSON.stringify({ email, password }));
});