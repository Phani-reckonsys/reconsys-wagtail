// FAQ toggle

const questions = document.querySelectorAll(".faq-wrapper");
questions.forEach((question) => {
  question.addEventListener("click", () => {
    const isActive = question.classList.contains("active");
    questions.forEach((question) => {
      question.classList.remove("active");
    });
    if (!isActive) {
      question.classList.add("active");
    }
  });
});

const accQuestions = document.querySelectorAll(".custom-question");
const accPlus = document.querySelectorAll(".accordian-plus");
const customAccordian = document.querySelectorAll(".custom-accordian");
const accAnswers = document.querySelectorAll(".custom-answer");
accQuestions.forEach((question, index) => {
  question.addEventListener("click", () => {
    const isActive = accAnswers[index].classList.contains("active");
    accQuestions.forEach((_, indexAll) => {
      accAnswers[indexAll].classList.remove("active");
      customAccordian[indexAll].classList.remove("up");
      accPlus[indexAll].classList.remove("rotate");
    });
    if (!isActive) {
      accAnswers[index].classList.add("active");
      customAccordian[index].classList.add("up");
      accPlus[index].classList.add("rotate");
    }
  });
});

