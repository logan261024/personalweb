const video = document.querySelector('#birthday-video');
const status = document.querySelector('#video-status');
video.addEventListener('play', () => { status.textContent = '正在播放 · 这一岁，值得珍藏。'; });
video.addEventListener('pause', () => { if (!video.ended) status.textContent = '已暂停 · 随时继续这一段回忆。'; });
video.addEventListener('ended', () => { status.textContent = '故事未完待续。可以再次播放。'; });
video.addEventListener('error', () => { status.textContent = '视频暂时无法播放，请尝试打开原片。'; });
