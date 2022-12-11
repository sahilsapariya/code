from captcha.image import ImageCaptcha
 
# Create an image instance of the given size
image = ImageCaptcha(width = 380, height = 100)
 
# Image captcha text
captcha_text = 'GeeksforGeeks' 
 
# generate the image of the given text
data = image.generate(captcha_text) 
 
# write the image on the given file and save it
image.write(captcha_text, 'CAPTCHA.png')