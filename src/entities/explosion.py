from ..utils import GameConfig
from .entity import Entity


class Explosion(Entity):
    def __init__(self, config: GameConfig, x: float, y: float) -> None:
        # Start with first explosion frame
        super().__init__(
            config=config,
            image=config.images.explosion[0],
            x=x,
            y=y,
        )
        self.frame = 0
        self.animation_speed = 2  # Lower = faster
        self.frame_count = 0
        self.complete = False

    def draw(self) -> None:
        if self.complete:
            return

        self.frame_count += 1
        if self.frame_count % self.animation_speed == 0:
            self.frame += 1
            if self.frame >= len(self.config.images.explosion):
                self.complete = True
                return

            # Update to next explosion frame
            self.update_image(self.config.images.explosion[self.frame])

        super().draw()
