class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            voiceButton: document.getElementById('voiceButton') // Add the voice button here
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton, voiceButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
                this.onSendButton(chatBox);
            }
        });

        // Add voice button event listener
        if (voiceButton) {
            voiceButton.addEventListener('click', () => this.onVoiceInput(chatBox));
        }
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if (this.state) {
            chatbox.classList.add('chatbox--active');
        } else {
            chatbox.classList.remove('chatbox--active');
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch($SCRIPT_ROOT + '/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(r => r.json())
        .then(r => {
            let msg2 = { name: "Sam", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox);
            textField.value = '';
        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox);
            textField.value = '';
        });
    }

    // Voice input handler
    onVoiceInput(chatbox) {
        if (!('webkitSpeechRecognition' in window)) {
            alert("Your browser doesn't support speech recognition. Please try a different browser.");
            return;
        }

        var recognition = new webkitSpeechRecognition();
        recognition.lang = "en-US";
        recognition.interimResults = false;

        recognition.onstart = function() {
            console.log("Voice recognition started. Speak now...");
        };

        recognition.onresult = (event) => {
            var transcript = event.results[0][0].transcript;
            console.log("Recognized text: " + transcript);
            chatbox.querySelector('input').value = transcript;  // Fill the input box with recognized text
            this.onSendButton(chatbox);  // Send the message just like text input
        };

        recognition.onerror = function(event) {
            console.error("Error occurred in recognition: " + event.error);
            alert("An error occurred during voice recognition. Please try again.");
        };

        recognition.onend = function() {
            console.log("Voice recognition ended.");
        };

        recognition.start();
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>';
            } else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display();
