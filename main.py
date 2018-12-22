print ("This program is version 0.01")
print ("Autor is Artur Kaktus Milovidov")
print ("github.com/ArturKaktus/SoccerPredictor")
print ("\n\n\n")

max_places = input("How many places in the standings? ")

print ("\n1. Home")
hm_place = input("Place in the standings ")
hm_balls = input("How many balls scored? ")
hm_balls_last = input("How many balls scored in the last 3 game? ")
hm_games = input("How many games are played per season? ")

print ("\n2. Guest")
gst_place = input("Place in the standings ")
gst_balls = input("How many balls scored? ")
gst_balls_last = input("How many balls scored in the last 3 game? ")
gst_games = input("How many games are played per season? ")

if hm_balls  > gst_balls:
    val_1 = float(hm_balls) - float(gst_balls)
else:
    if gst_balls > hm_balls:
        val_1 = float(gst_balls) - float(hm_balls)
    else:
        val_1 = 0

hm_score = (float(max_places) - float(hm_place)) + ((float(hm_balls_last) * 3) / 2)
gst_score = (float(max_places) - float(gst_place)) + ((float(gst_balls_last) * 3) / 2)

if hm_balls > gst_balls:
    hm_score += val_1
else:
    hm_score += 0

if gst_balls > hm_balls:
    gst_score += val_1
else:
    gst_score += 0
      
hm_score_total = float(hm_score) * (float(hm_balls) / float(hm_games))
gst_score_total = float(gst_score) * (float(gst_balls) / float(gst_games))

total_win = float(max_places) - 1 + 5 + ((float(hm_games)+float(gst_games))/2)+(((float(hm_balls)+float(gst_games))/2)/2) - 2

hm_win = (float(hm_score) / float(total_win)) * 100
gst_win = (float(gst_score) / float(total_win))* 100

val_2 = (((float(hm_balls)/float(hm_games))+float(hm_balls_last)/3)+(float(gst_balls)/float(gst_games)+float(gst_balls_last)/3))/2
val_3_1=(float(hm_games)+float(gst_games))/2
val_3 = ((float(val_3_1)/4)*3+(float(val_3_1)/2)+float(val_3_1)+(float(val_3_1)/5)*4)/float(val_3_1)
total_more = (float(val_2)/float(val_3))*100-10

print("\n###################################")
print("Home win: ", hm_win,"%")
print("Guest win: ", gst_win,"%")
print("Draw: ", 100-(hm_win+gst_win),"%")
print("###################################")
print("Total More 2.5: ", total_more,"%")
print("Total Less 2.5: ", 100-total_more,"%")
input()