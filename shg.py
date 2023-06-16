import math

class SpatialHashing:
    
    def __init__(self, bounds, dimensions):
        self.bounds = bounds
        self.dimensions = dimensions
        self.cells = {}

    def new_entity(self, position, dimensions):
        entity = {
            "position": position,
            "dimensions": dimensions,
            "indices": None
        }
        self.insertion(entity)
        return entity

    def insertion(self, entity):
        x, y = entity["position"]
        w, h = entity["dimensions"]

        i1 = self.compute_hash([x - w/2, y - h/2])
        i2 = self.compute_hash([x + w/2, y + h/2])

        entity["indices"] = [i1, i2]

        for x in range(i1[0], i2[0]):
            for y in range(i1[1], i2[1]):
                k = self.generate_key(x, y)
                if k not in self.cells:
                    self.cells[k] = []
                self.cells[k].append(entity)

    def generate_key(self, x, y):
        return str(x) + '.' + str(y)


    def compute_hash(self, position):
        x = (position[0] - self.bounds[0][0]) / (self.bounds[1][0] - self.bounds[0][0])
        y = (position[1] - self.bounds[0][1]) / (self.bounds[1][1] - self.bounds[0][1])

        x_index = math.floor(x * (self.dimensions[0] - 1))
        y_index = math.floor(y * (self.dimensions[1] - 1))

        return [x_index, y_index]

    def query(self, position, bounds):
        x, y = position
        w, h = bounds
        
        i1 = self.compute_hash([x - w/2, y - h/2])
        i2 = self.compute_hash([x + w/2, y + h/2])

        entities = {}

        for ix in range(i1[0], i2[0]):
            for iy in range(i1[1], i2[1]):
                k = self.generate_key(ix, iy)

                if k in self.cells:
                    for j in self.cells[k]:
                        entities[j] = None
                        
        return entities
                        