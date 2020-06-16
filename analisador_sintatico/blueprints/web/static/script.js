$('#btn-execucao-completa').click(function (e) { 
    e.preventDefault();
    const sentenca = $('#sentenca').val();
    const url = `${$SCRIPT_ROOT}/api/analisador_sintatico?sentenca=${sentenca}`
    $.ajax({
        url: url,
        method: "get",
        dataType: "json",
        success: function(data) {
            console.log(data);
        }
    })
});