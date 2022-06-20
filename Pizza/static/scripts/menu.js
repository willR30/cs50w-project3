var btn_agregar=document.getElementById('btn_agregar')

/*Agrgando el evento del boton*/
//Operador sprets en js
//Funcion filter
btn_agregar.addEventListener('click', ()=>{
    var table = document.getElementById('Tabla_menu');
    var arr = [...table.rows].map(r => [...r.querySelectorAll('td')].map(td => {
        return {
            td
        }
    }));
    console.log(arr)
}
)



