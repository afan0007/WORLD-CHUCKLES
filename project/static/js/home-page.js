// generate joke button 
// document.getElementById('generate-joke-button').addEventListener('click', function() {
//     alert('Joke generated!'); // You can replace this with the actual joke generation logic.
//   });
//new 5 star rating
// document.addEventListener('DOMContentLoaded', function () {
//   const stars = document.querySelectorAll('.star');

//   stars.forEach(star => {
//       star.addEventListener('click', function () {
//           const index = parseInt(star.getAttribute('data-index'));

//           // Fill the stars up to the clicked one
//           stars.forEach((s, i) => {
//               if (i < index) {
//                   s.classList.add('filled');
//               } else {
//                   s.classList.remove('filled');
//               }
//           });
//       });
//   });
// });
//5 star ratings 
// document.addEventListener('DOMContentLoaded', function() {
// const stars = document.querySelectorAll('.star');

// stars.forEach(star => {
//     star.addEventListener('click', function() {
//     const clickedIndex = Array.from(stars).indexOf(star);

//     // Remove 'filled' class from all stars
//     stars.forEach((star, index) => {
//         star.classList.remove('filled');
//         if (index <= clickedIndex) {
//         star.classList.add('filled');
//         }
//     });

//     // Optionally, you can send the rating to a server or perform other actions here
//     console.log('User rated:', clickedIndex + 1, 'stars');
//     });
// });
// });
 
//copy function 
function copyToClipboard() {
  const jokeText = document.getElementById('joke-text').innerText;
  const copyStatus = document.getElementById('copyStatus');
  
  // Create a temporary textarea element
  const tempTextArea = document.createElement('textarea');
  tempTextArea.value = jokeText;
  document.body.appendChild(tempTextArea);
  
  // Select and copy the text
  tempTextArea.select();
  document.execCommand('copy');
  
  // Remove the temporary element
  document.body.removeChild(tempTextArea);
  
  // Show the "Copied!" message
  copyStatus.style.display = 'inline';
  alert('Joke text copied to clipboard!');
  setTimeout(() => {
    copyStatus.style.display = 'none';
  }, 2000);
}
// dynamic height change of text bubble that holds joke
// window.addEventListener('load', function() {
//   var jokeText = document.getElementById('joke-text');
//   var rectangle = document.getElementById('rectangle');
  
//   // Update the height of the rectangle based on the content height
//   rectangle.style.height = jokeText.offsetHeight + 'px';
// });

// YET TO WORK (Can be omitted if its not useful )
// input prompt
//  pencil icon is hidden when the input field gains focus.
// pencil icon is shown again if the input field loses focus and is empty.
document.getElementById('joke-keywords-input').addEventListener('focus', function() {
    document.getElementById('edit-pencil-icon').style.display = 'none';
  });
  
document.getElementById('joke-keywords-input').addEventListener('blur', function() {
if (this.value === '') {
    document.getElementById('edit-pencil-icon').style.display = 'block';
}
});

function confirmLogout() {
  var confirmAction = confirm("Are you sure you want to logout?");
  if (confirmAction) {
      window.location.href = "index.html"; // Redirect to the login page
  } else {
      // Do nothing, stay on the current page
  }
}
