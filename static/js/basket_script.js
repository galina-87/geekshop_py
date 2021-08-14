'use strict';

window.onload = function () {
    let basketList = $('.b_list');
    basketList.on('change', 'input[type="number"]', function (event) {
        let t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                basketList.html(data.result);
            },
        });
    })
}