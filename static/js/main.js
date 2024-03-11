// методы для кнопок в шапке сайта
function onHover() {
  document
    .querySelector(".header__buttonNeeds")
    .classList.add("header__buttonNeedsActiv");

  document
    .querySelector(".header__buttonHelp")
    .classList.add("header__buttonHelpNotActiv");
}

function outHover() {
  document
    .querySelector(".header__buttonNeeds")
    .classList.remove("header__buttonNeedsActiv");

  document
    .querySelector(".header__buttonHelp")
    .classList.remove("header__buttonHelpNotActiv");
}

// методы для кнопок в подвале сайта
function onHoverFooter() {
  document
    .querySelector(".footer__buttonNeeds")
    .classList.add("footer__buttonNeedsActiv");

  document
    .querySelector(".footer__buttonHelp")
    .classList.add("footer__buttonHelpNotActiv");
}

function outHoverFooter() {
  document
    .querySelector(".footer__buttonNeeds")
    .classList.remove("footer__buttonNeedsActiv");

  document
    .querySelector(".footer__buttonHelp")
    .classList.remove("footer__buttonHelpNotActiv");
}

// медод раскрытия бургера в мобильной версии

function burgerMobile() {
  document.querySelector(".header").classList.toggle("open");
}

// // без функции 
// document.querySelector(".header__burger").addEventListener("click", () => {
//   document.querySelector(".header").classList.toggle("open");
// });
