from datetime import datetime
import comfy.utils

time = datetime.now()

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

class Chrono_reset:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return { "required": {"any": (AnyType("*"),), } }

    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("out",)

    FUNCTION = "reset"
    CATEGORY = "Chrono ⏱️"

    def reset(self, any):
        global time
        time = datetime.now()
        return (any,)

class Chrono_get:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return { "required": {"any": (AnyType("*"),), } }

    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("out",)

    FUNCTION = "get"
    CATEGORY = "Chrono ⏱️"

    def get(self, any): 
        print("⏱️ Time:", datetime.now() - time)
        return (any,)

NODE_CLASS_MAPPINGS = {
    "Chrono Reset": Chrono_reset,
    "Chrono Get": Chrono_get
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Chrono Reset": "⏱️ Reset Chrono",
    "Chrono Get": "❓ Get Chrono"
}
