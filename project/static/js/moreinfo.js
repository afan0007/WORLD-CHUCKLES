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