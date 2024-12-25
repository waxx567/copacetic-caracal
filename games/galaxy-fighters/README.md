### README: Galaxy Fighters Game

---

## Introduction

**Galaxy Fighters** is a 2D multiplayer space-themed shooter game built using Python's `pygame` library. It features two spaceships that battle against each other by firing bullets and maneuvering around the screen. The game is fast-paced and designed to provide an engaging player-versus-player experience.

---

## Features

1. **Multiplayer Gameplay**: Two players can compete on the same keyboard.
2. **Dynamic Graphics**: Includes spaceships, bullets, and a galactic background.
3. **Health Tracking**: Each player has 10 health points, displayed on the screen.
4. **Customizable Controls**: Players control their spaceship with the keyboard.
5. **Victory Screen**: Displays the winner at the end of the match.
6. **Smooth Animations**: Runs at 60 FPS for fluid gameplay.

---

## Controls

### Yellow Spaceship (Player 1)

- **Move Up**: `W`
- **Move Down**: `S`
- **Move Left**: `A`
- **Move Right**: `D`
- **Shoot**: `Left Ctrl`

### Red Spaceship (Player 2)

- **Move Up**: `Arrow Up`
- **Move Down**: `Arrow Down`
- **Move Left**: `Arrow Left`
- **Move Right**: `Arrow Right`
- **Shoot**: `Right Ctrl`

---

## Gameplay

- Players maneuver their spaceships and shoot bullets to hit their opponent.
- Each successful hit reduces the opponent's health by 1 point.
- A player wins when the opponent's health reaches 0.
- Bullets are limited to 3 active shots per player at a time.
- Movement is restricted by the game's border and a central divider.

---

## Prerequisites

- Python 3.7 or later.
- `pygame` library installed.

To install `pygame`, run:
```bash
pip install pygame
```

---

## Setup Instructions

1. Clone or download this repository.
2. Ensure the following directory structure:
   ```
   Galaxy_Fighters/
   ├── main.py
   ├── Assets/
       ├── spaceship_yellow.png
       ├── spaceship_red.png
       ├── space.png
       ├── Grenade+1.mp3 (optional)
       ├── Gun+Silencer.mp3 (optional)
   ```
3. Place all asset files in the `Assets` folder.

---

## Running the Game

1. Open a terminal and navigate to the game directory.
2. Run the game with:
   ```bash
   python main.py
   ```
3. Enjoy the game!

---

## Customization

### Modifying Game Settings

You can tweak the following variables in the code:
- **Screen Dimensions**: Modify `WIDTH` and `HEIGHT`.
- **Spaceship Speed**: Adjust `VEL`.
- **Bullet Speed**: Adjust `BULLET_VEL`.
- **Maximum Bullets**: Change `MAX_BULLETS`.
- **Health Points**: Update the initial values of `red_health` and `yellow_health`.

### Adding Sounds

Uncomment the lines for `BULLET_HIT_SOUND` and `BULLET_FIRE_SOUND` in the `main` function and ensure the corresponding sound files are in the `Assets` folder.

---

## Known Issues

Sound effects are commented out by default and require manual setup.

---

## Future Improvements

1. Add AI functionality for single-player mode.
2. Include power-ups and obstacles.
3. Implement network multiplayer support.

---

## License

This project is open-source and available for modification and personal use. 

---

## Acknowledgments

- [Tech With Tim](https://www.youtube.com/@TechWithTim)
- Background and spaceship assets from free online resources.
- Built using the `pygame` library for game development.

Happy gaming! 🚀
