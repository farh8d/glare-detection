from torchvision import transforms
import onnxruntime
import numpy as np 
from PIL import Image


class Glare:
    def __init__(self , model_path):  
        self.sz = 420
        self.model = onnxruntime.InferenceSession(model_path)   


        self.transforms =  transforms.Compose([
            transforms.Resize((self.sz, self.sz)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])


    def run(self , imgAddr):  # return true -> has glare  | false -> no-glare
        img = Image.open(imgAddr).convert('RGB')
        img = self.transforms(img)
        img = np.array(img)

        img = np.expand_dims(img, 0).astype(np.float32)
    
        ort_outs = self.model.run(None, {"input":img})
        return bool(1 - np.argmax(ort_outs))

        

