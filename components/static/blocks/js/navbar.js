const companyLogo = document.querySelector('.company-logo');
const darkSection = document.querySelector('.dark-section');

function updateLogoBackground() {
    if (darkSection && darkSection.getBoundingClientRect().top < window.innerHeight) {
        // Dark section is in view
        companyLogo.style.background = '#000'; // Change to desired dark color
    } else {
        // Dark section is not in view
        companyLogo.style.background = '#fff'; // Change to desired light color
    }
}

window.addEventListener('scroll', updateLogoBackground);




