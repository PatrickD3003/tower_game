import pygame
import math

class ProjectileSprite(pygame.sprite.Sprite):
    GRAVITY = -9.8

    def __init__(self, bitmap, unit, velocity=0, angle=0):
        super(ProjectileSprite, self).__init__(self)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.image = bitmap
        self.unit = unit
        self.rect = bitmap.get_rect()
        self.team = unit.team
        if self.team == "1":
            self.start_x = unit.rect.x + unit.rect.get_width()
        else:
            self.start_x = unit.rect.x
        self.start_y = self.h - self.rect.height
        self.rect.center = ((self.start_x, self.start_y))
        # Physics
        self.setInitialVelocityRadians(velocity, angle)

    def setInitialVelocityRadians( self, velocity, angle_rads):
        global NOW_MS
        self.start_time = NOW_MS
        self.velocity = velocity
        self.angle = angle_rads

    def update(self):
        global NOW_MS
        if (self.velocity > 0):
            time_change = (NOW_MS - self.start_time) / 150.0  # Should be 1000, but 100 looks better
            if (time_change > 0):

                # re-calcualte the velocity
                half_gravity_time_squared = self.GRAVITY * time_change * time_change / 2.0
                displacement_x = self.velocity * math.sin(self.angle) * time_change 
                displacement_y = self.velocity * math.cos(self.angle) * time_change + half_gravity_time_squared

                # reposition sprite
                self.rect.center = ( ( self.start_x + int( displacement_x ), self.start_y - int( displacement_y ) ) )

                # Stop at the bottom of the window
                if (self.rect.y >= self.h - self.rect.height):
                    self.rect.y = self.h - self.rect.height
                    self.velocity = 0
                    self.kill