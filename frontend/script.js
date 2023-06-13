const btn = document.querySelector("button")
const title = document.querySelector("h1")
const myUrl = "http://127.0.0.1:8000/articles/"

async function logJSONData(url) {
    const response = await fetch(url);
    const jsonData = await response.json();
    console.log(jsonData);
  }

logJSONData(myUrl)