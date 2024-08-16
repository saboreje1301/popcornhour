document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

    const username = document.getElementById('username').value;
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    const messageDiv = document.getElementById('message');

    if (password !== confirmPassword) {
        messageDiv.textContent = 'Las contraseñas no coinciden';
        messageDiv.classList.remove('hidden');
        messageDiv.classList.add('block');
        return;
    }

    const formData = { username, name, email, password };

    fetch('/register', {
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
        messageDiv.textContent = 'Registro exitoso';
        messageDiv.classList.remove('hidden');
        messageDiv.classList.add('block');
        setTimeout(() => {
            window.location.href = 'login';
        }, 2000); // Redirige después de 2 segundos
    })
    .catch(error => {
        console.error('Error:', error);
        messageDiv.textContent = 'Ocurrió un error: ' + error.message;
        messageDiv.classList.remove('hidden');
        messageDiv.classList.add('block');
    });
});