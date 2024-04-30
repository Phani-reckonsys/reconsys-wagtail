function submitContactDetails(){
    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;
    const countryCode = document.querySelector("#country-code").value;
    const phoneNumber = document.querySelector("#phone-number").value;
    const company = document.querySelector("#company").value;
    const service = document.querySelector("#services").value;

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
