function dialCodesData(data) {
  // Sort the data by dial_code
  data.sort((a, b) => a.dial_code.localeCompare(b.dial_code));

  var countryDropdown = document.querySelector("#country-code");

  data.forEach((country) => {
    var option = document.createElement("option");
    option.value = country.dial_code;
    option.text = `${country.dial_code} ${country.flag}  ${country.name} `;
    countryDropdown.add(option);
  });

  // Set the default value to +1 (e.g., for the United States)
  countryDropdown.value = "+1";
}

function submitContactDetails() {
  const name = document.querySelector("#name").value;
  const email = document.querySelector("#email").value;
  const countryCode = document.querySelector("#country-code").value;
  const phoneNumber = document.querySelector("#phone-number").value;
  const company = document.querySelector("#company").value;
  const service = document.querySelector("#services").value;
  const namefield = document.querySelector("#name");
  const emailfield = document.querySelector("#email");
  const countryCodefield = document.querySelector("#country-code");
  const phoneNumberfield = document.querySelector("#phone-number");
  const companyfield = document.querySelector("#company");
  const servicefield= document.querySelector("#services");
  const nameerror = document.querySelector(".name-error-message");
  const emailerror = document.querySelector(".email-error-message");
  const countryCodeerror = document.querySelector(".phn-error-message");
  const phoneNumbererror = document.querySelector(".phn-error-message");
  const companyerror = document.querySelector(".company-error-message");
  const serviceerror= document.querySelector(".services-error-message");
  let error = false;
  let errorvalid = false;
  if (name === "") {
    namefield.classList.add("error");
    nameerror.classList.add("active");
    nameerror.textContent = "Please enter your name"
    error=true;
  }else{
    namefield.classList.remove("error");
  nameerror.classList.remove("active");
  nameerror.textContent = "";
  }
  
  if (email === "") {
    emailfield.classList.add("error");
    emailerror.classList.add("active");
    emailerror.textContent = "Please enter your email"
    error=true;
  }else{
    emailfield.classList.remove("error");
    emailerror.classList.remove("active");
    emailerror.textContent = "";
  }
  
  if (countryCode === "") {
    countryCodefield.classList.add("error");
    countryCodeerror.classList.add("active");
    countryCodeerror.textContent = "Please enter your phone number"
    error=true;
  }else{
    countryCodefield.classList.remove("error");
  countryCodeerror.classList.remove("active");
  countryCodeerror.textContent = "";
  }
  
  if (phoneNumber === "") {
    phoneNumberfield.classList.add("error");
    phoneNumbererror.classList.add("active");
    phoneNumbererror.textContent = "Please enter your phone no."
    error=true;
  }else{
    phoneNumberfield.classList.remove("error");
    phoneNumbererror.classList.remove("active");
    phoneNumbererror.textContent = "";
  }
  
  if (service === "Select") {
    servicefield.classList.add("error");
    serviceerror.classList.add("active");
    serviceerror.textContent = "Please select service"
    error=true;
  }else{
    servicefield.classList.remove("error");
  serviceerror.classList.remove("active");
  serviceerror.textContent = "";
  }


  // Validate email format
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    emailfield.classList.add("error");
    emailerror.classList.add("active");
    emailerror.textContent = "Please enter a valid email address";
    error=true;
  }else{
    emailfield.classList.remove("error");
    emailerror.classList.remove("active");
    emailerror.textContent = "";
  }

  // Validate phone number format (example: XXX-XXXXXXX)
  const phonePattern = /^\d{10}$/;
  if (!phonePattern.test(phoneNumber)) {
    phoneNumberfield.classList.add("error");
    phoneNumbererror.classList.add("active");
    phoneNumbererror.textContent = "Please enter valid phone no.";
    error=true;
  }else{
    phoneNumberfield.classList.remove("error");
    phoneNumbererror.classList.remove("active");
    phoneNumbererror.textContent = "";
  }
  if(error)return;

  const sendData = {
    name: name,
    email: email,
    phone: countryCode + phoneNumber,
    company: company,
    service: service,
  };
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  fetch("https://www.reckonsys.com/backend/contact-us", {
    method: "POST",
    body: JSON.stringify(sendData),
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => response.json())
    .then((body) => {
      console.log("sussefull");
      window.location.href = "https://www.reckonsys.com/thankyou/";
    })
    .catch((error) => {
      console.log(error);
    });
}

const submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", (event) => {
  event.preventDefault();
  submitContactDetails();
});
