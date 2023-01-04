
print("If you want become your 'BMI' enter, please :" )
height = input("HEIGHT : ")
weight = input("WEIGHT: ")

height.strip()
weight.strip()
separator1= height.index(" ")
separator2=weight.index(" ")
height_val = float(height[0:separator1])
weight_val = float(weight[0:separator2])

#height
if height.endswith("m"):
    height_val=height_val
elif height.endswith("ft"):
    height_val= height_val * 30.48
elif height.endswith("cm"):
    height_val=height_val/100

#for Weigh
if weight.endswith("kg"):
    weight_val= weight_val
elif weight.endswith("lb"):
    weight_val = weight_val*0.454

bmi = float(weight_val / (height_val * height_val))
print("Your BMI is : ", "%.2f" % bmi)

