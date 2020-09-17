// Addon Opt-in actions
window.addEventListener("load", function() {
    // set up the appearance of the popup depending on the outcome of the opt-in
    browser.storage.local.get("optInShown", function(result) {
      console.log("Setting up UI. result.optInShown:" + result.optInShown);
      document.getElementById("opt-in-prompt").hidden = result.optInShown;
      document.getElementById("after-opt-in").hidden = !result.optInShown;
    });
  
    document.getElementById("button-enable").addEventListener(
      "click",
      function() {
        browser.storage.local.set({ "optIn" : true, "optInShown" : true });
        window.close();
    });
  
    document.getElementById("button-cancel").addEventListener(
      "click",
      function() {
        browser.storage.local.set({ "optIn" : false, "optInShown" : false });
        window.close();
    });
  });

////////// Plugin Event listeners //////////
// 3 Main formats
document.getElementById('audio_M4a').addEventListener('click', function(){
    browser.runtime.sendMessage("m4a");
    document.getElementById("aux").classList.add("hidden");
    document.querySelector("p").classList.add("hidden");
    document.querySelector("#progress-bar").classList.remove("hidden");
})
document.getElementById('audio_mp3').addEventListener('click', function(){
    browser.runtime.sendMessage("mp3");
    document.getElementById("aux").classList.add("hidden");
    document.querySelector("p").classList.add("hidden");
    document.querySelector("#progress-bar").classList.remove("hidden");
})
document.getElementById('video').addEventListener('click', function(){
    browser.runtime.sendMessage("mp4");
    document.getElementById("aux").classList.add("hidden");
    document.querySelector("p").classList.add("hidden");
    document.querySelector("#progress-bar").classList.remove("hidden");
})

// Other formats
document.getElementById('format').addEventListener('click', function(){
    browser.runtime.sendMessage("format");
    document.getElementById('load-format').classList.remove("hidden");
    document.getElementById('format').classList.add("hidden");    
})
document.getElementById('DL').addEventListener('click', function(){
    var e = document.getElementById("dropdown");
    var strUser = e.value;
    console.log(strUser)
    browser.runtime.sendMessage(strUser)
    document.querySelector("#main").classList.remove("buttons");
    document.querySelector("#main").classList.add("hidden");
    document.querySelector("p").classList.add("hidden");
    document.querySelector("#progress-bar").classList.remove("hidden");
})

////////// Listen for background script message //////////
browser.runtime.onMessage.addListener((response) => {
    if (response=="Complete"){
        document.querySelector("#progress-bar").classList.add("hidden");
    }
    if (response[0]=="PROG"){
        console.log(response)
        // Progression percent
        percent = response[1];
        percent2 = percent.substring(0,response[1].length-1);
        percentFloat=parseFloat(percent2);
        // Total DL size
        sizeDL = response[2];
        sizeDLFloat = parseFloat(sizeDL.substring(0,sizeDL.length-3))
        partDL = (sizeDLFloat*percentFloat/100).toFixed(2)
        // Real-time Speed value
        speedDL=response[3]
        if(speedDL!=null){
            valSpeed="Downloading... "+ speedDL;
        }
        

        // Update HTML
        document.querySelector("#prog").value=percentFloat;
        document.querySelector("#perc").textContent=partDL + " / "+ sizeDL;
        document.querySelector("#speed").textContent=valSpeed;
        // Verifier si meilleure astuce 
        document.querySelector("#progress-bar").classList.remove("hidden");
    }
    if (response[0]=="FORMAT"){
        formats = response[1]
        // Add dropdown options
        var x = document.getElementById("dropdown");
        
        for(a in formats){
            //console.log(formats[a])
            desc = formats[a][1]+" ("+formats[a][2]+")"+" - "+formats[a][3];
            console.log(desc)
            var option = document.createElement("option");
            option.text = desc;
            x.add(option, x[0]);
            option.value = formats[a][0]
        }
        option.selected = "selected"
        // Reveal Dropdown
        document.getElementById('load-format').classList.add("hidden");
        document.getElementById("ddMenu").classList.remove("hidden");
    }

  })


