from rich import print
from rich.prompt import IntPrompt
from tarot import Tarot

from rich.panel import Panel
print(Panel("Lets start your consultation...",
            title="[red]Tarot", subtitle=""))
tarot = Tarot('.tmp')
tarot.generate_library()

number_of_cards = IntPrompt.ask("How many cards do you want?")

print(Panel("1.Show In Desktop(PNG/Jpeg) \n2.ASCII Terminal",
            title="[green]Graphical Options", subtitle=""))

graphic_type = IntPrompt.ask("Graphical format to show these cards ?")


tarot.draw(number_of_cards)
for card in tarot.drawn_cards:
    if graphic_type == 1:
        tarot.show(card)
    if graphic_type == 2:
        tarot.show(card, ASCII=True)
