import keyboard
import time
import copy

class Push_Pull:
    def __init__(self, name, init_state):
        self.name = name
        self.init_state = init_state
        self.state = self.init_state
    
    def push(self, other):
        other.state += 1
    
    def pull(self, other):
        other.state -= 1
    
    def __repr__(self):
        return f"{self.name} ({self.state} / {self.init_state})"

class Map_Linea:
    def __init__(self, size):
        self.size = size
        self.edge_left = -self.size / 2
        self.edge_right = self.size / 2
        self.objects = []
    
    def add_objects(self, obj):
        self.objects.append(obj)
    
    def _colision_edge(self, other):
        if other.direction == 1:
            if other.position >= self.edge_right:
                other.direction = -1
        elif other.direction == -1:
            if other.position <= self.edge_left:
                other.direction = 1
    
    def _status_of_while(self, frame):
        ## NOTE: Ici first système sans push/pull
        old_frame_objects = copy.deepcopy(self.objects)
        for obj, old_obj in zip(self.objects, old_frame_objects):
            if obj.id == old_obj.id:                
                obj.state = frame
                obj.change_position()
                self._colision_edge(obj)
                for i in range(0, len(self.objects)):
                    if self.objects[i].id != obj.id:
                        if obj.position == self.objects[i].position:
                            obj.colision_obj(self.objects[i])

    def bind_position_on_map(self):
        key_code = "a"
        delta = 0
        while True:
            if keyboard.is_pressed(key_code):
                print(key_code)
                break
            
            if self.objects != []:
                self._status_of_while(delta)
            
            delta += 1
            print(f"Cycle {delta}:")
            for obj in self.objects:
                print(obj)
            time.sleep(0.1)

class Linea:
    quantity = 0
    def __init__(self, state, position, vitesse, direction):
        self.id = Linea.quantity
        Linea.quantity += 1
        self.state = state
        self.position = position
        self.vitesse = vitesse
        self.direction = direction
    
    def change_position(self):
        if self.direction == 1:
            self.position = self.position + self.vitesse
        elif self.direction == -1:
            self.position = self.position - self.vitesse
        elif self.direction == 0:
            pass
    
    def colision_obj(self, other):
        print(f"Colision {self.id} et {other.id}")
        self.change_position()
        other.change_position()
    
    def __repr__(self):
        return f"Obj {self.id}: at x = {self.position}, move at {self.vitesse * self.direction} unit/s"


if __name__=="__main__":
    obj_1 = Push_Pull('Obj 1', 5)
    obj_2 = Push_Pull('Obj 2', 5)
    
    map = Map_Linea(50)
    map.add_objects(Linea(0, -1, 1, -1))
    map.add_objects(Linea(0, 0, 1, 1))
    map.add_objects(Linea(0, 1, 1, 1))
    map.bind_position_on_map()