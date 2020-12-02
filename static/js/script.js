    const sleep_quality = document.querySelector('#sleep_quality');
    const sleep_quality_output = document.querySelector('.sleep_quality_output');

    output.textContent = sleep_quality.value;

    sleep_quality.addEventListener('input', function() {
    output.textContent = sleep_quality.value;
    });