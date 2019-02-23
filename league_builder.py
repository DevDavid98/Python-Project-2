if __name__ == "__main__":
    import csv
    import sys

    def teams_summary():
        with open('teams.txt', 'a') as file:
            file.write("Sharks\n"
                       "Joe Smith, YES, Jim and Jan Smith.\n"
                       "Jill Tanner, YES, Clara Tanner.\n"
                       "Bill Bon, YES, Sara and Jenny Bon.\n"
                       "Eva Gordon, NO, Wendy and Mike Gordon.\n"
                       "Mat Gill, NO, Charles and Sylvia Gill.\n"
                       "Kimmy Stein, NO, Billy and Hillary Stein.\n\n"

                       "Dragons\n"
                       "Karl Saygan, YES, Heather Bledsoe.\n"
                       "Suzane Greenburg, YES, Henrietta Dumas.\n"
                       "Diego Soto, YES, Robin and Sarika Soto.\n"
                       "Sammy Adams, NO, Jeff Adams.\n"
                       "Sal Dali, NO, Gala Dali.\n"
                       "Joe Kavalier, NO, Sam and Elaine Kavalier.\n\n"

                       "Raptors\n"
                       "Philip Helm, YES, Thomas Helm and Eva Jones.\n"
                       "Les Clay, YES, Wynonna Brown.\n"
                       "Herschel Krustofski, YES, Hyman and Rachel Krustofski.\n"
                       "Ben Finkelstein, NO, Aaron and Jill Finkelstein.\n"
                       "Chloe Alaska, NO, David and Jamie Alaska.\n"
                       "Arnold Willis, NO, Claire Willis.")

    def player_info():
        with open('soccer_players.csv') as csvfile:

            player_info = csv.reader(csvfile)
            for row in player_info:

                print(row)

    def team_sharks():
        experianced_players = {'name_1': 'Joe Smith',
                               'name_2': 'Jill Tanner',
                               'name_3': 'Bill Bon'}

        non_experianced_players = {'name_1': 'Eva Gordon',
                                   'name_2': 'Mat Gill',
                                   'name_3': 'Kimmy Stein'}
        sharks = []

        for name, names in experianced_players.items():
            sharks.append(names)

        for name, names in non_experianced_players.items():
            sharks.append(names)

        print("Team Sharks: {}\n".format(sharks))

    def team_dragons():
        experianced_players = {'name_1': 'Karl Saygan',
                               'name_2': 'Suzane Greenburg',
                               'name_3': 'Diego Soto'}

        non_experianced_players = {'name_1': 'Sammy Adams',
                                   'name_2': 'Sal Dali',
                                   'name_3': 'Joe Kavalier'}
        dragons = []

        for name, names in experianced_players.items():
            dragons.append(names)

        for name, names in non_experianced_players.items():
            dragons.append(names)

        print("Team Dragons: {}\n".format(dragons))

    def team_raptors():
        experianced_players = {'name_1': 'Philip Helm',
                               'name_2': 'Les Clay',
                               'name_3': 'Herschel Krustofski'}

        non_experianced_players = {'name_1': 'Ben Finkelstein',
                                   'name_2': 'Chloe Alaska',
                                   'name_3': 'Arnold Willis'}
        raptors = []

        for name, names in experianced_players.items():
            raptors.append(names)

        for name, names in non_experianced_players.items():
            raptors.append(names)

        print("Team Raptors: {}\n".format(raptors))

    def user_question():
        print("Type in 'B' to build the teams!\n")
        print("Type in 'I' to get player information!\n")
        print("Type in 'Q' to Quit!\n")

        while True:
            user_answer = input("What would you like to do?: \n")

            if user_answer.lower() == 'b':
                team_sharks()
                team_dragons()
                team_raptors()
                break

            elif user_answer.lower() == 'i':
                player_info()
                continue

            elif user_answer.lower() == 'q':
                sys.exit("Thanks for the precipitation!")

    print("Hello and welcome to League Builder!\n")

    teams_summary()
    user_question()

    print("Here are the teams!")
    print("Have a nice day!")
