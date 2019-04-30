import csv
import sys


def user_interaction():
    print("What would you like to do?\n")
    print("Type 'B' to build the teams!\n")
    print("Type 'E' to see team experience!\n")
    print("type 'P' to see player parents!\n")
    print("Type 'I' to see player information!\n")
    print("Type 'Q' to quit the program!\n")

    while True:
        user_options = input("Choose an option: ")
        if user_options.lower() == 'b':
            team_builder()
            continue
        elif user_options.lower() == 'e':
            soccer_experience()
            continue
        elif user_options.lower() == 'p':
            parents()
            continue
        elif user_options.lower() == 'i':
            player_info()
            continue
        elif user_options.lower() == 'q':
            sys.exit("Thanks for the parcipitation!!")


def program_start():
    print("Hello and welcome to League Builder!\n")
    print("Today we will create three teams called the:\n")
    print("Sharks, Dragons and the Raptors!\n")

    while True:
        user_start = input("Press 'S' to start!: ")
        if user_start.lower() == 's':
            user_interaction()


def team_builder():

    players = []
    sharks = []
    dragons = []
    raptors = []

    with open('soccer_players.csv', 'r') as csvfile:
        csv_file = csv.reader(csvfile)

        next(csv_file)
        for line in csv_file:
            players.append(line[0])

        sharks.append(players[0:6])
        print("Team Sharks: {} \n".format(sharks))
        del players[0:6]

        dragons.append(players[0:5])
        dragons.append(players[6])
        print("Team Dragons: {} \n".format(dragons))
        del players[0:5]
        del players[1]

        raptors.append(players[0:6])
        print("Team Raptors: {} \n".format(raptors))
        del players[0:6]


def soccer_experience():

    exp_players = []
    sharks = []
    dragons = []
    raptors = []

    with open('soccer_players.csv', 'r') as csvfile:
        csv_file = csv.reader(csvfile)

        next(csv_file)
        for line in csv_file:
            exp_players.append(line[2])

        sharks.append(exp_players[0:6])
        print("Experience for Team Sharks: {} \n".format(sharks))
        del exp_players[0:6]

        dragons.append(exp_players[0:5])
        dragons.append(exp_players[6])
        print("Experience for Team Dragons: {} \n".format(dragons))
        del exp_players[0:5]
        del exp_players[1]

        raptors.append(exp_players[0:6])
        print("Experience for Team Raptors: {} \n".format(raptors))
        del exp_players[0:6]


def parents():
    gaurdians = []
    sharks_parents = []
    dragons_parents = []
    raptors_parents = []
    with open('soccer_players.csv', 'r') as csvfile:
        csv_file = csv.reader(csvfile)

        next(csv_file)
        for line in csv_file:
            gaurdians.append(line[3])

        sharks_parents.append(gaurdians[0:6])

        print("Parent names for Team Sharks: {} \n"
              .format(sharks_parents))

        del gaurdians[0:6]

        dragons_parents.append(gaurdians[0:5])
        dragons_parents.append(gaurdians[6])

        print("Parent names for Team Dragons: {} \n"
              .format(dragons_parents))

        del gaurdians[0:5]
        del gaurdians[1]

        raptors_parents.append(gaurdians[0:6])

        print("Parent names for Team Raptors: {} \n"
              .format(raptors_parents))

        del gaurdians[0:6]


def player_info():
    with open('soccer_players.csv', 'r') as csvfile:
        csv_file = csv.reader(csvfile)
        for line in csv_file:
            print(', '.join(line))


def team_file():
    
    sharks = [
    ['Sharks'],
    ['Joe Smith', 'YES', 'Jim and Jan Smith'],
    ['Jill Tanner', 'YES', 'Clara Tanner'],
    ['Bill Bon', 'YES', 'Sara and Jenny Bon'],
    ['Eva Gordan', 'NO', 'Wendy and Mike Gordon'],
    ['Matt Gill', 'NO', 'Charles and Sylvia Gill'],
    ['Kimmy Stein','NO', 'Bill and Hillary Stein'],
    ]
    dragons = [
    ['Dragons'],
    ['Sammy Adams', 'NO', 'Jeff Adams'],
    ['Karl Saygan', 'YES', 'Heather Bledsoe'],
    ['Suzane Greenberg', 'YES', 'Henrietta Dumas'],
    ['Sal Dali', 'NO', 'Gala Dali'],
    ['Joe Kavalier', 'NO', 'Sam and Elaine Kavalier'],
    ['Diego Soto', 'YES', 'Robin and Sarika Soto'],
    ]
    raptors = [
    ['Raptors'],
    ['Ben Finkelstein', 'NO', 'Aaron and Jill Finkelstein'],
    ['Chloe Alaska', 'NO', 'David and Jamie Alaska'],
    ['Arnold Willis', 'NO', 'Claire Willis'],
    ['Philip Helm', 'YES', 'Thomas Helm and Eva Jones'],
    ['Les Clay', 'YES', 'Wynonna Brown'],
    ['Herschel Krustofski', 'YES', 'Hyman and Rachel Krustofski']
    ]
    
    with open('teams.txt', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sharks)
        writer.writerows(dragons)
        writer.writerows(raptors)

if __name__ == "__main__":
    team_file()
    program_start()
