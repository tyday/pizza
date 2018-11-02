// let shoppingcart2 = localStorage.getItem('localstorage_cart')
// console.log(cart_item)
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
    csrfToken = getCookie('csrftoken')  
    itemId = cart_item.target.dataset.itemid
    fetch('/removefromcart/',{
        method:'POST',
        credentials:'include',
        body:itemId,
        headers:{
            'X-CSRFToken': csrfToken,
            'Content-Type': 'text/plain'
        }
    }).then(function(response){
        console.log('hi_there',response);
        cancelSelection()
        return response.json()
    })
}