// Seleciona o elemento HTML com a classe card-number-input
const cardNumberInput = document.querySelector('.card-number-input');

// Adiciona um evento de entrada ao elemento
cardNumberInput.addEventListener('input', (event) => {
  // Obtém o valor atual do campo de entrada
  let cardNumber = event.target.value;
  
  // Remove todos os espaços em branco do valor atual
  cardNumber = cardNumber.replace(/\s/g, '');

  // Adiciona um espaço a cada quatro dígitos
  cardNumber = cardNumber.replace(/(\d{4})/g, '$1 ');

  // Define o valor atualizado do campo de entrada
  event.target.value = cardNumber;

//   // remova todos os caracteres não numéricos
//   const cleanCardNumber = cardNumber.replace(/\D/g, '');

//   // verifique se é um cartão Visa
//   const isVisa = /^4[0-9]{12}(?:[0-9]{3})?$/.test(cleanCardNumber);
  
//   // verifique se é um cartão Mastercard
//   const isMastercard = /^5[1-5][0-9]{14}$/.test(cleanCardNumber);

//   //se for um cartão visa, adicione a classe visa, se for mastercard adicione a classe mastercard
//   if (isVisa) {
//     cardNumberInput.classList.add('visa');
//     cardNumberInput.classList.remove('mastercard');
//   } else if (isMastercard) {
//     cardNumberInput.classList.add('mastercard');
//     cardNumberInput.classList.remove('visa');
//   } else {
//     cardNumberInput.classList.remove('visa');
//     cardNumberInput.classList.remove('mastercard');
//   }


});


document.querySelector('.card-number-input').oninput = () =>{
    document.querySelector('.card-number-box').innerText = document.querySelector('.card-number-input').value;
}

document.querySelector('.card-holder-input').oninput = () =>{
    document.querySelector('.card-holder-name').innerText = document.querySelector('.card-holder-input').value;
}

document.querySelector('.month-input').oninput = () =>{
    document.querySelector('.exp-month').innerText = document.querySelector('.month-input').value;
}

document.querySelector('.year-input').oninput = () =>{
    document.querySelector('.exp-year').innerText = document.querySelector('.year-input').value;
}

document.querySelector('.cvv-input').onmouseenter = () =>{
    document.querySelector('.front').style.transform = 'perspective(1000px) rotateY(-180deg)';
    document.querySelector('.back').style.transform = 'perspective(1000px) rotateY(0deg)';
}

document.querySelector('.cvv-input').onmouseleave = () =>{
    document.querySelector('.front').style.transform = 'perspective(1000px) rotateY(0deg)';
    document.querySelector('.back').style.transform = 'perspective(1000px) rotateY(180deg)';
}

document.querySelector('.cvv-input').oninput = () =>{
    document.querySelector('.cvv-box').innerText = document.querySelector('.cvv-input').value;
}