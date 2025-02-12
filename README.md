[FlapPyBird](https://github.com/legrandoc/FlapPyBird)
===============

A Flappy Bird Clone made using [python-pygame][pygame]

Setup (Workshop)
---------------------------

1. Install Python 3 from [here](https://www.python.org/download/releases/) (or use brew/apt/pyenv)

2. Create and activate virtual environment to avoid any conflict with your own python projects:
```bash
# Create virtual environment
python -m venv venv

# Activate it (on Windows):
venv\Scripts\activate
# OR on macOS/Linux:
source venv/bin/activate
```

3. Install invoke:
```bash
pip install invoke
```

4. Initialize the project:
```bash
invoke init
```

5. Run the game:
```bash
invoke run
```
Use `DEBUG=True invoke run` to see rects and coords

6. Use <kbd>&uarr;</kbd> or <kbd>Space</kbd> key to play and <kbd>Esc</kbd> to close the game.

7. Optionally run `invoke web` to run the game in the browser (`pygbag`).

### Testing

Run the tests:
```bash
invoke test
```

Try Cursor out
---------------------------

### Use Cursor chat to help you onboard
For example:
- I’m new to this codebase, could you provide an onboarding overview for me?
- Can you help me understand the codebase?
- How is the code organized?

### Use Cursor agent to add a new functionality
For example:
- Become invulnerable for a few second after a key press
- Add a new powerup that increases the score multiplier for 10 seconds
- Add an explosion animation when losing the game

### Use Cursor agent to generate unit tests specifically on your changes
  @PR (Diff with Main Branch) Can you add unit test for the changes I made?

### Use Cursor agent to refactor the code
For example:
- Can you refactor this code for better maintainability?
- Can you extract this function to a separate file?

### Use Ctrl-K in terminal to write a command
For example:
- What is the command again to rebase my branch on remote master?
- How do I create a new branch?
- How do I squash my commits?
- How to I run the tests?
- How to I run the game?

### Use you imagination to try out even more with Cursor :)

You can find more information about Cursor functionnalities in the [Cursor documentation](https://docs.cursor.com/features/chat)
