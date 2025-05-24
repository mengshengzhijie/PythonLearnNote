"""
Created by MengShengZhiJie 2025/5/24 09:35
"""
# #元组
# Tuple = (1,2,3,4,5)
# print(type(Tuple)) #<class 'tuple'>

dic = {
    'name' : 'zhansan',
    'age' : 18
}
print(dic) #  {'name': 'zhansan', 'age': 18}
print(dic['name']) # zhansan
print(dic.get('name')) # zhansan
print(dic.get('sex','None')) # None

dic['age'] = 19
dic['sex'] = 'male'
print(dic) # {'name': 'zhansan', 'age': 19, 'sex': 'male'}
#有则修改没有则添加

del dic['sex']
print(dic) # {'name': 'zhansan', 'age': 19}
#不存在会报错
