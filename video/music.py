import numpy as np, soundfile as sf
sr=24000; v,_=sf.read('voice.wav'); N=len(v)+int(sr*1.5); t=np.arange(N)/sr
def env(x,a,r): return np.minimum(1,x/a)*np.exp(-x/r)
mus=np.zeros(N)
chords=[[220,277.18,329.63,415.3],[196,246.94,293.66,369.99],[174.61,220,261.63,329.63],[196,246.94,293.66,392]]
bar=4.0
for i,b0 in enumerate(np.arange(0,N/sr,bar)):
    ch=chords[i%4]; s=int(b0*sr); L=min(N-s,int(bar*1.6*sr)); x=np.arange(L)/sr
    for f in ch:
        mus[s:s+L]+=0.05*np.sin(2*np.pi*f/2*x)*env(x,1.2,3.5)
        mus[s:s+L]+=0.02*np.sin(2*np.pi*f*x+np.sin(2*np.pi*.3*x))*env(x,1.5,3.0)
    for k,f in enumerate(ch*2):
        st=s+int(k*bar/8*sr)
        if st>=N: break
        l=min(N-st,int(1.2*sr)); xx=np.arange(l)/sr
        mus[st:st+l]+=0.035*np.sin(2*np.pi*f*2*xx)*np.exp(-xx*3)*(1-np.exp(-xx*200))
mus/=np.abs(mus).max()
vv=np.zeros(N); vv[:len(v)]=v
e=np.convolve(np.abs(vv),np.ones(int(sr*.4))/int(sr*.4),'same'); duck=1-0.55*np.clip(e/0.04,0,1)
fade=np.minimum(1,np.minimum(t/2,(N/sr-t)/2.5))
mix=vv*1.0+mus*0.2*duck*fade
mix/=np.abs(mix).max()/0.92
sf.write('soundtrack.wav',mix,sr); print(N/sr)
