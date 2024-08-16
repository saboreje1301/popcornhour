document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

    const formData = {
        username: document.getElementById('username').value,
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
    };

    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.message || 'Error en la solicitud');
            });
        }
        return response.json();
    })
    .then(data => {
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = 'Registro exitoso';
        messageDiv.classList.remove('hidden');
        messageDiv.classList.add('block');
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 2000); // Redirige después de 2 segundos
    })
    .catch(error => {
        console.error('Error:', error);
        const messageDiv = document.getElementById('message');
        messageDiv.textContent = 'Ocurrió un error: ' + error.message;
        messageDiv.classList.remove('hidden');
        messageDiv.classList.add('block');
    });
});