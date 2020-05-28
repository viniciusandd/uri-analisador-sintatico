$('#btn-execucao-completa').click(function (e) { 
    e.preventDefault();
    $.ajax({
        url: $SCRIPT_ROOT + "/api/analisador_sintatico",
        method: "get",
        dataType: "json",
        success: function(data) {
            console.log(data);
        }
    })
});