import cgi
import cgitb

cgitb.enable

form = cgi.FieldStorage() 
username  =  form.getvalue("username")
fichier  =  form.getvalue("fichier")
print(username)

if (username): 
    pass

else:  
    raise Exception("le  nom n'est pas correct")


print("content-type: text/html; charset=utf-8\n")
html =f"""
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Bonjour {username} Listes des SIRET</title>
		<link rel="stylesheet" type="text/css" href="output.css" />
		
	</head>

<body >
	<div id = "root" >
	<nav>
	<form method="POST" action='result.py'>
		<input name="username" type="text"/>
	</form>
	<input type="button" id="raz" onclick="razListe();" value = "Effacer tout">
	<input id="file" type="file" />	
	<input type="button" id="start" onclick="PDLSearch();" value = "Start">
	<input type="button" id="start2" onclick="entrSearchByDep();" value = "Start SIREN">
	<div id= "like_button_container"></div>
	</nav>
	<div id= "fiche">
		<table >
			<thead>
				<tr class = "label" >
				<th class = "label client_siren" >SIREN</th>
				<th class = "label pdl_rae" >RAE</th>
				<th class = "label pdl_voie" >PDL VOIE</th>
				<th class = "label pdl_cp">PDL_CP</th>
				<th class = "label pdl_commune">PDL_COMMUNE</th>			
				<th class = "label client_siege">SIEGE</th>
				<th class = "label client_etablissement" >NOM COMMERCIAL</th>
				<th class = "label client_nic" >NIC</th>
				<th class = "label client_rue" >RUE</th>
				<th class = "label client_cp" >CODE POSTAL</th>
				<th class = "label client_codeinsee" >CODE INSEE COMMUNE</th>
				<th class = "label client_commune" >COMMUNE</th>
				</tr>	
			</thead>

			<tbody id="view_pdl">
				<tr class = "value" >
				<td class = "value client_siren" ></td>
				<td class = "value pdl_rae" ></td>
				<td class = "value pdl_voie" ></td>
				<td class = "value pdl_cp"></td>
				<td class = "value pdl_commune"></td>			
				<td class = "value client_siege"></td>
				<td class = "value client_etablissement" ></td>
				<td class = "value client_nic" ></td>
				<td class = "value client_rue" ></td>
				<td class = "value client_cp" ></td>
				<td class = "value client_codeinsee" ></td>
				<td class = "value client_commune" ></td>
				</tr>
			</tbody>
		</table>
	</div>	
</div>
<div>{fichier}</div>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script type="text/javascript" src="scripts/data.js" ></script>
<script type="text/javascript" src="scripts/network.js" ></script>
<script type="text/javascript" src="scripts/etab.js" ></script>
<script type="text/javascript" src="scripts/sge.js" ></script>
<script type="text/javascript" src="scripts/views.js" ></script>
<script type="text/javascript" src="scripts/ctrl.js" ></script>
<script type="text/javascript" src="scripts/source_data.js" ></script>


 <script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>  
 <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
  <!-- Charge notre composant React -->
<!-- <script src="like_button.js"></script>  -->

</body>
</html>
"""

print(html)