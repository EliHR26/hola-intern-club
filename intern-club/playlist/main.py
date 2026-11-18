import random
from playlist import PLAYLIST
from funciones import duracion_total


def main():
    print("=== La Playlist del Intern Club ===")
    print(f"Total de canciones: {len(PLAYLIST)}")
    print(f"Duracion total: {duracion_total(PLAYLIST)}")
    print("\nLista de reproduccion:")

    for cancion in PLAYLIST:
        titulo = cancion["titulo"]
        artista = cancion["artista"]
        genero = cancion["genero"]
        print(f"♪ {titulo} - {artista} ({genero})")

    if len(PLAYLIST) > 0:
        cancion_aleatoria = random.choice(PLAYLIST)
        print(f"\nAhora suena: {cancion_aleatoria['titulo']} - {cancion_aleatoria['artista']}")


if __name__ == "__main__":
    main()
