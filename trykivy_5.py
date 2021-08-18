# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.widget import Widget
# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        label = Widget()
        btn = Button(text="далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn.pos = (720,0)
        label.add_widget(btn) # экран - это виджет, на котором могут создаваться все другие (потомки)

        txt = Label(text = '**стук в дверь** Откройте ,Полиция')
        txt.pos = (300,400)
        label.add_widget(txt)
        self.popit = Popup(content=Label(text=''),
                            size_hint = (None,None),size = (200,200),
                            auto_dismiss = False)
        self.add_widget(label)
    def closepopit(self,dt):
        self.popit.dismiss()

    def next(self):
        '''self.popit.open()
        self.manager.transition.direction = 'left' # объект класса Screen имеет свойство manager ''
        Clock.schedule_once(self.closepopit,10)    '''
        self.manager.current = 'second'

    


class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        label = Widget()
        btn = Button(text="Вернуться",size_hint = (None,None))
        btn1 = Button(text="Далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn1.size = (30,30)
        btn.on_press = self.remove
        btn1.on_press = self.next
        label.add_widget(btn)
        label.add_widget(btn1)
        btn1.pos = (720,0)
        btn.pos = (120,0)

        txt = Label(text = 'Ммммм ,что , что со мной вчера произошло? ааа что я сделал ')
        txt.pos = (300,400)
        label.add_widget(txt)

        self.add_widget(label)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'

    def remove(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        label = Widget()
        btn = Button(text="Вернуться",size_hint = (None,None))
        btn1 = Button(text="Далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn1.size = (30,30)
        btn.on_press = self.remove
        btn1.on_press = self.next
        label.add_widget(btn)
        label.add_widget(btn1)
        btn1.pos = (720,0)
        btn.pos = (120,0)

        txt = Label(text = 'Мы выпиливаем дверь. **Звук пилы режущий пилы по металлу** **Дверь упала**')
        txt.pos = (300,400)
        label.add_widget(txt)

        self.add_widget(label)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Fourth'

    def remove(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Second'

class ForthScr(Screen):
    def __init__(self, name='Fourth'):
        super().__init__(name=name)
        label = Widget()
        btn = Button(text="Вернуться",size_hint = (None,None))
        btn1 = Button(text="Далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn1.size = (30,30)
        btn.on_press = self.remove
        btn1.on_press = self.next
        label.add_widget(btn)
        label.add_widget(btn1)
        btn1.pos = (720,0)
        btn.pos = (120,0)

        txt = Label(text = 'Лежать руки заголову это омон.')
        txt.pos = (300,400)
        label.add_widget(txt)

        self.add_widget(label)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Fivth'

    def remove(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'third'

class FivthScr(Screen):
    def __init__(self, name='Fivth'):
        super().__init__(name=name)
        label = Widget()
        btn = Button(text="Вернуться",size_hint = (None,None))
        btn1 = Button(text="Далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn1.size = (30,30)
        btn.on_press = self.remove
        btn1.on_press = self.next
        label.add_widget(btn)
        label.add_widget(btn1)
        btn1.pos = (720,0)
        btn.pos = (120,0)

        txt = Label(text = '  Майор полиции Александр Грачев')
        txt.pos = (300,400)
        label.add_widget(txt)

        self.add_widget(label)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Sixth'

    def remove(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Fourth'

class SixthScr(Screen):
    def __init__(self, name='Sixth'):
        super().__init__(name=name)
        label = Widget()
        btn = Button(text="Вернуться",size_hint = (None,None))
        btn1 = Button(text="Далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn1.size = (30,30)
        btn.on_press = self.remove
        btn1.on_press = self.next
        label.add_widget(btn)
        label.add_widget(btn1)
        btn1.pos = (720,0)
        btn.pos = (120,0)

        txt = Label(text = 'В чем я  обвиняюсь?')
        txt.pos = (300,400)
        label.add_widget(txt)

        self.add_widget(label)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Seventh'

    def remove(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Fivth'        

class SeventhScr(Screen):
    def __init__(self, name='Seventh'):
        super().__init__(name=name)
        label = Widget()
        btn = Button(text="Вернуться",size_hint = (None,None))
        btn1 = Button(text="Далее",size_hint = (None,None))
        btn.on_press = self.next
        btn.size = (30,30)
        btn1.size = (30,30)
        btn.on_press = self.remove
        btn1.on_press = self.next
        label.add_widget(btn)
        label.add_widget(btn1)
        btn1.pos = (720,0)
        btn.pos = (120,0)

        txt = Label(text = 'Вы вчера расстреляли 14 человек')
        txt.pos = (300,400)
        label.add_widget(txt)

        self.add_widget(label)
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Sixth'

    def remove(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Fivth'      

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(ForthScr())
        sm.add_widget(FivthScr())
        sm.add_widget(SixthScr())
        sm.add_widget(SeventhScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'

        return sm

app = MyApp()
app.run()