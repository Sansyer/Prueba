document.getElementById("agregarNumeros").addEventListener("click", agregarNumeros);

function agregarNumeros() {
  console.log("Función agregarNumeros ejecutándose");

  var cantidad = parseInt(prompt("¿Cuántos números impares desea sumar?"));
  var numeros = [];
  for (var i = 0; i < cantidad; i++) {
    var numero = parseInt(prompt("Ingrese un número impar:"));
    while (numero % 2 === 0) {
      numero = parseInt(prompt("El número ingresado no es impar. Por favor, ingrese un número impar:"));
    }
    numeros.push(numero);
  }

  var suma = numeros.reduce(function(total, numero) {
    return total + numero;
  });

  var resultado = document.getElementById("resultado");
  resultado.innerHTML = "La suma de los " + cantidad + " números impares ingresados es " + suma + ".";
}
