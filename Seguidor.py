import random

class Grupo_segs:

    def __init__(self):
        self.seg_r=[];
        self.seg_v=[];
        self.seg_azu=[];
        self.seg_ama=[];
        self.seg_neg=[];
        self.num=40;

    def rellenar_color (self,color):
        for col in Color().color:
            if color== col:
                for n in range(self.num/len(Color().color)):
                    self.seg_r.append(Seguidor().dame_seguidor(col))

    def print_saco(self,segs):
        saco=""
        for s in segs:

            saco+=s;
        return saco

class Seguidor:


    def __init__(self):
        self.seg="S";

    def dame_todos(self):
        for s in Color.color():
            return dame_seguidor(s)

    def dame_seguidor(self,col):
        if col in Color().color:
            return self.to_String(col);
        return "color no existe"

    def to_String(self,color):
        return self.seg+" "+color+"\n";

class Color:

    def __init__(self):
        self.color=["rojo","verde","azul","amarillo","negro"];