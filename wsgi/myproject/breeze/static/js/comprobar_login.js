function validarlogin () {
var p1 = document.getElementById("clave1").value;
var p2 = document.getElementById("user").value;
if (p1.length == 0 || p2.length == 0) {
alert("Los campos de usuario/password no pueden quedar vacios");
return false;
} else {
return true;
}
}