document.addEventListener("keydown", function(event) {
    // Shortcut: Press '/' or 'Ctrl + K' to focus the search bar
    if (event.key === "/" || (event.ctrlKey && event.key === "k")) {
        event.preventDefault(); // Prevent default browser behavior
        let searchInput = document.querySelector("input.md-search__input");
        if (searchInput) {
            searchInput.focus();
        }
    }
});

