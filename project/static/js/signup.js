document.addEventListener('DOMContentLoaded', (event) => {
    const signUpBtn = document.querySelector('.sign-up-page-btn');
    const dialog = document.getElementById('messageDialog');
    const closeBtn = document.querySelector('.close-btn');
  
    signUpBtn.addEventListener('click', (event) => {
      event.preventDefault(); // Prevent the default form submission behavior
      dialog.style.display = 'block';
    });
  
    closeBtn.addEventListener('click', () => {
        dialog.style.display = 'none';
        window.location.href = 'index.html'; // Redirect to login page
      });
    
      window.addEventListener('click', (event) => {
        if (event.target == dialog) {
          dialog.style.display = 'none';
          window.location.href = 'index.html'; // Redirect to login page
        }
      });
    });