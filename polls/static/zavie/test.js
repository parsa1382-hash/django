//alert('hello world');
function te(){
    var old = prompt("how old are you?");
    var h1 = document.createElement('h1');
    var text = document.createTextNode("you are " + old*365 + " days old")
    h1.setAttribute('id','old');
    h1.appendChild(text);
    document.getElementById('flex-box-result').appendChild(h1);
    
}

function re() {
    document.getElementById('old').remove();
}

