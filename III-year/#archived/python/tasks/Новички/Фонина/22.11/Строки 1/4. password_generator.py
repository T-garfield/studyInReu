first_name = "Родриго"
last_name = "Вильянуэва"

length_fn=len(first_name)
length_ln=len(last_name)

temp_password = first_name[length_fn-3:] + last_name[length_ln-3:]
print(temp_password)
