document.getElementById('fill-card').addEventListener('click', function() {
    // Obtener los valores del formulario
    const title = document.getElementById('titulo_original').value;
    const imageUrl = document.getElementById('url').value;
    const description = document.getElementById('sinopsis').value;
    const year = document.getElementById('anio').value;
    const genre = document.getElementById('genero').value;

    // Actualizar el contenido de la tarjeta
    document.getElementById('card-title').textContent = title;
    document.getElementById('card-image').src = imageUrl;
    document.getElementById('card-description').textContent = `Descripción: ${description}`;
    document.getElementById('card-year').textContent = `Año: ${year}`;
    document.getElementById('card-genre').textContent = `Género: ${genre}`;
});

const cardOriginalTitle = document.getElementById('card-original-title');
const originalTitleInput = document.getElementById('titulo_original');

// Actualizar el título de la tarjeta cuando se escribe en el campo de título
originalTitleInput.addEventListener('input', function () {
    cardOriginalTitle.textContent = originalTitleInput.value || 'Título Original';
});

// Definir contentTypeInputs y cardContentType
const contentTypeInputs = document.querySelectorAll('input[name="tipo"]');
const cardContentType = document.getElementById('card-content-type');

// Actualizar el tipo de contenido de la tarjeta cuando se selecciona un tipo de contenido
contentTypeInputs.forEach(function (input) {
    input.addEventListener('change', function () {
        cardContentType.textContent = 'Tipo de Contenido: ' + (input.value.charAt(0).toUpperCase() + input.value.slice(1));
    });
});


