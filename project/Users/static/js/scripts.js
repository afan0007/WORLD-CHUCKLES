// static/js/scripts.js
document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];

    window.showModal = function(description, keyword, status) {
        document.getElementById("modal-description").innerText = "Description: " + description;
        document.getElementById("modal-keyword").innerText = "Keyword: " + keyword;
        document.getElementById("modal-status").innerText = "Status: " + status;
        modal.style.display = "block";
    }

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
