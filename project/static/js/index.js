document.addEventListener('DOMContentLoaded', (event) => {
    const togglePassword = document.querySelector('.toggle-password');
    const passwordField = document.querySelector('input[type="password"]');

    togglePassword.addEventListener('click', function () {
        // Toggle the type attribute
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        
        // Toggle the eye icon
        this.querySelector('i').classList.toggle('fa-eye');
        this.querySelector('i').classList.toggle('fa-eye-slash');
    });
});


  