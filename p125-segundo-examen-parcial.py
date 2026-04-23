#Objetivo:Se desea procesar el registro de vuelos de una aerolínea ("AeroRegistro"). Para ello, deberá solicitar al usuario los siguientes datos por cada vuelo.
#Nombre del Alumno: [Jimena Estefania Reyes Avila]
#Matrícula: [20202177]
#p125-segundo-examen-parcial.py 
#Se desea procesar el registro de vuelos de una aerolínea ("AeroRegistro"). Para ello, deberá solicitar al usuario los siguientes datos por cada vuelo:


def ejecutar_sistema():
    vuelos = []
    
    print("AeroRegistro - Sistema de Vuelos")
    print("Captura de datos de los vuelos (* para terminar):\n")


    while True:
        num_vuelo = input("Número de vuelo: ")
        if num_vuelo == "" or num_vuelo == "*":
            break
            
        origen = input("Origen: ")
        destino = input("Destino: ")
        aerolinea = input("Aerolínea: ")
        pasajeros = int(input("Pasajeros: "))
        tarifa = float(input("Tarifa: "))
        
       
        vuelo = {
            "numero_vuelo": num_vuelo,
            "origen": origen,
            "destino": destino,
            "aerolinea": aerolinea,
            "pasajeros": pasajeros,
            "tarifa": tarifa
        }
        vuelos.append(vuelo)
        print("-" * 20)

    if not vuelos:
        print("No se registraron vuelos.")
        return

    print("\nDatos (Lista de diccionarios):")
    print(vuelos)

  
    print("\n" + "="*80)
    header = f"{'No. Vuelo':<12} {'Origen':<15} {'Destino':<15} {'Aerolínea':<15} {'Pasajeros':<10} {'Tarifa':<10}"
    print(header)
    print("-" * 80)
    for v in vuelos:
        print(f"{v['numero_vuelo']:<12} {v['origen']:<15} {v['destino']:<15} {v['aerolinea']:<15} {v['pasajeros']:<10} {v['tarifa']:<10.2f}")
    print("="*80)

  
    total_vuelos = len(vuelos)
    
    conteo_aerolineas = {}
    conteo_destinos = {}
    suma_pasajeros = 0
    suma_tarifas = 0
    
    vuelo_caro = vuelos[0]
    vuelo_barato = vuelos[0]

    for v in vuelos:
       
        conteo_aerolineas[v['aerolinea']] = conteo_aerolineas.get(v['aerolinea'], 0) + 1
        conteo_destinos[v['destino']] = conteo_destinos.get(v['destino'], 0) + 1
        
      
        suma_pasajeros += v['pasajeros']
        suma_tarifas += v['tarifa']
        
        
        if v['tarifa'] > vuelo_caro['tarifa']:
            vuelo_caro = v
        if v['tarifa'] < vuelo_barato['tarifa']:
            vuelo_barato = v


    print("\nResumen:")
    print(f"Vuelos totales: {total_vuelos}")

    print("\nAerolíneas:")
    for aero, cant in conteo_aerolineas.items():
        print(f"  • {aero}: {cant}")

    print("\nDestinos:")
    for dest, cant in conteo_destinos.items():
        print(f"  • {dest}: {cant}")

    prom_pasajeros = suma_pasajeros / total_vuelos
    prom_tarifa = suma_tarifas / total_vuelos

    print(f"\nPasajeros -> Suma: {suma_pasajeros}, Promedio: {prom_pasajeros:.1f}")
    print(f"Tarifa -> Suma: {suma_tarifas:,.2f}, Promedio: {prom_tarifa:,.2f}")
    print(f"{vuelo_caro['numero_vuelo']} de ${vuelo_caro['tarifa']:,.2f} es el más caro, "
          f"{vuelo_barato['numero_vuelo']} de ${vuelo_barato['tarifa']:,.2f} es el más barato.")

if __name__ == "__main__":
    ejecutar_sistema()