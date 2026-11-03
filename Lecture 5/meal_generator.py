from random import randint
IDLI = 1
DOSA = 2
POHA = 3
UPMA = 4
BREAD_OMLETTE = 5

VEG_BIRYANI = 1
CHICKEN_BIRYANI = 2
DAL_RICE = 3
FRIED_RICE = 4
CHAPATI = 5

ROTI_WITH_CURRY = 1
PANEER_RICE = 2
CHICKEN_CURRY = 3
PULAO = 4 
CURD_RICE = 5

breakfast = randint(1,5)
lunch = randint(1,5)
dinner = randint(1,5)
if breakfast == IDLI:
    breakfast = "IDLI"
elif breakfast == DOSA:
    breakfast = "DOSA"
elif breakfast == POHA:
    breakfast = "POHA"   
elif breakfast == UPMA:
    breakfast = "UPMA"
elif breakfast == BREAD_OMLETTE:
    breakfast = "BREAD OMLETTE"

if lunch == VEG_BIRYANI:
    lunch = "VEG BIRYANI"
elif lunch == CHICKEN_BIRYANI:
    lunch = "CHICKENBIRYANI"
elif lunch == DAL_RICE:
    lunch = "DAL RICE"
elif lunch == FRIED_RICE:
    lunch = "FRIED RICE"
elif lunch == CHAPATI:
    lunch = "CHAPATI"

if dinner == ROTI_WITH_CURRY:
    dinner = "ROTI WITH CURRY"
elif dinner == PANEER_RICE:
    dinner = "PANEER RICE"
elif dinner == CHICKEN_CURRY:
    dinner = "CHICKEN CURRY"
elif dinner == PULAO:
    dinner = "PULAO"
elif dinner == CURD_RICE:
    dinner = "CURD RICE"
output = f"""========== RANDOM MENU GENERATOR ==========

Breakfast: {breakfast}
Lunch: {lunch}
Dinner: {dinner}

==========================================="""
print(output)
