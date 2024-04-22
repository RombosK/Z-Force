// ПРОГРЕСС ЛИНИЯ

let totalSum = document.querySelector(".projectsPost__totalSum").innerHTML;
let collectedSum = document.querySelector(
  ".projectsPost__collectedSum"
).innerHTML;

totalSum = totalSum.replace(/[^0-9]/g, "");
collectedSum = collectedSum.replace(/[^0-9]/g, "");
console.log(totalSum);
console.log(typeof(totalSum));

if (totalSum === '0') {
  console.log("иф сработал");
  document.querySelector(".projectsPost__shortDescription").style.display = "block";
  document.querySelector(".projectsPost__payment").style.display = "none";
  document.querySelector(".projectsPost__donations").style.display = "none";
  document.querySelector(".projectsPost__stillNeed").style.display = "none";
}

const percentages = ((collectedSum / totalSum) * 100).toFixed(2);

if (percentages >= 100) {
  document.querySelector(".projectsPost__donationsProgress").style.width =
    100 + "%";
  document
    .querySelector(".projectsPost__payment")
    .classList.add("projectsPost__collectedSum");
  document.querySelector(".projectsPost__payment").textContent = "Сбор закрыт";
} else {
  document.querySelector(".projectsPost__donationsProgress").style.width =
    percentages + "%";
}

const stillNeed = totalSum - collectedSum;

if (percentages >= 100) {
  document.querySelector(".projectsPost__stillNeed").style.display = "none";
} else {
  document.querySelector(".projectsPost__stillNeed").innerHTML =
    "Осталось собрать " + stillNeed;
}

// СЛАЙДНР

// елемент слайдера, чтобы не отображь его при отсутствии фото
const sliderElem = document.querySelector(".projectsPost__slider");
// стрелки
const leftArrowElem = document.querySelector(".projectsPost__slider_navLeft");
const rightArrowElem = document.querySelector(".projectsPost__slider_navRight");
//  массив фото
const imagesElem = document.querySelectorAll(".projectsPost__slider_img");
// элемент для фобавления номера текущего фото
let numberElem = document.querySelector(".projectsPost__slider_navNumber");

let index = 0;

// блокировка сладера при отсутствии фото
if (imagesElem.length < 1) {
  sliderElem.classList.add("projectsPost__slider_NotActive");
}

numberElem.textContent = index + 1 + " из " + imagesElem.length;
// начальное отображение первой фотографи
imagesElem[0].classList.remove("projectsPost__slider_imgHidden");

//  событие нажатие на стрелку вправо
rightArrowElem.addEventListener("click", () => {
  if (index >= imagesElem.length - 1) {
    imagesElem[index].classList.add("projectsPost__slider_imgHidden");
    index = 0;
    imagesElem[index].classList.remove("projectsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("projectsPost__slider_imgHidden");
    index++;
    imagesElem[index].classList.remove("projectsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});

//  событие нажатие на стрелку влево
leftArrowElem.addEventListener("click", () => {
  if (index === 0) {
    imagesElem[index].classList.add("projectsPost__slider_imgHidden");
    index = imagesElem.length - 1;
    imagesElem[index].classList.remove("projectsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  } else {
    imagesElem[index].classList.add("projectsPost__slider_imgHidden");
    index--;
    imagesElem[index].classList.remove("projectsPost__slider_imgHidden");
    numberElem.textContent = index + 1 + " из " + imagesElem.length;
  }
});
