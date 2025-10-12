const apiBase = location.origin.replace(/:\d+$/, ':8000') + '/api'; // adjust if needed
const tbody = document.querySelector('#leaderboard tbody');
const gameInput = document.getElementById('gameInput');
const refreshBtn = document.getElementById('refresh');

async function loadLeaderboard() {
  const gameId = gameInput.value || '1';
  document.getElementById('gameId').textContent = gameId;
  try {
    // expects endpoint /api/games/{id}/leaderboard/?top=10
    const res = await fetch(`${apiBase}/games/${gameId}/leaderboard/?top=10`);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const data = await res.json();
    tbody.innerHTML = '';
    data.forEach((row, idx) => {
      const tr = document.createElement('tr');
      tr.innerHTML = `<td>${idx+1}</td>
                      <td>${row.player_name || row.player}</td>
                      <td>${row.score}</td>
                      <td>${new Date(row.created_at || row.date).toLocaleString()}</td>`;
      tbody.appendChild(tr);
    });
  } catch (e) {
    tbody.innerHTML = `<tr><td colspan="4">Error loading: ${e.message}</td></tr>`;
  }
}

refreshBtn.addEventListener('click', loadLeaderboard);
loadLeaderboard();
