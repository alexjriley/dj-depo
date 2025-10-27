document.addEventListener('DOMContentLoaded', function() {
  const waveforms = {};

  // Select all waveform containers rendered by Django
  document.querySelectorAll('[data-audio-url]').forEach(div => {
    const id = div.dataset.postId;
    const audioUrl = div.dataset.audioUrl;

    const wavesurfer = WaveSurfer.create({
      container: div,
      waveColor: '#ccc',
      progressColor: '#1db954',
      cursorColor: '#fff',
      height: 80,
      responsive: true,
    });

    wavesurfer.load(audioUrl);
    waveforms[id] = wavesurfer;
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
