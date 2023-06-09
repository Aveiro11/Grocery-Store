$(function () {
    //Json data by api call for order table
    $.get(orderListApiUrl, function (response) {
        if(response) {
            var table = '';
            var totalCost = 0;
            $.each(response, function(index, order) {
                totalCost += parseFloat(order.total);
                table += '<tr>' +
                    '<td>'+ order.date +'</td>'+
                    '<td>'+ order.order_id +'</td>'+
                    '<td>'+ order.name +'</td>'+
                    '<td>'+ order.total.toFixed(2) +' Taka</td></tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>'+ totalCost.toFixed(2) +' Taka</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    });
});