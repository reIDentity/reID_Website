import json, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k = Kokoro("kokoro-v1.0.int8.onnx", "voices-v1.0.bin")
S = [
 ("intro","Meet reID.","Meet reID. One digital identity, for everything you do online. Sign in, verify, pay, share, and earn, with one secure passport."),
 ("individual","For you","For individuals, reID ends passwords. Sign in with a passkey, your wallet, or a social account. Verify your identity once, and every connected app trusts it. Hold cash and crypto in one wallet, and pay anyone by their name, like sam at reID, instead of a long address."),
 ("privacy","Virtual ID","Create a Virtual ID for anything. One for shopping, one for travel, one for your family. Each gets its own email, phone number, eSIM, and debit card, so your real details always stay private."),
 ("freelancer","For freelancers","For freelancers, reID is your verified business card. Share your profile with one QR code. Chat with clients who are verified too, and get paid right inside the conversation. Keep a separate Virtual ID for work, with its own card for tools and subscriptions."),
 ("business","For business","For businesses, there's reCorporate. One corporate account for your verified merchant identity, your team, roles and permissions, salaries, payments, and fiat and crypto accounts. Add Sign in with reID to your own app, and welcome verified customers without sign-up forms."),
 ("earn","Earn extra","And reID pays you back. Earn cashback on every eligible purchase. Invite friends with your QR code, and earn from your legacy network, across unlimited levels. Want more? Become a reID Ambassador, launch your own storefront, and earn commissions on everyone you bring in."),
 ("features","Everything unlocked","Everything is unlocked by one reID. Wallet, fiat account, virtual cards and eSIM, contact sharing, chat, cashback, your legacy network, and your corporate account."),
 ("cta","Get started","One identity, for everything. Get your reID today, at reidentity dot net."),
]
GAP=0.55
out=[]; t=0.0; sr=24000; chunks=[]
for key,title,text in S:
    a,sr=k.create(text, voice="af_heart", speed=0.97, lang="en-us")
    a=a.astype(np.float32)
    lead=np.zeros(int(sr*0.35),np.float32); tail=np.zeros(int(sr*GAP),np.float32)
    seg=np.concatenate([lead,a,tail]); dur=len(seg)/sr
    out.append({"key":key,"title":title,"text":text,"start":round(t,3),"dur":round(dur,3)})
    chunks.append(seg); t+=dur
v=np.concatenate(chunks); sf.write("voice.wav",v,sr)
json.dump(out,open("chapters.json","w"),indent=1)
print(round(t,2)); [print(c["key"],c["start"],c["dur"]) for c in out]
