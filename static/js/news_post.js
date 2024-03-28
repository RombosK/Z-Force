// елемент слайдера, чтобы не отображь его при отсутствии фото
const sliderElem = document.querySelector(".newsPost__slider");
// стрелки
const leftArrowElem = document.querySelector(".newsPost__slider_navLeft");
const rightArrowElem = document.querySelector(".newsPost__slider_navRight");
//  массив фото
const imagesElem = document.querySelectorAll(".newsPost__slider_img");
// элемент для фобавления номера текущего фото
let numberElem = document.querySelector(".newsPost__slider_navNumber");

let index = 0;

console.log(imagesElem);

// блокировка сладера при отсутствии фото
if (imagesElem.length < 1) {
  sliderElem.classList.add("newsPost__slider_NotActive");
}

numberElem.textContent = index + 1 + " из " + imagesElem.length;
// начальное отображение первой фотографи
imagesElem[0].classList.remove("newsPost__slider_imgHidden");

//  событие нажатие на стрелку вправо
rightArrowElem.addEventListener("click", () => {
  if (index >= imagesElem.length - 1) {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index = 0;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index++;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});

//  событие нажатие на стрелку влево
leftArrowElem.addEventListener("click", () => {
  if (index === 0) {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index = imagesElem.length - 1;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("newsPost__slider_imgHidden");
    index--;
    imagesElem[index].classList.remove("newsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});

// document.querySelector(".newsPost__slider_imgBox").addEventListener('click', () => {

//   document.querySelector(".newsPost__slider_imgline").style.height = "700px"
//   // console.log(document.querySelector(".slider_imgline").style.height);

// });

document.querySelector(".newsPost__slider_imgBox").addEventListener('click', () => {

  // document.querySelector(".newsPost__slider").classList.toggle('show');
  document.querySelector(".container-md").classList.toggle('show_back');
  document.querySelector(".header").classList.toggle('header__none');
  document.querySelector(".footer").classList.toggle('header__none');
  document.querySelector(".newsPost__titleBox").classList.toggle('header__none');
  document.querySelector(".newsPost__top").classList.toggle('header__none');
  document.querySelector(".newsPost__text").classList.toggle('header__none');
  document.querySelector(".newsPost__data").classList.toggle('header__none');
  document.querySelector(".newsPost__slider_imgline").classList.toggle('show__size');
  document.querySelector(".button__back_conteiner").classList.toggle('header__none');


  // document.querySelector(".container-md").classList.toggle('show_back');
  
  // document.querySelector(".newsPost__slider_imgline").style.height = "700px"
  // console.log(document.querySelector(".slider_imgline").style.height);

});
