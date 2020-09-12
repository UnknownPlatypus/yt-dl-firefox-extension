////////// Plugin event listeners //////////
// 3 Main clicks
document.getElementById('audio_M4a').addEventListener('click', function(){
    browser.runtime.sendMessage("m4a");
    document.querySelector("#progress-bar").classList.remove("hidden");
})
document.getElementById('audio_mp3').addEventListener('click', function(){
    browser.runtime.sendMessage("mp3");
    document.querySelector("#progress-bar").classList.remove("hidden");
})
document.getElementById('video').addEventListener('click', function(){
    browser.runtime.sendMessage("mp4")
    document.querySelector("#progress-bar").classList.remove("hidden");
})
// Other formats
document.getElementById('format').addEventListener('click', function(){
    // Look for other formats
    browser.runtime.sendMessage("format");
    document.getElementById('load-format').classList.remove("hidden");
    document.getElementById('format').classList.add("hidden");    
})
document.getElementById('DL').addEventListener('click', function(){
    var e = document.getElementById("dropdown");
    var strUser = e.value;
    console.log(strUser)
    browser.runtime.sendMessage(strUser)
    //document.querySelector("#progress-bar").classList.remove("hidden");
})

////////// Listen for background script message //////////
browser.runtime.onMessage.addListener((response) => {
    if (response=="Complete"){
        document.querySelector("#progress-bar").classList.add("hidden");
    }
    if (response[0]=="PROG"){
        // Progression percent
        percent=response[1];
        percent2=percent.substring(0,response[1].length-1);
        percentFloat=parseFloat(percent2);
        // Total DL size
        sizeDL=response[2];
        sizeDLFloat=parseFloat(sizeDL.substring(0,sizeDL.length-3))
        partDL=(sizeDLFloat*percentFloat/100).toFixed(2)
        // Real-time Speed value
        valSpeed="Downloading... "+ response[3];

        // Update HTML
        document.querySelector("#prog").value=percentFloat;
        document.querySelector("#perc").textContent=partDL + " / "+ sizeDL;
        document.querySelector("#speed").textContent=valSpeed;
        // Verifier si meilleure astuce 
        document.querySelector("#progress-bar").classList.remove("hidden");
    }
    if (response[0]=="FORMAT"){
        formats=response[1]
        // Add dropdown options
        var x = document.getElementById("dropdown");
        console.log(formats)
        for(a in formats){
            console.log(formats[a])
            desc=formats[a][1]+"("+formats[a][2]+")"+" - "+formats[a][3];
            console.log(desc)
            var option = document.createElement("option");
            option.text = desc;
            x.add(option, x[-1]);
            option.value = formats[a][0]
        }
        option.selected = "selected"
        // Reveal Dropdown
        document.getElementById('load-format').classList.add("hidden");
        document.getElementById("ddMenu").classList.remove("hidden");
    }

  })
