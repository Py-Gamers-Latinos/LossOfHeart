import pygame
from pygame.locals import *

class Graficos():
	def __init__(self):
		pygame.init()
		Graficos.MUSICA_STATUS = True
		Graficos.SONIDO_STATUS = True
		Graficos.RESOLUCION = (0, 0)
		Graficos.TAMANO_CARTAS = (0,0)
		
	def establecer_pantalla(self, size, fullscreen = 0):
		if fullscreen == 0:
			self.screen = pygame.display.set_mode(size)
		else:
			self.screen = pygame.display.set_mode(size,pygame.DOUBLEBUF|pygame.HWSURFACE|pygame.FULLSCREEN)
	
	def establecer_icono(self, imagen):
		pygame.display.set_icon(imagen)
	
	def fullscreen(self):
		#Investigar como usar
		#self.screen.toggle_fullscreen()
		pass
	
	def establecer_cursor(self, imagen):
		#investigar
		#pygame.mouse.set_cursor()
		pass
	
	def imprimir_fondo(self, color):
		self.screen.fill(color)
		return
		
	def imprimir_imagen(self, imagen, posicion):
		self.screen.blit(imagen, posicion)
		return
	
	def actualizar_pantalla(self):
		pygame.display.flip()
		return
	
	def actualizar_rect_pantalla(self, punto, tamano):
		Px = punto[0]
		Py = punto[1]
		Sx = tamano[0]
		Sy = tamano[1]
		pygame.display.update((Px, Py, Sx, Sy))
		return
		
	def imprimir_rectangulo(self, color, rectangulo, ancho=0):
		pygame.draw.rect(self.screen, color, rectangulo, ancho)
		return
		
	def titulo_ventanta(self, titulo):
		pygame.display.set_caption(titulo)
		return
		
	def Iniciar_texto(self, tamano):
		fuente = pygame.font.Font(None, tamano)
		return fuente
	
	def imprimir_texto(self, mensaje, color, posicion, fuente):
		texto = fuente.render(str(mensaje), 1, color)
		self.screen.blit(texto,posicion)
		return
		
	def imprimir_texto_ajustable(self, mensaje, color, posicion, fuente, caracteres_per_line, espaciado):
		zero = 0
		aumento = caracteres_per_line
		times = (len(mensaje)/caracteres_per_line)+1
		Px, Py = posicion
		for time in range(0,times):
			mostrar = mensaje [zero:caracteres_per_line]
			texto = fuente.render(mostrar, 1, color)
			self.screen.blit(texto,(Px, Py))
			caracteres_per_line += aumento
			zero += aumento
			Py += espaciado
	
	def imprimir_texto_cuadro_linea(self, mensaje, color, (x0,y0), (x1,y1), tamano_max = 90):
		tamano = 0
		extension = len(mensaje)
		largo = int((x1-x0)*2.1)
		ancho = y1-y0
		area = largo * ancho
		while True:
			tamano += 1
			if area - (tamano**2)*extension == 0:
				break
			elif area - (tamano**2)*extension < 0:
				tamano -= 1
				break
		#Se verifica si el tamano de letra no es demasiado grande
		if tamano > tamano_max:
			tamano = tamano_max
		fuente = pygame.font.Font(None, tamano)
		Px, Py = (x0,y0)
		indice = 0
		indices = []
		for element in range(0, mensaje.count(" ")):
			indices.append(mensaje.find(" ",indice+1 ))
			indice = indices[element]
		linea = 1
		espacio = largo/tamano
		indices.append(len(mensaje))
		subindice = 0
		contador = 0
		for element in indices:
			if element <= espacio*linea:
				texto_linea = mensaje[subindice:element]
				contador += 1
			else:
				texto = fuente.render(texto_linea, 1, color)
				self.screen.blit(texto,(Px, Py))
				#subindice = element+1
				subindice = indices[contador-1]
				linea += 1
				Py += tamano
				contador += 1
		texto = fuente.render(texto_linea, 1, color)
		self.screen.blit(texto,(Px, Py))
		
	def imprimir_texto_cuadro(self, mensaje, color, (x0,y0), (x1,y1), tamano_max = 90):
		#Se declaran las variables que se usaran en la funcion
		tamano = 0
		largo = int((x1-x0)*2.1)
		ancho = y1-y0
		area = largo * ancho
		#Se calcula el tamano ideal de la letra
		while True:
			tamano += 1
			if area - (tamano**2)*len(mensaje) == 0:
				break
			elif area - (tamano**2)*len(mensaje) < 0:
				tamano -= 1
				break
		#Se verifica si el tamano de letra no es demasiado grande
		if tamano > tamano_max:
			tamano = tamano_max
		#Se inicializa la fuente de texto
		fuente = pygame.font.Font(None, tamano)
		Px, Py = (x0, y0)
		espacio = largo/tamano
		variable = espacio
		subindice = 0
		times = 1
		print "se repetira:", len(mensaje)
		for time in range(0, len(mensaje)+99):
			print time
			try:
				if mensaje[variable] == " ":
					if mensaje[subindice:variable] == "":
						pass
					else:
						texto = fuente.render(mensaje[subindice:variable], 1, color)
						self.screen.blit(texto,(Px, Py))
						Py += tamano
					subindice = variable + 1
					variable = espacio * times
					times += 1
				else:
					variable -=1
			except:
				texto = fuente.render(mensaje[subindice:len(mensaje)], 1, color)
				print "ultima linea"
				print mensaje[subindice:len(mensaje)]
				self.screen.blit(texto,(Px, Py))
				break

	def imprimir_texto_cuadro_centrado(self, mensaje, color, (x0,y0), (x1,y1), tamano_max = 90):
		#Se declaran las variables que se usaran en la funcion
		tamano = 0
		largo = int((x1-x0)*2.1)
		ancho = y1-y0
		area = largo * ancho
		#Se calcula el tamano ideal de la letra
		while True:
			tamano += 1
			if area - (tamano**2)*len(mensaje) == 0:
				break
			elif area - (tamano**2)*len(mensaje) < 0:
				tamano -= 1
				break
		#Se verifica si el tamano de letra no es demasiado grande
		print tamano
		if tamano > tamano_max:
			tamano = tamano_max
		elif tamano == 0:
			tamano = 1
		#Se inicializa la fuente de texto
		fuente = pygame.font.Font(None, tamano)
		Py = y0
		espacio = largo/tamano
		variable = espacio
		subindice = 0
		times = 1
		print "se repetira:", len(mensaje)
		for time in range(0, len(mensaje)+99):
			print time
			try:
				if mensaje[variable] == " ":
					if mensaje[subindice:variable] == "":
						pass
					else:
						Pxn = (x0 + x1) / 2
						Pxn = Pxn - ((len(mensaje[subindice:variable]) / 2) * (tamano / 2.2))
						texto = fuente.render(mensaje[subindice:variable], 1, color)
						self.screen.blit(texto,(Pxn, Py))
						Py += tamano
					subindice = variable + 1
					variable = espacio * times
					times += 1
				else:
					variable -=1
			except:
				Pxn = (x0 + x1) / 2
				Pxn = Pxn - ((len(mensaje[subindice:len(mensaje)]) / 2) * (tamano / 2.2))
				texto = fuente.render(mensaje[subindice:len(mensaje)], 1, color)
				print "ultima linea"
				print mensaje[subindice:len(mensaje)]
				self.screen.blit(texto,(Pxn, Py))
				#break
	def imprimir_texto_cuadro_centrado_nuevo(self, mensaje, color, (x0,y0), (x1,y1), tamano_max = 90):
		#Se declaran las variables que se usaran en la funcion
		tamano = 0
		largo = int(x1*3)
		ancho = y1
		area = largo * ancho
		#Se calcula el tamano ideal de la letra
		while True:
			tamano += 1
			if area - (tamano**2)*len(mensaje) == 0:
				break
			elif area - (tamano**2)*len(mensaje) < 0:
				tamano -= 1
				break
		#Se verifica si el tamano de letra no es demasiado grande
		print tamano
		if tamano > tamano_max:
			tamano = tamano_max
		elif tamano == 0:
			tamano = 1
		#Se inicializa la fuente de texto
		fuente = pygame.font.Font(None, tamano)
		Py = y0
		espacio = largo/tamano
		variable = espacio
		subindice = 0
		times = 1
		print "se repetira:", len(mensaje)
		for time in range(0, len(mensaje)+99):
			print time
			try:
				if mensaje[variable] == " ":
					if mensaje[subindice:variable] == "":
						pass
					else:
						Pxn = (x0 + x0 + x1) / 2
						Pxn = Pxn - ((len(mensaje[subindice:variable]) / 2) * (tamano / 2.2))
						texto = fuente.render(mensaje[subindice:variable], 1, color)
						self.screen.blit(texto,(Pxn, Py))
						Py += tamano
					subindice = variable + 1
					variable = espacio * times
					times += 1
				else:
					variable -=1
			except:
				Pxn = (x0 + x0 + x1) / 2
				Pxn = Pxn - ((len(mensaje[subindice:len(mensaje)]) / 2) * (tamano / 2.2))
				texto = fuente.render(mensaje[subindice:len(mensaje)], 1, color)
				print "ultima linea"
				print mensaje[subindice:len(mensaje)]
				self.screen.blit(texto,(Pxn, Py))
				
	def cargar_imagen(self, path, transparencia=False):
		#Metodo usado para importar imagenes y fijar transparencias
		try: 
			imagen = pygame.image.load(path)
		except pygame.error, message:
			raise SystemExit, message
		imagen = imagen.convert()
		if transparencia == True:
			color = imagen.get_at((0,0))
			imagen.set_colorkey(color, RLEACCEL)
		return imagen

	def pasar_color (self, color):
		if color == "blanco":
			return (255,255,255)
		elif color == "negro":
			return (0,0,0)
	
	def establecer_frames(self, frames):
		self.clock = pygame.time.Clock()
		self.frames = frames
	
	def controlar_frames(self):
		self.clock.tick(self.frames)
	
	def obtener_frames(self):
		return self.clock.get_fps()
		
	def resize_imagen(self, imagen, tamano):
		Sx = int(tamano[0])
		Sy = int(tamano[1])
		imagen = pygame.transform.scale(imagen, (Sx, Sy))
		return imagen
	
	def cursor_sobre(self, Posicion, Tamano):
		posicionMouse = pygame.mouse.get_pos() 
		PxM, PyM = posicionMouse
		Px, Py = Posicion 
		Dx, Dy = Tamano
		if PxM > Px and PxM < (Px+Dx):
			if PyM > Py and PyM < (Py+Dy):
				return "Dentro"
			return "Fuera"
		return	"Fuera"	
	
	def guardar_pantalla(self, nombre, pantalla, formato = ".png"):
		nombre = nombre + formato
		pygame.image.save(pantalla.screen,nombre)
		
	def transparencia(self, imagen, transparencia = 0):
		if transparencia < 0:
			imagen.alpha(0, RLEACCEL)
		elif transparencia >= 0 or transparencia <= 255:
			imagen.set_alpha(transparencia, RLEACCEL)
		else:
			imagen.alpha(255, RLEACCEL)
	
	def rotar_imagen(self, imagen, angle):
		return pygame.transform.rotate(imagen, angle)
	
	def cargar_cancion(self, path):
		pygame.mixer.music.load(path)
		
	def reproducir_cancion(self, loops):
		if self.MUSICA_STATUS == True:
			pygame.mixer.music.play(loops)
		else:
			pass
		
	def detener_cancion(self):
		pygame.mixer.music.stop()
		
	def cargar_sonido(self, path):
		sonido = pygame.mixer.Sound(path)
		return sonido
	
	def reproducir_sonido(self, sonido):
		if self.SONIDO_STATUS == True:
			sonido.play()
		else:
			pass
		
	def detener_sonido(self, sonido):	
		sonido.stop()
		
	def terminar_graficos(self):
		pygame.quit()


	