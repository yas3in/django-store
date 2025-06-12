let password = document.querySelector("#password")
let message = document.querySelector(".password-lengh-error")
let eye = document.querySelector(".bi-eye-slash")


password.addEventListener("input", () => {
    if (password.value.length < 6) {
        message.style.visibility = "visible";
        password.classList.add("password-error")
        message.innerHTML = "پسورد کوتاه است"
    }
    else {
        message.style.visibility = "hidden";
        password.classList.remove("password-error")
    }
})


eye.addEventListener("click", ()=> {
    if (eye.classList.contains("bi-eye-slash")){
        password.type = "text";
        eye.classList.remove("bi-eye-slash")
        eye.classList.add("bi-eye")
    } else {
        password.type = "password";
        eye.classList.remove("bi-eye")
        eye.classList.add("bi-eye-slash")
    }
})