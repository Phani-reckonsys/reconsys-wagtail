document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".navigation-wrapper");
  const darkSections = document.querySelectorAll(".dark-section");
  let lastScrollTop = 0;
  document.addEventListener("scroll", () => {
    if (window.innerWidth > 1000) {
      var st = document.documentElement.scrollTop;
      if (st < lastScrollTop) {
        navbar.classList.remove("move-up");
      } else {
        navbar.classList.add("move-up");
      }
      lastScrollTop = Math.max(0, st);
    }
  });

  const body = document.querySelector("body");

  //navbar interactivity part starts
  const menuBars = document.querySelector(".menu-bars");
  const mobileMenu = document.querySelector(".navigation-wrapper");
  const closeMenu = document.querySelector(".close-menu");

  menuBars.addEventListener("click", (event) => {
    mobileMenu.classList.add("menu-open");
    body.style.overflow = "hidden";
  });

  closeMenu.addEventListener("click", (event) => {
    mobileMenu.classList.remove("menu-open");
    body.style.overflow = "scroll";
  });

  const companyLogo = document.querySelector(".company-logo");
  const darkSection = document.querySelector(".dark-section");

  let darkSectionsInView = 0;

  function updateLogoBackground() {
    darkSections.forEach((darkSection) => {
      const darkSectionTop = darkSection.getBoundingClientRect().top;
      const darkSectionBottom = darkSection.getBoundingClientRect().bottom;
      if (darkSectionTop <= 60 && darkSectionBottom > 60) {
        // Dark section is in view
        darkSectionsInView++;
      }
    });
    if (darkSectionsInView > 0) {
      // At least one dark section is in view
      companyLogo.style.backgroundColor = "#232020";
      navbar.style.backgroundColor = "#232020";
      navbar.classList.add("dark-navbar");
    } else {
      // No dark sections are in view
      companyLogo.style.backgroundColor = "#fff";
      navbar.style.backgroundColor = "#fff";
      navbar.classList.remove("dark-navbar");
    }

    // Reset the count for the next scroll event
    darkSectionsInView = 0;
  }

  window.addEventListener("scroll", updateLogoBackground);

  // Initial update
  updateLogoBackground();
});
