import random

def dad_joke_generator(request):
    """Gives back a random dad joke from an array
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    # Make a list with strings containing dad jokes
    dad_jokes = [
      'Why are elevator jokes so good? They work on so many levels.',
      'Where do baby cats learn to swim? The kitty pool.',
      'Why does Snoop Dogg always carry an umbrella? Fo\' Drizzle.',
      'How do you organize a space party? You planet.',
      'Why are skeletons so calm? Because nothing gets under their skin.',
      'What do you get from a pampered cow? Spoiled milk!',
      'Wanna hear a joke about paper? Never mind—it\'s tearable.'
    ]

    # Get a random choice from the list
    random_joke = random.choice(dad_jokes)

    # Return it, thus printing it and displaying it
    return random_joke
