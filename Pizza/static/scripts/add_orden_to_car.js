var btn_item_into_orden=document.getElementById('Formulario');
var product_price=document.getElementById('product_price');

let instancia_form=new FormData(btn_item_into_orden);


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

btn_item_into_orden.addEventListener('submit',(e)=>{
   let values_list=[];
   /*Teniendo el evento validamos los item seleccionados*/
   e.preventDefault();
   var checked_list=document.querySelectorAll('.form-check-input:checked');
   
   for(const i of checked_list){
      values_list.push(i.value);
      console.log(values_list);
   }
   instancia_form.append('toppings_list', values_list)
   const csrf = getCookie('csrftoken');
   instancia_form.append('csrfmiddlewaretoken',csrf)
   instancia_form.append('txt_amount', document.querySelector('#amount_txt').value)

   fetch('/add_item_to_car/'+instancia_form.get('txt_id__product'), {
      'method': 'POST',
      'body': instancia_form
   }).then(()=>{
      return location.pathname='/menu';
   }).catch(
      ()=>{
         alert("Error!");
      }
   )
   
})