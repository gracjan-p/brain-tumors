![bg](./media/bg.png)

# Brain tumors
In this project I analyzed 'Brain tumor dataset', a T1 weighted image dataset from figshare. <br>
The project is in jupyter notebook format (.ipynb) that shows the process of data analysis and building models.

### Libraries I've used:
- ***tensorflow, keras, sklearn*** for machine learning
- ***numpy, scipy, random*** for numerical operations
- ***matplotlib, seaborn*** for plotting
- ***os, cv2*** for loading images<br>
*for specific versions check *requirements.txt*

### The full process includes:
1) **Data exploration**
   - Image extraction
   - Splitting Data
   - Preview images
   - Black/White balance
   - Skull size
   - Class weights
   - Feature scaling

2) **1st Model (tumor type)**
   - Building a model
   - Visualising results
   - Testing the model

3) **Predicting tumor location**
   - Mask extraction
   - Splitting Data
   - Preview the masks
   - Tumor size
   - Feature scaling

4) **2nd Model (tumor location)**
5) **Conclusion**

### What I achieved:
- AI model that predicts tumor type with accuracy of roughly 95%
- AI model that predicts tumor location based on predicted binary mask

### Future ideas:
- filter out certain head size
- border box around predicted tumor localization
- finish full web/desktop application

# Example features I extracted from data
### Head size
I calculated amount of white pixels inside image.
In summary this plot returns images where head fills specified % of area in image.

![skull-size-1](./media/skull-size.png)
![skull-size-2](./media/skull-size-2.png)

### Tumor size
Similarly to head size I also calculated amount of white pixels inside,<br>
but this time I used tumor border coordinates to create binary mask and then counted the white pixels in it.

![tumor-size-1](./media/tumor-size.png)
![tumor-size-2](./media/tumor-size-2.png)
