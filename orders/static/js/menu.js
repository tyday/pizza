let thisvariable=0;
let shopping_cart = [];

function selectMenuItem(li, itemName, itemDescription, itemJsonII){
    // const itemJson = li.dataset.name;
    const itemJson = JSON.parse(itemJsonII);
    a = JSON.parse(li.dataset.toppings)
    b= Object.keys(a)

    /* Creates a card that contains:
     item name, description, price large and small
     and allows additional toppings to be added */
    const overlay = document.createElement('div');
    overlay.classList.add('overlay') 
    const card = document.createElement('div');
    card.classList.add('overlay_card');
    card.dataset.information = itemJsonII;
    
    // Create Name & description
    for(item of [itemName, itemDescription]){
        let p = document.createElement('p');
        p.innerHTML = item;
        card.appendChild(p);
    }
    
    // Radio buttons for Item size
    if(itemJson.price_small != "None"){
        const size_btn = document.createElement('input');
        const label_btn = document.createElement('label');
        label_btn.innerHTML = "Small: $" + itemJson.price_small;
        label_btn.appendChild(size_btn)
        size_btn.name = "size"
        size_btn.value = "small"
        size_btn.type = "radio"
        card.appendChild(label_btn);
    }
    if(itemJson.price_large){
        const size_btn = document.createElement('input');
        const label_btn = document.createElement('label');
        label_btn.innerHTML = "Large: $" + itemJson.price_large;
        label_btn.appendChild(size_btn)
        size_btn.name = "size"
        size_btn.value = "large"
        size_btn.type = "radio"
        size_btn.checked = true;
        card.appendChild(label_btn);
    }
    
    // Create toppings:
    select = createToppingSelection(a);
    if(select){
        card.appendChild(select);
    }
    // Buttons to add to cart and cancel order
    const add_to_cart_btn = document.createElement('button');
    add_to_cart_btn.innerHTML = "Add to cart";
    add_to_cart_btn.onclick = function(event){
        add_to_shoppingcart();
    }
    const cancel_order_btn = document.createElement('button');
    cancel_order_btn.innerHTML = "Cancel"
    cancel_order_btn.onclick = function(event){
        cancelSelection();
    }
    card.appendChild(add_to_cart_btn);
    card.appendChild(cancel_order_btn);

    overlay.appendChild(card);
    document.body.appendChild(overlay);
}

function createToppingSelection(toppingList){
    if(Object.entries(toppingList).length > 0){
        toppingList_keys = Object.keys(toppingList);

        const select = document.createElement('select')
        select.setAttribute("class","topping-select")
        select.name="topping-select"
        select.dataset.cloned = false;
        select.onchange = function(event){
            selectionitem = event.target
            if (selectionitem.dataset.cloned == 'false'){
                console.log('it fired',event.target.value)
                console.log(event)
                selecteditem = event.target.value;
                selecteditem = JSON.parse(selecteditem)
                delete toppingList[selecteditem[0]];
                if(Object.entries(toppingList).length > 0){
                    newtoppinglist = createToppingSelection(toppingList);
                    selectionitem.parentNode.insertBefore(newtoppinglist, selectionitem.nextSibling);
                }
            }
            else{
                console.log('nothing')
            }
        }
        const firstOption = document.createElement('option');
        firstOption.innerHTML = "--Please choose your toppings--";
        firstOption.value = "";
        select.appendChild(firstOption);
        for(item of Object.entries(toppingList)){
            let option = document.createElement('option');
            option.value = JSON.stringify(item);
            option.innerHTML = item[0];
            option.dataset.price_large = item[1].price_large;
            option.dataset.price_small = item[1].price_small;
            select.appendChild(option);
        }
        return select
    }
    else {
            return
    }
}
function cancelSelection(){
    card = document.getElementsByClassName('overlay')[0]
    document.body.removeChild(card);
}
function add_to_shoppingcart(){
    cart_item = {};
    card = document.getElementsByClassName('overlay_card')[0]
    cart_item = JSON.parse(card.dataset.information);
    console.log(card.dataset.information);
    console.log(typeof card.dataset.information)
    console.log(cart_item, typeof cart_item)
    console.log(cart_item.invoice_name)

    // get size of the selected item
    // small or large
    let radiobuttons = document.getElementsByName('size')
    let item_size = ""
    let item_price = ""
    for(var i = 0; i < radiobuttons.length;i++){
        if (radiobuttons[i].checked == true){
            item_size = radiobuttons[i].value
        }
    }
    if (item_size == "small"){
        item_price = cart_item.price_small;
    } else {
        item_price = cart_item.price_large;
    }
    // Get all the toppings
    toppings_list = [];
    let toppings = document.getElementsByClassName("topping-select");
    let topping = new Object();
    try {
        for(var i=0; i < toppings.length; i++){
            let topping = {}
            selectionValue = JSON.parse(toppings[i].value)
            topping.name = selectionValue[0]
            topping.id = selectionValue[1].id
            if (item_size == "small"){
                topping.cost = selectionValue[1].price_small;
            }else {
                topping.cost = selectionValue[1].price_large;
            }
            toppings_list.push(JSON.parse(JSON.stringify(topping)));
            
        }
    } catch(e) { console.log(e)}
    let itemToAddToCart = {"item":cart_item["invoice_name"],"toppings":toppings_list, "cost":item_price,"id":cart_item["id"]}
    console.log('hello!')
    console.log(itemToAddToCart)

    shopping_cart.push(itemToAddToCart)
}