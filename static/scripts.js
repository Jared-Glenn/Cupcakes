async function createCupcake() {
    const flavor = $("#flavor");
    const size = $("#size");
    const rating = $("#rating");
    const image = $("#image");

    // START HERE - I'm having trouble getting the data into a json format that the api link can read.
    // At the moment, I'm getting an error as if it thinks it is converting from a dict (as in, from Python.)

    await axios.post('/api/cupcakes', {
        "flavor": flavor,
        "size": size,
        "rating": rating,
        "image": image})
    
    $(".cupcake-list").append('<li>'+ flavor + size + rating + image + '</li>')
    console.log("That worked!")
}


$("#new-cupcake").click(createCupcake)