const totalSum = [];
const collectedSum = [];

// const lineElem = document.querySelectorAll(".allYouNeedis__item_line");

[...document.querySelectorAll(".allYouNeedis__item_totalSum")].forEach(
  (item) => {
    totalSum.push(item.innerHTML);
  }
);

[...document.querySelectorAll(".allYouNeedis__item_collectedSum")].forEach(
  (item) => {
    collectedSum.push(item.innerHTML);
  }
);
console.log(document.querySelectorAll(".allYouNeedis__item_collectedSum"));

console.log(totalSum);
console.log(collectedSum);

const percentages = [];
console.log(percentages);

for (let i = 0; i < totalSum.length; i++) {
  percentages.push(((collectedSum[i] / totalSum[i]) * 100).toFixed(2));
}

console.log(percentages);

// for (let i = 0; i < lineElem.length; i++) {
//   lineElem[i].innerHTML = percentages[i];
// }

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
