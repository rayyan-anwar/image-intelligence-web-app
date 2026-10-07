import hashlib
import numpy as np
def analyze(image):
    a=np.asarray(image.convert("RGB"),dtype=float)/255
    return {"author":"Rayyan Anwar","width":image.width,"height":image.height,"aspect_ratio":round(image.width/image.height,4),"mean_brightness":float(a.mean()),"contrast_std":float(a.std()),"fingerprint":hashlib.sha256(a.tobytes()).hexdigest()[:16]}
def compare(a,b):
    x=np.asarray(a.convert("RGB").resize((64,64)),dtype=float)
    y=np.asarray(b.convert("RGB").resize((64,64)),dtype=float)
    d=float(np.mean(np.abs(x-y)))
    return {"author":"Rayyan Anwar","distance":d,"similarity":max(0,1-d/255)}
