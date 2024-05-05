const showMoreBtn = document.querySelector(".ourwork-display .outline-btn");
const showMoreBtnText = document.querySelector(".ourwork-display .outline-btn h4");
let ourWorkCardVisibleCount = 8;
const ourWorkCards = document.querySelectorAll(".our-works-card");  // All cards selector
function setOurWorksCardCount(count) {
  ourWorkCardVisibleCount = count;
  for (const [index, card] of ourWorkCards.entries()) {
    if (index < count) {
      card.classList.remove("hidecard");
      showMoreBtnText.textContent = "Show Less"
    } else {
      card.classList.add("hidecard");
      showMoreBtnText.textContent = "show more"
    }
  }
}

setOurWorksCardCount(8);
showMoreBtn.addEventListener("click", () => {
  if (ourWorkCardVisibleCount > 20) setOurWorksCardCount(8);
  else setOurWorksCardCount(50);
});

const allBtn = document.querySelector(".all-btn");
const csdBtn = document.querySelector(".csd-btn");
const uiBtn = document.querySelector(".ui-btn");

const csdCards = document.querySelectorAll(".our-works-card.csd");  // All cards selector
const uiCards = document.querySelectorAll(".our-works-card.ui");  // All cards selector

allBtn.addEventListener('click', () => {
  ourWorkCards.forEach(card => {
    card.classList.remove("none");
    card.classList.remove("active");
  });
});

csdBtn.addEventListener('click', () => {
  ourWorkCards.forEach(card => {
    card.classList.remove("none");
    card.classList.remove("active");
  });
  uiCards.forEach(card => {
    card.classList.add("none");
  });
  csdCards.forEach(card => {
    card.classList.add("active");
  });
});

uiBtn.addEventListener('click', () => {
  ourWorkCards.forEach(card => {
    card.classList.remove("none");
    card.classList.remove("active");
  });
  uiCards.forEach(card => {
    card.classList.add("active");
  });
  csdCards.forEach(card => {
    card.classList.add("none");
  });
});

