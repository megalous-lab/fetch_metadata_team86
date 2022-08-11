console.log("sign up connnected");

const registerForm = document.querySelector("#registeration-form"),
userName = document.querySelector("#username"),
email = document.querySelector("#email"),
password = document.querySelector("#password"),
confirmPassword = document.querySelector("#cpassword"),
submitBtn = document.querySelector("#submit-register-form");

// const registerationData = {
//   'username': "stilltesteresossres",
//   'email': "stilltesterossres@mail.com",
//   'password': "cvfgdgfhgty565765857",
//   'confirm_password': "cvfgdgfhgty565765857",
// }

async function postData(formdata) {
  const { username, email, password, confirm_password } = formdata;
  var requestOptions = {
    method: 'POST',
    redirect: 'follow',
  };
  const fetchUrl = "https://metafetch86.herokuapp.com/api/auth/register/";
  let response = await fetch(`${fetchUrl}?username=${username}&email=${email}&password=${password}&confirm_password=${confirm_password}`, requestOptions);
    let result = await response.json();
    return result;
}

registerForm.onsubmit = (e)=> {
  e.preventDefault();
  const registerationData = {
    'username': userName.value,
    'email': email.value,
    'password': password.value,
    'confirm_password': confirmPassword.value,
  }
  postData(registerationData).then(result=> {
    console.log(result);
    if(result.code === 200) {
      console.log("success");
      window.location.replace("http://127.0.0.1:5500/frontend/pages/login.html");
    } else {
      console.log("error");
    }
  });
}
