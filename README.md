[FlapPyBird](https://github.com/legrandoc/FlapPyBird)
===============

A Flappy Bird Clone made using [python-pygame][pygame]

Setup (Workshop - crossplatform)
---------------------------

1. Install Python 3 from [here](https://www.python.org/download/releases/) (or use brew/apt/pyenv)

2. Install invoke:
```bash
pip install invoke
```

3. Initialize the project:
```bash
invoke init
```

4. Run the game:
```bash
invoke run
```
Use `DEBUG=True invoke run` to see rects and coords

5. Use <kbd>&uarr;</kbd> or <kbd>Space</kbd> key to play and <kbd>Esc</kbd> to close the game.

6. Optionally run `invoke web` to run the game in the browser (`pygbag`).


Setup (MacOS)
---------------------------

1. Install Python 3 from [here](https://www.python.org/download/releases/) (or use brew/apt/pyenv)

2. Run `make init` (this will install pip packages, use virtualenv or something similar if you don't want to install globally)

3. Run `make` to run the game. Run `DEBUG=True make` to see rects and coords

4. Use <kbd>&uarr;</kbd> or <kbd>Space</kbd> key to play and <kbd>Esc</kbd> to close the game.

5. Optionally run `make web` to run the game in the browser (`pygbag`).


Demo
----------

https://user-images.githubusercontent.com/2307626/130682424-9254b32d-efe0-406e-a6ea-3fb625a2df5e.mp4
