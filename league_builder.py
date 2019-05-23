import csv
import sys
# imported both libraries to make program run as planned


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
# user interface to control the whole program


def program_start():
    print("Hello and welcome to League Builder!\n")
    print("Today we will create three teams called the:\n")
    print("Sharks, Dragons and the Raptors!\n")

    while True:
        user_start = input("Press 'S' to start!: ")
        if user_start.lower() == 's':
            user_interaction()
# introduction to the program and starts the said program up


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
# creates all three teams using list slicing and list deletions


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
        print("Experience for Team Raptors:{} \n"
              .format(raptors))

        del exp_players[0:6]
# litterally the same as the function 'team_builder'
# but shows just the experience


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
# same as the funtion 'team_builder' but to show the parents of said players


def player_info():
    with open('soccer_players.csv', 'r') as csvfile:
        csv_file = csv.reader(csvfile)
        for line in csv_file:
            print(', '.join(line))
# Gets and extracts all known data from CSV file
# to display to the user if need be


def sharks():
    team_name = []
    team = 'Sharks'
    team_name.append(team)

    with open('soccer_players.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        team = []

        for line in list(data)[0:6]:
            del line[1]
            team.append(line)

    with open('teams.txt', 'w') as txtfile:
        txtdata = csv.writer(txtfile)
        txtdata.writerow(team_name)
        txtdata.writerow(team[0])
        txtdata.writerow(team[1])
        txtdata.writerow(team[2])
        txtdata.writerow(team[3])
        txtdata.writerow(team[4])
        txtdata.writerow(team[5])
# creates a text file called 'teams.txt'
# to show every teams player and the team their on in a orderly fashion


def dragons():
    team_name = []
    team = 'Dragons'
    team_name.append(team)

    with open('soccer_players.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        team = []

        for line in list(data)[6:13]:
            del line[1]
            team.append(line)

        del team[5]
    with open('teams.txt', 'a') as txtfile:
        txtdata = csv.writer(txtfile)
        txtdata.writerow(team_name)
        txtdata.writerow(team[1])
        txtdata.writerow(team[2])
        txtdata.writerow(team[5])
        txtdata.writerow(team[0])
        txtdata.writerow(team[3])
        txtdata.writerow(team[4])
# to show every teams player and the team their on in a orderly fashion


def raptors():
    team_name = []
    team = 'Raptors'
    team_name.append(team)

    with open('soccer_players.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        next(data)
        team = []

        for line in list(data)[11:20]:
            del line[1]
            team.append(line)

        del team[1]
    with open('teams.txt', 'a') as txtfile:
        txtdata = csv.writer(txtfile)
        txtdata.writerow(team_name)
        txtdata.writerow(team[3])
        txtdata.writerow(team[4])
        txtdata.writerow(team[5])
        txtdata.writerow(team[0])
        txtdata.writerow(team[1])
        txtdata.writerow(team[2])
# to show every teams player and the team their on in a orderly fashion


if __name__ == "__main__":
    sharks()
    dragons()
    raptors()
    program_start()
