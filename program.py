from random import randint

# case 1    p = 1,000,000    v = 10    m = 5    r = 0.1

print("Case 1 : ")

total_people = 1000000

total_virus = 0
patient = 10
people_infected_today = [0]
# i is day
i = 0

while patient>=0:
    # Immunized 3 days after getting the virus, 
    # so no one has immunized in the first 3 days
    if i<3:
        random = randint(0,5)
        #Calculate how many people will be infected
        people_infected_today.append(round((total_people - patient)/total_people * patient * 0.1 * random))
        i = i + 1
        patient = patient + people_infected_today[i]
        total_virus = total_virus + people_infected_today[i]
        print("Day : "+str(i)+"   Total Patient : "+str(patient)+"   Today Patient : "+str(people_infected_today[i]))
    elif i>=3:
        immune = 10
        #Calculate how many people are immune
        for j in range (len(people_infected_today)-3):
            immune = immune + people_infected_today[j]
        random = randint(0,5)
        people_infected_today.append(round((total_people - immune - patient)/total_people * patient * 0.1 * random))
        i = i + 1
        patient = patient + people_infected_today[i] - people_infected_today[i-3]
        total_virus = total_virus + people_infected_today[i]

        if patient - 10 > 0:
            print("Day : "+str(i)+"   Total patient : "+str(patient-10)+"   Today Patient : "+str(people_infected_today[i])+"   Immyne Number:  "+str(immune))
        else:

            #Output result
            print("Case 1 :")
            print("The Average Number of Sick Individuals a Day : "+str(total_virus/i))
            print("Maximun Sick a Day : "+str(max(people_infected_today)))
            print("In dat "+str(i)+", none people get sick.")
            print("In day "+str(i)+", "+str(immune+10)+" People Immune")
            print("\n\n\n============================================\n\n\nCase 2 : ")
            break






# case 2    p = 1,000,000    v = 100    m = 10    r = 0.15

total_people = 1000000

total_virus2 = 0
patient2 = 100
people_infected_today2 = [0]
i = 0

while patient2>=0:

    # Immunized 3 days after getting the virus, 
    # so no one has immunized in the first 3 days
    if i<3:
        random = randint(0,10)
        #Calculate how many people will be infected
        people_infected_today2.append(round((total_people - patient2)/total_people * patient2 * 0.15 * random))
        i = i + 1
        patient2 = patient2 + people_infected_today2[i]
        total_virus2 = total_virus2 + people_infected_today2[i]
        print("Day : "+str(i)+"   Total Patient : "+str(patient2)+"   Today Patient : "+str(people_infected_today2[i]))
    elif i>=3:

        #Calculate how many people are immune
        immune2 = 100
        for j in range (len(people_infected_today2)-3):
            immune2 = immune2 + people_infected_today2[j]
        if total_people - immune2 - patient2 > 0:
            random = randint(0,10)
            if total_people - immune2 - patient2 > round((total_people - immune2 - patient2)/total_people * patient2 * 0.15 * random):
                people_infected_today2.append(round((total_people - immune2 - patient2)/total_people * patient2 * 0.15 * random))
            else:
                people_infected_today2.append(total_people - immune2 - patient2)
        else:
            people_infected_today2.append(total_people - patient2 - immune2)
        i = i + 1
        patient2 = patient2 + people_infected_today2[i] - people_infected_today2[i-3]
        total_virus2 = total_virus2 + people_infected_today2[i]
        
        #Calculate how many people are immune
        if patient2-100 > 0:
            print("Day : "+str(i)+"   Total patient : "+str(patient2-100)+"   Today Patient : "+str(people_infected_today2[i])+"   Immyne Number:  "+str(immune2+100))
        
        #All people are immune
        else:

            #Output result
            print("Day : "+str(i)+"   Total patient : "+str(patient2-100)+"   Today Patient : "+str(people_infected_today2[i])+"   Immyne Number:  "+str(immune2+100))
            print("Case 2 :")
            print("The Average Number of Sick Individuals a Day : "+str(total_virus2/i))
            print("Maximun Sick a Day : "+str(max(people_infected_today2)))
            print("In dat "+str(i)+", none people get sick.")
            print("In day "+str(i)+", "+str(immune2+100)+" People Immune")
            print("\n\n\n============================================\n\n\nCase 3 : ")
            break



# case 3    p = 1,000,000    v = 200    m = 20    r = 0.2

total_virus3 = 0
patient3 = 200
people_infected_today3 = [0]
i = 0



while patient3>=0:

    # Immunized 3 days after getting the virus, 
    # so no one has immunized in the first 3 days
    if i<3:
        random = randint(0,20)
        #Calculate how many people will be infected
        people_infected_today3.append(round((total_people - patient3)/total_people * patient3 * 0.2 * random))
        i = i + 1
        patient3 = patient3 + people_infected_today3[i]
        total_virus3 = total_virus3 + people_infected_today3[i]
        print("Day : "+str(i)+"   Total Patient : "+str(patient3)+"   Today Patient : "+str(people_infected_today3[i]))
    elif i>=3:

        #Calculate how many people are immune
        immune3 = 200
        for j in range (len(people_infected_today3)-3):
            immune3 = immune3 + people_infected_today3[j]
        if total_people - immune3 - patient3 > 0:
            random = randint(0,20)
            if total_people - immune3 - patient3 > round((total_people - immune3 - patient3)/total_people * patient3 * 0.2 * random):
                people_infected_today3.append(round((total_people - immune3 - patient3)/total_people * patient3 * 0.2 * random))
            else:
                people_infected_today3.append(total_people - immune3 - patient3)
        else:
            people_infected_today3.append(total_people - patient3 - immune3)
        i = i + 1
        patient3 = patient3 + people_infected_today3[i] - people_infected_today3[i-3]
        total_virus3 = total_virus3 + people_infected_today3[i]
        
        #Calculate how many people are immune
        if patient3 - 200 > 0:
            print("Day : "+str(i)+"   Total patient : "+str(patient3-200)+"   Today Patient : "+str(people_infected_today3[i])+"   Immyne Number:  "+str(immune3+200))
        
        #All people are immune
        else:
            
            #Output result
            print("Day : "+str(i)+"   Total patient : "+str(patient3-200)+"   Today Patient : "+str(people_infected_today3[i])+"   Immyne Number:  "+str(immune3+200))
            print("Case 3 :")
            print("The Average Number of Sick Individuals a Day : "+str(total_virus3/i))
            print("Maximun Sick a Day : "+str(max(people_infected_today3)))
            print("In dat "+str(i)+", none people get sick.")
            print("In day "+str(i)+", "+str(immune3+200)+" People Immune")
            break