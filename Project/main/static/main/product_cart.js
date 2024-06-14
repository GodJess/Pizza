const amount = document.querySelector('.amount');
const plus = document.getElementById('plus');
const minus = document.getElementById('minus');

var count = 1;
amount.value = count;

    plus.addEventListener("click", () => {
      if (count < 100) {
        count += 1;
        amount.value = count;
      } else if (count == 100) {
        count = 100;
        amount.value = count;
      }
    });
  
    minus.addEventListener("click", () => {
      if (count > 1) {
        count -= 1;
        amount.value = count;
      } else if (count == 1) {
        count = 1;
        amount.value = count;
      }
    });
  
