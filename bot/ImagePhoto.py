from captcha.image import ImageCaptcha
from random import choice

class Image:
    def generated_capthca(self):
        a = 6
        alphabet = ['1','2','3','4','5','6','7','8','9',
                   'a','b','c','d','e','f','g','h','i',
                   'j','k','l','m','n','o','p','q','r',
                   's','t','u','v''w','x','y','z']

        pattern = []

        for i in range(a):
            pattern.append(choice(alphabet))

        image_captcha = ImageCaptcha(width=300, height=300)
        image_captcha.write(pattern, 'captcha.png')
        return pattern

image = Image()