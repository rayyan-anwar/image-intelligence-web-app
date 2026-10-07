from PIL import Image
from backend.app.image_engine import analyze,compare
def test_analysis(): assert analyze(Image.new("RGB",(20,10)))["author"]=="Rayyan Anwar"
def test_compare(): assert compare(Image.new("RGB",(20,20)),Image.new("RGB",(20,20)))["similarity"]==1
