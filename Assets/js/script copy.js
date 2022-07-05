let listasGastosGeral=[
   {id: 1, tag: 'transport', item: 'Uber', ammount: -10},
   {id: 2, tag: 'alimentacao', item: 'Pizza', ammount: -50},
   {id: 3, tag: 'saude', item: 'Dorflex', ammount: -7},
   {id: 4, tag: 'lazer', item: 'Parquinho', ammount: -20},
   {id: 5, tag: 'lazer', item: 'Salário', ammount: 1000}

]

function addOnList(){
   let tagItem = document.querySelector('select#tag').value
   let descItem = document.querySelector('input#desc').value
   let valorItem = Number(document.querySelector('input#valor').value)

   console.log(tagItem)
   console.log(descItem)
   console.log(valorItem)

   const transaction = {id: Math.random(), tag: tagItem, item: descItem, ammount: valorItem};

   listasGastosGeral.push(transaction)
   
   console.log(listasGastosGeral)
}

function showList(){
   let lista = document.querySelector("#lista").appendChild('li')

   console.log(lista)



   // document.querySelector('#lista').innerHTML(`<li>${listasGastosGeral}</li>`)
   // document.getElementById('lista').document.(innerHTML = '<li>html data</li>')

}

// function montaLista(){
//    let textoDaLista = '';
//    document.querySelector("#lista").innerHTML

//    return textoDaLista;

// }
