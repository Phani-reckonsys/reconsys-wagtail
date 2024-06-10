function dialCodesData(data) {
  // Sort the data by country name
  data.sort((a, b) => a.name.localeCompare(b.name));

  var countryDropdown = document.querySelector("#country-code");
  var searchInput = document.querySelector("#search-input");

  function updateDropdown(filteredData) {
    // Clear existing options
    countryDropdown.innerHTML = "";

    // Add options for filtered countries
    filteredData.forEach((country) => {
      var option = document.createElement("option");
      option.value = country.dial_code;
      option.text = `${country.name} ${country.dial_code} ${country.flag}`;
      countryDropdown.add(option);
    });
    countryDropdown.value = "+91";
  }

  // Initial population of dropdown
  updateDropdown(data);

  // Event listener for search input
  searchInput.addEventListener("input", function() {
    var searchTerm = searchInput.value.toLowerCase();
    var filteredData = data.filter((country) => {
      return country.name.toLowerCase().includes(searchTerm);
    });
    updateDropdown(filteredData);
  });
}



  

function submitContactDetails(token) {
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
    token: token,
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
  grecaptcha.ready(function() {
    grecaptcha.execute('6Ldc9-spAAAAAIyosghMB05nLNStmWlCnEuzagPL', {action: 'submit'}).then(function(token) {
        submitContactDetails(token);
    });
  });
});
