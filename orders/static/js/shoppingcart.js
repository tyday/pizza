// let shoppingcart2 = localStorage.getItem('localstorage_cart')
// console.log(cart_item)
function addHeighttoList() {
    var elements = document.getElementsByClassName('shoppingcartListItem');
    for (i=0; i<elements.length; i++){
        eheigth = elements[i].scrollHeight;
        elements[i].style.height = eheigth+'px';
}}
function getCookie(name) {
    if (!document.cookie) {
      return null;
    }
  
    const xsrfCookies = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith(name + '='));
  
    if (xsrfCookies.length === 0) {
      return null;
    }
  
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}
function remove_from_shoppingcart(cart_item){
    // console.log(cart_item.target.dataset.itemid)
    csrfToken = getCookie('csrftoken');
    itemId = cart_item.target.dataset.itemid;
    listElement = cart_item.target;
    fetch('/removefromcart/',{
        method:'POST',
        credentials:'include',
        body:itemId,
        headers:{
            'X-CSRFToken': csrfToken,
            'Content-Type': 'text/plain'
        }
    }).then(function(response){
        console.log('response1',response, listElement);
        return response.json();
    }).then(function(response){
        // remove the ul that requested
        console.log('response2',response,listElement)
        listElement.parentElement.addEventListener('transitionend',function(){
            listElement.parentElement.remove();})
        listElement.parentElement.classList.add('vanishingItem')
        listElement.parentElement.style.height = '0px';
        })
        // listElement.parentElement.remove()
}
function place_order(){
    csrfToken = getCookie('csrftoken');
    fetch('/placeorder/',{
        method:'POST',
        credentials:'include',
        body:'nothing to see here',
        headers:{
            'X-CSRFToken': csrfToken,
            'Content-Type': 'text/plain'
        }
    }).then(function(response){
        console.log('order has been plassed')
        // Remove the order items
        var elements = document.getElementsByClassName('shoppingcartListItem');
        for (i=0; i<elements.length; i++){
            elements[i].classList.add('vanishingItem')
            elements[i].style.height = '0px';
            elements[i].addEventListener('transitionend',function(){
                this.remove();});
            }
        // Add text to thank them for ordering
        thankyou_text = document.createElement('p');
        thankyou_text.innerHTML = 'Thank you for ordering with us';
        welcome_element = document.getElementById('welcome');
        welcome_element.appendChild(thankyou_text)
    })
}
window.onload = addHeighttoList;