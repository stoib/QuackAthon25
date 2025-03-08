
export function createTimetableEvent(){
    var table = document.getElementById("Monday table table-hover caption-top");
    var row = table.insertRow(0);   //create row <tr>
    var nameRow = row.insertCell(0);  //<td scope="row">{"name"}</td>
    var locationRow = row.insertCell(1);    //<td>{"location"}</td>
    var timeRow = row.insertCell(2);    //<td>{"time"}</td>
    var linkRow = row.insertCell(3);    //<td>{"linktomap"}</td>
    nameRow.innerHTML = "NEW CELL1";
    locationRow.innerHTML = "NEW CELL2";
    timeRow.innerHTML = "NEW";
    linkRow.innerHTML = "NEW";        
}
export function maki(){
    const card = document.createElement("div");
    card.className = "Card";
    card.innerText = "weee";
    
}

// var table = document.getElementById("myTable");
//   var row = table.insertRow(0);
//   var cell1 = row.insertCell(0);
//   var cell2 = row.insertCell(1);
//   cell1.innerHTML = "NEW CELL1";
//   cell2.innerHTML = "NEW CELL2";