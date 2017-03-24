var submit = function() {
  var data = document.getElementById('input').value;
  
  if (username != '') {
    ons.notification.alert('Congratulations!');
  }
  else {
    ons.notification.alert('We do not take empty words');
  }
};