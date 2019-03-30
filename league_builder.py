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
            print(line)


def team_file():
    with open('teams.txt', 'w') as txtfile:
        team_names = csv.writer(txtfile)
        fieldnames = ['Name', 'Soccer Experience', 'Gaurdian Name(s)']
        writer = csv.DictWriter(txtfile, fieldnames=fieldnames)

        team_names.writerow(['Sharks'])
        writer.writerow({'Name': 'Joe Smith', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Jim and Jan Smith'})
        writer.writerow({'Name': 'Jill Tanner', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Clara Tanner'})
        writer.writerow({'Name': 'Bill Bon', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Sara and Jenny Bon'})

        writer.writerow({'Name': 'Eva Gordan', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Wendy and Mike Gordon'})
        writer.writerow({'Name': 'Matt Gill', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Charles and Sylvia Gill'})
        writer.writerow({'Name': 'Kimmy Stein', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Bill and Hillary Stein'})

        team_names.writerow([])

        team_names.writerow(['Dragons'])
        writer.writerow({'Name': 'Sammy Adams', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Jeff Adams'})
        writer.writerow({'Name': 'Karl Saygan', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Heather Bledsoe'})
        writer.writerow({'Name': 'Suzane Greenberg',
                         'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Henrietta Dumas'})

        writer.writerow({'Name': 'Sal Dali', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Gala Dali'})
        writer.writerow({'Name': 'Joe Kavalier', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Sam and Elaine Kavalier'})
        writer.writerow({'Name': 'Diego Soto', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Robin and Sarika Soto'})

        team_names.writerow([])

        team_names.writerow(['Raptors'])
        writer.writerow({'Name': 'Ben Finkelstein',
                         'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Aaron and Jill Finkelstein'})
        writer.writerow({'Name': 'Chloe Alaska', 'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'David and Jamie Alaska'})
        writer.writerow({'Name': 'Arnold Willis',
                         'Soccer Experience': 'NO',
                         'Gaurdian Name(s)': 'Claire Willis'})

        writer.writerow({'Name': 'Philip Helm', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Thomas Helm and Eva Jones'})
        writer.writerow({'Name': 'Les Clay', 'Soccer Experience': 'YES',
                         'Gaurdian Name(s)': 'Wynonna Brown'})
        writer.writerow({'Name': 'Herschel Krustofski',
                         'Soccer Experience': 'YES',
                         'Gaurdian Name(s)':
                         'Hyman and Rachel Krustofski'})

if __name__ == "__main__":
    team_file()
    program_start()
