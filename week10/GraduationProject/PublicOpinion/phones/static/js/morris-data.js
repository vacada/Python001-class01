$(function() {
    let lg05 = $("#morris-donut-chart").attr('lg05')
    let lt05 = $("#morris-donut-chart").attr('lt05')
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "大于0.5",
            value: lg05
        }, {
            label: "小于等于0.5",
            value: lt05
        }],
        resize: true
    });


});
