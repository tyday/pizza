let thisvariable=0;

function selectMenuItem(li, itemName, itemDescription){
    console.log(li, itemName, itemDescription);
    console.log(li.dataset.toppings);
    a = JSON.parse(li.dataset.toppings)
    b= Object.keys(a)
    // for(i=0;i<b.length;i++){
    //     console.log(`Name: ${b[i]} Price large: ${a[b[i]].price_large} Price small: ${a[b[i]].price_small}`)
    // }

    /* Creates a card that contains:
     item name, description, price large and small
     and allows additional toppings to be added */
    const overlay = document.createElement('div');
    overlay.classList.add('overlay') 
    const card = document.createElement('div');
    card.classList.add('overlay_card');
    // let p = document.createElement('p');
    // p.innerHTML = itemName;
    // card.appendChild(p);
    // p = document.createElement('p');

    for(item of [itemName, itemDescription]){
        let p = document.createElement('p');
        p.innerHTML = item;
        card.appendChild(p);
    }

    // create selection box and populate with toppings
    // const select = document.createElement('select')
    // for(item of b){
    //     let option = document.createElement('option')
    //     option.value = item
    //     option.innerHTML = item
    //     select.appendChild(option)
    // }
    select = createToppingSelection(b);
    if(select){
        card.appendChild(select);
    }
    

    overlay.appendChild(card);
    document.body.appendChild(overlay);
}

function createToppingSelection(toppingList){
    if(toppingList.length > 0){
        const select = document.createElement('select')
        select.setAttribute("id","topping-select")
        select.name="topping-select"
        select.dataset.cloned = false;
        select.onchange = function(event){
            selectionitem = event.target
            if (selectionitem.dataset.cloned == 'false'){
                console.log('it fired',event.target.value)
                console.log(event)
                selecteditem = event.target.value;
                itemposition = toppingList.indexOf(selecteditem)
                selectionitem.dataset.cloned = 'true';
                toppingList.splice(itemposition,1);
                newtoppinglist = createToppingSelection(toppingList);
                selectionitem.parentNode.insertBefore(newtoppinglist, selectionitem.nextSibling);
            }
            else{
                console.log('nothing')
            }
        }
        const firstOption = document.createElement('option');
        firstOption.innerHTML = "--Please choose your toppings--";
        firstOption.value = "";
        select.appendChild(firstOption);
        for(item of toppingList){
            let option = document.createElement('option');
            option.value = item;
            option.innerHTML = item;
            select.appendChild(option);
        }
        return select
    }
    else {
            return
    }
}