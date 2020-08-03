/*
On startup, connect to the 'firefox_command_runner' app.
*/
console.log('Starting firefox command runner!')
var port = browser.runtime.connectNative('firefox_command_runner');

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("Received: " + response);
  browser.notifications.create({
    'type': 'basic',
    'iconUrl': browser.extension.getURL('icons/YTIcon.png'),
    'title': 'Download Completed !',
    'message': response,
  });
});

/*
Listen for messages from the content script.
*/

browser.runtime.onMessage.addListener(function(message) {
  //console.log('getting tab url : ' + tab.url);
  console.log('getting button message :' + message)
  function logTabs(tabs) {
    let tab = tabs[0]; // Safe to assume there will only be one result
    console.log(tab.url);
  port.postMessage(message+tab.url)
} browser.tabs.query({currentWindow: true, active: true}).then(logTabs, console.error);
  //port.postMessage(tab.url);
});


/*
On a click on the browser action, send the app a message.

browser.browserAction.onClicked.addListener(function(tab) {
  console.log('getting tab url : ' + tab.url);
  port.postMessage(tab.url);
});
*/


/*
Log that we received the message.
Then display a notification. The notification contains the URL,
which we read from the message.

function notify(message) {
  console.log('background script received message');
  browser.notifications.create({
    'type': 'basic',
    'iconUrl': browser.extension.getURL('icons/message.svg'),
    'title': 'Received Message from Backend!',
    'message': message,
  });
}
*/