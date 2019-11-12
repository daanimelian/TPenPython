import db_store as manejador_db

def main():
	""" Ejecuta todas las funciones del archivo. """
	tenencias_por_categoria = manejador_db.load()
	print("¡Biendenido! \n")
	while True:
		print("\n Elija una opción: \n 1. Ingresar las transacciones por vendedor. \n 2. Actualizar los montos con el valor del dólar. \n 3. Imprimir tenencias hasta el momento. \n 4. Salir \n \n")
		opcion = input("Ingrese una opción: ")
		if opcion == "":
			print("Opción no válida. \n")
			continue
		elif opcion == "1":
			manejar_datos_ingresados(tenencias_por_categoria)
		elif opcion == "2":
			actualizar_montos_segun_el_valor_del_dolar(tenencias_por_categoria)
		elif opcion == "3":
			mostrar_datos(tenencias_por_categoria)
		elif opcion == "4":
			break
		else:
			print("Opción no válida. \n")
			continue
	manejador_db.store(tenencias_por_categoria)

def combinar(diccionario1, diccionario2):
	""" Combina dos diccionarios en uno sólo. """
	for keys, values in diccionario2.items():
		diccionario1[keys] = diccionario1.get(keys, 0) + values

def calcular_distancia(dic_1,dic_2):
	"""Calcula la distancia entre dos diccionarios como la suma de las diferencias entre los valores 
	de ambos diccionarios, en valor absoluto y  elemento a elemento, elevadas a la intensidad(que en este caso es igual a 1."""
	distancia = 0
	intensidad = 1
	list_a = ()
	list_b = ()
	for a in dic_1.values():
		try:
			a = float(a)
		except ValueError:
			return 'Error. Los valores del primer diccionario no son numericos. No se puede realizar esta operacion.'
	for b in dic_2.values():
		try:
			b = float(b)
		except ValueError:
			return 'Error. Los valores del segundo diccionario no son numericos. No se puede realizar esta operacion.'
	for a in dic_1:
		if a in dic_2:
			termino = (abs(dic_1[a]-dic_2[a]))**intensidad
		else:
			termino = (abs(dic_1[a]))**intensidad
		distancia += termino
	for b in dic_2:
		if b in dic_1:
			termino = 0
		else:
			termino = (abs(dic_2[b]))**intensidad
		distancia += termino
	return "Esta es la distancia:", distancia

def escalar_diccionario(diccionario, m):
	""" Multiplica por un número y reemplaza a los valores de un diccionario. """
	for key, value in diccionario.items():
		nuevos_valores = m * value
		diccionario[key] = nuevos_valores

def manejar_datos_ingresados(tenencias_por_categoria):
	inventario = {}
	dinero = {}
	neto = {}
	suma_neta = 0
	while True:
		ventas_por_vendedor = input("Ingrese las ventas por vendedor, en formato ---> vendedor categoría1:monto1 categoría2:monto2...: ")
		if ventas_por_vendedor == "":
			break
		partes = ventas_por_vendedor.split()
		nombre = partes[0]
		ventas = partes[1:]
		vendedor = neto.get(nombre, {})
		for x in ventas:
			suma_por_vendedor = 0
			if not ":" in x:
				print("Sintáxis incorrecta.")
				continue
			categoria, monto = x.split(":", 1)
			try:
				monto = float(monto)
			except ValueError:
				return("El monto ingresado no es un número.")
			inventario[categoria] = inventario.get(categoria, 0) + monto
			vendedor[categoria] = vendedor.get(categoria, 0) + monto
			neto[nombre] = vendedor
			dinero[nombre] = sum(vendedor.values())
		for clave, valor in dinero.items():
			print(clave, ":", valor)
		combinado = combinar(tenencias_por_categoria, inventario)
		calcular_distancia(inventario,  combinado)
	return combinado

def actualizar_montos_segun_el_valor_del_dolar(tenencias_por_categoria):
	""" Recibe los valores del dólar al comienzo y final del día y devuelve los diccionarios actualizados, aplicando la fluctuación del dólar a los montos allí guardados. """
	dolar1 = input("Ingrese el valor del dolar al iniciar el dia: ")
	try:
		dolar1 = float(dolar1)
	except ValueError:
		return "El valor ingresado no es un número."
		dolar2 = input("Ingrese el valor del dolar al finalizar el dia: ")
	try:
		dolar2 = float(dolar2)
	except ValueError:
		return "El valor ingresado no es un número"
	porcentaje = dolar1 / dolar2
	escalar_diccionario(tenencias_por_categoria, porcentaje)

def mostrar_datos(tenencias_por_categoria):
	""" Recibe un diccionario, lo ordena, calcula el monto de ganancias en pesos, actualizado según el dólar e imprime los nombrados valores. """
	for a, b in sorted(tenencias_por_categoria.items()):
		print(a, ":", b, "\n")


main()