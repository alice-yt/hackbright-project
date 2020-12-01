$('#login-form').on('submit', (evt) => { // what should replace '#order-form'?
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

// should I add a scriptag to link my html form to this JS file?
// how do I know that my AJAX request is working?