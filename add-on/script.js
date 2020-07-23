document.getElementById('audio_M4a').addEventListener('click', function(){
    browser.runtime.sendMessage("m4a")
})
document.getElementById('audio_mp3').addEventListener('click', function(){
    browser.runtime.sendMessage("mp3")
})
document.getElementById('video').addEventListener('click', function(){
    browser.runtime.sendMessage("mp4")
})

