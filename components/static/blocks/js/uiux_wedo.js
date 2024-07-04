
gsap.registerPlugin(ScrollTrigger);

// Parallax effect for number image
gsap.to(".number-image", {
  yPercent: -20, // Moves slower than the default scroll
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
  yPercent: -40, // Moves at a different speed
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
  yPercent: -60, // Moves even slower
  ease: "none",
  scrollTrigger: {
    trigger: ".uiux-card",
    start: "top bottom", 
    end: "bottom top",
    scrub: true
  }
});