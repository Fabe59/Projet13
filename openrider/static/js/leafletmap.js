//let name = 'Treulan, Pluneret';
//let coordinates = [47.7076568, -2.9810811];

// Création de la map
let map = L.map('mapid').setView([47.7076568, -2.9810811], 9);

// Création et ajout du tyleLayer à la map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
}).addTo(map);

// Création d'un marker
//let marker = L.marker(coordinates).addTo(map);
let element = document.querySelectorAll('.leaflet-marker');
let elArr = Array.from(element);
console.log(element);
console.log(elArr);
elArr.forEach(item => console.log(item));

//{% for elt in result %}
//    L.marker({{ elt.coordinates }}).addTo(map);
//{% endfor %}
