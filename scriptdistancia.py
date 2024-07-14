import googlemaps
import sys

def obtener_duracion_viaje(origen, destino, modo_transporte):
    gmaps = googlemaps.Client(key=AIzaSyCEEUhFqwXApRbaexs3Ndv0WCBBKrKoRpc)
    result = gmaps.distance_matrix(origen, destino, mode=modo_transporte)
    
    distancia_km = result['rows'][0]['elements'][0]['distance']['value'] / 1000.0
    distancia_millas = distancia_km * 0.621371
    duracion = result['rows'][0]['elements'][0]['duration']['text']
    
    return distancia_km, distancia_millas, duracion

def main():
    while True:
        print("Para salir del programa, ingrese 's'.")
        
        origen = input("Ciudad de Origen: ")
        if origen.lower() == 's':
            break
            
        destino = input("Ciudad de Destino: ")
        if destino.lower() == 's':
            break
        
        print("Seleccione el tipo de medio de transporte:")
        print("1. Conduciendo")
        print("2. Caminando")
        print("3. Bicicleta")
        print("4. Transporte público")
        modo_transporte = input("Opción (1/2/3/4): ")
        
        if modo_transporte == '1':
            modo = "driving"
        elif modo_transporte == '2':
            modo = "walking"
        elif modo_transporte == '3':
            modo = "bicycling"
        elif modo_transporte == '4':
            modo = "transit"
        else:
            print("Opción no válida. Intente nuevamente.")
            continue
        
        try:
            distancia_km, distancia_millas, duracion = obtener_duracion_viaje(origen, destino, modo)
            print(f"\nDistancia desde {origen} hasta {destino}:")
            print(f"{distancia_km:.2f} km")
            print(f"{distancia_millas:.2f} millas")
            print(f"Duración del viaje: {duracion}\n")
        except Exception as e:
            print(f"Error al calcular la distancia y duración del viaje: {e}")

if __name__ == "__main__":
    main()

