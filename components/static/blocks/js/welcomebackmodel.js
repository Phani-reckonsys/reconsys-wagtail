const welcomebackCloseBtn = document.querySelector(".welcomeback-close-btn");
const welcomebackContainer = document.querySelector(".body-container-welcomeback-model");

// document.addEventListener('visibilitychange', function() {
//     // Check if the 'seenMessage' cookie exists
//     // if (document.cookie.split(';').some((item) => item.trim().startsWith('seenMessage='))) {
//     //     // Cookie exists, do not show the message
//     //     welcomebackContainer.classList.remove('remove');
//     //     console.log("phani");
//     // } 
//     if (document.hidden) {
//         // Page is hidden (user switched to a different tab or minimized the window)
//         welcomebackContainer.classList.remove('remove');
//     } 
// });




// welcomebackCloseBtn.addEventListener("click", ()=>{
//     welcomebackContainer.classList.add("remove");
//     // Set a cookie named 'seenMessage' that expires in 30 days
//     document.cookie = 'seenMessage=true; expires=' + new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toUTCString() + '; path=/';

// })

document.addEventListener('mouseout', function(event) {
    // welcomebackContainer.classList.remove('remove');
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

