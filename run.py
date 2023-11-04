from rich import print
from rich.prompt import Prompt, IntPrompt
from tarot import Tarot

from rich.panel import Panel
print(Panel("Lets start your consultation...", title="[red]Tarot", subtitle=""))
tarot = Tarot('.tmp')
tarot.generate_library()

number_of_cards = IntPrompt.ask("How many cards do you want?")


tarot.draw(number_of_cards)
for card in tarot.drawn_cards:
    tarot.show(card)