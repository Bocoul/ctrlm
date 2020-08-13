getData();



function PDLSearch(){
	    for(let i=1; i<SOURCE_DATA.length; i++){
		    const fichePrm = new FichePrm(SOURCE_DATA[i].split(";")[1]);
		    fichePrm.loadFicheSGE();
		}
}


function SirenSearch(){
	    for( trPrm in  TABLE_BODY_INFO.childNodes){
		  console.log(trPrm);
		}
}

