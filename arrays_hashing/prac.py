def train_model(model_name , *args , **kwargs ):
    print(f"model name is {model_name}")
    print(f"dimensions are {args}")
    print(f"hyperparameters are {kwargs}")
train_model("CNN" , 10 , 20 , 30 , learning_rate = 0.01 , batch_size = 32)

aqi_data = [45, 120, 350, 50, 210]
list1 = list(filter(lambda x :x>200 , aqi_data))
print(list1)