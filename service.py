training_types = ('Weights', 'Fingerboarding', 'Bouldering', 'Sport Climbing')
date = 'null'


def initial_log():
    """
    # Request user what training they would like to do and return integer ID

    :return:training_type as an INT
    """

    print("What training would you like to do?")

    for i in range(len(training_types)):
        print(f"[{i + 1}] {training_types[i]}")

    training_type = input("Please enter a number:")

    while training_type not in '1234':
        training_type = input("Please enter a value between 1-4:")
    print('')

    return int(training_type) - 1


def suggest_exercise(training_id):
    """
    This will request the user choose training methods for a given exercise type and will loop through until all
    exercises are logged.

    :return: None
    """

    weights_exercises = ('Weighted Pull-Ups', 'Bench Press', 'Deadlifts', 'Core')
    fingerboarding_exercises = ('Max hangs', 'Repeaters', 'Density Hangs', 'Injury Prevention')
    bouldering_exercises = ('4x4', 'Limit Bouldering', 'Skills Session', 'Open Session')
    sport_exercises = ('Redpointing', 'Onsighting', '4x4', 'Open Session')
    exercises = [weights_exercises, fingerboarding_exercises, bouldering_exercises, sport_exercises]

    # Ask user what exercise they want to do within a given training type
    print(f"For {training_types[training_id]} what exercise do you want to log:")

    for i in range(len(exercises[training_id])):
        print(f"[{i + 1}] {exercises[training_id][i]}")

    exercise_id = input("Please enter a number:")

    while exercise_id not in '1234':
        exercise_id = input("Please enter a value between 1-4:")
    print('')

    log_exercise(training_types[training_id], exercises[training_id][int(exercise_id) - 1])


def log_exercise(training, exercise):
    """
    This will request more details from the user and log the training in training_log.txt.

    :return: None
    """

    print("Training log entry:")
    get_date()
    details = input("Please write the details of the training:")

    with open('training_log.txt', 'a') as f:
        f.write(f'{date},{training},{exercise},{details}\n')

    print('Training logged.\n')


def same_additional(training_id):
    """
    This will request whether the user would like to log more of the same training and will recursively call itself
    until the user says no.

    :return: None
    """

    sametype = input("Would you like to log a different type of exercise for the same training type? (y/n)").lower()

    while not (sametype == 'y' or sametype == 'n'):
        sametype = input("Please enter either 'y' or 'n':").lower()

    if sametype == 'y':
        suggest_exercise(training_id)
        same_additional(training_id)
    print('')


def different_additional():
    """
    This will request whether the user would like to log different training and will recursively call itself until the
    user says no.

    :return: None
    """

    different = input("Would you like to log an exercise for a different training type? (y/n)").lower()

    while not (different == 'y' or different == 'n'):
        different = input("Please enter either 'y' or 'n':").lower()
    print('')

    if different == 'y':
        training_id = initial_log()
        suggest_exercise(training_id)
        same_additional(training_id)
        different_additional()


def get_date():
    """
    For the first training log, will request the date from the user, else will request if the user wants to use the
    previous date or input a new date.
    user says no.

    :return: None
    """

    global date

    if date != 'null':
        samedate = input("Would you like to use the same date (y/n)?").lower()
        while not (samedate == 'y' or samedate == 'n'):
            samedate = input("Please enter either 'y' or 'n':").lower()

        if samedate == 'n':
            date = input("Please enter the date (dd/mm/yyyy):")

    else:
        date = input("Please enter the date (dd/mm/yyyy):")
        while not len(date) == 10:
            date = input("Please enter the date using the format 'dd/mm/yyyy':")
