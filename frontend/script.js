const btn = document.querySelector("button")
const title = document.querySelector("h1")
const isSuccess = true
let articles




//hoisitng
if (isSuccess) {
    article = ["article1", "article2"]
} else {
    console.log("something went wrong")
}

//functions
btn.addEventListener("click", () => {
    title.innerHTML = "Wiktor"
}
)

const printName = (name) => {
    console.log(`Hello ${name}`)
}

printName("Wiktor")