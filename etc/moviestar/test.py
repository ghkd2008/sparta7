order_list = [{"menu_name" : "메뉴1", "order_quantity" : 2},{"menu_name" : "메뉴2", "order_quantity" : 1},{"menu_name" : "메뉴3", "order_quantity" : 3}]

key = ['설탕', '소금', '후추',]
val = [1,2,3]
val2= []
for i in val:
    val2.append(i*order_list[0]["order_quantity"])
kv = [key, val2]
ingredient_type_dict = dict(zip(*kv))

print(ingredient_type_dict)