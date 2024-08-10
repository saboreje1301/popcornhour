    document.getElementById('fill-card').addEventListener('click', function() {
        // Obtener los valores del formulario
        const title = document.getElementById('title').value;
        const imageUrl = document.getElementById('image-url').value;
        const description = document.getElementById('description').value;
        const year = document.getElementById('year').value;
        const genre = document.getElementById('genre').value;

        // Actualizar el contenido de la tarjeta
        document.getElementById('card-title').textContent = title;
        document.getElementById('card-image').src = imageUrl;
        document.getElementById('card-original-title').textContent = `Descripción: ${description}`;
        document.getElementById('card-year').textContent = `Año: ${year}`;
        document.getElementById('card-genre').textContent = `Género: ${genre}`;
    });

    document.getElementById('moderator-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevenir el comportamiento por defecto del formulario

        // Obtener los valores del formulario
        const title = document.getElementById('title').value;
        const imageUrl = document.getElementById('image-url').value;
        const description = document.getElementById('description').value;
        const year = document.getElementById('year').value;
        const genre = document.getElementById('genre').value;

        // Guardar los datos (aquí puedes agregar la lógica para guardar los datos, por ejemplo, enviarlos a un servidor)
        console.log('Datos guardados:', { title, imageUrl, description, year, genre });
    });

    document.addEventListener('DOMContentLoaded', function () {
        const titleInput = document.getElementById('title');
        const originaltitleInput = document.getElementById('original-title');
        const contentTypeInputs = document.querySelectorAll('input[name="content-type"]');
        const cardTitle = document.getElementById('card-title');
        const cardOriginalTitle = document.getElementById('card-original-title');
        const cardContentType = document.getElementById('card-content-type');
    
        // Actualizar el título de la tarjeta cuando se escribe en el campo de título
        titleInput.addEventListener('input', function () {
            cardTitle.textContent = titleInput.value || 'Título de la Película/Serie';
        });

        // Actualizar el título de la tarjeta cuando se escribe en el campo de título
        originaltitleInput.addEventListener('input', function () {
            cardOriginalTitle.textContent = originaltitleInput.value || 'Título Original';
        });
    
        // Actualizar el tipo de contenido de la tarjeta cuando se selecciona un tipo de contenido
        contentTypeInputs.forEach(function (input) {
            input.addEventListener('change', function () {
                cardContentType.textContent = 'Tipo de Contenido: ' + (input.value.charAt(0).toUpperCase() + input.value.slice(1));
            });
        });
        // Actualizar la URL de la imagen del póster en la tarjeta
        const imageUrlInput = document.getElementById('image-url');
        const cardImage = document.getElementById('card-image');

        imageUrlInput.addEventListener('input', function () {
            cardImage.src = imageUrlInput.value;
        });

        // Actualizar el año en la tarjeta cuando se selecciona un año
        const yearInput = document.getElementById('year');
        const cardYear = document.getElementById('card-year');

        yearInput.addEventListener('input', function () {
            cardYear.textContent = 'Año: ' + yearInput.value;
        });
        
    });

