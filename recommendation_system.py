def recomendar_peliculas(generos_favoritos, peliculas):
	"""Ordena las películas según cuántos géneros favoritos comparten."""
	recomendaciones = []

	for titulo, generos in peliculas.items():
		coincidencias = [
			genero for genero in generos if genero in generos_favoritos
		]
		if coincidencias:
			recomendaciones.append((titulo, coincidencias))

	return sorted(recomendaciones, key=lambda item: len(item[1]), reverse=True)


def main():
	# Cada película se relaciona con una lista de géneros.
	peliculas = {
		"Viaje estelar": ["ciencia ficción", "aventura"],
		"El misterio del faro": ["misterio", "drama"],
		"Risas en la oficina": ["comedia"],
		"La última frontera": ["aventura", "drama"],
		"Robots del mañana": ["ciencia ficción", "acción"],
		"Sombras en el bosque": ["terror", "misterio"],
		"Un día inesperado": ["comedia", "romance"],
		"Guardianes del valle": ["acción", "aventura"],
	}

	# Lee géneros separados por comas y normaliza mayúsculas y espacios.
	entrada = input("Escribe tus géneros favoritos separados por comas: ")
	generos_favoritos = [
		genero.strip().lower() for genero in entrada.split(",") if genero.strip()
	]

	if not generos_favoritos:
		print("No ingresaste ningún género favorito.")
		return

	recomendaciones = recomendar_peliculas(generos_favoritos, peliculas)
	if not recomendaciones:
		print("No encontramos películas para esos géneros.")
		return

	print("\nPelículas recomendadas:")
	for titulo, coincidencias in recomendaciones:
		generos = ", ".join(coincidencias)
		print(f"- {titulo} (coincide con: {generos})")


if __name__ == "__main__":
	main()
