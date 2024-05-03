function submitNewsletterDetails(){
    const email = document.querySelector("#newsletter-email").value; 
    if (email === "") {
        alert("Please provide email for newsletter");
        return;
    }
     // Validate email format
     const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
     if (!emailPattern.test(email)) {
         alert("Please enter a valid email address");
         return;
     }
     const sendData = {
        email: email,
    }
    fetch("https://qa.reckonsys.com/backend/news-letter", {
        method: "POST",
        body: JSON.stringify(sendData),
        headers: {
            "Content-Type": "application/json"
        }
    }).then((response)=>response.json())
    .then((body)=>{console.log("sussefull");}).catch((error)=>{console.log(error)})
}

const submitEmailBtn = document.querySelector(".newsletter-submit");
submitEmailBtn.addEventListener("click", (event) => {
    event.preventDefault();
    submitNewsletterDetails();
})