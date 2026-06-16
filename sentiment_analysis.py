import requests, re, random
from config1 import HF_API_KEY

MODEL = "sentence-transformer/all-MiniLM-L6-v2"
API = f"https://router.huggingface.co/hf-inference/models{MODEL}"
HEAD = {"Authorization" :f"Bearer {HF_API_KEY}"}
TH = 0.72
DEMOS = [("how to delete my acount", "how do i remove my acount"),
         ("starts the game", "begin the game"),
         ("nearest hospital to me", "closest clinic near me"),
         ("mobile games are geting bigger in size", "game sizes on phones is increasing"),
         ("is it going to rain today", "today is rainy"),
         ("reset my password", "change my password")]

TOK = lambda s:" | ".join(s.split())
bar = lambda s: "█"*int(s*10) + "░"*(10-int(s*10))
clean = lambda t:[w for w in (re.sub(r"[^a-z0-9']+", "", x.lower()) for x in t.split()) if w]
nums = lambda t:set(re.findall(r"\d+(?:\.\d+)?", t))
has_any = lambda t, arr:any(a in set(clean(t)) for a in arr)
