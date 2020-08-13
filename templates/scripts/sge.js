const TITLE_SGE = "Système de Gestion des Echanges";
const URL_SGE = "https://sge.enedis.fr/sgePortail/appmanager/portail/bureau?" + 
                "_nfpb=true&_windowLabel=portlet_gestion_pdl_2&portlet_gestion_pdl_2_actionOverride=%2Fportlets%2FgestionPdl%2FconsulterPdm&portlet_gestion_pdl_2idPdm=[PDL]&_pageLabel=sge_page_accueil"; 

function FichePrm(noRAE){
    this.noRAE = noRAE;
    this.domFicheSGE;
    this.addressSGE;
    this.isDisplay = function (){
        return  document.getElementById( this.noRAE)
    }
    this.readAddressPrm = function(){
            this.addressSGE = {
                                pdl_id:this.domFicheSGE.all("prmId").value,
                                pdl_voie: this.domFicheSGE.all("voie").value, 
                                pdl_cp: this.domFicheSGE.all("codePostal").value, 
                                pdl_commune: this.domFicheSGE.all("commune").value
                                };
            return  this.addressSGE;      
    try {
    
        } 
        catch (error) {
          console.error("la page sge n'est pas correct");
          return  false;
        }
    }

    this.getUrlFicheSGE = function(){
        return URL_SGE.replace("[PDL]", this.noRAE)
    }

    this.loadFicheSGE = function (){
        if (this.addressSGE) return true;

            const that = this;		
            callAjax(
                "POST", 
                this.getUrlFicheSGE(),
                function(o_xhr){
                    if (o_xhr.response.title === TITLE_SGE) {
                        that.domFicheSGE = o_xhr.response;
                        that.readAddressPrm();
                        that.DisplayPDL();
                    
                    }  

                    else
                    {
                       console.log("Error connexion: la page chargée n'est celle qui est attendue " + o_xhr.response.title) 
                        //setTimeout(10000, callSGE(this.noRAE))
                    }
                }, 
                function(o_xhr){
                    console.log("Error connexion: pas de reponse") ;
                }
            );				
    }

    this.DisplayPDL = function(){
        try{
            const o_htmlRowElement = document.getElementById(  this.addressSGE.pdl_id); 
            HTMLTableRowElement.display(o_htmlRowElement,this.addressSGE)
                                   /* [
                                        ["pdl_voie", this.addressSGE.pdl_voie], 
                                        ["pdl_cp", this.addressSGE.pdl_cp],
                                        ["pdl_commune", this.addressSGE.pdl_commune]
                                    ]); */
        } catch(error){
            console.log("error : pas d'info d'adresse disponible");
        }
    }

}

/*
function StringRepeat(str, nombre){
    const arr = new Array();
    for(let i=0; i<nombre; i++){
        arr.push(str);
    } 
    return  arr.join("");
}

}*/