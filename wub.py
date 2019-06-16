class Ball(object):
    def __init__(self, param="regular"):
        if len(param) != 0:
            self.type = 'super'
        else:
            self.type = 'regular'

ball = Ball()
print(ball.type)
ball2 = Ball('normal')
print(ball2.type)