
	let SOURCE_DATA;	
	const DOM_inputFile = document.querySelector('#file');
	
	function getData(){
	    const reader = new FileReader();
	    reader.onload = function() {
					        //SOURCE_DATA = this.result.split(String.fromCharCode(13)).map((a) => new  Map(a.split(";") ));/**/
					        SOURCE_DATA = this.result.split(String.fromCharCode(13)).map(
					        	function (a) {
								  return new Map(a.split(";"));
								}
							);
							debugger
					        console.log(SOURCE_DATA.length);
					        PdlDisplay(SOURCE_DATA);
			    		};

		DOM_inputFile.onchange = function() {
						    		reader.readAsText(this.files[0]);  
								};
	}




