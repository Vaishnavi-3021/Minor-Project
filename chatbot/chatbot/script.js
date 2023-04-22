const chatContainer = document.querySelector('.chat-container');
const messages = document.querySelector('.messages');
const inputBox = document.querySelector('#chat-input-box');
const sendBtn = document.querySelector('#send-btn');

sendBtn.addEventListener('click', sendMessage);

function sendMessage() {
  const userMessage = inputBox.value;
  if (userMessage.trim() === '') return;
  const messageHTML = `
    <div class="message user">
      <span>${userMessage}</span>
    </div>
  `;
  messages.innerHTML += messageHTML;
  inputBox.value = '';
  scrollToBottom();
  getBotResponse(userMessage);
}

function getBotResponse(message) {
  // Make a request to your backend API with the message parameter
  // Receive and parse the response from the backend API
  // Use the response data to create an HTML element for the bot message
  const botMessage = 'This is a dummy bot response';
  const messageHTML = `
    <div class="message bot">
      <span>${botMessage}</span>
    </div>
  `;
  setTimeout(() => {
    messages.innerHTML += messageHTML;
    scrollToBottom();
  }, 1000);
}

function scrollToBottom() {
  messages.scrollTop = messages.scrollHeight;
}
