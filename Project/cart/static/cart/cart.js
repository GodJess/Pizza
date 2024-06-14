const deletebutton = document.querySelector(".delete");

deletebutton.addEventListener("click", () => {
    const row = this.closest('tr');
    if (row) {
        // Удаляем родительский элемент tr
        row.remove();
      }
})
const price = document.querySelector('.input-price');
const itog = document.querySelectorAll('.itog');
let totalPrice = 0;

itog.forEach((itogs) =>{
  const priceitog = Number(itogs.textContent);
  totalPrice += priceitog;
})      

price.value = totalPrice

//const login = document.getElementById('login');
//const pass = document.querySelector('.pass');

//login.value = pass.value