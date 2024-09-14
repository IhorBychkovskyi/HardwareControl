let modalEditPC = document.getElementById("modalEditPC");
let modalAddPC = document.getElementById("modalAddPC");
let modalEditInstitution = document.getElementById("editInstitution");
let modalAddInstitution = document.getElementById("modalAddInstitution");
let modalAddUser = document.getElementById("modalAddUser");

let closeBtn1 = document.getElementsByClassName("close")[0];
let closeBtn2 = document.getElementsByClassName("close")[1];
let closeBtn3 = document.getElementsByClassName("close")[2];
let closeBtn4 = document.getElementsByClassName("close")[3];
let closeBtn5 = document.getElementsByClassName("close")[4];

function showFileName(input) {
    var fileName = input.value.split("\\").pop();
    let spanContent = document.getElementsByClassName("file-name");
    for(let i = 0; i<spanContent.length;i++){
        spanContent[i].textContent = fileName

    }
  }



// Функція для закриття спливаючого вікна
function closeModal() {
    modalEditPC.style.display = "none";
    modalAddPC.style.display = "none";
    modalEditInstitution.style.display = "none";
    modalAddInstitution.style.display = "none";
    modalAddUser.style.display  = "none"
    let forms = document.getElementsByTagName("form")
    for (let i = 0; i < forms.length; i++) {
        forms[i].reset();
      }

    let spanContent = document.getElementsByClassName("file-name");
    for(let i = 0; i<spanContent.length;i++){
          spanContent[i].textContent = "Файл не вибрано"
    }
 }
  

  // Додаємо обробник подій на кнопку закриття спливаючого вікна
closeBtn1.onclick = function() {
    closeModal();
}

closeBtn2.onclick = function() {
    closeModal();
}

closeBtn3.onclick = function() {
    closeModal();
}

closeBtn4.onclick = function() {
    closeModal();
}


closeBtn5.onclick = function() {
    closeModal();
}





function addPC(){
    modalAddPC.style.display = "flex"
    }



function addInstitution(){
    modalAddInstitution.style.display = "flex"
}

function showAddUserForm(){
    modalAddUser.style.display = "flex"
}



