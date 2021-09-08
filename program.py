import service


def main():
    # Print header for log
    header()

    # Request user to define training type for log
    training_id = service.initial_log()

    # Request user to define exercise and log to training_log.txt
    service.suggest_exercise(training_id)

    # Request whether user would like to log another exercise for the same training type
    service.same_additional(training_id)

    # Request whether user would like to log another exercise for a different training type
    service.different_additional()

def header():
    print('-------------------------------------')
    print('       Climbing Training Log')
    print('-------------------------------------')

def footer():
    print('-------------------------------------')
    print('       Training all logged.')
    print('-------------------------------------')

if __name__ == '__main__':
    main()
