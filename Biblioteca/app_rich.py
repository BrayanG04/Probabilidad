# Importación de módulos de la librería 'rich' para salida formateada en consola
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print  # Reemplaza el print estándar por uno con colores y estilos

# Inicializa el objeto consola de rich para imprimir con formato
console = Console()

# Lista donde se almacenarán las tareas; cada tarea será un diccionario con texto y estado
tareas = []  # Lista de tareas: cada tarea es un dict {'texto': str, 'hecha': bool}


def mostrar_tareas():
    # Se crea una tabla con título y estilo para mostrar las tareas
    table = Table(title="Lista de Tareas", header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Tarea", style="bold")
    table.add_column("Estado", style="green")

    # Si no hay tareas, se muestra un mensaje
    if not tareas:
        console.print("[italic yellow]No hay tareas registradas aún.[/italic yellow]")
    else:
        # Recorre la lista de tareas e imprime cada una con su estado
        for i, tarea in enumerate(tareas, start=1):
            estado = "✅ Hecha" if tarea['hecha'] else "❌ Pendiente"
            table.add_row(str(i), tarea['texto'], estado)
        console.print(table)


def agregar_tarea():
    # Solicita al usuario que escriba la nueva tarea
    texto = Prompt.ask("📝 Escribe la nueva tarea")
    # Agrega la tarea a la lista con estado 'hecha' en False
    tareas.append({'texto': texto, 'hecha': False})
    print("[bold green]Tarea agregada correctamente[/bold green] ✅")


def marcar_como_hecha():
    mostrar_tareas()  # Muestra la lista de tareas para que el usuario vea los ID
    if tareas:
        try:
            # Solicita el ID de la tarea a marcar como hecha
            idx = int(Prompt.ask("✔️ Ingresa el ID de la tarea a marcar como hecha")) - 1
            tareas[idx]['hecha'] = True
            print("[bold cyan]¡Tarea marcada como hecha![/bold cyan]")
        except (IndexError, ValueError):  # Si el ID no es válido
            print("[bold red]❌ ID inválido[/bold red]")


def eliminar_tarea():
    mostrar_tareas()  # Muestra la lista de tareas para elegir cuál eliminar
    if tareas:
        try:
            idx = int(Prompt.ask("🗑️ Ingresa el ID de la tarea a eliminar")) - 1
            eliminada = tareas.pop(idx)  # Elimina la tarea de la lista
            print(f"[red]Tarea eliminada:[/red] {eliminada['texto']}")
        except (IndexError, ValueError):  # Manejo de errores si el ID es inválido
            print("[bold red]❌ ID inválido[/bold red]")


def menu(): 
    while True:
        # Muestra las opciones del menú principal
        print("\n[bold yellow]¿Qué deseas hacer?[/bold yellow]")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar como hecha")
        print("4. Eliminar tarea")
        print("5. Salir")

        # Solicita la opción al usuario
        opcion = Prompt.ask("👉 Escribe el número de la opción")
        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            marcar_como_hecha()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("[bold blue]👋 ¡Hasta luego![/bold blue]")
            break  # Sale del ciclo y termina el programa
        else:
            print("[bold red]Opción inválida, intenta de nuevo.[/bold red]")


if __name__ == "__main__":
    menu()  # Llama al menú principal si se ejecuta el script directamente

