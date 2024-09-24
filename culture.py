import flet as ft 
cc=ft.Container(width=1000,height=1000)
def Culpage(page):
    global cc
    appbar=ft.AppBar(leading=ft.IconButton(on_click=lambda _:page.go('/Home')))
    
    page.add(appbar,cc)