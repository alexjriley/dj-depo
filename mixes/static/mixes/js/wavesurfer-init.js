document.addEventListener('DOMContentLoaded', function() {
  const waveforms = {};

  // Read theme colors from CSS variables so JS matches the CSS theme
  const _docStyles = getComputedStyle(document.documentElement);
  const _waveFill = (_docStyles.getPropertyValue('--wave-fill') || '#ccc').trim();
  const _waveProgress = (_docStyles.getPropertyValue('--wave-progress') || '#1db954').trim();
  const _cursorColor = (_docStyles.getPropertyValue('--cursor-color') || '#fff').trim();

  // Helper: convert hex color (#rgb or #rrggbb) to rgba string with alpha
  function hexToRgba(hex, alpha) {
    if (!hex) return `rgba(0,0,0,${alpha})`;
    const h = hex.replace('#', '').trim();
    if (h.length === 3) {
      const r = parseInt(h[0] + h[0], 16);
      const g = parseInt(h[1] + h[1], 16);
      const b = parseInt(h[2] + h[2], 16);
      return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }
    if (h.length === 6) {
      const r = parseInt(h.substr(0,2), 16);
      const g = parseInt(h.substr(2,2), 16);
      const b = parseInt(h.substr(4,2), 16);
      return `rgba(${r}, ${g}, ${b}, ${alpha})`;
    }
    // fallback: return original string (could be rgb/rgba already)
    return hex;
  }
  const _waveProgressRgba = hexToRgba(_waveProgress, 0.45);
  const _waveProgressRgbaStrong = hexToRgba(_waveProgress, 0.35);

  // Format seconds -> M:SS
  function formatTime(seconds) {
    if (!seconds || isNaN(seconds) || seconds <= 0) return '0:00';
    const s = Math.floor(seconds % 60);
    const m = Math.floor(seconds / 60);
    return `${m}:${s.toString().padStart(2, '0')}`;
  }

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
      // use a semi-transparent progress color so waveform detail shows through
      progressColor: _waveProgressRgba,
      cursorColor: _cursorColor,
      // increase height for better visibility and use a bar-style rendering
      height: 120,
      responsive: true,
      barWidth: 3,
      barGap: 2,
      barRadius: 2,
      normalize: true,
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
   /* use the precomputed rgba progress color so the overlay is translucent
     and blend it with the waveform using mix-blend-mode to avoid blocking
     the bar detail. multiply is a safe default; change to 'overlay' or
     'screen' if you'd like a different visual effect. */
  /* use a thin vertical gradient so the progress overlay doesn't form a
    solid rectangle — center is stronger while top/bottom are transparent */
  ${tag}::part(progress) { background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, ${_waveProgressRgbaStrong} 50%, rgba(0,0,0,0) 100%) !important; mix-blend-mode: overlay !important; }
   ${tag}::part(cursor) { background: ${_cursorColor} !important; }
   ${tag}::part(timeline) { color: ${_docStyles.getPropertyValue('--color-muted').trim() || '#6b7280'}; }
   `;

      const s = document.createElement('style');
      s.id = styleId;
      s.appendChild(document.createTextNode(css));
      document.head.appendChild(s);
    })();

    // Fallback: try to access the shadowRoot and style the internal progress element
    // directly. Some browsers (Chrome) can render parts in a way that prevents
    // blending from the outside; this attempts to set inline styles inside the
    // shadow root for best compatibility.
    (function applyShadowProgressStyles(retries = 0) {
      try {
        const host = div.firstElementChild;
        if (host && host.shadowRoot) {
          const prog = host.shadowRoot.querySelector('[part="progress"]');
          const waveEl = host.shadowRoot.querySelector('[part="wave"]');
          if (prog) {
            // apply a thin vertical gradient into the shadow DOM so the progress
            // area doesn't cover bar detail. Use a stronger center color and
            // transparent edges.
            const grad = `linear-gradient(to bottom, rgba(0,0,0,0) 0%, ${_waveProgressRgbaStrong} 50%, rgba(0,0,0,0) 100%)`;
            prog.style.background = grad;
            prog.style.mixBlendMode = 'overlay';
            prog.style.opacity = '1';
          }
          if (waveEl) {
            waveEl.style.background = _waveFill;
          }
          return;
        }
      } catch (e) {
        // ignore and retry
      }
      // retry a few times to account for rendering timing
      if (retries < 8) {
        setTimeout(() => applyShadowProgressStyles(retries + 1), 80);
      }
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
      console.debug('[wavesurfer] ready for post', id);
      // Enable the play button and set duration
      const btn = document.querySelector(`.playPause[data-post-id="${id}"]`);
      const timeEl = document.getElementById(`mix-time-${id}`);
      try {
        const duration = wavesurfer.getDuration();
        if (timeEl) timeEl.textContent = `${formatTime(0)} / ${formatTime(duration)}`;
      } catch (e) {
        // ignore
      }
      if (btn) {
        btn.disabled = false;
        btn.setAttribute('aria-pressed', 'false');
      }

      // Update on audioprocess to show elapsed time
      wavesurfer.on('audioprocess', (time) => {
        const tEl = document.getElementById(`mix-time-${id}`);
        if (tEl) {
          const dur = wavesurfer.getDuration() || 0;
          tEl.textContent = `${formatTime(time)} / ${formatTime(dur)}`;
        }
      });

      wavesurfer.on('finish', () => {
        // reset button UI when finished
        const b = document.querySelector(`.playPause[data-post-id="${id}"]`);
        if (b) {
          b.classList.remove('playing');
          b.setAttribute('aria-pressed', 'false');
          const playI = b.querySelector('.icon-play');
          const pauseI = b.querySelector('.icon-pause');
          if (playI) playI.classList.remove('d-none');
          if (pauseI) pauseI.classList.add('d-none');
        }
      });
    });

    // Attempt to load the (possibly rewritten) audio URL
    if (audioUrl) {
      wavesurfer.load(audioUrl);
      waveforms[id] = wavesurfer;
    } else {
      console.warn('[wavesurfer] no audio URL for post', id);
    }
  });

  // Track currently playing waveform
  let currentlyPlayingId = null;

  // Play/pause buttons
  document.querySelectorAll('.playPause').forEach(btn => {
    // initialize buttons disabled until corresponding wavesurfer is ready
    btn.disabled = true;
    btn.addEventListener('click', () => {
      const id = btn.dataset.postId;
      const ws = waveforms[id];

      if (!ws) {
        console.warn('[wavesurfer] No waveform found for post', id);
        return;
      }

      // Pause only the currently playing waveform if it's different
      if (currentlyPlayingId && currentlyPlayingId !== id) {
        const prevWs = waveforms[currentlyPlayingId];
        if (prevWs) prevWs.pause();
        const prevBtn = document.querySelector(`.playPause[data-post-id="${currentlyPlayingId}"]`);
        if (prevBtn) {
          prevBtn.classList.remove('playing');
          prevBtn.setAttribute('aria-pressed', 'false');
          const playI = prevBtn.querySelector('.icon-play');
          const pauseI = prevBtn.querySelector('.icon-pause');
          if (playI) playI.classList.remove('d-none');
          if (pauseI) pauseI.classList.add('d-none');
        }
      }

      ws.playPause();

      // Update button UI based on playing state
      setTimeout(() => {
        const isPlaying = ws.isPlaying();
        if (isPlaying) {
          currentlyPlayingId = id;
          btn.classList.add('playing');
          btn.setAttribute('aria-pressed', 'true');
          const playI = btn.querySelector('.icon-play');
          const pauseI = btn.querySelector('.icon-pause');
          if (playI) playI.classList.add('d-none');
          if (pauseI) pauseI.classList.remove('d-none');
        } else {
          if (currentlyPlayingId === id) currentlyPlayingId = null;
          btn.classList.remove('playing');
          btn.setAttribute('aria-pressed', 'false');
          const playI = btn.querySelector('.icon-play');
          const pauseI = btn.querySelector('.icon-pause');
          if (playI) playI.classList.remove('d-none');
          if (pauseI) pauseI.classList.add('d-none');
        }
      }, 50);
    });
  });
});
