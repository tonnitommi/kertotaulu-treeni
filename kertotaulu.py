from random import seed, random
import time

first = [3, 4, 5, 6, 7, 8, 9, 13]
second = [2, 3, 4, 5, 6, 7, 8, 9]

print("Mikä sinun nimi on? ")
name = input()
print(f"\nHei {name}, tervetuloa kertotaulutreeniin!")
print(f"Vastaa kysymykseen tai paina X lopettaaksesi.\n")

reply = ""
correct = 0
wrong = 0
total_time = 0

while reply != "X":
    seed()
    first_index = round(random()*len(first))-1
    second_index = round(random()*len(second))-1

    if first_index < 0:
        first_index = 0

    if second_index < 0:
        second_index = 0

    print(f"\n({wrong+correct+1}) Mitä on {first[first_index]} * {second[second_index]}: ")

    start_time = time.time()
    reply = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    total_time += elapsed_time

    if reply == "X":
        break

    try:
        int_reply = int(reply)
    except:
        continue

    if int(reply) == (first[first_index] * second[second_index]):
        print("Oikein! <3")
        correct += 1
    else:
        print("Uups, väärin meni! Tarkemmin ensi kerralla")
        wrong += 1

avg_time = round(total_time/(correct+wrong))


print(f"\n\nTeit yhteensä {correct+wrong} laskutehtävää! Hienoa {name}!")
print(f"Oikein: {correct}")
print(f"Väärin: {wrong}")
print(f"Keskimäärin aikaa yhteen vastaukseen meni {avg_time} sekuntia.")

if avg_time < 4:
    print("Olet supernopea!")
else:
    print("Pitää vielä treenata nopeutta.")

print("\nHeippa!!")
