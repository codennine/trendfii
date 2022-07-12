chrome.runtime.onInstalled.addListener(() => {
  console.log('extension installed!');
  console.log(chrome);
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  console.log("sent from tab.id=", sender.tab.id);
  console.log(chrome.scripting);
  chrome.scripting.insertCSS({
    files: ['./informe-trimestral.css'],
    target: {tabId: sender.tab.id}
  }, function(...args) {console.log('inserted', args);});
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status == 'complete' && tab.active) {
    console.log('dispatching request... to get data');
    console.log({tabId, tab});
  }
});
