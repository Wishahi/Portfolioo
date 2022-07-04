let div = document.getElementsByClassName('listPlanets');
let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"];
let colors = ["red", "yellow", "orange", "blue", "green"];

for ( let x=0; x <planets.length;x++){
    let planet = document.createElement('div');
    planet.style.backgroundColor=colors[x];
    planet.textContent = planets[x];
    div[0].appendChild(planet);
    planet.style.height="100px";
    planet.style.width="100px";
    planet.style.borderRadius="50%";
    planet.style.display="inline-block";
    planet.style.textAlign="center";
} 


//planet.classlist.add style 

