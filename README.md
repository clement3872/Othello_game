# Othello Game

## Overview
This Othello game project encompasses a complete set of functionalities for playing the Othello board game, including music playback, game logic, and an AI opponent using the Minimax algorithm. Each module is designed to work together to offer an engaging and interactive game experience.

## Modules

### 1. Musik
Manages all music and audio-related functionalities, enabling audio playback and volume adjustments to enhance the gaming experience.

### 2. Launcher
Serves as the main executable script that initializes and launches the game components, ensuring all modules are loaded and integrated correctly.

### 3. Interface
Oversees the graphical user interface, handling user inputs and visual outputs, facilitating interaction during gameplay.

### 4. Connection
Responsible for managing network or database connections if needed, ensuring robust data communication and management.

### 5. Board
Contains the logic for managing the Othello game board states, processing player moves, and enforcing game rules.

### 6. AI
Implements the Minimax algorithm for the AI opponent, providing a challenging and strategic gameplay experience where players compete against a computer-controlled opponent.

## Installation

To run this Othello game, you will need Python installed along with the following packages:
- `playsound` for handling in-game music and sound effects. 
- `wheel` or `patch` might be necessary on some systems to facilitate the installation of `playsound`.

You can install the required packages using pip:
```bash
pip install --upgrade wheel
pip install playsound
```

If you are on Linux, especially on a Arch-based distribution:

```bash
sudo pacman -S python-wheel
yay -S python-playsound
```

## Running

After you've installed all the packages needed, you can play by entering this command:

```bash
python connection.py
```
