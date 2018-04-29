function init(address){
	buildServiceTiles(address);
}

function buildServiceTiles(url){
	cleanContols();
	$.ajax({url: url + "/services", success: function(serviceList){
		for (var serviceIndex in serviceList){
			callback = "buildElementTiles(\'" + serviceList[serviceIndex]["href"] + "\')"
			appendTile(buildTileDiv(serviceList[serviceIndex]["id"], callback))
		}
    }});
}


function buildElementTiles(url){
	cleanContols();
	$.ajax({url: url + "/elements", success: function(serviceList){
		for (var serviceIndex in serviceList){
			//callback = "buildBasicTiles(\'" + serviceList[serviceIndex]["href"] + "\')"
			appendTile(buildTileDiv(serviceList[serviceIndex]["id"], ""))
		}
    }});
}



function buildTileDiv(content, callback){
	onclickHtml = "";

	if (callback && 0 != callback.length){
		onclickHtml = "onclick=\"" + callback + "\"";
	}

	html = "";
	html += "<div style=\"margin-bottom: 10px; margin-top: 10px;\" class=\"col-sm-4 col-6 col-lg-2\">";
	html += "<div " + onclickHtml + " style=\"padding-top:25%; padding-bottom:25%;\" class=\"bg-secondary text-light text-center rounded\">"
	html += content;
	html += "</div></div>";
	return html
}


function cleanContols(){
	$("#tile_panel").html("");
}

function appendTile(content){
	$("#tile_panel").append(content)
}