$('#login-form').on('submit', (evt) => {
  evt.preventDefault();

  const formInputs = {
    'email': $('#login-email').val(),
    'password': $('#login-password').val(),
  };

  $.post('/', formInputs, (res) => {
    if (res === 'Login successful') {
        window.location.replace('/menu')
    } else {
        alert(res)
    }
  });
});
