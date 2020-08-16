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


// Addon button actions
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


