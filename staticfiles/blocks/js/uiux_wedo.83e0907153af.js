gsap.registerPlugin(ScrollTrigger);

// Function to check if screen width is above 1000 pixels
function isWideEnough() {
  return window.innerWidth > 1000;
}

// Define the animations within a conditional check for screen width
if (isWideEnough()) {
  // Parallax effect for number image
  gsap.to(".number-image", {
    yPercent: -20,
    ease: "none",
    scrollTrigger: {
      trigger: ".uiux-card",
      start: "top bottom",
      end: "bottom top",
      scrub: true
    }
  });

  // Parallax effect for main image
  gsap.to(".main-image", {
    yPercent: -40,
    ease: "none",
    scrollTrigger: {
      trigger: ".uiux-card",
      start: "top bottom",
      end: "bottom top",
      scrub: true
    }
  });

  // Parallax effect for decor image
  gsap.to(".decor-image", {
    yPercent: -60,
    ease: "none",
    scrollTrigger: {
      trigger: ".uiux-card",
      start: "top bottom",
      end: "bottom top",
      scrub: true
    }
  });
}
