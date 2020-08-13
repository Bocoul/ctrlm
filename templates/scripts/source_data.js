SOURCE_DATA = ['339379984;30000244083560','339379984;30000510568387','339379984;30001720064119','789877776;30001911349967','339379984;30002111271177','539047951;30002321191761','542080486;50072503563557','339379984;30000140353951','339379984;30000230162160','339379984;30000240661879','339379984;30000241188480','339379984;30000250339904','339379984;30000410270164','339379984;30000510189379','339379984;30000510711838','339379984;30000560104511','339379984;30000560461355','339379984;30000560477539','339379984;30000910285505','339379984;30000920027668','339379984;30000930000801','339379984;30000930016658','339379984;30000930237810','339379984;30000930267290'];
const DepartementInconnu = 'DepartementInconnu'
/*tab = []
A_LIST_SIREN  = SOURCE_DATA.reduce(function(acc, noSiren){
	if(acc.indexof(noSiren) = -1) acc.push(noSiren);

}, tab)
*/
var MAP_LIST_SIREN 

UpdateListSiren = function(){
	MAP_LIST_SIREN = new Map()
	for (let i = 0; i < SOURCE_DATA.length; i++) {
		const noSiren = SOURCE_DATA[i].split(";")[0], noRAE = SOURCE_DATA[i].split(";")[1];


		with(MAP_LIST_SIREN){
			if  (!get(noSiren)) {
				set(noSiren, new Map()) 
			}

			with(get(noSiren)){
				if  (!has(DepartementInconnu)) {
					set(DepartementInconnu, {'pdl':{} , 'etab':{}}) 
				}	

				get(DepartementInconnu)['pdl'][noRAE] = {'noRAE' : noRAE}
			}

		}
	}
}



UpdateListSiren()
console.log(MAP_LIST_SIREN);

PdlDisplay(SOURCE_DATA);


/*
AffecterDepartementPdl(noSiren, noDep, infoPDl){

	with(MAP_LIST_SIREN.get(noSiren)){

		get(noDep)['pdl'].push(.get(DepartementInconnu)['pdl'][])
	}
}*/