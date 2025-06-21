import { createSignal } from 'solid-js';
import { chat } from './lib/api';
import './index.css';

function App() {
  const [messages, setMessages] = createSignal([]);
  const [input, setInput] = createSignal('');
  let chatboxRef;

  // ⬇️  Fixed: only add the user once, then add the bot
  const sendMessage = async () => {
    const text = input().trim();
    if (!text) return;

    // 1️⃣ add user bubble once
    setMessages(m => [...m, { role: 'user', content: text }]);
    setInput('');

    try {
      const res = await chat(text);

      // 2️⃣ add bot reply only
      setMessages(m => [...m, { role: 'bot', content: res.reply }]);

      // auto‑scroll to bottom
      setTimeout(() => {
        if (chatboxRef) chatboxRef.scrollTop = chatboxRef.scrollHeight;
      });
    } catch (err) {
      console.error(err);
      setMessages(m => [
        ...m,
        { role: 'bot', content: '❌ Could not reach server' }
      ]);
    }
  };

  return (
    <div class="chat-container">
      <h1>🤖 AI Chatbot</h1>

      <div class="chat-box" ref={el => (chatboxRef = el)}>
        {messages().map((msg, i) => (
          <div class={`message ${msg.role}`} key={i}>
            <div class="bubble">{msg.content}</div>
          </div>
        ))}
      </div>

      <div class="input-area">
        <input
          type="text"
          placeholder="Type your message..."
          value={input()}
          onInput={e => setInput(e.currentTarget.value)}
          onKeyDown={e => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
