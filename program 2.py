from random import randint

n = input("Enter the Initial Number of Patient : ")
v = {}
v[0] = int(n)       # patient number
patient = int(n)    # patient number
today_patient = [0]
immune = 0      #count how many people immune
day = 0         # day
count_infected4 = 0 # count how many people infected for 4 days
count_infected5 = 0 # count how many people infected for 5 days


while patient >= 0 and immune <1000000:

    r = randint(1,1000000)      #random number between 1 to 1000000 because total people is 1000000
    v[day+1] = v[day]

    # day begin 
    # because probability R=.10. These are all cells distance one from the infected individual
    # and to individuals in cells distance 2 with probability R=.04.
    # so know 4 people in the edge, 8 people beside the edge, 999*4-4-8 people in else in the outermost edge
    # and 4 people in the second edge, 997*4-4 people else in the second edge, and 996*996 people else 
    for i in range (patient):
        if patient + immune < 1000000:
            if 1 <= r <= 4:
                # 3 people, chance of infection 0.1
                for j in range (3):
                    rv = randint(1,100)
                    if 1 <= rv <= 10:
                        v[day+1] = v[day+1] + 1
                        patient += 1
                # 5 people, chance of infection 0.04
                for j in range (5):
                    rv = randint(1,100)
                    if 1 <= rv <= 4:
                        v[day+1] = v[day+1] + 1
                        patient += 1
            elif 5 <= r <= 12:
                # 5 people, chance of infection 0.1
                for j in range (5):
                    rv = randint(1,100)
                    if 1 <= rv <= 10:
                        v[day+1] = v[day+1] + 1
                        patient += 1
                # 6 people, chance of infection 0.04
                for j in range (6):
                    rv = randint(1,100)
                    if 1 <= rv <= 4:
                        v[day+1] = v[day+1] + 1
                        patient += 1
            elif 13 <= r <= 16:
                # 8 people, chance of infection 0.1
                for j in range (8):
                    rv = randint(1,100)
                    if 1 <= rv <= 10:
                        v[day+1] = v[day+1] + 1
                        patient += 1
                # 7 people, chance of infection 0.04
                for j in range (7):
                    rv = randint(1,100)
                    if 1 <= rv <= 4:
                        v[day+1] = v[day+1] + 1
                        patient += 1
            elif 17 <= r <= 4000:
                # 5 people, chance of infection 0.1
                for j in range (5):
                    rv = randint(1,100)
                    if 1 <= rv <= 10:
                        v[day+1] = v[day+1] + 1
                        patient += 1
                # 9 people, chance of infection 0.04
                for j in range (9):
                    rv = randint(1,100)
                    if 1 <= rv <= 4:
                        v[day+1] = v[day+1] + 1
                        patient += 1
            elif 4001 <= r <= 7984:
                # 8 people, chance of infection 0.1
                for j in range (8):
                    rv = randint(1,100)
                    if 1 <= rv <= 10:
                        v[day+1] = v[day+1] + 1
                        patient += 1
                # 11 people, chance of infection 0.04
                for j in range (11):
                    rv = randint(1,100)
                    if 1 <= rv <= 4:
                        v[day+1] = v[day+1] + 1
                        patient += 1
            # 7984~1000000
            else:
                # 8 people, chance of infection 0.1
                for j in range (8):
                    rv = randint(1,100)
                    if 1 <= rv <= 10:
                        v[day+1] = v[day+1] + 1
                        patient += 1
                # 16 people, chance of infection 0.04
                for j in range (16):
                    rv = randint(1,100)
                    if 1 <= rv <= 4:
                        v[day+1] = v[day+1] + 1
                        patient += 1

    # immune
    today_immune = 0    # count 
    ri = randint(1,10)  #An infected individual recovers after 2, 3, 4, or 5 days
    if day == 1:
        for j in range (v[day-1]):
            # 0.1
            if ri == 1:
                immune += 1
                today_immune += 1
                v[day-1] = v[day-1] - 1
                patient = patient -1

    elif day == 2:
        for j in range (v[day-1]):
            # 0.1
            if ri == 1:
                immune += 1
                today_immune += 1
                v[day-1] = v[day-1] - 1
                patient = patient -1
        for j in range (v[day-2]):
            # 0.2
            if ri == 2 or ri == 3:
                immune += 1
                today_immune += 1
                v[day-2] = v[day-2] - 1
                patient = patient -1

    elif day == 3:
        for j in range (v[day-1]):
            # 0.1
            if ri == 1:
                immune += 1
                today_immune += 1
                v[day-1] = v[day-1] - 1
                patient = patient -1
        for j in range (v[day-2]):
            # 0.2
            if ri == 2 or ri == 3:
                immune += 1
                today_immune += 1
                v[day-2] = v[day-2] - 1
                patient = patient -1
        for j in range (v[day-3]):
            # 0.3
            if ri == 4 or ri == 5 or ri == 6:
                immune += 1
                today_immune += 1
                v[day-3] = v[day-3] - 1
                patient = patient -1

    elif day == 4:
        for j in range (v[day-1]):
            # 0.1
            if ri == 1:
                immune += 1
                today_immune += 1
                v[day-1] = v[day-1] - 1
                patient = patient -1
        for j in range (v[day-2]):
            # 0.2
            if ri == 2 or ri == 3:
                immune += 1
                today_immune += 1
                v[day-2] = v[day-2] - 1
                patient = patient -1
        for j in range (v[day-3]):
            # 0.3
            if ri == 4 or ri == 5 or ri == 6:
                immune += 1
                today_immune += 1
                v[day-3] = v[day-3] - 1
                patient = patient -1
        for j in range (v[day-4]):
            #0.3
            if ri == 7 or ri == 8 or ri == 9:
                immune += 1
                today_immune += 1
                v[day-4] = v[day-4] - 1
                patient = patient -1
                count_infected4 += 1

    elif day >= 5:
        for j in range (v[day-1]):
            # 0.1
            if ri == 1 and patient > 0:
                immune += 1
                today_immune += 1
                v[day-1] = v[day-1] - 1
                patient = patient -1
        for j in range (v[day-2]):
            # 0.2
            if ri == 2 or ri == 3 and patient > 0:
                immune += 1
                today_immune += 1
                v[day-2] = v[day-2] - 1
                patient = patient -1
        for j in range (v[day-3]):
            # 0.3
            if ri == 4 or ri == 5 or ri == 6 and patient > 0:
                immune += 1
                today_immune += 1
                v[day-3] = v[day-3] - 1
                patient = patient -1
        for j in range (v[day-4]):
            #0.3
            if ri == 7 or ri == 8 or ri == 9 and patient > 0:
                immune += 1
                today_immune += 1
                v[day-4] = v[day-4] - 1
                patient = patient -1
                count_infected4 += 1
        for j in range (v[day-5]):
            #0.1
            if patient > 0:
                immune += 1
                today_immune += 1
                v[day-5] = v[day-5] - 1
                patient = patient -1
                count_infected5 += 1

    sick_but_not_immune = 0

    for j in range (today_immune):
        r = randint(1,10)
        if r == 1:
            sick_but_not_immune += 1

    immune = immune - sick_but_not_immune
    patient = patient + sick_but_not_immune

    day = day + 1
    today_patient.append(v[day]-v[day-1])

    if patient >=0 :
        print("Day : "+str(day)+"   Total Patient Number : "+str(patient)+"   Total Immunized People : "+str(immune)+"   Today Patient Number : "+str(today_patient[day])+"   Sick But Not Immune : "+str(sick_but_not_immune))

print("Day : "+str(day)+"   All people healed")
print("Maxima sick a day : "+ str(max(today_patient)))
print("The Average Number of Sick Individuals a Day : "+str(sum(today_patient)/day))
print("Infected for 4 days : "+str(count_infected4)+"    Infected for 5 days : "+str(count_infected5))