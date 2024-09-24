import flet as ft
import requests

def Qpage(page:ft.page):
    page.padding=0

    url=""
    d={
        "X-Rapidapi-Key":"",
        "X-Rapidapi-Host":""
    }

    def is_connected():
        response=requests.get(url,headers=d)
        return response.status_code==200

    def fetch(e):
        response=requests.get(url,headers=d)
        data=response.json()
        quote=data.get('content')
        author=data.get('originator',{}).get('name')
        tq.value=quote
        ta.value=author
        page.update()

    tq=ft.Text(value="cliquer sur le button",size=20,font_family="Roboto",weight=ft.FontWeight.BOLD)
    ta=ft.Text("",size=14,font_family="Roboto",weight=ft.FontWeight.BOLD)
    col=ft.Column(controls=[ta,ft.Text(""),tq])
    c=ft.SelectionArea(content=tq)
    container=ft.Container(content=c,
    blur=ft.Blur(10,0.1,ft.BlurTileMode.REPEATED),
    border_radius=ft.border_radius.all(10))
    ap=ft.AppBar(adaptive=True,leading=ft.IconButton(on_click= lambda _:page.go('/Home')),bgcolor='indigo')
    dec=ft.Container(bgcolor='',border_radius=ft.border_radius.only(0,0,20,20),padding=0,margin=0)
    but=ft.ElevatedButton("Generer",on_click=fetch,adaptive=True,bgcolor='indigo')
    if not is_connected():
        container.visible=False
        t=ft.Text("Hors Connection.",font_family="Roboto",weight=ft.Fontweight.BOLD)
        page.add(ap,ft.Column(controls=[dec,t],alignment=ft.MainAxisAlignment.START))
        page.update()
    else:
        page.add(ap,ft.Column(controls=[dec,container,but,ft.Container()],alignment=ft.MainAxisAlignment.START))
        page.update()
