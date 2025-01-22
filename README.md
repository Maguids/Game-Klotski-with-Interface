# Game - Kslotski (Terminal Version)

This project was developed for the "Elements of Artificial Intelligence and Data Science" course and aims to **develop and implement a solitaire game**. The project should include the use of **heuristic search methods and uninformed search methods** that should be able to **solve different versions or levels of this game** and a **graphical interface.**

**Authors:**
- [Magda Costa](https://github.com/Maguids)
- Sofia Machado

<br></br>

## Programming Language:

<div style = "display: inline_block"><br/>
  <img align="center" alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
</div><br/>

<br></br>

## Requirements:

- python version 3.8.10
- pygame version 1.9.6

This were the tested requirements.
In order to install pygame run:
```bash 
pip install pygame==1.9.6
```

<br></br>

## Running the Game:
In order to start the game, just run:

```bash 
python3 start.py
```

<br></br>

## About the Game:

### How to play:
Klotski is a version of the "PuzzlePacked IQ games", in which the objective of the game is to move the largest block and position it in the right place. To do this, you need to move a set of smaller blocks, allowing the larger block to move. Each block occupies one or more cells, and blocks can move in any of the four cardinal directions (up, down, left, or right) as long as there are no obstacles in the way.

### Search Algorithms:
- **Breadth-First Search (BFS)**;
- **Greedy Best-First Search** - with Manhattan distance;
- **A\* Algorithm** (A Star) - with Manhattan distance.

### Features:
- You can choose whether you want to **play in the terminal** or in **the graphical interface** developed in **pygame**;

**In Terminal Mode:**
- Possibility to **choose different boards with different levels of difficulty**;
- Possibility to return to the **Menu** at any time by typing 'menu'
- It is possible to **restart** the chosen level by typing 'r';
- Possibility to **end the game** at any time by typing 'quit';
- Option to **choose the desired search algorithm**;
- **Hint function**, which varies depending on the search algorithm used, which shows the next possible move, just type 'hint'.

**In Pygame Mode:**
Same features, the only difference is that you have buttons to use the features, no need to type anything.
**New Feature:** **<u>Colorblind Mode</u>** - The pieces may or not be identified with numbers, to help better distinguish them.

## About the repository:
In the folder <u>"Klotski"</u>, you can find several files, each of which is assigned to a specific set of tasks, which are:

**Regardless of the game mode:**
- levels.py ➡️ Has five different game boards of each of the three difficulties;
- creat_board.py ➡️ Function that allows to create the board depending on the chosen level;
- game.py ➡️ Development of the game Klotski, has all the functions that allows it to work; 
- a_star.py ➡️ Development of A*;
- bfs.py ➡️ Development of BFS;
- greedy.py ➡️ Development of Greedy;
- start.py ➡️ Starts the functioning of everything and lets you choose either pygame ou terminal version;

**In terminal mode:**
- menu_terminal.py ➡️ Explains the functionalities of the game and lets you choose the level and the difficulty;
- play_in_terminal.py ➡️ Starts the game according to what was chosen in the menu and allows you to use 'Hint';

**In Pygame Mode:**
- menu_pygame.py ➡️ It allows you to choose the game difficulty, the desired level, the search method to use and whether or not we are using colorblind mode.
- play_in_pygame.py ➡️ Starts the game according to what was chosen in the menu;
- settings.py ➡️ Allows you to save pygame mode settings and define the Button class

Note: The development of the search algorithms' operating mode is based on the way the game was created

<br></br>

## Link to the course: 

This course is part of the **<u>second semester</u>** of the **<u>first year</u>** of the **<u>Bachelor's Degree in Artificial Intelligence and Data Science</u>** at **<u>FCUP</u>** and **<u>FEUP</u>** in the academic year 2022/2023. You can find more information about this course at the following link:

<div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
  <a href="hhttps://sigarra.up.pt/fcup/pt/UCURR_GERAL.FICHA_UC_VIEW?pv_ocorrencia_id=507945">
    <img alt="Link to Course" src="https://img.shields.io/badge/Link_to_Course-0077B5?style=for-the-badge&logo=logoColor=white" />
  </a>

  <div style="display: flex; gap: 10px; justify-content: center;">
    <a href="https://sigarra.up.pt/fcup/pt/web_page.inicial">
      <img alt="FCUP" src="https://img.shields.io/badge/FCUP-808080?style=for-the-badge&logo=logoColor=grey" />
    </a>
    <a href="https://sigarra.up.pt/feup/pt/web_page.inicial">
      <img alt="FEUP" src="https://img.shields.io/badge/FEUP-808080?style=for-the-badge&logo=logoColor=grey" />
    </a>
  </div>
</div>
