"""Capture the 64 official website previews using a real Chromium browser.
Run: pip install playwright && playwright install chromium && python capture_screenshots.py
"""
import asyncio, json, pathlib, time
from playwright.async_api import async_playwright
ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT/'screenshots'
OUT.mkdir(exist_ok=True)
async def main():
    results=[]
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,args=['--disable-dev-shm-usage'])
        home=await browser.new_page()
        await home.goto((ROOT/'index.html').as_uri(),wait_until='domcontentloaded')
        venues=await home.evaluate('items.map(x=>({id:x.id,name:x.name,url:x.url}))')
        await home.close()
        print(f'Found {len(venues)} venues')
        for v in venues:
            target=OUT/f"{int(v['id']):02d}.jpg"
            if target.exists() and target.stat().st_size>8000:
                results.append({**v,'status':'existing','bytes':target.stat().st_size})
                continue
            page=await browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1,locale='en-US')
            try:
                response=await page.goto(v['url'],wait_until='domcontentloaded',timeout=25000)
                if response and response.status>=400:raise RuntimeError(f'HTTP {response.status}')
                await page.wait_for_timeout(1600)
                await page.screenshot(path=str(target),type='jpeg',quality=80,full_page=False,timeout=15000,animations='disabled')
                if target.stat().st_size<8000:
                    target.unlink(missing_ok=True)
                    raise RuntimeError('Screenshot suspiciously small')
                print('OK',v['name'],target.stat().st_size)
                results.append({**v,'status':'captured','bytes':target.stat().st_size})
            except Exception as e:
                target.unlink(missing_ok=True)
                print('FAILED',v['name'],str(e)[:180])
                results.append({**v,'status':'failed','error':str(e)[:300]})
            finally:
                await page.close()
        await browser.close()
    (OUT/'report.json').write_text(json.dumps(results,indent=2))
    print('Captured or existing:',sum(r['status']!='failed' for r in results),'/',len(results))
if __name__=='__main__':asyncio.run(main())
