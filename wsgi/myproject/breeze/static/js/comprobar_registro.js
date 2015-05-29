function validarPasswd () {
var p1 = document.getElementById("clave1").value;
var p2 = document.getElementById("clave2").value;
var p3 = document.getElementById("user").value;
var p4 = document.getElementById("email").value;
var espacios = false;
var cont = 0;
var err = 0;
// Este bucle recorre la cadena para comprobar
// que no todo son espacios
while (!espacios && (cont < p1.length)) {
if (p1.charAt(cont) == " ")
espacios = true;
cont++;
}
if (espacios) {
alert ("La contraseña no puede contener espacios en blanco");
return false;
}
if (p1.length == 0 || p2.length == 0 || p3.length == 0 || p4.length == 0) {
alert("Los campos de usuario/password/email no pueden quedar vacios");
return false;
}
if (p1 != p2) {
alert("Las passwords deben de coincidir");
return false;
} else {

return true;
}
}