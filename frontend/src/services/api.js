const API_URL = "http://127.0.0.1:8001";

export async function analyze(question) {
  const response = await fetch(`${API_URL}/api/analyze`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Request failed.");
  }

  return data;
}

export async function health() {
  const response = await fetch(`${API_URL}/api/health`);

  if (!response.ok) {
    throw new Error("Backend is unavailable.");
  }

  return response.json();
}
