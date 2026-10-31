import json, subprocess, os, sys
from playwright.sync_api import sync_playwright
FPS=30; OUT='/tmp/claude-0/render'
CH=json.load(open('/home/claude/reid_website/video/chapters.json'))
END=CH[-1]['start']+CH[-1]['dur']+1.5
bounds=[c['start'] for c in CH]+[END]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('http://localhost:3211/video/scenes.html',wait_until='networkidle');pg.wait_for_function('window.READY',timeout=30000)
    for i in range(len(CH)):
        f0=round(bounds[i]*FPS); f1=round(bounds[i+1]*FPS)
        tmp=f'{OUT}/s{i}.tmp.mp4'; fin=f'{OUT}/s{i}.mp4'
        if os.path.exists(fin): continue
        ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-r',str(FPS),tmp],stdin=subprocess.PIPE)
        for f in range(f0,f1):
            pg.evaluate(f'seek({f/FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
        ff.stdin.close(); rc=ff.wait()
        if rc==0: os.rename(tmp,fin)
        print('scene',i,f1-f0,'frames',rc,flush=True)
    b.close()
open(f'{OUT}/list.txt','w').write(''.join(f"file 's{i}.mp4'\n" for i in range(len(CH))))
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',f'{OUT}/list.txt','-c','copy',f'{OUT}/video.mp4'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{OUT}/video.mp4','-i','/tmp/claude-0/tts/soundtrack.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',f'{OUT}/reid-explainer.mp4'],check=True)
print('DONE',flush=True)
