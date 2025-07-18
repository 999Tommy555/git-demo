a=eval(input("請輸入a:"))
b=eval(input("請輸入b:"))
if a>b:
    print(f"a比b大{a-b}")
elif b>a:
    print(f"b比a大{b-a}")
else:
    print("a跟b一樣大")