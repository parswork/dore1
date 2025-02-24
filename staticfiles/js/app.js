function showPass() {
  const password = document.getElementById("password");
  const show = document.getElementById("show");
  if (password.type === "password") {
    password.type = "text";
    show.classList.remove("fa-eye");
    show.classList.add("fa-eye-slash");
    show.classList.add("showColor");
  } else {
    password.type = "password";
    show.classList.add("fa-eye");
    show.classList.remove("fa-eye-slash");
    show.classList.remove("showColor");
  }
}
function checkPass() {
  const password = document.getElementById("password").value;

  const er1 = document.getElementById("er1");
  const er2 = document.getElementById("er2");
  const er3 = document.getElementById("er3");

  const er1i = document.getElementById("er1i");
  const er2i = document.getElementById("er2i");
  const er3i = document.getElementById("er3i");

  const submit = document.getElementById("submit");

  submit.classList.add("stop");

  er1.classList.remove("green");
  er2.classList.remove("green");
  er3.classList.remove("green");
  er1.classList.add("red");
  er2.classList.add("red");
  er3.classList.add("red");
  er1i.classList.add("fa-circle-xmark");
  er1i.classList.remove("fa-circle-check");
  er2i.classList.add("fa-circle-xmark");
  er2i.classList.remove("fa-circle-check");
  er3i.classList.add("fa-circle-xmark");
  er3i.classList.remove("fa-circle-check");

  if (password.length > 8) {
    er1.classList.remove("red");
    er1.classList.add("green");
    er1i.classList.remove("fa-circle-xmark");
    er1i.classList.add("fa-circle-check");
  }
  if (password.search(/[A-Z]/) != -1) {
    er2.classList.remove("red");
    er2.classList.add("green");
    er2i.classList.remove("fa-circle-xmark");
    er2i.classList.add("fa-circle-check");
  }
  if (password.search(/[@|$|#]/) != -1) {
    er3.classList.remove("red");
    er3.classList.add("green");
    er3i.classList.remove("fa-circle-xmark");
    er3i.classList.add("fa-circle-check");
  }
  if (
    password.length > 8 &&
    password.search(/[A-Z]/) != -1 &&
    password.search(/[@|$|#]/) != -1
  ) {
    submit.classList.remove("stop");
  }
}
