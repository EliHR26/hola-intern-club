from funciones import duracion_total

# Descomenta las funciones conforme las vayas implementando:
# from funciones import (
#     filtrar_por_genero,
#     cancion_mas_larga,
#     buscar_por_artista,
#     mezclar,
#     recomendar,
# )

# Playlist de prueba con datos conocidos
MUESTRA_PRUEBA = [
    {
        "titulo": "Cancion A",
        "artista": "Artista 1",
        "genero": "Pop",
        "duracion_segundos": 120,
    },
    {
        "titulo": "Cancion B",
        "artista": "Artista 2",
        "genero": "Rock",
        "duracion_segundos": 90,
    },
]


def test_duracion_total():
    # 120 + 90 = 210 segundos -> 3 min 30 seg
    resultado = duracion_total(MUESTRA_PRUEBA)
    assert resultado == "3 min 30 seg", f"Esperado '3 min 30 seg', pero se obtuvo '{resultado}'"

    # Prueba con lista vacia
    assert duracion_total([]) == "0 min 0 seg", "Una playlist vacia deberia durar '0 min 0 seg'"


# =====================================================================
# Pruebas para las demas funciones (descomenta segun la funcion de tu equipo):
# =====================================================================

# def test_filtrar_por_genero():
#     rock = filtrar_por_genero(MUESTRA_PRUEBA, "Rock")
#     assert len(rock) == 1, "Deberia encontrar exactamente 1 cancion de Rock"
#     assert rock[0]["titulo"] == "Cancion B"
#     assert filtrar_por_genero(MUESTRA_PRUEBA, "Jazz") == [], "Genero inexistente debe regresar lista vacia"

# def test_cancion_mas_larga():
#     larga = cancion_mas_larga(MUESTRA_PRUEBA)
#     assert larga["titulo"] == "Cancion A", "La cancion mas larga debe ser 'Cancion A' (120 seg)"
#     assert cancion_mas_larga([]) is None, "Una playlist vacia debe regresar None"

# def test_buscar_por_artista():
#     canciones = buscar_por_artista(MUESTRA_PRUEBA, "Artista 1")
#     assert len(canciones) == 1
#     assert canciones[0]["titulo"] == "Cancion A"
#     assert buscar_por_artista(MUESTRA_PRUEBA, "Inexistente") == []

# def test_mezclar():
#     mezclada = mezclar(MUESTRA_PRUEBA)
#     assert len(mezclada) == len(MUESTRA_PRUEBA), "La lista mezclada debe tener la misma cantidad de elementos"
#     assert mezclada is not MUESTRA_PRUEBA, "mezclar() debe regresar una NUEVA lista, no modificar la original"

# def test_recomendar():
#     recomendacion = recomendar(MUESTRA_PRUEBA, "Pop")
#     assert recomendacion is not None
#     assert recomendacion["genero"] == "Pop"
#     assert recomendar(MUESTRA_PRUEBA, "Metal") is None, "Si no hay del genero, debe regresar None"


def ejecutar_pruebas():
    test_duracion_total()

    # Descomenta la llamada a la prueba de tu funcion aqui:
    # test_filtrar_por_genero()
    # test_cancion_mas_larga()
    # test_buscar_por_artista()
    # test_mezclar()
    # test_recomendar()

    print("Todas las pruebas pasaron")


if __name__ == "__main__":
    ejecutar_pruebas()
