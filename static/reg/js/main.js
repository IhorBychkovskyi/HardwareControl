document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("burger").addEventListener("click", function() {
        document.querySelector("header").classList.toggle("open")
    })
})

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

$('#reg_Form').submit(function(event) {
    // Зупинка відправки форми на сервер
    event.preventDefault();

    // Отримання даних форми
    var formData = $(this).serialize();

    // Відправка AJAX запиту на сервер
    $.ajax({
      url: '/registration/reg/',
      type: 'POST',
      data: formData,
      beforeSend: function(xhr) {
          xhr.setRequestHeader('X-CSRFToken', csrftoken);
      },
      success: function(data) {
          location.href = "/login/";
      }
    });
  });
