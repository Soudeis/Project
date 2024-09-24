import flet as ft
from home import Hpage
from download import Dopage
from dictionnary import Dpage
from chat import Cpage
from quote import Qpage
from culture import Culpage
from short import Spage

def main(page:ft.page):
    
    
    #Mc le container qui contiendrait les differentes pages
    Mc=ft.Container(padding=0)
    
    def ch(e):   
        if e.control.selected_index==0:
            page.go("/Home")
        elif e.control.selected_index==1:
            page.go("/Dic")
        elif e.control.selected_index==2:
            page.go("/Chat")
        elif e.control.selected_index==3:
            page.go("/Down")

    def route_change(route):
        page.controls.clear()
        if page.route=='/Home': # page principale 
            Mc.content=Hpage(page)
            page.add(Bapp,Mc)
        elif page.route=='/Dic': # page dictionnaire
            Mc.content=Dpage(page)
            page.add(Bapp,Mc)
        elif page.route=='/Down':# nouveau trend page
            Mc.content=Dopage(page)
            page.add(Bapp,Mc)
        elif page.route=='/Chat': # chatgpt page
            Mc.content=Cpage(page)
            page.add(Bapp,Mc)

        elif page.route=='/Par': #parametre page
            Mc.content=Ppage(page)
            page.add(Mc)
        elif page.route=='/Quote':
            Mc.content=Qpage(page)
            page.add(Mc)
        elif page.route=='/Short': # page dedié aux femmes
            Mc.content=Spage(page)
            page.add(Mc)
        
        elif page.route=='/Cul': # page dediée à la culture 
            Mc.content=Culpage(page)
            page.add(Mc)
        page.update()
    
    Bapp=ft.CupertinoNavigationBar(
    bgcolor=ft.colors.TRANSPARENT,
    on_change=ch,
    active_color=ft.colors.BLUE,
    inactive_color=ft.colors.BLUE_100,
    icon_size=25,
    destinations=[
        ft.NavigationBarDestination(icon=ft.icons.HOME,label="Acceuil"),
        ft.NavigationBarDestination(icon=ft.icons.BOOK,label="Dictionnaire"),
        ft.NavigationBarDestination(icon=ft.icons.CHAT,label="AI"),
        ft.NavigationBarDestination(icon=ft.icons.LYRICS,label="Lyrics")
    ])
    
    page.on_route_change=route_change
    page.go('/Home')
    page.add(Mc)

ft.app(target=main,view=ft.AppView.WEB_BROWSER)
        

