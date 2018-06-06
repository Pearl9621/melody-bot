function add_statement(statement){
    var form = document.createElement("form");
    var message = document.createTextNode(statement);
    form.appendChild(message);
    if (statement.endsWith("?")){
        var input = document.createElement("input");
        form.appendChild(input)
    }
    document.body.appendChild(form);
    form.addEventListener("submit", function(event){
        converse(this[0].value);
        event.preventDefault();
        return false;
    });
}

function start_conversation(){
    var name = document.getElementById("name").value;
    fetch('/converse?reset=true&name=' + name)
        .then(function(response) {
            response.text().then(add_statement);
        })
}

function converse(answer){
    var name = document.getElementById("name").value;
    fetch("/converse?name=" + name + "&answer=" + answer)
        .then(function(response){
            response.text().then(add_statement);
        })
}