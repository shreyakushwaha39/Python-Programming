#wap that create two dictionaries .one that store conversion value from meter to centimeter 
# and the other that store values from cm to m
m_to_cm={i:i*100 for i in range(1,11)}
cm_to_m={i*100:i for i in range(1,11)}
print("meter to centimeter:",m_to_cm)
print("centimeter to meter:",cm_to_m)