ul = document.querySelector('ul')


items = ['Item1', 'Item2', 'Item3']

items.forEach(item => {
    console.log(`${item}`);
    ul.innerHTML +=`<li><a href="#">${item}</a></li>`
});

console.dir(ul);


// <li><a href="#">Item1</a></li>
// <li><a href="#">Item2</a></li>
// <li><a href="#">Item3</a></li>