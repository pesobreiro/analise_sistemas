#!/usr/bin/python
#-*- coding: utf-8 -*-

from Viatura import Viatura

class Pesado(Viatura):
    def __init__(self):
        self.capacidade_carga = None
        self.numero_eixos = None

