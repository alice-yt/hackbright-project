$('#order-form').on('submit', (evt) => { // what should replace '#order-form'?
  evt.preventDefault();

  const formInputs = {
    'sleeptime': $('#sleeptime').val(),
    'waketime': $('#waketime').val(),
    'sleep-quality': $('#sleep_quality').val(),
    'stress': $('#stress').val(),
    'energy': $('#energy').val(),
    'productivity': $('#productivity').val(),
    'exercise': $('#exercise').val(),
    'alcoholic-units': $('#alcoholic_units').val()
  };

  $.post('/log_entry', formInputs, (res) => {
    alert(res);
  });
});

// should I add a scriptag to link my html form to this JS file?
// how do I know that my AJAX request is working?