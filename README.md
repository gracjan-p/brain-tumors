<div class="img-bg">
    <img src="./media/bg.png">
</div>

# Predicting tumor type and it's location
In this project I analyzed 'Brain tumor dataset', a T1 weighted image dataset from figshare.
The project is in notebook format (.ipynb) that shows the process of data analysis and building models.

### In this project you will find:
- Image data analysis
- Preprocessing image data
- Creating neural network models with TensorFlow and Keras

### What I achieved:
- AI model that predicts tumor type with accuracy of roughly 95%
- AI model that predicts tumor location based on predicted binary mask

# Example features I extracted from data
### Head size
I calculated amount of white pixels inside image.
In summary this plot returns images where head fills specified % of area in image.

<img src="./media/skull-size.png">
<img src="./media/skull-size-2.png">

### Tumor size
Similarly to head size I also calculated amount of white pixels inside,<br>
but this time I used tumor border coordinates to create binary mask and then counted the white pixels in it.

<img src="./media/tumor-size.png">
<img src="./media/tumor-size-2.png">