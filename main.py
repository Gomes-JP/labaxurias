from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

# Listas de termos para combinar
primeira_parte = ["Labareda", "Marreta", "Espada", "Trovão", "Fogo", "Glória", "Poder", "Voz", "Luz", "Cajado"]
segunda_parte = ["de Fogo", "de Matar Demônios", "do Senhor", "Celestial", "Divina", "do Espírito", "da Vitória", "Eterna", "da Salvação", "do Céu"]

class GeradorNomeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text="Clique no botão para gerar um nome!", font_size=20)
        self.layout.add_widget(self.label)

        self.botao = Button(text="Gerar Nome", font_size=20, on_press=self.gerar_nome)
        self.layout.add_widget(self.botao)

        return self.layout

    def gerar_nome(self, instance):
        primeira = random.choice(primeira_parte)
        segunda = random.choice(segunda_parte)
        nome_gerado = f"{primeira} {segunda}"
        self.label.text = nome_gerado

if __name__ == "__main__":
    GeradorNomeApp().run()