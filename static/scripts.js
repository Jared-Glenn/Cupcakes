async function fillList() {
    
    console.log("Ready!")
    const cupcakeList = await axios.get('/api/cupcakes');

    console.log(cupcakeList)

    for (let i = 0; i < (cupcakeList.data.cupcakes).length; i++) {
        let cupcake = cupcakeList.data.cupcakes[i]
        console.log("go!")
        $(".cupcake-list").append('<li>'+ cupcake.flavor + '</li>')
    }
}



async function createCupcake() {
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const image = $("#image").val();


    await axios.post('/api/cupcakes', {
        flavor: flavor,
        size: size,
        rating: parseFloat(rating),
        image: image
    })
    
    $(".cupcake-list").append('<li>'+ flavor + '</li>')
}


$( document ).ready(function() {
    fillList();
});

$( document ).ready(fillList);
$("#new-cupcake").click(createCupcake);