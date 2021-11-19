import streamlit as st
import PIL, random, sys
from PIL import Image, ImageDraw

def random_colors():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def create_invader(border, draw, sprite_size):
    x0, y0, x1, y1 = border
    squareSize = (x1-x0)/sprite_size
    randColors = [random_colors(), random_colors(), random_colors(), (0,0,0), (0,0,0), (0,0,0)]
    for y in range(0, sprite_size):
        listSym = []
        for x in range(0, sprite_size):
            topLeftX = x*squareSize + x0
            topLeftY = y*squareSize + y0
            botRightX = topLeftX + squareSize
            botRightY = topLeftY + squareSize
            if len(listSym)<(sprite_size/2):
                listSym.append(random.choice(randColors))
            else:
                listSym.append(listSym[sprite_size-x-1])
            draw.rectangle((topLeftX, topLeftY, botRightX, botRightY), listSym[x])
    return None

def gen(sprite_size, invaders, imgSize):
    origDimension = imgSize
    origImage = Image.new('RGB', (origDimension, origDimension))
    draw = ImageDraw.Draw(origImage)
    invaderSize = origDimension/invaders
    padding = invaderSize/sprite_size
    for x in range(0, invaders):
        for y in range(0, invaders):
            topLeftX = x*invaderSize + padding
            topLeftY = y*invaderSize + padding
            botRightX = topLeftX + invaderSize - padding*2
            botRightY = topLeftY + invaderSize - padding*2
            create_invader((topLeftX, topLeftY, botRightX, botRightY), draw, sprite_size)
    return origImage

def main():
    st.header("Space invader sprite generator")
    st.markdown("""This is based on the [code](https://github.com/erdavids/Space-Invaders) in [Eric Davidson's](https://www.erdavids.com/) [article](https://www.freecodecamp.org/news/how-to-create-generative-art-in-less-than-100-lines-of-code-d37f379859f/) on [freecodecamp](https://www.freecodecamp.org/news/) """, unsafe_allow_html=True)

    img_size = st.slider('Image Size', 300, 2000, 1500, 50)
    invaders = st.slider('No. of invaders', 2, 32, 4)
    sprite_size = st.slider('Sprite dimensions', 3, 32, 7)
    if st.button("Generate"):
        my_canvas = gen(sprite_size, invaders, img_size)
        st.write(my_canvas)
        st.image(my_canvas)

    return None

if __name__ == '__main__':
    main()