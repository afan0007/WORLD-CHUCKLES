function confirmLogout() {
    var confirmAction = confirm("Are you sure you want to logout?");
    if (confirmAction) {
        window.location.href = "index.html"; // Redirect to the login page
    } else {
        // Do nothing, stay on the current page
    }
}

// function confirmDelete() {
//     var confirmAction = confirm("Are you sure you want to delete this item?");
//     if (confirmAction) {
//         alert("Item deleted successfully."); // Optional: Show a success message
//     } else {
//         // Do nothing, stay on the current page
//     }
// }