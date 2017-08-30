function getQueryString(name) { 

  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i"); 
  var r = window.location.search.substr(1).match(reg); 
   if (r != null) return unescape(r[2]); return null; 
} 
function test(){
	var result = getQueryString("name");
	alert(result);
	alert("../static/"+result+".jpg");
    console.log('11111');

	$("#resultImg").attr("src","../static/"+result);
}