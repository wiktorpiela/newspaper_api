const btn = document.querySelector("button")
const title = document.querySelector("h1")
const norrisUrl = "https://api.chucknorris.io/jokes/"


async function logJSONData(url, queryName) {
    const response = await fetch(`${url}search?query=${queryName}`);
    const jsonData = await response.json();
    console.log(jsonData);
  }

logJSONData(norrisUrl, "cat")