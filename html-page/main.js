$.getJSON("../weeks/active.json", function(json) {
    print(json); // this will show the info it in firebug console
});

$.getJSON('../weeks', data => {
    console.log(data); //["doc1.jpg", "doc2.jpg", "doc3.jpg"] 
    var selector = document.getElementById("file-selector");
    tmp_string = ""
    for (var [index, name] of Object.entries(data)) {
        tmp_string+= "<option value='"+name+"'>"+name+"</option>"
    }

    selector.innerHTML = tmp_string
});
function loadSelectedFile(){
    var e = document.getElementById("file-selector");
    var value = e.options[e.selectedIndex].value;
    var text = e.options[e.selectedIndex].text;
    
    console.log(typeof value)
    clearDoc()
    loadDataFromFile(value)
}

function loadDataFromFile(fileName){
    $.getJSON("../weeks/"+fileName, function(json) {
        print(json); // this will show the info it in firebug console
    });
}
var outStrings = []
function print(obj){
    
    outStrings = []
    var tmp_string = ""
    for (var [char, vendors] of Object.entries(obj)) {
        if(char == "all_notable_rolls"){

        }else{
        tmp_string = ""
        tmp_string +=" <div class='class-grid'>"
        tmp_string +=    "<span id='class-name'>"+ char+"</span>"
        tmp_string +=    "<div class='spacer'></div>"
        tmp_string +=    "<div class='spacer'></div>"
        tmp_string +=    "<div class='spacer'></div>"
        
        //console.log(key + ' ' + value); 
        for( var [vendor, items] of Object.entries(vendors)){
            if(vendor == "total_notable_rolls"){

            }else{

            
            
            tmp_string += "<div class='vendor-grid'>"
            tmp_string +=    "<span id='vendor-name'>"+ vendor + "</span>"
            tmp_string +=    "<div class='spacer'></div>"
            for( var [item, items] of Object.entries(items)){
                if(item != "notable_rolls"){
                for( var [item, stats] of Object.entries(items)){
                    
                    tmp_string += "<div class='item-card'>"
                    tmp_string += "<div class='card-grid-item item-type'>"
                    tmp_string +=    '<span id="item-type">'
                    tmp_string +=        item
                    tmp_string +=    "</span>"
                    tmp_string += "</div>"
                    tmp_string += "<div class='card-grid-item title-bar'><div id='spacer'></div></div>"
                    tmp_string += "<div class='card-grid-item notability'>"
                    if(stats["is_notable"]){
                        tmp_string +=    "<div id='notability' class='notability-indicator' style='background-color: rgb(43, 255, 0);'>"
                    }else{
                        tmp_string +=    "<div id='notability' class='notability-indicator' style='background-color: rgba(255, 0, 0, 0.466);'>"
                    }
                    
                    tmp_string +=    "</div>"
                    tmp_string += "</div>  "
                    for( var [stat, value] of Object.entries(stats)){
                        
                        if(stat == "stat_total" || stat == "is_notable"){
                            
                        }else{
                        tmp_string +=    "<div class='card-grid-item stat-name' id="+ stat+">"+stat+": </div>"
                        tmp_string += "<div class='card-grid-item stat-bar'>"
                        tmp_string += "<div id='mobility-bar' class='bar'>"
                        tmp_string +=    "<div class='bar-value' style='width: "+(value/3.5)+"rem;'> </div>"
                        tmp_string += "</div>"
                        tmp_string += "</div>"
                        tmp_string += "<div class='card-grid-item stat-value'><span id='mobility-value'>"+value+"</span></div>"
        
                        }
                        
                    }
                    tmp_string+="</div>"
                    
                }
                }
            }
        }
            tmp_string+="</div>"
        }
        tmp_string+="</div>"
        outStrings.push(tmp_string)
        }
        
    }
    clearDoc();
    loadToDoc();
}

function loadToDoc(){
    
   var frame = document.getElementById("frame");
   
   outStrings.forEach(function(element){
       frame.innerHTML += element
   })
   
    
}

function clearDoc(){
    var frame = document.getElementById("frame").innerHTML = " ";
}