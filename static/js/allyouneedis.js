// allYouNeedis

const totalSum = [];
const collectedSum = [];

// массив с суммой сбора
[...document.querySelectorAll(".allYouNeedis__item_totalSum")].forEach(
  (item) => {
    let temp = item.innerHTML;
    temp = temp.replace(/[^0-9]/g, '');
    totalSum.push(temp);
  }
);

// массив с собранной суммой
[...document.querySelectorAll(".allYouNeedis__item_collectedSum")].forEach(
  (item) => {
    let temp = item.innerHTML;
    temp = temp.replace(/[^0-9]/g, '');
    collectedSum.push(temp);
  }
);


const percentages = [];
// массив собранной суммы в процентах
for (let i = 0; i < totalSum.length; i++) {
  percentages.push(((collectedSum[i] / totalSum[i]) * 100).toFixed(2));
}


// задание свойства ширины блока (в процентаХ)
const percentagesSet = document.querySelectorAll(
  ".allYouNeedis__item_donationsProgress"
);

for (let i = 0; i < percentagesSet.length; i++) {
  percentagesSet[i].style.width = percentages[i] + "%";
}





