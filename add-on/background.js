/*
On startup, connect to the 'firefox_command_runner' app.
*/
console.log('Starting firefox command runner!')
var port = browser.runtime.connectNative('firefox_command_runner');

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("Received: ");
  console.log(response);
  if(response[0]=="END"){
  browser.notifications.create({
    'type': 'basic',
    'iconUrl': browser.extension.getURL('icons/YTIcon.png'),
    'title': 'Download Completed !',
    'message': response[1],
  });
  browser.runtime.sendMessage("Complete")
}
  else if(response[0]=="PROG" && response[1][2]=="of"){
    values=["PROG",response[1][1],response[1][3],response[1][5]]
    browser.runtime.sendMessage(values)
  }
});

/*
Listen for messages from the content script.
*/

browser.runtime.onMessage.addListener(function(message) {
  if(message!="Complete"){
    console.log('getting button message :' + message)
    function logTabs(tabs) {
      let tab = tabs[0]; // Safe to assume there will only be one result
      console.log(tab.url);
    port.postMessage(message+tab.url)
    } 
  browser.tabs.query({currentWindow: true, active: true}).then(logTabs, console.error);
  } 
});