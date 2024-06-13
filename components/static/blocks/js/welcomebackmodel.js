function delayedExecution() {
    const welcomebackCloseBtn = document.querySelector(".welcomeback-close-btn");
    const welcomebackContainer = document.querySelector(".body-container-welcomeback-model");

    document.addEventListener('mouseout', function(event) {
        if (event.clientY <= 0) {
            if (!document.cookie.split(';').some((item) => item.trim().startsWith('seenMessage='))) {
                // Cookie does not exist, show the message
                welcomebackContainer.classList.remove('remove');
            } 
        }
    });

    welcomebackCloseBtn.addEventListener("click", () => {
        welcomebackContainer.classList.add("remove");
        // Set a cookie named 'seenMessage' that expires in 30 days
        document.cookie = 'seenMessage=true; expires=' + new Date(Date.now() + 2 * 60 * 60 * 1000).toUTCString() + '; path=/';
    });

}

// Call the function after 1 minute of page load
setTimeout(delayedExecution, 60000); // 1 minute in milliseconds
