document.addEventListener("DOMContentLoaded",(r=>{gsap.registerPlugin(ScrollTrigger);gsap.utils.toArray(".our-process-card"),gsap.utils.toArray(".our-process-card-width");const e=document.querySelector(".our-process-card-wrapper"),t=document.querySelector(".our-process-card-width");if(e&&t){const{scrollWidth:r,clientWidth:o}=e;Math.max((r-o)/o,0);gsap.to(t,{x:-r+o,scrollTrigger:{trigger:e,pin:!0,scrub:1,end:"+=3000",markers:!1}})}const o=document.querySelector(".slider-marker");o&&e&&gsap.to(o,{width:"100%",scrollTrigger:{trigger:e,start:"top left",end:"+=3000",scrub:1}});const s=document.querySelector(".indicator-flag");s&&e&&gsap.to(s,{left:"98%",scrollTrigger:{trigger:e,start:"top left",end:"+=3000",scrub:1}})}));