from configs import gameConfigs


class Ship:
    """Class representing a ship in the game."""

    width = 71  # Width of the ship
    height = 85  # Height of the ship
    gunLastShot = 0  # Time since the last shot from the ship's gun
    gunDelay = 25  # Delay between shots from the ship's gun
    speed = 5  # Speed of the ship

    def __init__(self, screen, pos, image):
        """
        Initialize the Ship object.

        Args:
            screen: The game screen to render the ship.
            pos: The initial position of the ship (x, y).
            image: The image representing the ship.
        """
        self.x, self.y = pos
        self.image = image
        self.screen = screen

    def update(self):
        """
        Update the ship's position and handle boundaries.

        The ship's position is updated based on its speed.
        The ship is prevented from moving outside the game screen boundaries.
        """
        if self.x >= gameConfigs["width"] - self.width:
            self.x = gameConfigs["width"] - self.width

        if self.x <= 0:
            self.x = 0

        self.render()

    def render(self):
        """Render the ship on the game screen."""
        self.screen.blit(self.image, (self.x, self.y))

    def speedUp():
        """Increase the ship's speed if it is below the maximum speed limit."""
        if Ship.speed <= gameConfigs["maxSpeed"]:
            Ship.speed += 1
