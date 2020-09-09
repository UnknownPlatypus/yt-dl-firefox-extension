document.getElementById('audio_M4a').addEventListener('click', function(){
    browser.runtime.sendMessage("m4a");
    document.querySelector("#progress-bar").classList.remove("hidden");
})
document.getElementById('audio_mp3').addEventListener('click', function(){
    browser.runtime.sendMessage("mp3");
    document.querySelector("#progress-bar").classList.add("hidden");
})
document.getElementById('video').addEventListener('click', function(){
    browser.runtime.sendMessage("mp4")
})
document.getElementById('format').addEventListener('click', function(){
    //browser.runtime.sendMessage("m4a");
    var x = document.getElementById("dropdown");
    var option = document.createElement("option");
    option.text = "Kiwi";
    
    x.add(option, x[0]);
})

// Listen for background script message
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

  })
