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

function buscarAutomato() {
    const sentenca = $('#sentenca').val();
    const url = `${$SCRIPT_ROOT}/api/analisador_sintatico?sentenca=${sentenca}`;
    return $.get(url);
 }

const botaoExecucaoCompleta = function(dataTable) {
    $('#btn-execucao-completa').click(function (e) { 
        e.preventDefault();
        dataTable.clear();        
        buscarAutomato().done(function(automato) { 
            dataTable.rows.add(automato).draw(); 
        });
    });
}

var contadorDeClicks = 0;
var globalAutomato = [];
const botaoExecucaoPorLinha = function(dataTable) {
    $('#btn-execucao-linha').click(function (e) {
        e.preventDefault();
        if (globalAutomato.length == 0) {
            buscarAutomato().done(function(automato) {
                globalAutomato = automato;
                dataTable.row.add(globalAutomato[0]).draw();
            });
        } else {
            if (contadorDeClicks < globalAutomato.length) {
                dataTable.row.add(globalAutomato[contadorDeClicks]).draw();
            } else {
                alert('terminou');
            }
        }
        contadorDeClicks++;
    });    
}