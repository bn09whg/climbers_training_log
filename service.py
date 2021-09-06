def initial_log():
    # Request user what training they would like to do and return integer ID
    training_type = input("What training would you like to do? (Please enter a number)\n"
                          "1 = Weights\n"
                          "2 = Fingerboarding\n"
                          "3 = Bouldering\n"
                          "4 = Sport Climbing")

    return training_type


def suggest_exercise(type: int):
    """
    This will request the user choose training methods for a given exercise type
    and will loop through until all exercises are logged.

    :param type: The ID of the
    :return:exercise type as an INT
    """

    type_dict = {
        1: 'Weights',
        2: 'Fingerboarding',
        3: 'Bouldering',
        4: 'Sport Climbing'
    }

    # Ask user what exercise they want to do within a given training type
    print(f"For type_dict[type] do you feel like\n")

    if input("Would you like to do "):
        'xxx'
    elif input("Would you like to do a different type of exercise?"):
        initial_log()


def weights():
    # Define different weights exercises
    weights_exercises = {
        1: 'Weighted Pull-Ups',
        2: 'Bench Press',
        3: 'Deadlifts'
    }

    # Iterate through each exercises
    for key, value in weights_exercises:
        print(f'weights_exercises.key = weighted_exercises.value')

    return input("Please choose a number from the above list:")
