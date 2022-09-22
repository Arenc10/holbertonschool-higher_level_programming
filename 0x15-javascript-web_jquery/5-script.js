$('div#add_item').click(function () {
  const newItem = $('<li></li>').text('Item');
  $('ul.my_list').append(newItem);
});
