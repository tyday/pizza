let thisvariable=0;

function selectMenuItem(li, itemName, itemDescription){
    console.log(li, itemName, itemDescription);
    console.log(li.dataset.toppings);
    a = li.dataset.toppings
    // for (item in a){
    //     console.log(item)
    // }
    console.log(typeof a);
    a = JSON.parse(a)
    b= Object.keys(a)
    for(i=0;i<b.length;i++){
        console.log(`Name: ${b[i]} Price large: ${a[b[i]].price_large} Price small: ${a[b[i]].price_small}`)
    }
}