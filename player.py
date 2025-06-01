from circleshape import *
from constants import PLAYER_TURN_SPEED, PLAYER_RADIUS, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius, shots):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shots = shots

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Create a shot at the player's position, facing the player's direction
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        self.shots.add(shot)
        return shot

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt