class Animacion:
    def __init__(self, frames, velocidad):
        self.frames = frames
        self.velocidad = velocidad
        self.index =0
        self.contador =0
    
    def actualizar(self):
        self.contador +=1
        if self.contador >= self.velocidad:
            self.contador =0
            self.index = (self.index + 1) % len(self.frames)
    
    def get_frame(self):
        self.frames[self.index]
        return