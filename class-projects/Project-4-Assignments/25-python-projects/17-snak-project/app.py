import pygame, random
pygame.init()

# Game constants
W, H, G = 600, 400, 20  # Width, Height, Grid size
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")

class Snake:
    def __init__(self):
        self.b = [[100, 100]]  # Snake body starting position
        self.d = "RIGHT"       # Initial direction
    
    def move(self):
        # Create new head position based on current direction
        h = self.b[0][:]
        if self.d == "UP": h[1] -= G
        elif self.d == "DOWN": h[1] += G
        elif self.d == "LEFT": h[0] -= G
        elif self.d == "RIGHT": h[0] += G
        
        # Add new head and remove tail
        self.b.insert(0, h)
        self.b.pop()
    
    def grow(self):
        # Add new segment by duplicating tail
        self.b.append(self.b[-1][:])
    
    def collide(self):
        # Check wall collision and self-collision
        return (self.b[0][0] < 0 or self.b[0][0] >= W or
                self.b[0][1] < 0 or self.b[0][1] >= H or
                self.b[0] in self.b[1:])
    
    def draw(self):
        # Draw each segment of the snake
        [pygame.draw.rect(win, (0, 255, 0), (x, y, G, G)) for x, y in self.b]

class Food:
    def __init__(self):
        self.p = self.spawn()  # Initial food position
    
    def spawn(self):
        # Generate random position aligned with grid
        return [random.randrange(0, W, G), random.randrange(0, H, G)]
    
    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (*self.p, G, G))

def main():
    s, f = Snake(), Food()  # Create snake and food
    clock = pygame.time.Clock()
    
    while True:  # Main game loop
        win.fill((0, 0, 0))  # Clear screen
        
        # Event handling
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Keyboard controls (prevent 180° turns)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and s.d != "DOWN": s.d = "UP"
        if keys[pygame.K_DOWN] and s.d != "UP": s.d = "DOWN"
        if keys[pygame.K_LEFT] and s.d != "RIGHT": s.d = "LEFT"
        if keys[pygame.K_RIGHT] and s.d != "LEFT": s.d = "RIGHT"
        
        # Game logic
        s.move()  # Move snake
        
        # Check food collision
        if s.b[0] == f.p:
            s.grow()    # Grow snake
            f.p = f.spawn()  # New food position
        
        # Check game over conditions
        if s.collide():
            print("Game Over!")
            pygame.quit()
            return
        
        # Draw everything
        s.draw()
        f.draw()
        pygame.display.update()
        clock.tick(10)  # Control game speed (10 FPS)

if __name__ == "__main__":
    main()