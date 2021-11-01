#Python dictionary

dic={"Saddaam":1213, "Rayhan":1245}
print(dic)

#Length of the Dictionary
print("Length Of the Dictionary: ",len(dic))

#Another Dictionary
dic2={"islam":0000, "Biology": 4587, "Human Rights":6525,"Political Science":1542}
print(dic2)
print("Length of the Second Dictionary",len(dic2))

#Another Dictionary including list
dic3={'color':["pink", "Blue","Red"], "Br" :[1,2,3,5,4]}
print(dic3)
print("Length of the third Disctionary",len(dic3))
print(dic3.keys())

#Adding items into the dictionary
dic3["Model"]=["forshe", "lamborgini","BMW"]
print(dic3)

#Adding with different way
dic3.update({"Quantity":[1,2,3,4]})
print(dic3)
print(len(dic3))

#remove the values of the dictionary
del dic
print("After Delete what is exist in dic ",dic)


