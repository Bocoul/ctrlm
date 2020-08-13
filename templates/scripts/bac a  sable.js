
var objSirenDepartement
const testAjax = function (){
					const url  =  "http://avis-situation-sirene.insee.fr/IdentificationListeSiret.action?form.critere=A&form.departement=&form.departement_actif=33&form.nic=&form.siren=339+379+984"
					let  objSirenDepartement;
					callAjax(
						'GET',
						 url,
						 function(objXhr){
						 		objSirenDepartement = Siren_2(objXhr);

						}, 
						function(objXhr){
							console.log(" error")
						}
					)

				}
while (!objSirenDepartement ){}
console.log(objSirenDepartement)


const eee = new Map()




function readAddress(ListeTR){
const resultat = ListeTR.map(function (tr) {
	return {tr.cells.map((td) =>{
})
}