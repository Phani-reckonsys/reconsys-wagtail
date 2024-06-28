document.addEventListener('DOMContentLoaded', function() {
  // Sort country data and populate dropdown
  function dialCodesData(data) {
      data.sort((a, b) => a.name.localeCompare(b.name));

      const countryDropdown = document.querySelector("#country-code");

      function updateDropdown(filteredData) {
          countryDropdown.innerHTML = "";

          filteredData.forEach(country => {
              const option = document.createElement("option");
              option.value = country.dial_code;
              option.text = `${country.dial_code} ${country.name} ${country.flag}`;
              countryDropdown.add(option);
          });

          countryDropdown.value = "+91";
      }

      updateDropdown(data);
  }

  // Validate email format
  function validateEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
  }

  // Validate phone number format (example: XXX-XXXXXXX)
  function validatePhoneNumber(phoneNumber) {
      const phonePattern = /^\d{10}$/;
      return phonePattern.test(phoneNumber);
  }

  // Show error message
  function showError(field, message) {
      field.classList.add("error");
      const errorElement = field.nextElementSibling;
      errorElement.classList.add("active");
      errorElement.textContent = message;
  }

  // Hide error message
  function hideError(field) {
      field.classList.remove("error");
      const errorElement = field.nextElementSibling;
      errorElement.classList.remove("active");
      errorElement.textContent = "";
  }

  // Submit contact details
  function submitContactDetails(token) {
      const nameField = document.querySelector("#name");
      const emailField = document.querySelector("#email");
      const countryCodeField = document.querySelector("#country-code");
      const phoneNumberField = document.querySelector("#phone-number");
      const companyField = document.querySelector("#company");
      const serviceField = document.querySelector("#services");

      const name = nameField.value.trim();
      const email = emailField.value.trim();
      const countryCode = countryCodeField.value;
      const phoneNumber = phoneNumberField.value.trim();
      const company = companyField.value.trim();
      const service = serviceField.value;

      let hasError = false;

      if (!name) {
          showError(nameField, "Please enter your name");
          hasError = true;
      } else {
          hideError(nameField);
      }

      if (!email) {
          showError(emailField, "Please enter your email");
          hasError = true;
      } else if (!validateEmail(email)) {
          showError(emailField, "Please enter a valid email address");
          hasError = true;
      } else {
          hideError(emailField);
      }

      if (!countryCode) {
          showError(countryCodeField, "Please enter your phone number");
          hasError = true;
      } else {
          hideError(countryCodeField);
      }

      if (!phoneNumber) {
          showError(phoneNumberField, "Please enter your phone number");
          hasError = true;
      } else if (!validatePhoneNumber(phoneNumber)) {
          showError(phoneNumberField, "Please enter a valid phone number");
          hasError = true;
      } else {
          hideError(phoneNumberField);
      }

      if (service === "Select") {
          showError(serviceField, "Please select a service");
          hasError = true;
      } else {
          hideError(serviceField);
      }

      if (hasError) return;

      const sendData = {
          name,
          email,
          phone: `${countryCode}${phoneNumber}`,
          company,
          service,
          token
      };

      const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

      fetch("https://www.reckonsys.com/backend/contact-us", {
          method: "POST",
          body: JSON.stringify(sendData),
          headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken
          }
      })
      .then(response => response.json())
      .then(body => {
          console.log("Subscription successful");
          window.location.href = "https://www.reckonsys.com/thankyou/";
      })
      .catch(error => {
          console.error(error);
      });
  }

  const submitBtn = document.getElementById("submit-btn");
  submitBtn.addEventListener("click", event => {
      event.preventDefault();
      grecaptcha.ready(function() {
          grecaptcha.execute('6Ldc9-spAAAAAIyosghMB05nLNStmWlCnEuzagPL', { action: 'submit' })
          .then(function(token) {
              submitContactDetails(token);
          });
      });
  });
});
