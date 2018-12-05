
// Author:  Wilmer Martínez
// Web:     www.wilmermartinez.com 
// Email:   wilmermorelmartinez@gmail.com
// ----------------------------------------------------------------------------






// Realiza el cálculo de la cuota de un préstamo
// ----------------------------------------------------------------------------


var DIARIO = "diario";
var SEMANAL = "semanal";
var QUINCENAL = "quincenal";
var MENSUAL = "mensual";
var BIMESTRAL = "bimestral";
var TRIMESTRAL = "trimestral";
var CUATRIMESTRAL = "cuatrimestral";
var SEMESTRAL = "semestral";
var ANUAL = "anual";

function getTasa(tasa, tasa_tipo, periodo) {
    if (tasa_tipo == ANUAL) { tasa = tasa / 12 }
    tasa = tasa / 100.0
    if (periodo == DIARIO) { tasa = tasa / 30.4167 };
    if (periodo == SEMANAL) { tasa = tasa / 4.34524 };
    if (periodo == QUINCENAL) { tasa = tasa / 2 };
    if (periodo == MENSUAL) { };
    if (periodo == BIMESTRAL) { tasa = tasa * 2 };
    if (periodo == TRIMESTRAL) { tasa = tasa * 3 };
    if (periodo == CUATRIMESTRAL) { tasa = tasa * 4 };
    if (periodo == SEMESTRAL) { tasa = tasa * 6 };
    if (periodo == ANUAL) { tasa = tasa * 12 };
    return tasa;
}

function getValorDeCuotaFija(monto, tasa, cuotas, periodo, tasa_tipo) {
    tasa = getTasa(tasa, tasa_tipo, periodo);
    valor = monto *( (tasa * Math.pow(1 + tasa, cuotas)) / (Math.pow(1 + tasa, cuotas) - 1) );
    return valor.toFixed(2);
}

function getAmortizacion(monto, tasa, cuotas, periodo, tasa_tipo) {
    var valor_de_cuota = getValorDeCuotaFija(monto, tasa, cuotas, periodo, tasa_tipo);
    var saldo_al_capital = monto;
    var items = new Array();

    for (i=0; i < cuotas; i++) {
        interes = saldo_al_capital * getTasa(tasa, tasa_tipo, periodo);
        abono_al_capital = valor_de_cuota - interes;
        saldo_al_capital -= abono_al_capital;
        numero = i + 1;
        
        interes = interes.toFixed(2);
        abono_al_capital = abono_al_capital.toFixed(2);
        saldo_al_capital = saldo_al_capital.toFixed(2);

        item = [numero, interes, abono_al_capital, valor_de_cuota, saldo_al_capital];
        items.push(item);
    }
    return items;
}


function setMoneda(num) {
    num = num.toString().replace(/\$|\,/g, '');
    if (isNaN(num)) num = "0";
    sign = (num == (num = Math.abs(num)));
    num = Math.floor(num * 100 + 0.50000000001);
    cents = num % 100;
    num = Math.floor(num / 100).toString();
    if (cents < 10) cents = "0" + cents;
    for (var i = 0; i < Math.floor((num.length - (1 + i)) / 3); i++)
        num = num.substring(0, num.length - (4 * i + 3)) + ',' + num.substring(num.length - (4 * i + 3));
    return (((sign) ? '' : '-') + '$' + num + ((cents == "00") ? '' : '.' + cents));
}


function calcular() {
    var monto = document.getElementById("monto").value;
    var cuotas = document.getElementById("cuotas").value;
    var tasa = document.getElementById("tasa").value;
    var errores = document.getElementById("errores");
    errores.innerHTML = ""
    if (!monto) {
        errores.innerHTML = '<div class="note5 center">Indique el monto del préstamo.</div>'
        window.location.href = "#errores"
        return;
    }
    if (!cuotas) {
        errores.innerHTML = '<div class="note5 center">Indique la cantidad de cuotas.</div>'
        window.location.href = "#errores"
        return;
    }
    if (!tasa) {
        errores.innerHTML = '<div class="note5 center">Indique la tasa de interés.</div>'
        window.location.href = "#errores"
        return;
    }
    if (parseInt(cuotas) < 1) {
        errores.innerHTML = '<div class="note5 center">Las cuotas deben ser de 1 en adelante.</div>'
        window.location.href = "#errores"
        return;
    }
    var select_periodo = document.getElementById("periodo");
    periodo = select_periodo.options[select_periodo.selectedIndex].value;
    var tasa_tipo = "mensual"
    var items = getAmortizacion(monto, tasa, cuotas, periodo, tasa_tipo);
    var tbody = document.getElementById("tbody_1");
    tbody.innerHTML = "";
  
    if (parseInt(cuotas) > 3000) { 
        errores.innerHTML = '<div class="note5 center">Indicó una cantidad excesiva de cuotas, trate de indicar menos de 3,000 cuotas..</div>'
        window.location.href = "#errores"
        return; 
    }

    for (i = 0; i < items.length; i++) {
        item = items[i];
        tr = document.createElement("tr");
        for (e = 0; e < item.length; e++) {
            value = item[e];
            if (e > 0) { value = setMoneda(value); }
            td = document.createElement("td");
            textCell = document.createTextNode(value);
            td.appendChild(textCell);
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }

    try {
        var div1 = document.getElementById("valor_cuota");
        valor = setMoneda(items[0][3]);
        div1.innerHTML = valor;
    } catch (error) {
        //Generalmente pasa cuando no existe el elmento con el id 'valor_cuota'.
        //Igual, si no está, pues no se mostrará este valor.
    }
    
    var msg = "sssss";
    if (periodo == "diario") { 
    msg = "Usted estará pagando " + valor + ", todos los dias durante " + items.length + " dias.";
    }
    if (periodo == "semanal") {
    msg = "Usted pagará " + valor + ", semanalmente durante " + items.length + " semanas.";
    }
    if (periodo == "mensual") {
    msg = "Usted pagará " + valor + ", mensualmente durante " + items.length + " meses.";
    }
    if (periodo == "quincenal") {
    msg = "Usted pagará " + valor + ", de manera quincenal por un periodo de " + items.length + " quincenas.";
    }
    if (periodo == "bimestral") {
    msg = "Usted pagará " + valor + ", cada 2 meses durante un periodo de " + items.length + " bimestres.";
    }
    if (periodo == "trimestral") {
    msg = "Usted va a pagar " + valor + ", cada 3 meses durante " + items.length + " trimestres.";
    }
    if (periodo == "cuatrimestral") {
    msg = "Usted pagará " + valor + ", cada cuatrimestre (4 meses) por un periodo de " + items.length + " cuatrimestres.";
    }
    if (periodo == "semestral") {
    msg = "Usted pagará " + valor + ", cada 6 meses durante " + items.length + " semestres";
    }
    if (periodo == "anual") {
    msg = "Usted pagará " + valor + ", anualmente por un periodo de " + items.length + " años";
    }

    try {
        var div2 = document.getElementById("div_comentario");
        div2.innerHTML = msg;
    } catch (error) {
        //Generalmente pasa cuando no existe el elmento con el id 'valor_cuota'.
        //Igual, si no está, pues no se mostrará este valor.
    }
    
}

