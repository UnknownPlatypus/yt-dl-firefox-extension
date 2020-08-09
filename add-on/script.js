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


// Listen for background script message
browser.runtime.onMessage.addListener((response) => {
    if (response=="Complete"){
        document.querySelector("#progress-bar").classList.add("hidden");
    }
    if (response[0]=="PROG"){
        percent=response[1];
        percentFloat=percent.substring(0,response[1].length-1);
        float_val=parseFloat(percentFloat);
        sizeDL=response[2];
        sizeDLFloat=sizeDL.substring(0,sizeDL-3)
        valSpeed="Downloading... "+ response[3];
        document.querySelector("#prog").value=float_val;
        document.querySelector("#perc").innerHTML=percent + " / "+ sizeDL;
        document.querySelector("#speed").innerHTML=valSpeed;
    }

  })
