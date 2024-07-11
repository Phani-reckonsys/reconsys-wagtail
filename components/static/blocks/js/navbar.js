  setTimeout(() => {
    const navbar = document.querySelector(".navigation-wrapper");
    const darkSections = document.querySelectorAll(".dark-section");
    const body = document.querySelector("body");
    const menuBars = document.querySelector(".menu-bars");
    const mobileMenu = document.querySelector(".navigation-wrapper");
    const closeMenu = document.querySelector(".close-menu");
    const companyLogo = document.querySelector(".company-logo");

    let lastScrollTop = 0;

    document.addEventListener("scroll", () => {
      if (window.innerWidth > 1000) {
        let st = document.documentElement.scrollTop;
        if (st < lastScrollTop) {
          navbar.classList.remove("move-up");
        } else {
          navbar.classList.add("move-up");
        }
        lastScrollTop = Math.max(0, st);
      }
    });

    menuBars.addEventListener("click", () => {
      mobileMenu.classList.add("menu-open");
      body.style.overflow = "hidden";
    });

    closeMenu.addEventListener("click", () => {
      mobileMenu.classList.remove("menu-open");
      body.style.overflow = "scroll";
    });

    function updateLogoBackground() {
      let darkSectionsInView = 0;

      darkSections.forEach((darkSection) => {
        const rect = darkSection.getBoundingClientRect();
        if (rect.top <= 60 && rect.bottom > 60) {
          darkSectionsInView++;
        }
      });

      if (darkSectionsInView > 0) {
        companyLogo.style.backgroundColor = "#232020";
        navbar.style.backgroundColor = "#232020";
        navbar.classList.add("dark-navbar");
      } else {
        companyLogo.style.backgroundColor = "#fff";
        navbar.style.backgroundColor = "#fff";
        navbar.classList.remove("dark-navbar");
      }
    }

    window.addEventListener("scroll", updateLogoBackground);

    // Initial update
    updateLogoBackground();
  }, 2000); // 2 seconds delay
