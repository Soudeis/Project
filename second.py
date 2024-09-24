import flet as ft

def view(D):
    ap=ft.AppBar(adaptive=True,bgcolor='blue',title=ft.Text('Real'),leading=ft.IconButton(icon=ft.icons.MENU,on_click=D))
    v=ft.View('/',[ap])
    return v