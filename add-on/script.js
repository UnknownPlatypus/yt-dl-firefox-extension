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
    document.querySelector("#progress-bar").classList.add("hidden");}
  })
