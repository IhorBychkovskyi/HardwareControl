//   ------------------------------------------------
const rows1 = document.querySelectorAll('table tr:not(:first-child)');

rows1.forEach(row => {

    row.addEventListener('contextmenu', e => {
    try{
        const contextMenuClose = document.querySelector('.context-menu[style*="display: block"]');    
        contextMenuClose.style.display = 'none';
    }catch (error) {

        
      }
   
   
    e.preventDefault();
    rows1.forEach(row => {
        row.style.transform = 'none';
    });
  
    
    const contextMenu = document.getElementsByClassName('context-menu')[row.rowIndex-1];
    // Встановлюємо позицію вікна контекстного меню
    contextMenu.style.left = `${row.getBoundingClientRect().left}px`;
    contextMenu.style.top = `${row.getBoundingClientRect().bottom+10}px`;
    contextMenu.style.width = `${row.offsetWidth/2}px`;

    // Показуємо вікно контекстного меню
    contextMenu.style.display = 'block';

    // Зсуваємо інші рядки вниз
    rows1.forEach(r => {
      if (r !== row) {
        const rowTop = r.getBoundingClientRect().top;
        const rowBottom = rowTop + r.offsetHeight;

        if (rowBottom > e.pageY) {
          r.style.transform = `translateY(${contextMenu.offsetHeight+15}px)`;
        }
      }
    });
  });
});

document.addEventListener('click', e => {
  const contextMenu = document.querySelector('.context-menu[style*="display: block"]');

    if(contextMenu.contains(e.target)){
        return;
    }

  if (e.button === 0 && !e.ctrlKey) {

    rows1.forEach(row => {
      row.style.transform = 'none';
    });

   
    contextMenu.style.display = 'none';
  }
});

var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

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

    $('.showPC').click(function() {
        var button = $(this);
        var value = button.data('value');
        location.href = `/profile/${value}` ;
    })   
})


//------------------------------------------Обробка подій подвійного натискання кнопки інситутів------------------------------------------ 

  