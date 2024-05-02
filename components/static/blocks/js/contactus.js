function submitContactDetails(){
    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;
    const countryCode = document.querySelector("#country-code").value;
    const phoneNumber = document.querySelector("#phone-number").value;
    const company = document.querySelector("#company").value;
    const service = document.querySelector("#services").value;
    
    if (name === "" || email === "" || countryCode === "" || phoneNumber === "" || company === "" || service === "") {
        alert("Please fill in all fields");
        return;
    }

    // Validate email format
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address");
        return;
    }

    // Validate phone number format (example: XXX-XXXXXXX)
    const phonePattern = /^\d{3}-\d{7}$/;
    if (!phonePattern.test(phoneNumber)) {
        alert("Please enter a valid phone number (XXX-XXXXXXX)");
        return;
    }

    const sendData = {
        name: name,
        email: email,
        phone: countryCode+phoneNumber,
        company: company,
        service: service,
    }
    fetch("https://qa.reckonsys.com/backend/contact-us", {
        method: "POST",
        body: JSON.stringify(sendData),
        headers: {
            "Content-Type": "application/json"
        }
    }).then((response)=>response.json())
    .then((body)=>{console.log("sussefull")}).catch((error)=>{console.log(error)})
}

const submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", (event) => {
    event.preventDefault();
    submitContactDetails();
})
