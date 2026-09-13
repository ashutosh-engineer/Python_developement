# Property attribute
# Getters
# Setters

class Ex:
    def __init__(self, car, model):
        self.car = car
        self.model = model

    @property
    def model(self):  # Getter
        print("Getter called")
        if self._model > 2000:
            print("Very old car")
        return self._model

    @model.setter
    def model(self, value):  # Setter
        if value <= 2000:
            value = 5000
        self._model = value


gt = Ex("Toyota", 2000)
print(gt.model)