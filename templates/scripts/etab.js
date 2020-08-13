
const URL_SIRENE_LISTE_SIRET_old = "http://avis-situation-sirene.insee.fr/IdentificationEtabToEntr.action?form.siren=[SIREN]&form.nic=";
const URL_SIRENE_LISTE_SIRET_LOOKUP = "http://avis-situation-sirene.insee.fr/LookupEntr.action";
const URL_SIRENE_LISTE_SIRET = "http://avis-situation-sirene.insee.fr/IdentificationListeSiret.action?"
const PARAM_SEND_LIST_ = "etabEntreprises=etabsDepartement&form.adrPreponderante=0&form.departement=75&form.siren=[SIREN]&method:executeAfficher";
const PARAM_SEND_LIST = "/form.critere=A&form.departement=&form.departement_actif=[CODE_DEPARTEMENT]&form.nic=&form.siren=[SIREN]"
const regExpNumericOnly =  /[0-9]/g 
let mapSIREN


/*const setMapSiren = function(){
	const liste = new Map()


}*/
/*const ReadAllSiren = function () {
	
	with(TABLE_BODY_INFO.querySelectorAll(".pdl_cp")){

		for (let i = 0; i < length; i++ ){

			const noSiren = item(i).parentNode.querySelector('.client_siren').innerText;
			const noDepartement = item(i).innerText.substr(0,2);	

			if (noDepartement.length > 0)  {	
				if (!mapSIREN.get(noSiren) ) mapSIREN.set(noSiren, new Map())  


					if(!mapSIREN.get(noSiren).get(noDepartement)) {
						ReadSiretsDepartement(noSiren, noDepartement);
					}
	/*			
						try{			}	

				catch(e){
					console.log("erreur  sur le  siren " + noSiren + " dep " + noDepartement);
				}
			}

		} 
	}

}*/



const ReadAllSiren = function () {
	
	with(MAP_LIST_SIREN){
		for (let elt in MAP_LIST_SIREN){

			const noSiren = item(i).parentNode.querySelector('.client_siren').innerText;
			const noDepartement = item(i).innerText.substr(0,2);	

			if (noDepartement.length > 0)  {	
				if (!mapSIREN.get(noSiren) ) mapSIREN.set(noSiren, new Map())  


					if(!mapSIREN.get(noSiren).get(noDepartement)) {
						ReadSiretsDepartement(noSiren, noDepartement);
					}

			}

		} 
	}

}


const ReadSiretsDepartement = function (noSiren, noDepartement){
					noSiren =  noSiren.substr(0,3) + "+" + noSiren.substr(3,3) +  "+" +  noSiren.substr(6,3)
					const url  = URL_SIRENE_LISTE_SIRET +  PARAM_SEND_LIST.replace('[CODE_DEPARTEMENT]', noDepartement).replace('[SIREN]', noSiren)
					//const url  =  "http://avis-situation-sirene.insee.fr/IdentificationListeSiret.action?form.critere=A&form.departement=&form.departement_actif=33&form.nic=&form.siren=339+379+984"
					callAjax(
						'GET',
						 url,
						 function(objXhr){
						 		const objSirenDepartement = Siren_2(objXhr);
						 		with(mapSIREN){
							 		if (!get(objSirenDepartement[0])) {
										set(objSirenDepartement[0],  new Map());
							 		} 
							 		get(objSirenDepartement[0]).set(objSirenDepartement[1], objSirenDepartement[2]);						 			
						 		}						 		

						}, 
						function(objXhr){
							console.log(" error")
						}
					)

				}

function Siren_2(objxhr){

	const noSiren = objxhr.response.querySelector("div.contenu").querySelector("p.criteres").innerText.match(regExpNumericOnly).join('');
	console.log(noSiren);
	const siretRows = objxhr.response.querySelector("#PaginationListeSiretActifs").querySelectorAll("tr.resultPair,tr.resultImpair");
	const mapSiretDepartement = new Map();
	let departement = ""

	for (let info,  i = 0; i< siretRows.length; i++ ){
		with(siretRows[i]){
			
			info = 	{
					Siren : noSiren,
					urlEtablissement : cells[1].querySelector('a').getAttribute('href'),
					siretNic : cells[1].innerText,
					denomination : cells[2].innerText,
					voie : cells[3].innerText,
					codeDepartement : cells[4].innerText.substr(0,2),
					commune : cells[4].innerText.substring(3)
				}
			departement = info.codeDepartement;
			mapSiretDepartement.set(info.siretNic, info);
		}
	}

	return [noSiren, departement , mapSiretDepartement];

}

function Siren(noSiren){

	this.noSiren = noSiren;	
	this.setListDepartement = new Array();
	this.setListPDL = new Array() ;

	this.loadListEtabDepartement = loadListEtabDepartement;
	this.getParamSendforListSiret = getParamSendforListSiret;
	this.onsuccess = function(o_xhr){
		console.log(o_xhr.response);
		console.log("youpi");
	}

	this.onerror = function(o_xhr){
		console.log("connexion échoué " + o_xhr.status);
	}


	function loadListEtabDepartement(s_codePostal){
		callAjax(
                "POST", 
                URL_SIRENE_LISTE_SIRET,
               	this.onsuccess, 
               	this.onerror,
               	this.getParamSendforListSiret(s_codePostal)

            );    
              
	}
	function getParamSendforListSiret(s_codePostal){
		if (!isCodePostalValid(s_codePostal)) {
			console.log(s_codePostal + "n'est  pas un code postal valide");
			return null;
		}

		this.codeDepartement = s_codePostal.substr(0, 2);
		return	PARAM_SEND_LIST.replace("[CODE_DEPARTEMENT]" , this.codeDepartement);
	}

	function Etablissement(noSiren, noNIC){
		this.noSiren = noSiren;
		this.loadinfoEtab = function (){
		this.noNIC = noNIC;
		}

		this.toString = function (){
			return this.noSiren + "" + this.noNIC;
		}
	}






} 

function isCodePostalValid(s_codePostal){
	return s_codePostal.length == 5; 
}	
function entrSearchByDep(){
	     for(let i=1; i<3; i++){
	       callAvisSireneEntr(a_data[i].split(";")[0]);
	        }
}

const callAvisSireneEntr = function(s_siren){

							const paramsend = PARAM_SEND_LIST.replace("[CODE_DEPARTEMENT]" , "33").replace("[SIREN]", s_siren.substr(0,3) + "+" + s_siren.substr(3,3) +  "+" +  s_siren.substr(6,3) )
                        	callAjax(
                                    "POST", 
                                    URL_SIRENE_LISTE_SIRET,
                                    function(o_xhr){
                                        o_xhr.response.getElementById("").value = "etabsDepartement";
                                        o_xhr.response.getElementById("LookupEntr_etabEntreprises").fireEvent('onChange', null);
                                        o_xhr.response.getElementById("departement").value= "75";
                                        o_xhr.response.getElementById("LookupEntr").submit();
                                        console.log(o_xhr.response);
                                        console.log("youpi");

                                    }, 
                                    function(o_xhr){
                                        console.log("connexion échoué " + o_xhr.status);
                                    }, 
                                   	paramsend
                                );                 
}
