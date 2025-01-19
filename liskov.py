## Exemplo ruim
class Bird:
    def fly(self):
        print("voar")


class Eagle(Bird):
    def fly(self):
        print("voando!")


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Pinguim não voa!")
    


## Exemplo Bom

class Bird:
    def move(self):
        print("movendo")


class Eagle(Bird):
    def fly(self):
        print("voando!")


class Penguin(Bird):
    def fly(self):
        raise print("nadando")