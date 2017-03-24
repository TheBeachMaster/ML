var submit = function () {
    var data = document.getElementById('input').value;

    if (data != '') {
        ons.notification.alert('Congratulations!');

        var content = document.getElementById("classif");
        content.innerHTML = "<ons-list-item modifier=\"longdivider\">Item B</ons-list-item>";


    }
    else {
        ons.notification.alert('We do not take empty words');
    }
};