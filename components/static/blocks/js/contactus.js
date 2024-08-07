document.addEventListener('DOMContentLoaded', function () {
    // Function to update the dropdown with sorted and filtered data
    function dialCodesData(data) {
        // Sort the data by country name
        data.sort((a, b) => a.name.localeCompare(b.name));

        var countryDropdown = document.querySelector("#country-code");

        // Function to update the dropdown options
        function updateDropdown(filteredData) {
            // Clear existing options
            countryDropdown.innerHTML = "";

            // Add options for filtered countries
            filteredData.forEach((country) => {
                var option = document.createElement("option");
                option.value = country.dial_code;
                option.text = `${country.dial_code} ${country.name}`;
                countryDropdown.add(option);
            });

            // Set the default value to "+91"
            countryDropdown.value = "+91";
        }

        // Initial population of dropdown
        updateDropdown(data);
    }

    // Function to fetch country data
    function fetchCountryData() {
        fetch('https://restcountries.com/v3.1/all')
            .then(response => response.json())
            .then(data => {
                const countries = data.map(country => ({
                    name: country.name.common,
                    dial_code: country.idd.root + (country.idd.suffixes ? country.idd.suffixes[0] : ''),
                    flag: country.flags[0] // Assuming this is the flag URL
                }));
                dialCodesData(countries);
            })
            .catch(error => {
                console.error('Error fetching country data:', error);
            });
    }

    // Fetch country data when the page loads
    fetchCountryData();

    // Function to validate email format
    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    // Function to validate phone number format
    function validatePhoneNumber(phoneNumber) {
        const phonePattern = /^\d{10}$/;
        return phonePattern.test(phoneNumber);
    }


    // Function to show error message
    function showError(field, message) {
        field.classList.add("error");
        const errorElement = field.parentElement.querySelector(".error-message");
        errorElement.classList.add("active");
        errorElement.textContent = message;
    }

    // Function to hide error message
    function hideError(field) {
        field.classList.remove("error");
        const errorElement = field.parentElement.querySelector(".error-message");
        errorElement.classList.remove("active");
        errorElement.textContent = "";
    }

    // Function to submit contact details
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
        const service = serviceField.value.trim();

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

        if (!company) {
            showError(companyField, "Please enter your company name");
            hasError = true;
        } else {
            hideError(companyField);
        }

        if (!service) {
            showError(serviceField, "Please enter your company name");
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
        grecaptcha.ready(function () {
            grecaptcha.execute('6Ldc9-spAAAAAIyosghMB05nLNStmWlCnEuzagPL', { action: 'submit' })
                .then(function (token) {
                    submitContactDetails(token);
                });
        });
    });
});
