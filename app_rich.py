from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print

console = Console()
tareas = []  # Lista de tareas: cada tarea es un dict {'texto': str, 'hecha': bool}


def mostrar_tareas():
    table = Table(title="📋 Lista de Tareas", header_style="bold magenta")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Tarea", style="bold")
    table.add_column("Estado", style="green")

    if not tareas:
        console.print("[italic yellow]No hay tareas registradas aún.[/italic yellow]")
    else:
        for i, tarea in enumerate(tareas, start=1):
            estado = "✅ Hecha" if tarea['hecha'] else "❌ Pendiente"
            table.add_row(str(i), tarea['texto'], estado)
        console.print(table)


def agregar_tarea():
    texto = Prompt.ask("📝 Escribe la nueva tarea")
    tareas.append({'texto': texto, 'hecha': False})
    print("[bold green]Tarea agregada correctamente[/bold green] ✅")


def marcar_como_hecha():
    mostrar_tareas()
    if tareas:
        try:
            idx = int(Prompt.ask("✔️ Ingresa el ID de la tarea a marcar como hecha")) - 1
            tareas[idx]['hecha'] = True
            print("[bold cyan]¡Tarea marcada como hecha![/bold cyan]")
        except (IndexError, ValueError):
            print("[bold red]❌ ID inválido[/bold red]")


def eliminar_tarea():
    mostrar_tareas()
    if tareas:
        try:
            idx = int(Prompt.ask("🗑️ Ingresa el ID de la tarea a eliminar")) - 1
            eliminada = tareas.pop(idx)
            print(f"[red]Tarea eliminada:[/red] {eliminada['texto']}")
        except (IndexError, ValueError):
            print("[bold red]❌ ID inválido[/bold red]")


def menu():
    while True:
        print("\n[bold yellow]¿Qué deseas hacer?[/bold yellow]")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar como hecha")
        print("4. Eliminar tarea")
        print("5. Salir")

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
            break
        else:
            print("[bold red]Opción inválida, intenta de nuevo.[/bold red]")


if __name__ == "__main__":
    menu()
