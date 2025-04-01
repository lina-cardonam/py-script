import pandas as pd;

class Color:
    def __init__(self, className, name,):
        self.className = className;
        self.name = name;
       
COLOR_CLASS = "Color"; 
colors = ["Blue", "Orange", "Green", "Brown", "Slate", "White", "Red", "Black", "Yellow", "Violet", "Rose", "Aqua"]

colors_out = [{"className": COLOR_CLASS, "name": color} for color in colors]
    
headers = ["className", "name"]

df = pd.DataFrame(colors_out, columns=headers)

df.to_csv("src/files_out/COLORS.csv", index=False, encoding="utf-8", sep=";")