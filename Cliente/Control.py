#!/usr/bin/env python
# -*- coding: utf-8 -*-
					##################################################
					#Proyecto: Juego mitos y leyendas                #
					#Version: 0.0.4                                  #
					#Nombre:Eric Christian Bernstorff Corona         #
					#Fecha de inicio: 24/09/2013                     #
					#Fase: En desarrollo                             #
					##################################################
#Controles

import pygame
from sys import exit
from pygame.locals import *

class Control:
	def __init__(self):
		self.click_sound = False
	
	def eventos_poll(self):
		if True:
			event =  pygame.event.poll()
			if event.type == KEYDOWN:
				if event.key == K_TAB:
					return "tab"
				elif event.key == K_F1:
					#Modificar
					return "@"
				elif event.key == K_F2:
					#Modificar
					return "."
				elif event.key == K_COMMA:
					return ","
				elif event.key == K_SPACE:
					return " "
				elif event.key == K_BACKSPACE:
					return "backspace"
				elif event.key == K_0:
					return "0"
				elif event.key == K_1:
					return "1"
				elif event.key == K_2:
					return "2"
				elif event.key == K_3:
					return "3"
				elif event.key == K_4:
					return "4"
				elif event.key == K_5:
					return "5"
				elif event.key == K_6:
					return "6"
				elif event.key == K_7:
					return "7"
				elif event.key == K_8:
					return "8"
				elif event.key == K_9:
					return "9"
				elif event.key == K_a:
					return "a"
				elif event.key == K_b:
					return "b"
				elif event.key == K_c:
					return "c"
				elif event.key == K_d:
					return "d"
				elif event.key == K_e:
					return "e"
				elif event.key == K_f:
					return "f"
				elif event.key == K_g:
					return "g"
				elif event.key == K_h:
					return "h"
				elif event.key == K_i:
					return "i"
				elif event.key == K_j:
					return "j"
				elif event.key == K_k:
					return "k"
				elif event.key == K_l:
					return "l"
				elif event.key == K_m:
					return "m"
				elif event.key == K_n:
					return "n"
				elif event.key == K_o:
					return "o"
				elif event.key == K_p:
					return "p"
				elif event.key == K_q:
					return "q"
				elif event.key == K_r:
					return "r"
				elif event.key == K_s:
					return "s"
				elif event.key == K_t:
					return "t"
				elif event.key == K_u:
					return "u"
				elif event.key == K_v:
					return "v"
				elif event.key == K_w:
					return "w"
				elif event.key == K_x:
					return "x"
				elif event.key == K_y:
					return "y"
				elif event.key == K_z:
					return "z"
				elif event.key == K_UP:
					return "flechaArriba"
				elif event.key == K_DOWN:
					return "flechaAbajo"
				elif event.key == K_LEFT:
					return "flechaIzquierda"
				elif event.key == K_RIGHT:
					return "flechaDerecha"
				elif event.key == K_ESCAPE:
					pygame.quit();
					exit()
				else:
					return ""
			elif event.type == KEYUP:
				return "Se solto"
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					if self.click_sound != False:
						self.click_sound.play()
					print pygame.mouse.get_pos()
					return "click derecho"
				elif event.button == 3:
					if self.click_sound != False:
						self.click_sound.play()
					print pygame.mouse.get_pos()
					return "click izquierdo"
				else:
					return ""
			elif event.type == MOUSEMOTION:
				return "motion" 
			else:
				return ""
		return ""
	
#def dentro_de(Px, Py, base, altura):
#	Pxm, Pym = pygame.mouse.get_pos()
#	if Pxm > Px and Pxm < Px+base:
#		if Pym > Py and Pym < Py+altura:
#			return True
#		else:
#			return False
#	else:
#		return False
	
	def dentro_de(self, Punto, tamano):
		Px, Py = Punto
		Pxm, Pym = pygame.mouse.get_pos()
		base, altura = tamano
		#print Px, Py, base, altura
		if Pxm > Px and Pxm < Px+base:
			if Pym > Py and Pym < Py+altura:
				return True
			else:
				return False
		else:
			return False
		
	def repeat(self, delay, interval):
		pygame.key.set_repeat(delay, interval)