$(document).ready(function () {
    const dataTable = iniciarDataTable();
    botaoExecucaoCompleta(dataTable);
    botaoExecucaoPorLinha(dataTable);
});

const iniciarDataTable = function() {
    return $('#analisador-top-down').DataTable({
        "bPaginate": false,
        "ordering": false,
        "searching": false,
        "columns": [
            { "data": "pilha" },
            { "data": "entrada" },
            { "data": "acao" }            
        ]
    });
}

const botaoExecucaoCompleta = function(dataTable) {
    $('#btn-execucao-completa').click(function (e) { 
        e.preventDefault();
        const sentenca = $('#sentenca').val();
        const url = `${$SCRIPT_ROOT}/api/analisador_sintatico?sentenca=${sentenca}`;   
        $.ajax({
            url: url,
            method: "get",
            dataType: "json",
            success: function(automato) { dataTable.rows.add(automato).draw(); }
        });
    });
}

const botaoExecucaoPorLinha = function(dataTable) {
    $('#btn-execucao-linha').click(function (e) {
        alert('hehe');
    });    
}