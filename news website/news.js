let key="252286fe96f24fd6a78006f6560a18f8";
let cardData=document.querySelector(".cardData");
let searchBtn=document.getElementById("searchBtn");
let inputData=document.getElementById("inputData");
let searchType=document.getElementById("type");

const getData=async(input)=>{
    let res=await fetch(`https://newsapi.org/v2/everything?q=${input}&apiKey=${key}`);
    // let res=await fetch(`https://newsapi.org/v2/everything?q=tesla&from=2025-03-28&sortBy=publishedAt&apiKey=252286fe96f24fd6a78006f6560a18f8`);
    console.log(res);
    let jsondata=await res.json();
    console.log(jsondata.articles);
   
    searchType.innerText="Search : "+input;
    inputData.value="";
    // for show seach result
    cardData.innerHTML="";
     jsondata.articles.forEach(function(article) {
        console.log(article);
    
    let divs=document.createElement("div");
    divs.classList.add("card");
    cardData.appendChild(divs);

    divs.innerHTML=`
    <img src="${article.urlToImage}" alt="images">
    <h3>${article.title}</h3>
    <p>${article.description}</p>
    `
    divs.addEventListener("click",function(){
        window.open(article.url);
    });  
})
}


    // for show default data

window.addEventListener("load",function(){
    getData("breaking news");
})
searchBtn.addEventListener("click",function(){
    let inputText=inputData.value;
    getData(inputText);
})

function navClick(navName){
    if (navName=="politics"){
       document.getElementById("politics").style.color="black";
       document.getElementById("sport").style.color="white";
       document.getElementById("Bollywood").style.color="white";
    }
    if (navName=="sport"){
        document.getElementById("politics").style.color="white";
        document.getElementById("sport").style.color="black";
        document.getElementById("Bollywood").style.color="white";
     }

    if (navName=="Bollywood"){
        document.getElementById("politics").style.color="white";
        document.getElementById("sport").style.color="white";
        document.getElementById("Bollywood").style.color="black";
    }
       getData(navName);
  
}
// 
// 
// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
// let key = "252286fe96f24fd6a78006f6560a18f8";
// let cardData = document.querySelector(".cardData");
// let searchBtn = document.getElementById("searchBtn");
// let inputData = document.getElementById("inputData");
// let searchType = document.getElementById("type");

// const getData = async (input) => {
//     let res = await fetch(`https://newsapi.org/v2/everything?q=${input}&apiKey=${key}`);
//     let jsondata = await res.json();
//     console.log(jsondata.articles);

//     searchType.innerText = "Search: " + input;
//     inputData.value = "";
//     cardData.innerHTML = "";

//     jsondata.articles.forEach(function (article) {
//         let divs = document.createElement("div");
//         divs.classList.add("card");
//         cardData.appendChild(divs);

//         divs.innerHTML = `
//             <img src="${article.urlToImage || 'https://via.placeholder.com/150'}" alt="Image">
//             <h3>${article.title || 'No title'}</h3>
//             <p>${article.description || 'No description available.'}</p>
//         `;

//         divs.addEventListener("click", function () {
//             window.open(article.url);
//         });
//     });
// };

// // Load default data on page load
// window.addEventListener("load", function () {
//     getData("breaking news");
// });

// // Search button click
// searchBtn.addEventListener("click", function () {
//     let inputText = inputData.value.trim();
//     if (inputText !== "") {
//         getData(inputText);
//     }
// });

// // Navigation button click
// function navClick(navName) {
//     // Update nav colors
//     document.getElementById("politics").style.color = navName === "politics" ? "black" : "white";
//     document.getElementById("sport").style.color = navName === "sport" ? "black" : "white";
//     document.getElementById("Bollywood").style.color = navName === "Bollywood" ? "black" : "white";

//     // Fetch category news
//     getData(navName);
// }
