var searchTimer;

$("#search").keydown(function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
        $(".small-preview").html("");
        $(".small-preview").append(getEvent({
            image: 'https://b.zmtcdn.com/data/pictures/8/16517128/8d49b048120845d29050897f51e3e1ac_top_thumb_620_314.jpg?output-format=webp',
            title: $("#search").val(),
            rate: '4,5',
            menu: [
                {
                    title: 'První menu',
                    cost: '75'
                }
            ]
        }));
    }, 400);
});

$(document).ready(function(){
    $(".small-preview").append(getEvent({
        image: 'https://b.zmtcdn.com/data/pictures/8/16517128/8d49b048120845d29050897f51e3e1ac_top_thumb_620_314.jpg?output-format=webp',
        title: 'název',
        rate: '4,5',
        menu: [
            {
                title: 'První menu',
                cost: '75'
            }
        ]
    }));
});

function getEvent(data)
{
    var html = '<div class="col l6 m6 s12">\n' +
        '                <div class="card hoverable medium">\n' +
        '                    <div class="card-image">\n' +
        '                        <img src="' + data.image + '">\n' +
        '                        <span class="card-title">' + data.title + '</span>\n' +
        '                        <div class="active-people">' + data.rate + '   </div>\n' +
        '                    </div>\n' +
        '                    <div class="card-content">\n' +
        '                        <span class="right">' + data.rate + 'x</span>\n' +
        '                        Polední menu\n' +
        '                        <br><br>\n' +
        '                        <div>\n';
    var positionMenu = 1;
    for (var menuKey in data.menu) {
        html += '<div>' + positionMenu + '. ' + data.menu[menuKey].title + ' <span class="right">' + data.menu[menuKey].cost + ',-</span></div>\n';
        positionMenu++;
    }

        html += '                        </div>\n' +
        '                    </div>\n' +
        '                </div>\n' +
        '            </div>';
        return html;
}