ymaps.ready(init);
var myMap;

function init () {
    myMap = new ymaps.Map("map", {
        center: [51.6716, 39.2130], // воронеж
        zoom: 11
    }, {
        balloonMaxWidth: 200,
        searchControlProvider: 'yandex#search'
    });

    // Обработка события, возникающего при щелчке
    // левой кнопкой мыши в любой точке карты.
    // При возникновении такого события откроем балун.
    myMap.events.add('click', function (e) {
        if (!myMap.balloon.isOpen()) {
            var coords = e.get('coords');
            myMap.balloon.open(coords, {
                contentHeader:'Новая метка',
                contentBody:'<p><label for="uname">Опишите проблему: </label>' +
                    '<input type="text" id="uname" name="name" />' + '</p>' +
                    '<input type="button" value="Опубликовать" />' + '</p>',
                contentFooter:'<sup>Щелкните еще раз</sup>'
            });
        }
        else {
            myMap.balloon.close();
        }
    });
    myMap.events.add('balloonopen', function (e) {
        myMap.hint.close();
    });
}