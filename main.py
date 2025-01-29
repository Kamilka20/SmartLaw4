from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "SmartLaw"
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Menu"
                    title_color: "#4a4939"
                    text: "SmartLaw"
                    spacing: "10dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Youridicheskie litsya"

                DrawerClickableItem:
                    icon: "Bank"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Bank"

                DrawerClickableItem:
                    icon: "People"
                    text: "Vladeltsy"
                    
                DrawerClickableItem:
                    icon: "People"
                    text: "Sotrydniki"
                    
                DrawerClickableItem:
                    icon: "People"
                    text: "Oplata"
                    
                DrawerClickableItem:
                    icon: "People"
                    text: "Raion"
                    
                DrawerClickableItem:
                    icon: "People"
                    text: "Ulitsy"
                    
                DrawerClickableItem:
                    icon: "People"
                    text: "Tip organizatsy"
                    
                DrawerClickableItem:
                    icon: "People"
                    text: "Ustanovka"


                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Дополнительно"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Настройки"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Помощь"
'''


class SmartLaw(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


SmartLaw().run()