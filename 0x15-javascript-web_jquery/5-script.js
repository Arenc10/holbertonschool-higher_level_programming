$("div#add_item").click(function(){
    let newItem = $("<li></li>").text("Item");
    $("ul.my_list").append(newItem);
})