document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.list-institute button');
    buttons.forEach(function(button, index) {
      button.addEventListener('contextmenu', function(event) {
        event.preventDefault();
        // Перевірка, чи кнопка не є першою або останньою
        if (index !== 0 && index !== buttons.length - 1) {
          modalEditInstitution.style.display = "flex";
          input = modalEditInstitution.getElementsByClassName("form_input");
          var button = $(this);
          input[0].value = button.data('value')
          input[1].value = button.text();
        } else {
          event.preventDefault();
        }
      });
    });


    var downloadBtn = document.getElementById('download-pdf-btn');
    downloadBtn.addEventListener('click', function() {
        var tableData = [];
        var tableRows = document.querySelectorAll('.table-info tr');
        
        for (var i = 0; i < tableRows.length; i++) {
          var row = tableRows[i];
          
          // Перевірка видимості рядка
          if (!row.hasAttribute('hidden')) {
            var rowData = [];
            var cells = row.querySelectorAll('th:not([hidden]), td:not([hidden])');
        
            for (var j = 0; j < cells.length; j++) {
              rowData.push(cells[j].innerText);
            }
        
            tableData.push(rowData);
          }
        }
    
  
      // Відправка AJAX-запиту на сервер
      $.ajax({
        url: '/profile/generate_pdf/',
        type: 'POST',
        data: JSON.stringify({ table_data: tableData }),
        contentType: 'application/json',
        headers: {
          'X-CSRFToken': csrftoken // Додано CSRF-токен у заголовки запиту
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(response) {
          // Завантаження отриманого PDF-файлу
          var blob = new Blob([response], { type: 'application/pdf' });
          var url = URL.createObjectURL(blob);
          var link = document.createElement('a');
          link.href = url;
          link.download = 'table_data.pdf';
          link.click();
          URL.revokeObjectURL(url);
        },
        error: function(xhr, textStatus, errorThrown) {
          console.log('Помилка при відправці AJAX-запиту:', errorThrown);
        }
    });
 });
})
        

  
//------------------------------------------ Відправка форми додавання ПК------------------------------------------
$(document).ready(function() {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $('#addPCform').submit(function(event) {
      // Зупинка відправки форми на сервер
      event.preventDefault();
  
      // Отримання даних форми
      var formData = new FormData(this);
      formData.append("image", $("input[id^='imageAddPC']")[0].files[0])
      // Відправка AJAX запиту на сервер
      $.ajax({
        url: '/profile/add_pc/',
        type: 'POST',
        data: formData,
        contentType: 'multipart/form-data',
        processData: false,
        contentType: false,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
            location.href = location.href;
        }
      });
    });


    $('#addInstitutionForm').submit(function(event) {
        // Зупинка відправки форми на сервер
        event.preventDefault();
    
        // Отримання даних форми
        var formData = $(this).serialize();
    
        // Відправка AJAX запиту на сервер
        $.ajax({
          url: '/profile/add_institution/',
          type: 'POST',
          data: formData,
          beforeSend: function(xhr) {
              xhr.setRequestHeader('X-CSRFToken', csrftoken);
          },
          success: function(data) {
              location.href = location.href;
          }
        });
      });
    
      $('.showPC').click(function() {
        var button = $(this);
        var value = button.data('value');
        location.href = `/profile/${value}` ;
    })

    $('#deletePC').click(function(event) {
        event.preventDefault();
        formData = $('#PC_Edit_Form').serialize();
        $.ajax({
            url: '/profile/delete_pc/',
            type: 'POST',
            data: formData,
            
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(data) {
                location.href = location.href;
            }
          });
    })

    $('#PC_Edit_Form').submit(function(event) {
        // Зупинка відправки форми на сервер
        event.preventDefault();
    
        // Отримання даних форми
        var formData = new FormData(this);
        formData.append("image", $("input[id^='imageEditPC']")[0].files[0])
        // Відправка AJAX запиту на сервер
        $.ajax({
          url: '/profile/edit_pc/',
          type: 'POST',
          data: formData,
          contentType: 'multipart/form-data',
          processData: false,
          contentType: false,
          beforeSend: function(xhr) {
              xhr.setRequestHeader('X-CSRFToken', csrftoken);
          },
          success: function(data) {
              location.href = location.href;
          }
        });
      });

    $('#deleteInstitution').click(function(event) {
        event.preventDefault();
        formData = $('#Edit_Institution_Form').serialize();
        $.ajax({
            url: '/profile/delete_institution/',
            type: 'POST',
            data: formData,
            
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(data) {
                location.href = location.href;
            }
          });
    })

    $('#saveDataInsitution').click(function(event) {
        event.preventDefault();
        formData = $('#Edit_Institution_Form').serialize();
        $.ajax({
            url: '/profile/edit_institution/',
            type: 'POST',
            data: formData,
            
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            },
            success: function(data) {
                location.href = location.href;
            }
          });
    })

    $('#addUserForm').submit(function(event) {
        // Зупинка відправки форми на сервер
        event.preventDefault();
    
        // Отримання даних форми
        var formData = new FormData(this);
        // Відправка AJAX запиту на сервер
        $.ajax({
          url: '/profile/add_user/',
          type: 'POST',
          data: formData,
          contentType: 'multipart/form-data',
          processData: false,
          contentType: false,
          beforeSend: function(xhr) {
              xhr.setRequestHeader('X-CSRFToken', csrftoken);
          },
          success: function(data) {
              location.href = location.href;
          }
        });
      });


  });


  let table = document.getElementsByClassName("table-info")[0];
let rows = table.getElementsByTagName("tr");

for (let i = 1; i < rows.length; i++) {
    rows[i].ondblclick = function() {
        let rowNumber = this.rowIndex;
        modalEditPC.style.display = "flex";

        cells = rows[rowNumber].cells
        input = modalEditPC.getElementsByClassName("form_input")
        for (let j = 0; j < input.length; j++){
            if (j == 3){
              
                input[j].value = cells[j].textContent.split(".").reverse().join("-");
                continue
            }

            if (j == 4){
              
                if (cells[j].textContent === "Працює"){
                    input[j].value = "W"        
                    continue
                }

                else if (cells[j].textContent === "Не працює"){
                    input[j].value = "DW"         
                    continue
                }

                else{
                    input[j].value = "R"                 
                    continue
                }
                
            }

            if (j == 12 && cells[j].innerHTML === "None"){
                input[j].value = "null" 
                continue
            }

            if(j==12){
                input[j].value = (cells[j].innerHTML.replace(/\D/g, ''))
                continue
            }

            if (j==13 && cells[j].innerHTML=="Опису немає"){
                continue
            }

            input[j].value = cells[j].innerHTML
        }

    };
}

