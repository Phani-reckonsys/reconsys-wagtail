// const companyLogo = document.querySelector('.company-logo');
// const darkSection = document.querySelector('.dark-section');

// const observer = new IntersectionObserver(entries => {
//     entries.forEach(entry => {
//         if (entry.isIntersecting) {
//             // Dark section is in view
//             companyLogo.style.background = '#000'; // Change to desired dark color
//         } else {
//             // White section is in view
//             companyLogo.style.background = '#fff'; // Change to desired light color
//         }
//     });
// });

// observer.observe(darkSection);


// const companyLogo = document.querySelector('.company-logo');
// const darkSection = document.querySelector('.dark-section');

// if (darkSection) {
//     const observer = new IntersectionObserver(entries => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 // Dark section is in view
//                 companyLogo.style.background = '#000'; // Change to desired dark color
//                 console.log("dark");
//             } else {
//                 // White section is in view
//                 companyLogo.style.background = '#fff'; // Change to desired light color
//             }
//         });
//     });

//     observer.observe(darkSection);
// }


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

// Initial update
updateLogoBackground();


