import flet as ft
import requests 

def Spage(page:ft.page):
    def qr(e):
        pass


    searchbar=ft.TextField(hint_text="  Recherche...",on_submit=qr,border_color=ft.colors.INDIGO_400,bgcolor=ft.colors.INDIGO_50,border_radius=ft.border_radius.all(15),width=300,height=50)
    af=ft.TextField(disabled=True,border_color=ft.colors.INDIGO_400,bgcolor=ft.colors.INDIGO_50,border_radius=ft.border_radius.all(15),width=100,height=50)
    f=ft.SelectionArea(content=af)
    r=ft.Row(controls=[f,ft.IconButton()])

    ap=ft.AppBar(leading=ft.IconButton(on_click= lambda _:page.go('/Home')),bgcolor=ft.colors.DEEP_ORANGE)

    co=ft.Column(controls=[enter,r])
    page.add(ap,co)
    page.update()