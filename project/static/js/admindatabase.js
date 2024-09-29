function confirmLogout() {
    var confirmAction = confirm("Are you sure you want to logout?");
    if (confirmAction) {
        window.location.href = "index.html"; // Redirect to the login page
    } else {
        // Do nothing, stay on the current page
    }
}

function confirmDelete() {
    var confirmAction = confirm("Are you sure you want to delete this item?");
    if (confirmAction) {
        alert("Item deleted successfully."); // Optional: Show a success message
    } else {
        // Do nothing, stay on the current page
    }
}

// search function (still yet to work )
// document.addEventListener("DOMContentLoaded", () => {
//     const users = JSON.parse(document.getElementById("users-data").textContent);

//     function filterUsers() {
//         const query = document.getElementById("search-bar").value.toLowerCase();
//         const resultsContainer = document.getElementById("search-results");
//         resultsContainer.innerHTML = ""; // Clear previous results

//         if (query) {
//             const filteredUsers = users.filter(user => user.username.toLowerCase().includes(query));
//             if (filteredUsers.length > 0) {
//                 const ul = document.createElement("ul");
//                 filteredUsers.forEach(user => {
//                     const li = document.createElement("li");
//                     li.textContent = user.username;
//                     li.onclick = () => showUserDetails(user.username);
//                     ul.appendChild(li);
//                 });
//                 resultsContainer.appendChild(ul);
//             }
//         }
//     }

//     function showUserDetails(username) {
//         const userItems = document.querySelectorAll(".user-info");
//         userItems.forEach(item => {
//             item.style.display = item.dataset.username === username ? "block" : "none";
//         });
//         document.getElementById("search-results").innerHTML = ""; // Clear search results
//     }

//     window.filterUsers = filterUsers;
//     window.showUserDetails = showUserDetails;
// });