document.addEventListener('DOMContentLoaded', function() {
  // Get the necessary DOM elements
  const showMoreBtn = document.querySelector(".ourwork-display .outline-btn-white");
  const showMoreBtnText = document.querySelector(".ourwork-display .outline-btn-white h4");
  const ourWorkCards = document.querySelectorAll(".our-works-card");
  const allBtn = document.querySelector(".all-btn");
  const csdBtn = document.querySelector(".csd-btn");
  const uiBtn = document.querySelector(".ui-btn");

  // Initial count of visible cards
  let ourWorkCardVisibleCount = 8;

  // Function to set the number of visible cards and update button text
  function setOurWorksCardCount(count) {
      ourWorkCardVisibleCount = count;
      ourWorkCards.forEach((card, index) => {
          // Toggle the hidecard class based on the count
          card.classList.toggle("hidecard", index >= count);
      });
      // Update button text based on the number of visible cards
      showMoreBtnText.textContent = (ourWorkCardVisibleCount > 20) ? "Show Less" : "Show More";
  }

  // Initially set the count of visible cards to 8
  setOurWorksCardCount(8);

  // Add click event listener to the show more/less button
  showMoreBtn.addEventListener("click", () => {
      // Toggle between showing 8 and 50 cards
      setOurWorksCardCount(ourWorkCardVisibleCount > 20 ? 8 : 50);
  });

  // Function to filter cards based on their class
  function filterCards(filterClass) {
      ourWorkCards.forEach(card => {
          // Toggle the none class to hide/show cards
          card.classList.toggle("none", !card.classList.contains(filterClass) && filterClass !== 'all');
      });
  }

  // Add click event listener to the 'all' button
  allBtn.addEventListener('click', () => {
      // Set the active class to the 'all' button and remove from others
      allBtn.classList.add("active");
      csdBtn.classList.remove("active");
      uiBtn.classList.remove("active");
      // Show all cards
      filterCards('all');
  });

  // Add click event listener to the 'csd' button
  csdBtn.addEventListener('click', () => {
      // Set the active class to the 'csd' button and remove from others
      csdBtn.classList.add("active");
      allBtn.classList.remove("active");
      uiBtn.classList.remove("active");
      // Show only csd cards
      filterCards('csd');
  });

  // Add click event listener to the 'ui' button
  uiBtn.addEventListener('click', () => {
      // Set the active class to the 'ui' button and remove from others
      uiBtn.classList.add("active");
      allBtn.classList.remove("active");
      csdBtn.classList.remove("active");
      // Show only ui cards
      filterCards('ui');
  });

  // Set the initial state to show all cards and mark the 'all' button as active
  allBtn.classList.add("active");
  filterCards('all');
});
