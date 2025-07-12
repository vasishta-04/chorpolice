# ChorPolice

->Description

This project is a **Chor-Police-style game**, but instead of manual controls, the Thief(chor) character is controlled by an **AI bot using the Minimax algorithm with Alpha-Beta Pruning**. Meanwhile, the Police utilize **Depth-First Search (DFS) with a probability-based movement strategy** to create dynamic and unpredictable gameplay.

-> Features

**Thief(chor)**  
  - Uses **Minimax Algorithm with Alpha-Beta Pruning** to determine the best moves.  
  - Considers multiple steps ahead to **maximize score and minimize danger**.
  - Uses **Minimax algorithm with a depth limiting** strategy to reduce the computation.

**Polices (2)**
  - Moves using **Depth-First Search (DFS)**.
  - Initialised with random start co-ordinates where neither Pac-man nor walls are present.
  - Has a configurable probability to **introduce randomness in movement**, making gameplay more challenging.  

**Game Mechanics**  
  - Classic **maze-based gameplay** inspired by Chor-Police.
  - **Score-based rewards** for collecting " * " and avoiding Polices.  
  - Adjustable **difficulty settings** for AI complexity.  



https://github.com/user-attachments/assets/16d44380-fdc2-4d68-a1d3-574f499225f0

