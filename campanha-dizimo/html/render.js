const { chromium } = require('playwright');
const path = require('path');

const jobs = [
  { file: 'feed-01-capa.html', out: 'feed-01-capa.png', w: 1080, h: 1350 },
  { file: 'feed-02-liturgia.html', out: 'feed-02-liturgia.png', w: 1080, h: 1350 },
  { file: 'feed-03-catequese.html', out: 'feed-03-catequese.png', w: 1080, h: 1350 },
  { file: 'feed-04-comunidade.html', out: 'feed-04-comunidade.png', w: 1080, h: 1350 },
  { file: 'feed-05-cta.html', out: 'feed-05-cta.png', w: 1080, h: 1350 },
  { file: 'story-1-hook.html', out: 'story-1-hook.png', w: 1080, h: 1920 },
  { file: 'story-2-beneficios.html', out: 'story-2-beneficios.png', w: 1080, h: 1920 },
  { file: 'story-3-cta.html', out: 'story-3-cta.png', w: 1080, h: 1920 },
];

(async () => {
  const browser = await chromium.launch();
  const outDir = path.join(__dirname, '..', 'imagens');
  for (const job of jobs) {
    const page = await browser.newPage({ viewport: { width: job.w, height: job.h }, deviceScaleFactor: 1 });
    const fileUrl = 'file://' + path.join(__dirname, job.file);
    await page.goto(fileUrl, { waitUntil: 'networkidle' });
    await page.evaluate(async () => { await document.fonts.ready; });
    await page.waitForTimeout(150);
    await page.screenshot({ path: path.join(outDir, job.out) });
    await page.close();
    console.log('rendered', job.out);
  }
  await browser.close();
})();
