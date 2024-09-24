import flet as ft

def Cpage(page:ft.page):
    v=ft.WebView("https://google.com",bgcolor='deep_orange',expand=True)
    page.add(v)
    page.update()