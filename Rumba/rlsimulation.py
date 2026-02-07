import numpy as np
import random

# 1. Setup Environment
grid_size = 10
q_table = np.zeros((grid_size, grid_size, 4))  # 10x10 grid, 4 actions (0:Up, 1:Down, 2:Left, 3:Right)
learning_rate = 0.1
discount_factor = 0.95
epsilon = 0.1  # Exploration rate
episodes = 5000

dirt_pos = (5, 6)
dock_pos = (0, 0)

# 2. Training Loop
for i in range(episodes):
    state = [0, 0]  # Start at (0,0)
    found_dirt = False
    done = False
    
    while not done:
        # Choose action (Exploration vs Exploitation)
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(q_table[state[0], state[1]])

        # Move logic
        next_state = list(state)
        if action == 0 and state[1] < 9: next_state[1] += 1 # Up
        elif action == 1 and state[1] > 0: next_state[1] -= 1 # Down
        elif action == 2 and state[2] > 0: next_state[0] -= 1 # Left
        elif action == 3 and state[0] < 9: next_state[0] += 1 # Right

        # 3. Reward System
        reward = -0.1  # Small penalty for every move (encourages speed)
        
        if tuple(next_state) == dirt_pos and not found_dirt:
            reward = 10
            found_dirt = True
        
        if found_dirt and tuple(next_state) == dock_pos:
            reward = 20
            done = True # Goal reached!

        # 4. Update Q-Table (Bellman Equation)
        old_value = q_table[state[0], state[1], action]
        next_max = np.max(q_table[next_state[0], next_state[1]])
        
        # New Q-value calculation
        q_table[state[0], state[1], action] = (1 - learning_rate) * old_value + \
                                              learning_rate * (reward + discount_factor * next_max)
        
        state = next_state