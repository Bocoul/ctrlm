


const TABLE_BODY_INFO = document.querySelector('#view_pdl');

function PdlDisplay(a_arrayData) {
    for(let i=1; i<a_arrayData.length; i++){
        const s_siren = a_arrayData[i].split(";")[0];
        const s_pdl = a_arrayData[i].split(";")[1];
        TableDisplay(s_pdl, {client_siren : s_siren, pdl_rae : s_pdl})
   }
}


function getLastItem(array){
	return	array[array.length - 1];
}

function duplicateStructRow(tr){
	o_newhtmlRowElement =  tr.offsetParent.insertRow(tr.rowIndex + 1);
	for(let i = 0; i <tr.cells.length; i++){
		const newCell = o_newhtmlRowElement.insertCell(-1);
		newCell.className = tr.cells.item(i).className;
	} 
	return tr;
}

function razListe() {
   TABLE_BODY_INFO.innerHTML = ""; 
}


HTMLTableRowElement.display = function(tr, Listfields){

    for (let field in Listfields){
        const tdField = tr.querySelector("." + field);
        try{
          if (tdField) {tdField.innerHTML =  Listfields[field]}  ; 
        }
        catch(error){
          console.error(error + " echec  saisie");
        }
    }        
}

function TableResize(table){
    const o_htmlRowElement = getLastItem (table.rows); //.insertRow(-1); 
    duplicateStructRow(o_htmlRowElement);
    return  o_htmlRowElement;
}

function TableDisplay(id, ArrayParam ){
        let o_htmlRowElement 
        if (!document.getElementById(id)){
            o_htmlRowElement =TableResize(TABLE_BODY_INFO);
            o_htmlRowElement.id = id;
        } 
        HTMLTableRowElement.display (o_htmlRowElement, ArrayParam)

   /*     o_htmlRowElement.querySelector(".client_siren").innerHTML = s_siren;
        o_htmlRowElement.querySelector(".pdl_rae").innerHTML = s_pdl ;*/
}