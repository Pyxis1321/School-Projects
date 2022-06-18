// select the button using ID
var button = document.querySelector('#translateBtn');
var userInput = document.querySelector('#userInput');
var resultInput = document.querySelector('#result');
var loadingDiv = document.querySelector('#loading');
var data = [];
var tmp = '';
var webResponse;
var element = document.getElementById("history");

if(window.localStorage.getItem('storage') == null){
	localStorage.setItem('storage','[]')
}
data = JSON.parse(localStorage.getItem('storage'));

for(let i = 0; i < data.length; i+=2){
	tmp += data[i] + " -> " + data[i+1] + "<BR>";
}
element.innerHTML = tmp;
tmp = '';

button.onclick = function () {

    // show the loading dialog
    loadingDiv.style.display = 'block';
    // disable translate button
    button.setAttribute('disabled','disabled');

    var inputText = userInput.value;
    data.push(inputText);

    // test - write into DOM
    resultInput.value = inputText;

    // REST API url endpoint
    var url = 'https://api.mymemory.translated.net/get?q=' + inputText + '&langpair=cs|en';

    // create the GET request against API to obtain JSON result
    fetch(url)
    .then(function(response) {
        // server returns the response, parse it to JSON
        return response.json();
    })
    .then(function(myJson) {
        // get translation string from JSON, put it in result input
        resultInput.value = myJson.responseData.translatedText;
        webResponse = JSON.stringify(resultInput.value);
        // hide the loading dialog
        loadingDiv.style.display = 'none';
        // enable translate button
        button.removeAttribute('disabled');

    }).then(function(){
        data.push(webResponse);
        for(let i = 0; i < data.length; i+=2){
            tmp += data[i] + " -> " + data[i+1] + "<BR>";
        }
        element.innerHTML = tmp;
        tmp = '';

        localStorage.setItem('storage', JSON.stringify(data));
    });

}