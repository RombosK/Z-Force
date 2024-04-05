
// слАйдер

// контейнер для конвейера фотограций
const sliderLineElem = document.querySelector(".index__slider_items");
// Массив изображений
const sliderItemsElem = document.querySelectorAll(".index__slider_item");
// левая стрелка
const arrowLeftElem = document.querySelector(".index__slider_arrowLeft");
// правая стрелка
const arrowRightElem = document.querySelector(".index__slider_arrowRight");


let activeImage = 0;

// начальное отображение картинки
function slider() {
  for (let i = 0; i < sliderItemsElem.length; i++) {
    sliderItemsElem[i].classList.add("index__slider_item-opasity");
  }
  sliderItemsElem[activeImage].classList.remove("index__slider_item-opasity");
}

slider();

// события нажатия на стрелки
arrowRightElem.addEventListener("click", () => {
  if (activeImage >= sliderItemsElem.length - 1) {
    activeImage = 0;
  } else {
    activeImage++;
  }
  slider();
});
arrowLeftElem.addEventListener("click", () => {
  if (activeImage <= 0) {
    activeImage = sliderItemsElem.length - 1;
  } else {
    activeImage--;
  }
  slider();
});

// авто прокрутка
setInterval(() => {
  if (activeImage >= sliderItemsElem.length - 1) {
    activeImage = 0;
  } else {
    activeImage++;
  }
  slider();
}, 9000);



// ПРОГРЕСС ЛИНИЯ
const totalSum = [];
const collectedSum = [];

// массив с суммой сбора
[...document.querySelectorAll(".index__allYouNeedis_totalSum")].forEach(
  (item) => {
    let temp = item.innerHTML;
    temp = temp.replace(/[^0-9]/g, "");
    totalSum.push(temp);
  }
);

// массив с собранной суммой
[...document.querySelectorAll(".index__allYouNeedis_collectedSum")].forEach(
  (item) => {
    let temp = item.innerHTML;
    temp = temp.replace(/[^0-9]/g, "");
    collectedSum.push(temp);
  }
);

// массив собранной суммы в процентах
const percentages = [];
for (let i = 0; i < totalSum.length; i++) {
  percentages.push(((collectedSum[i] / totalSum[i]) * 100).toFixed(2));
}

// задание свойства ширины блока (в процентаХ)
const percentagesSet = document.querySelectorAll(
  ".index__allYouNeedis_donationsProgress"
);

for (let i = 0; i < percentagesSet.length; i++) {
  if (percentages[i] >= 100) {
    percentagesSet[i].style.width = 100 + "%";
    document
      .querySelectorAll(".index__allYouNeedis_payment")
      [i].classList.add("index__allYouNeedis_collectedSum");
    document.querySelectorAll(".index__allYouNeedis_payment")[i].textContent =
      "Сбор закрыт";
  } else {
    percentagesSet[i].style.width = percentages[i] + "%";
  }
}

