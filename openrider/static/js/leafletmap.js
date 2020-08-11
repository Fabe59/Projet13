// Création d'une liste vide pour les coordonnées et le centrage de la carte
bounds = []

// Création de la map
let map = L.map('mapid');

// Création et ajout du tyleLayer à la map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
}).addTo(map);

// Création des marqueurs
let result_elt = document.querySelectorAll('.result_elt');
for (var i = 0; i < result_elt.length; i++) {
    let lat = result_elt[i].querySelector('.lat').textContent;
    let lon = result_elt[i].querySelector('.lon').textContent;
    //let name = result_elt[i].querySelector('.name').textContent;
    coord = [lat, lon];
    bounds.push(coord)
    L.marker(coord).setLatLng(coord).addTo(map)
    //L.popup()
    //.setLatLng(coord)
    //.setContent(name)
    //.addTo(map);
  }

// Centrage dynamique de la carte
if (bounds.length >= 2) {
    map.fitBounds(bounds);
}
else {
    map.setView(coord, 13);
}








