---
layout: default
title: Text-Based Video Game
description: A Python console adventure where the player collects items without waking the toddler.
tech: [Python, Console App, Game Logic]
link: https://github.com/EricaBoterf/TextBasedGame
---

This game prints instructions, lets you move by **North/South/East/West**, **retrieve items** from rooms, and you **lose if you enter the room with the sleeping toddler** (wake the toddler). Win by collecting all items. :contentReference[oaicite:0]{index=0}


<details class="mt-3" markdown="1">
  <summary class="cursor-pointer text-blue-600 hover:underline font-semibold">
    Show Sample Code
  </summary>

```python
def main():
    current_room = 'Living Room'
    inventory = []

    show_instructions()

    while True:
        show_status(current_room, inventory)
        move = input('> ').title().split()

        if move[0] == 'Go':
            if move[1] in rooms[current_room]:
                current_room = rooms[current_room][move[1]]
                if current_room == 'Laundry':
                    print("The toddler wakes up... Game Over!")
                    break
            else:
                print("You can't go that way!")
        elif move[0] == 'Get':
            if 'item' in rooms[current_room] and move[1] == rooms[current_room]['item']:
                inventory.append(move[1])
                print(f"{move[1]} collected!")
                del rooms[current_room]['item']
            else:
                print("Can't get that!")

### How to run locally
```bash
python assets/code/TextBasedGame.py