export async function chat(message) {
  const base = import.meta.env.VITE_API_URL;
  console.log('[api.js] Sending POST to', base + '/chat/', 'with message:', message);

  const res = await fetch(base + '/chat/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  console.log('[api.js] Response status:', res.status);

  if (!res.ok) {
    const text = await res.text();
    console.error('[api.js] Error response body:', text);
    throw new Error('Server error');
  }

  const json = await res.json();
  console.log('[api.js] Response JSON:', json);
  return json;
}
