# reID explainer video

- `voice.py` — narration script + Kokoro TTS (voice `af_heart`, model files from thewh1teagle/kokoro-onnx v1.0). Writes `voice.wav` and `chapters.json`.
- `music.py` — soft ambient piano/pad, ducked under the voice → `soundtrack.wav`.
- `scenes.html` + `render.js` — 1920×1080 animated scenes on one paused GSAP timeline (`seek(t)`), captions burned in.
- `render.py` — Playwright renders 30 fps per scene, ffmpeg joins and adds the soundtrack.
- Output used by the site: `assets/video/reid-explainer.mp4` (720p web copy) and `reid-explainer-poster.jpg`.
