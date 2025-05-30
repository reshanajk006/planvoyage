document.getElementById('trip-form').addEventListener('submit', async function (e) {
  e.preventDefault();
  const location = document.getElementById('location').value.trim();
  const days = document.getElementById('days').value.trim();
  const budget = document.getElementById('budget').value.trim();
  const resultDiv = document.getElementById('generated-plan');
  const resultSection = document.getElementById('trip-result');

  if (!location || !days || !budget) {
    resultDiv.textContent = 'Please fill in all fields.';
    resultSection.style.display = 'block';
    return;
  }

  resultDiv.textContent = 'Generating your travel plan...';
  resultSection.style.display = 'block';

  try {
    const response = await fetch('/trip-plan', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ location, days, budget })
    });

    const data = await response.json();

    if (data.error) {
      resultDiv.textContent = `Error: ${data.error}`;
    } else {
      resultDiv.innerHTML = data.plan;
    }
  } catch (err) {
    resultDiv.textContent = `Fetch error: ${err.message}`;
  }
});
