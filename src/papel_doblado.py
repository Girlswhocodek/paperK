
"""
Cálculo del grosor del papel doblado 43 veces
Programa para CodeSpaces y GitHub
"""

import time
import matplotlib.pyplot as plt

# Grosor inicial del papel (metros)
THICKNESS = 0.00008
NUM_FOLDS = 43
DISTANCE_TO_MOON = 384400  # km

def metodo_exponenciacion():
    """Método 1: Usando operador de exponenciación"""
    folded_thickness = THICKNESS * (2 ** NUM_FOLDS)
    return folded_thickness

def metodo_for_loop():
    """Método 2: Usando bucle for"""
    folded_thickness = THICKNESS
    for _ in range(NUM_FOLDS):
        folded_thickness *= 2
    return folded_thickness

def calcular_grosor_proceso():
    """Calcula el grosor en cada doblez y retorna la lista"""
    grosores = [THICKNESS]  # Grosor inicial
    
    current_thickness = THICKNESS
    for i in range(NUM_FOLDS):
        current_thickness *= 2
        grosores.append(current_thickness)
    
    return grosores

def comparar_tiempos():
    """Compara los tiempos de ejecución de ambos métodos"""
    print("=" * 60)
    print("COMPARACIÓN DE TIEMPOS DE EJECUCIÓN")
    print("=" * 60)
    
    # Método 1: Exponenciación
    start = time.time()
    resultado1 = metodo_exponenciacion()
    tiempo1 = time.time() - start
    
    # Método 2: Bucle for
    start = time.time()
    resultado2 = metodo_for_loop()
    tiempo2 = time.time() - start
    
    print(f"Método exponenciación: {tiempo1:.8f} segundos")
    print(f"Método bucle for:     {tiempo2:.8f} segundos")
    print(f"Diferencia:           {abs(tiempo1 - tiempo2):.8f} segundos")
    print(f"¿Resultados iguales?  {resultado1 == resultado2}")
    
    return tiempo1, tiempo2

def mostrar_resultados():
    """Muestra los resultados principales"""
    resultado = metodo_exponenciacion()
    
    print("=" * 60)
    print("RESULTADOS DEL CÁLCULO")
    print("=" * 60)
    print(f"Grosor inicial del papel: {THICKNESS} metros")
    print(f"Número de dobleces: {NUM_FOLDS}")
    print(f"Grosor final: {resultado:.2f} metros")
    print(f"Grosor final: {resultado/1000:.2f} kilómetros")
    print(f"Grosor final: {resultado/1000000:.2f} millones de kilómetros")
    
    # Comparación con la distancia a la Luna
    distancia_km = resultado / 1000
    print(f"\nDistancia a la Luna: {DISTANCE_TO_MOON} km")
    print(f"Grosor del papel doblado: {distancia_km:.2f} km")
    
    if distancia_km >= DISTANCE_TO_MOON:
        veces = distancia_km / DISTANCE_TO_MOON
        print(f"✅ El papel DOBLEGADO ALCANZA la Luna ({veces:.1f} veces)")
    else:
        print("❌ El papel doblado NO ALCANZA la Luna")

def visualizar_graficos():
    """Crea y muestra los gráficos de visualización"""
    grosores = calcular_grosor_proceso()
    
    print("\n" + "=" * 60)
    print("VISUALIZACIÓN GRÁFICA")
    print("=" * 60)
    print(f"Número de valores en la lista: {len(grosores)}")
    
    # Configuración para CodeSpaces (sin interfaz gráfica interactiva)
    plt.switch_backend('Agg')  # Usar backend no interactivo
    
    # Gráfico 1: Básico
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.title("Grosor del papel doblado - Básico", fontsize=12)
    plt.xlabel("Número de dobleces")
    plt.ylabel("Grosor [m]")
    plt.plot(grosores)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 2: Con personalización
    plt.subplot(2, 2, 2)
    plt.title("Grosor del papel doblado - Personalizado", fontsize=12)
    plt.xlabel("Número de dobleces", fontsize=10)
    plt.ylabel("Grosor [m]", fontsize=10)
    plt.tick_params(labelsize=8)
    plt.plot(grosores, color='red', linewidth=2, linestyle='-', marker='o', markersize=3)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 3: Escala logarítmica (para mejor visualización)
    plt.subplot(2, 2, 3)
    plt.title("Grosor - Escala logarítmica", fontsize=12)
    plt.xlabel("Número de dobleces")
    plt.ylabel("Grosor [m] - Escala log")
    plt.yscale('log')
    plt.plot(grosores, color='green', linewidth=2)
    plt.grid(True, alpha=0.3)
    
    # Gráfico 4: Comparación con distancia a la Luna
    plt.subplot(2, 2, 4)
    plt.title("Comparación con distancia a la Luna", fontsize=12)
    plt.xlabel("Número de dobleces")
    plt.ylabel("Distancia [km]")
    
    # Convertir grosores a kilómetros
    grosores_km = [g / 1000 for g in grosores]
    plt.plot(grosores_km, color='purple', linewidth=2, linestyle='--')
    plt.axhline(y=DISTANCE_TO_MOON, color='orange', linestyle=':', 
                label=f'Luna: {DISTANCE_TO_MOON} km')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Guardar gráfico para CodeSpaces
    plt.savefig('grosor_papel_doblado.png', dpi=150, bbox_inches='tight')
    print("📊 Gráfico guardado como 'grosor_papel_doblado.png'")
    
    # Mostrar información del gráfico
    plt.show()

def main():
    """Función principal del programa"""
    print("🎯 PROGRAMA: CÁLCULO DEL GROSOR DEL PAPEL DOBLADO 43 VECES")
    print("🌙 ¿Llega a la Luna? - Análisis completo\n")
    
    try:
        # Mostrar resultados principales
        mostrar_resultados()
        
        # Comparar tiempos de ejecución
        tiempo1, tiempo2 = comparar_tiempos()
        
        # Visualización gráfica
        visualizar_graficos()
        
        # Resumen final
        print("\n" + "=" * 60)
        print("RESUMEN EJECUTIVO")
        print("=" * 60)
        resultado_final = metodo_exponenciacion() / 1000  # km
        
        print(f"• Grosor después de {NUM_FOLDS} dobleces: {resultado_final:,.0f} km")
        print(f"• Distancia a la Luna: {DISTANCE_TO_MOON:,} km")
        print(f"• El papel doblado es {resultado_final/DISTANCE_TO_MOON:.1f} veces la distancia")
        print(f"• Método más rápido: {'Exponenciación' if tiempo1 < tiempo2 else 'Bucle for'}")
        print("• Gráfico guardado: 'grosor_papel_doblado.png'")
        
        if resultado_final >= DISTANCE_TO_MOON:
            print("🎉 CONCLUSIÓN: ¡EL MITO ES VERDADERO!")
        else:
            print("❌ CONCLUSIÓN: El mito no se cumple con estos parámetros")
            
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")

# Ejecutar el programa solo si es el archivo principal
if __name__ == "__main__":
    main()
