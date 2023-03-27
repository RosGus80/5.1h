import datetime, random, collections




def get_birthdays(birthday, sims):
    birthdays = []
    for i in range(sims):
        birth = []
        for num in range(birthday):
            a = str(datetime.date(2000, random.randint(1, 12), 1))
            if a[5]+a[6] in ["01", "03", "05", "07", "08", "10", "12"]:
                birth.append(f"{a[5]+a[6]}.{random.randint(1, 31)}")
            elif a[5]+a[6] == "02":
                birth.append(f"{a[5] + a[6]}.{random.randint(1, 28)}")
            else:
                birth.append(f"{a[5] + a[6]}.{random.randint(1, 30)}")
        birthdays.append(birth)
    return birthdays

def check_percentage(list=[]):
    counter = 0
    for sim in list:
        a = dict(collections.Counter(sim))
        for num in a.values():
            if int(num) > 1:
                counter += 1
                break

    return round(counter/len(list)*100, 2)


def main():
    while True:
        print("How many birthdays shall I generate? (max: 100)")
        birthdays_in_sim = input()
        if birthdays_in_sim.isdigit() and 1 <= int(birthdays_in_sim) <= 100:
            birthdays_in_sim = int(birthdays_in_sim)
            break
    while True:
        print("How many simulations shall I generate? (max: 100000)")
        sims_num = input()
        if sims_num.isdigit() and 1 <= int(sims_num) <= 100000:
            sims_num = int(sims_num)
            break
    birthdays = get_birthdays(birthdays_in_sim, sims_num)
    percent = check_percentage(birthdays)
    print(f"In {sims_num} simulations there were {percent} chance that two people in this group have their birthdays at one day")


main()

