// allYouNeedis

const totalSum = [];
const collectedSum = [];


[...document.querySelectorAll(".allYouNeedis__item_totalSum")].forEach(
  (item) => {
    let temp = item.innerHTML;
    temp = temp.replace(/[^0-9]/g, '');
    totalSum.push(temp);
  }
);

[...document.querySelectorAll(".allYouNeedis__item_collectedSum")].forEach(
  (item) => {
    let temp = item.innerHTML;
    temp = temp.replace(/[^0-9]/g, '');
    collectedSum.push(temp);
  }
);

console.log(totalSum);
console.log(collectedSum);

const percentages = [];

for (let i = 0; i < totalSum.length; i++) {
  percentages.push(((collectedSum[i] / totalSum[i]) * 100).toFixed(2));
}

console.log(percentages);


const percentagesSet = document.querySelectorAll(
  ".allYouNeedis__item_donationsProgress"
);

for (let i = 0; i < percentagesSet.length; i++) {
  percentagesSet[i].style.width = percentages[i] + "%";
}

for (let i = 0; i < totalSum.length; i++) {
  percentages.push(
    ((collectedSum[i].split(" ")[0] / totalSum[i].split(" ")[0]) * 100).toFixed(
      2
    )
  );
}



