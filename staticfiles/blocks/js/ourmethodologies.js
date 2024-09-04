document.addEventListener("DOMContentLoaded", () => {
    // Get all selector groups and content displays
    const selectorGroups = document.querySelectorAll(".selector-group");
    const contentDisplays = document.querySelectorAll(".contentdisplay");
  
    // Function to handle selector group clicks
    const handleSelectorClick = (index) => {
      // Remove 'active' class from all selector groups and content displays
      selectorGroups.forEach((group) => group.classList.remove("active"));
      contentDisplays.forEach((display) => display.classList.remove("active"));
  
      // Add 'active' class to the clicked selector group and corresponding content display
      if (selectorGroups[index]) {
        selectorGroups[index].classList.add("active");
      }
      if (contentDisplays[index]) {
        contentDisplays[index].classList.add("active");
      }
    };
  
    // Add click event listeners to each selector group
    selectorGroups.forEach((group, index) => {
      group.addEventListener("click", () => {
        handleSelectorClick(index);
      });
    });
  
    // Optionally, show the first content display by default
    if (contentDisplays.length > 0) {
      contentDisplays[0].classList.add("active");
      selectorGroups[0].classList.add("active");
    }
  });
  