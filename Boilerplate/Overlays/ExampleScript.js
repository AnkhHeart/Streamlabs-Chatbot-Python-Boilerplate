var Overlay = {

	//---------------------------------
	// HTML Elements
	//---------------------------------
	myEvent = document.getElementById('my_event'),
	lastEvent = document.getElementById('last_event'),

	Listen = function() {

		this.socket = new WebSocket('ws://127.0.0.1:3337/streamlabs');

		//---------------------------------
		// Open Event
		//---------------------------------
		this.socket.onopen = function() {
			// Format your Authentication Information
			var auth = {
				author = 'YOUR_NAME',
				website = 'YOUR_SITE',
				api_key = API_Key,
				events = ['EVENT_MINE']
			}
			// Send your Data to the server
			this.socket.send(JSON.stringify(auth));
		}

		//---------------------------------
		// Error Event
		//---------------------------------
		this.socket.onerror = function(error) {
			// Something went terribly wrong... Respond?!
			console.log('Error: ' + error);
		}

		//---------------------------------
		// Message Event
		//---------------------------------
		this.socket.onmessage = function(message) {
			var json = JSON.parse(message);
			if(json.event == 'EVENT_MINE') {
				Overlay.myEvent.innerText = json.data;
			} else {
				Overlay.lastEvent.innerText = json.data;
			}

			// You have received new data now process it
			console.log(message);
		}

		//---------------------------------
		// Close Event
		//---------------------------------
		this.socket.onclose = function() {
			// Connection has been closed by you or the server
			console.log('Connection Closed!');
		}
	}
}

//---------------------------------
// API KEY Check
//---------------------------------
if (typeof API_Key === "undefined") {
	document.body.innerHTML = "No API Key found!<br>Right-click on the script in Streamlabs Chatbot and select \"Insert API Key\"";
	document.body.style.cssText = "font-family: sans-serif; font-size: 20pt; font-weight: bold; color: rgb(255, 22, 23); text-align: center;";
	throw new Error("API Key not loaded or missing.");
}

// Start Script
Overlay.Listen();
