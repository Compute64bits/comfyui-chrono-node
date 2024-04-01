from datetime import datetime
import comfy.utils

time = datetime.now()

class Chrono_reset:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return { "required": {"clip": ("CLIP",), } }

    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)

    FUNCTION = "reset"
    CATEGORY = "Chrono ⏱️"

    def reset(self, clip):
        global time
        time = datetime.now()
        return (clip,)

class Chrono_get:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return { "required": {"image": ("IMAGE",), } }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)

    FUNCTION = "get"
    CATEGORY = "Chrono ⏱️"

    def get(self, image): 
        print("⏱️ Time:", datetime.now() - time)
        return (image,)

NODE_CLASS_MAPPINGS = {
    "Chrono Reset": Chrono_reset,
    "Chrono Get": Chrono_get
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Chrono Reset": "⏱️ Reset Chrono",
    "Chrono Get": "❓ Get Chrono"
}
