// var name_cho = document.querySelectorAll('li')
console.log("Checking")

function title_change(){
    var nameList = document.getElementById('jack_item')
    if(nameList.options[nameList.selectedIndex].text != '---Choose a jack-----'){
        document.getElementById('title_name').innerText = nameList.options[nameList.selectedIndex].text
    }
    else{
        document.getElementById('title_name').innerText = 'No Jack chosen yet'
    }   
    
}

function title_change2(){
    var nameList = document.getElementById('jack_name')
        document.getElementById('title_name').innerText = nameList.options[nameList.selectedIndex].text

}