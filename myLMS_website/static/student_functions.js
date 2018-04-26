function blockPassword() {
  var enteredValue = document.getElementById('inputPassword');
  if(enteredValue.type === "password"){
    enteredValue.type = "text";
  } else {
    enteredValue.type = "password";
  }
}
