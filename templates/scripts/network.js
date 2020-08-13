
function callAjax(s_methode, s_url, fn_Success, fn_Error, paramSend, responseType){
    if (paramSend == undefined){paramSend = null;}
    if (responseType == undefined){responseType = "document";}
    const objxhr = new XMLHttpRequest();
    objxhr.open(s_methode, s_url, true);
    objxhr.responseType = responseType;
    objxhr.withCredentials = true;

    objxhr.onload = function(){
                return fn_Success(this);                                  
                    }
    objxhr.onerror= function(){
                return fn_Error(this);
                    }

    objxhr.send(paramSend);



}

