//malas practicas de programación
x = 10; 

function p(a,b){
var res; 
if(true){
res=Math.pow(a,b); 
}
    
return res; 
}


var n1 = 2;
var n2 = 3;


console.log("el result es:"+p(n1,n2)); 



//Buenas prácticas de programación
// Función para calcular la potencia de un número
function potencia(base, exponente) {
    return Math.pow(base, exponente);
}

console.log(potencia(2, 3)); // Resultado: 8


