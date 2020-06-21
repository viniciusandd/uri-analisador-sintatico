$(document).ready(function () {
    const dataTable = iniciarDataTable();
    botaoExecucaoCompleta(dataTable);
    botaoExecucaoPorLinha();
    botaoProximaLinha(dataTable);
    botaoPararReiniciar(dataTable);
    botaoGerarSentenca();
    botaoVoltarTopo();
    $('#btn-proxima-linha').hide();
    $('#btn-voltar-topo').hide();
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
        $(this).prop("disabled", true);
        $('#btn-execucao-linha').prop("disabled", true);
        $('#btn-gerar-sentenca').prop("disabled", true);
        $('#sentenca').prop("disabled", true);
        buscarAutomato().done(function(automato) { 
            dataTable.rows.add(automato).draw(); 
            $(document).scrollTop($(document).height());
            $('#btn-voltar-topo').show().focus();
        }).fail(function(xhr) {
            bootbox.alert(xhr.responseJSON.erro);
        });
    });
}

const botaoExecucaoPorLinha = function() {
    $('#btn-execucao-linha').click(function (e) {
        e.preventDefault();
        $(this).prop("disabled", true);
        $('#btn-execucao-completa').prop("disabled", true);
        $('#btn-gerar-sentenca').prop("disabled", true);
        $('#sentenca').prop("disabled", true);        
        $('#btn-proxima-linha').prop("disabled", false).show().focus();
    });
}

var contadorDeClicks = 0;
var globalAutomato = [];
const botaoProximaLinha = function(dataTable) {
    $('#btn-proxima-linha').click(function (e) {
        e.preventDefault();
        $(document).scrollTop($(document).height()); 
        const botao = $(this);
        botao.focus();
        if (globalAutomato.length == 0) {
            botao.prop("disabled", true);
            buscarAutomato().done(function(automato) {
                globalAutomato = automato;
                dataTable.row.add(globalAutomato[0]).draw();
                botao.prop("disabled", false);
            }).fail(function(xhr) {
                bootbox.alert(xhr.responseJSON.erro);
            });
        } else {
            if (contadorDeClicks < globalAutomato.length)
                dataTable.row.add(globalAutomato[contadorDeClicks]).draw();
            else {
                botao.prop("disabled", true);
                $('#btn-voltar-topo').show().focus();
            }
        }
        contadorDeClicks++;
    });    
}

const botaoGerarSentenca = function() {
    $('#btn-gerar-sentenca').click(function (e) {
        e.preventDefault();
        const botao = $(this);
        botao.prop("disabled", true);
        $('#btn-execucao-completa').prop("disabled", true);
        $('#btn-execucao-linha').prop("disabled", true);
        const url = `${$SCRIPT_ROOT}/api/sentenca`;
        $.get(url, function(resposta) {
            botao.prop("disabled", false);
            $('#btn-execucao-completa').prop("disabled", false);
            $('#btn-execucao-linha').prop("disabled", false);
            $('#sentenca').val(resposta.sentenca);
        });
    });
}

const botaoVoltarTopo = function() {
    $('#btn-voltar-topo').click(function (e) {
        e.preventDefault();
        $(document).scrollTop(0);
        $(this).hide();
        $('#btn-parar-reiniciar').focus();
    });
}

const botaoPararReiniciar = function(dataTable) {
    $('#btn-parar-reiniciar').click(function (e) {
        e.preventDefault();
        dataTable.clear().draw();
        $('#btn-execucao-completa').prop("disabled", false);
        $('#btn-execucao-linha').prop("disabled", false);
        $('#btn-gerar-sentenca').prop("disabled", false);
        $('#btn-proxima-linha').hide();
        $('#btn-voltar-topo').hide();
        $('#sentenca').prop("disabled", false).focus();
        contadorDeClicks = 0;
        globalAutomato = [];
    });
}