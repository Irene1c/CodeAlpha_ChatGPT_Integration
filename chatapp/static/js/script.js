const socket = io('/chat');
const chats = document.getElementById('chat-messages');
const messageInput = document.getElementById('message');
const sendBtn = document.getElementById('send-button');

function displayUserMessage (message) {
  chats.innerHTML += `
    <div id="user-message">${message}</div>
    `;
}

function displayResponseMessage (response) {
  chats.innerHTML += `
    <div id="response-message">${response}</div>
    `;
}

function sendMessage (event) {
  event.preventDefault();

  const message = messageInput.value.trim();
  if (message !== '') {
        socket.emit('message', { message: message });
        messageInput.value = '';
        displayUserMessage(message);
    } else {
        alert('Please enter a message.');
    }
}

socket.on('response', function(data) {
    const response = data.message;
    displayResponseMessage(response);
});

sendBtn.addEventListener('click', sendMessage);
