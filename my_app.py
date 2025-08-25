import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
#음식들 인덱스

    
class 점메추App(App):
    def menua(self, instance):
           ran = random.choice(self.menu)
           self.menu_label.text = ran
    def build(self):

        layout = BoxLayout(orientation="vertical")
        

        self.menu = ['김치찌개','된장찌개','부대찌개','떡볶이','마라탕','탕후루','라면','요아정','붕어빵','초밥','토스트']
        self.menu_label = Label(text='오늘 점심을 뭐 먹을지 고민된다면? 점메추 버튼 한번으로 점심먹기!', font_name='BMJUA_ttf.ttf')
        button = Button(text='점메추하기',font_name='BMJUA_ttf.ttf',size_hint_y=None, height=100)
        button.bind(on_press=self.menua)
        
        layout.add_widget(self.menu_label)
        layout.add_widget(button)
        return layout
    
        

if __name__ == '__main__':
    점메추App().run()