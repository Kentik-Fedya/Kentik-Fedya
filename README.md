<style>
  img { border: none !important; outline: none !important; box-shadow: none !important; }
  a { border: none !important; outline: none !important; box-shadow: none !important; }
  table { border: none !important; outline: none !important; }
  td { border: none !important; outline: none !important; box-shadow: none !important; }
</style>

<!-- 1. ВЕРХ: Анимированный macOS Терминал zsh -->
<p align="center">
  <img src="terminal.svg" width="100%" alt="Terminal UI">
</p>

<!-- 2. ЦЕНТР: Два горизонтальных окна 50/50 (Аватар + Музыкальный Плеер) -->
<table align="center" border="0" cellspacing="0" cellpadding="0" style="border: none; background: transparent; width: 100%;">
  <tr style="border: none; background: transparent;">
    <td width="50%" align="center" style="border: none; background: transparent; padding: 10px; outline: none; box-shadow: none;">
      <a href="#" style="border: none; outline: none; box-shadow: none;">
        <!-- Твой Ultra-HD ASCII Аватар -->
        <img src="avatar.svg" width="90%" alt="ASCII Avatar" style="border: none; outline: none; box-shadow: none; display: block;">
      </a>
    </td>
    <td width="50%" align="center" style="border: none; background: transparent; padding: 10px; outline: none; box-shadow: none;">
      <a href="#" style="border: none; outline: none; box-shadow: none;">
        <!-- Твой Киберпанк Музыкальный Плеер с Эквалайзером -->
        <img src="player.svg" width="90%" alt="Music Player" style="border: none; outline: none; box-shadow: none; display: block;">
      </a>
    </td>
  </tr>
</table>

<!-- 3. НИЗ: Кастомный счетчик просмотров профиля с киберпанк стилем -->
<p align="center">
  <svg width="200" height="50" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="neon" x1="0%" y1="0%" x2="100%">
        <stop offset="0%" style="stop-color:#00FF41;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#00CC33;stop-opacity:1" />
      </linearGradient>
      <filter id="glow">
        <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
        <feMerge>
          <feMergeNode in="coloredBlur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>
    <!-- Фон -->
    <rect width="200" height="50" fill="#000000" rx="4"/>
    <!-- Неоновая граница -->
    <rect width="200" height="50" fill="none" stroke="#00FF41" stroke-width="1.5" rx="4" filter="url(#glow)"/>
    <!-- Текст -->
    <text x="100" y="32" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#00FF41" text-anchor="middle" filter="url(#glow)">PROFILE VIEWS: 0</text>
  </svg>
</p>
