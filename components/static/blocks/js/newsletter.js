function submitNewsletterDetails() {
  const email = document.querySelector("#newsletter-email").value;
  const emailfield = document.querySelector("#newsletter-email");
  const thankyouForSubscription = document.querySelector(
    ".newsletter-subscription-thankyou"
  );
  const emailerror = document.querySelector(".subscription-error-message");
  if (email === "") {
    emailfield.classList.add("error");
    emailerror.classList.add("active");
    emailerror.textContent = "Please enter your email"
    return;
  }else{
    emailfield.classList.remove("error");
    emailerror.classList.remove("active");
    emailerror.textContent = "";
  }
  // Validate email format
  // Validate email format
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    emailfield.classList.add("error");
    emailerror.classList.add("active");
    emailerror.textContent = "Please enter a valid email address";
    return;
  }else{
    emailfield.classList.remove("error");
    emailerror.classList.remove("active");
    emailerror.textContent = "";
  }
  const sendData = { email: email };
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  fetch("https://www.reckonsys.com/backend/news-letter", {
    method: "POST",
    body: JSON.stringify(sendData),
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => response.json())
    .then((body) => {
      thankyouForSubscription.classList.add("active");
      console.log("sussefull");
    })
    .catch((error) => {
      console.log(error);
    });
}

const submitEmailBtn = document.querySelector(".newsletter-submit");
submitEmailBtn.addEventListener("click", (event) => {
  event.preventDefault();
  submitNewsletterDetails();
});
