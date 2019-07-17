###
### Author: Abhishek Agarwal
### Description: This program is a pictureable form of Nebulon Spaceship. 
###              It generally takes six inputs to built it structure. 
###              The layers at the bottom are dependable on the front length input by the user
print("Large Layers on bottom:")
larlay=int(input())# TAKE INPUT FOR THE LARGE LAYER
print("Medium Layers on bottom:")
medlay=int(input())# TAKE INPUT FOR THE MEDIUM LAYER
print("Small Layers on bottom:")
smalllay=int(input())# TAKE INPUT FOR THE SMALL LAYER
print("Front length:")
frolen=int(input()) # TAKE INPUT FOR FRONT BODY WIDTH
print("Middle length:")
middlen=int(input())# TAKE INPUT FOR THE MIDDLE BODY WIDTH
print("Back length:")
backlen=int(input())# TAKE INPUT FOR THE BACK BODY WIDTH
print()
Large_length=(frolen-3) #LENGTH OF LARGE LAYER
Medium_length=int(frolen/2)# TO ROUND THE VALUE DOWN AND DECIDE LENGTH OF MEDIUM LAYER
Small_length=int(frolen/3) # LENGTH OF SMALL LAYER
print("  /=" + "-" * frolen + "\\" + " " * (9 + middlen) + "/" + "-" * backlen + "|")
print(" /==" + "/" * frolen + "==\\\\\\" + " " * (4 + middlen) + "|=" + "=" * backlen + "|")
print("|==-" + "\\" * frolen + "======\\--" + "=" * (middlen + backlen + 2) + "|")
print(" \==" + "=" * frolen + "==-------" + "-" * (middlen + backlen + 2) + "|")
print("  \\=" + "-" * frolen+"=///" + " " * (5 + middlen) + "\\=" + "=" * (backlen) + "/")
print(("   /" + "-"*Large_length + "|" + "\n" + "   \\" + "="*Large_length + "|" + "\n") * larlay , end='')
print(("    " + " "*(Large_length - Medium_length - 1) + "/" + "+"*Medium_length + "|" + "\n"
      +"    " + " "*(Large_length - Medium_length-1) + "\\" + "-"*Medium_length + "|" + "\n") * medlay , end='')  
print(( " " * (frolen-Small_length-1) + "\\" + "<"*Small_length + "|" + "\n"
      +" " * (frolen-Small_length-1) +" "+ "<"*Small_length + "|" + "\n") * smalllay , end='')
 
