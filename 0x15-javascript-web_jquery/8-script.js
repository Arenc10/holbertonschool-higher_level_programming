$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    $.each(data.results, function(index, value) {
        let newItem = $("<li></li>").text(value.title);
        $("ul#list_movies").append(newItem);
    })
})
