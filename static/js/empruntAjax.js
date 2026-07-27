

window.onload=function(){
	initListeners(); 
}

var spanRes;

//var calculBaseUrl = "http://127.0.0.1:5000/mensualite"
//var calculBaseUrl = "http://localhost:5000/mensualite"
var calculBaseUrl = "../mensualite" //vis à vis de static

function initListeners(){
	spanRes = document.getElementById("spanRes");
	
	let btnMensualite = document.getElementById("btnMensualite");
	
	btnMensualite.addEventListener("click" , ()=>{
		let montantValue= (document.getElementById("inputMontant")).value;
		let dureeValue= (document.getElementById("inputDuree")).value;
		let tauxValue= (document.getElementById("inputTaux")).value;
		let wsUrl = calculBaseUrl + "?montant=" + montantValue + "&duree=" + dureeValue + "&taux=" + tauxValue;
		console.log("wsUrl="+wsUrl);
		makeAjaxGetRequest(wsUrl,(responseJson)=>{
			console.log("responseJson="+responseJson);
			let resObj = JSON.parse(responseJson);
			spanRes.innerHTML="" + resObj.mensualite
		});
	});
	
	
	spanRes.innerHTML="0"; //by default
}
