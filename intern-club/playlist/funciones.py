"""Modulo de funciones para manipular y analizar la playlist del Intern Club.

Contiene funciones de consulta, filtrado y recomendacion musical.
"""

import random


def duracion_total(playlist):
    """Suma la duración de todas las canciones y la regresa como texto 'X min Y seg'."""
    total = 0
    for cancion in playlist:
        total += cancion["duracion_segundos"]
    minutos = total // 60
    segundos = total % 60
    return f"{minutos} min {segundos} seg"


def filtrar_por_genero(playlist, genero):
    """Filtra y regresa una lista con las canciones que pertenecen al genero indicado.

    Recibe:
        playlist (list): Lista de diccionarios con las canciones.
        genero (str): Nombre del genero musical a buscar (ejemplo: 'Rock').

    Regresa:
        list: Lista de diccionarios con las canciones que coinciden con el genero.

    Ejemplo:
        filtrar_por_genero(PLAYLIST, "Rock")
        -> [{'titulo': 'De Musica Ligera', ...}, {'titulo': 'Rayando el Sol', ...}]
    """
    # TODO: tu codigo aqui
    pass


def cancion_mas_larga(playlist):
    """Encuentra y regresa el diccionario de la cancion con mayor duracion en segundos.

    Recibe:
        playlist (list): Lista de diccionarios con las canciones.

    Regresa:
        dict: Diccionario de la cancion con la duracion mas alta. Si la playlist esta vacia, regresa None.

    Ejemplo:
        cancion_mas_larga(PLAYLIST)
        -> {'titulo': 'Rayando el Sol', 'artista': 'Mana', 'genero': 'Rock', 'duracion_segundos': 251}
    """
    # TODO: tu codigo aqui
    pass


def buscar_por_artista(playlist, artista):
    """Busca y regresa todas las canciones de un artista en especifico.

    Recibe:
        playlist (list): Lista de diccionarios con las canciones.
        artista (str): Nombre exacto del artista o banda (ejemplo: 'Selena').

    Regresa:
        list: Lista de diccionarios con las canciones de ese artista.

    Ejemplo:
        buscar_por_artista(PLAYLIST, "Selena")
        -> [{'titulo': 'Amor Prohibido', 'artista': 'Selena', 'genero': 'Tex-Mex', 'duracion_segundos': 169}]
    """
    # TODO: tu codigo aqui
    pass


def mezclar(playlist):
    """Regresa una nueva lista con las canciones en un orden aleatorio.

    No debe modificar la lista original. Utiliza el modulo random.

    Recibe:
        playlist (list): Lista de diccionarios con las canciones.

    Regresa:
        list: Nueva lista con los mismos elementos pero en orden aleatorio.

    Ejemplo:
        mezclar(PLAYLIST)
        -> [{'titulo': 'Rayando el Sol', ...}, {'titulo': 'De Musica Ligera', ...}, ...]
    """
    # TODO: tu codigo aqui
    pass


def recomendar(playlist, genero):
    """Selecciona y regresa una sola cancion aleatoria del genero indicado.

    Recibe:
        playlist (list): Lista de diccionarios con las canciones.
        genero (str): Genero deseado para la recomendacion.

    Regresa:
        dict o None: Diccionario de una cancion seleccionada al azar del genero, o None si no hay canciones de ese genero.

    Ejemplo:
        recomendar(PLAYLIST, "Rock")
        -> {'titulo': 'De Musica Ligera', 'artista': 'Soda Stereo', ...}
    """
    # TODO: tu codigo aqui
    pass
