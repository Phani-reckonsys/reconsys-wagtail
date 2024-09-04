document.addEventListener('DOMContentLoaded', function() {
  const emailField = document.querySelector("#newsletter-email");
  const submitEmailBtn = document.querySelector(".newsletter-submit");
  const thankyouForSubscription = document.querySelector(".newsletter-subscription-thankyou");
  const emailError = document.querySelector(".subscription-error-message");
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  function validateEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
  }

  function showError(message) {
      emailField.classList.add("error");
      emailError.classList.add("active");
      emailError.textContent = message;
  }

  function hideError() {
      emailField.classList.remove("error");
      emailError.classList.remove("active");
      emailError.textContent = "";
  }

  function submitNewsletterDetails() {
      const email = emailField.value.trim();

      // Validate email input
      if (email === "") {
          showError("Please enter your email");
          return;
      }

      if (!validateEmail(email)) {
          showError("Please enter a valid email address");
          return;
      }

      hideError();

      // Send data to the server
      fetch("https://www.reckonsys.com/backend/news-letter", {
          method: "POST",
          body: JSON.stringify({ email }),
          headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken,
          },
      })
      .then(response => response.json())
      .then(body => {
          thankyouForSubscription.classList.add("active");
          console.log("Subscription successful");
      })
      .catch(error => {
          console.log(error);
      });
  }

  // Add event listener to the submit button
  submitEmailBtn.addEventListener("click", event => {
      event.preventDefault();
      submitNewsletterDetails();
  });
});
