document.addEventListener('DOMContentLoaded', function() {
  const waveforms = {};

  // Read theme colors from CSS variables so JS matches the CSS theme
  const _docStyles = getComputedStyle(document.documentElement);
  const _waveFill = (_docStyles.getPropertyValue('--wave-fill') || '#ccc').trim();
  const _waveProgress = (_docStyles.getPropertyValue('--wave-progress') || '#1db954').trim();
  const _cursorColor = (_docStyles.getPropertyValue('--color-bg') || '#fff').trim();

  // Select all waveform containers rendered by Django
  document.querySelectorAll('[data-audio-url]').forEach(div => {
    const id = div.dataset.postId;
    let audioUrl = div.dataset.audioUrl;

    // Quick fix for mixed-content: force HTTPS if an HTTP URL was stored.
    // This prevents browsers from blocking the fetch when the page is HTTPS.
    if (audioUrl && audioUrl.startsWith('http://')) {
      console.warn('[wavesurfer] replacing insecure audio URL with HTTPS for post', id, audioUrl);
      audioUrl = audioUrl.replace(/^http:\/\//i, 'https://');
    }

    const wavesurfer = WaveSurfer.create({
      container: div,
      waveColor: _waveFill,
      progressColor: _waveProgress,
      cursorColor: _cursorColor,
      height: 80,
      responsive: true,
    });

    // Inject ::part() CSS rules for the wavesurfer host so theme colors apply
    // (wavesurfer v7 renders into a Shadow DOM; ::part() allows styling.
    // We generate rules dynamically based on the host tag so the CSS works
    // regardless of the custom element name.)
    (function injectPartStyles() {
      // Find the shadow host inserted by WaveSurfer inside our container
      const host = div.firstElementChild;
      if (!host || !host.tagName) return;

      const tag = host.tagName.toLowerCase();
      const styleId = `wavesurfer-parts-${tag}`;
      if (document.getElementById(styleId)) return; // already injected

      const css = `
${tag}::part(wave) { background: ${_waveFill} !important; }
${tag}::part(progress) { background: ${_waveProgress} !important; }
${tag}::part(cursor) { background: ${_cursorColor} !important; }
${tag}::part(timeline) { color: ${_docStyles.getPropertyValue('--color-muted').trim() || '#6b7280'}; }
`;

      const s = document.createElement('style');
      s.id = styleId;
      s.appendChild(document.createTextNode(css));
      document.head.appendChild(s);
    })();

    // Surface load errors in console and show a minimal fallback UI
    wavesurfer.on('error', err => {
      console.error('[wavesurfer] error loading waveform for post', id, err);
      // Add a small fallback message if not already present
      if (!div.querySelector('.wave-error')) {
  const msg = document.createElement('div');
  msg.className = 'wave-error';
  msg.textContent = 'Waveform unavailable — click play to listen.';
  msg.style.color = (_docStyles.getPropertyValue('--color-muted') || '#bbb').trim();
  msg.style.fontSize = '0.9rem';
  msg.style.marginTop = '0.5rem';
  div.appendChild(msg);
      }
    });

    wavesurfer.on('ready', () => {
      // ready — nothing special for now, but helpful if you want to
      // enable UI controls for duration, etc.
      console.debug('[wavesurfer] ready for post', id);
    });

    // Attempt to load the (possibly rewritten) audio URL
    if (audioUrl) {
      wavesurfer.load(audioUrl);
      waveforms[id] = wavesurfer;
    } else {
      console.warn('[wavesurfer] no audio URL for post', id);
    }
  });

  // Play/pause buttons
  document.querySelectorAll('.playPause').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.postId;
      const ws = waveforms[id];

      // Optional: pause all others first
      for (const key in waveforms) {
        if (parseInt(key) !== parseInt(id)) {
          waveforms[key].pause();
        }
      }

      ws.playPause();
    });
  });
});
