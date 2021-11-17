import random

def dad_joke_generator_background(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.
	   It also generates a random dad joke and writes it to Google Cloud Logging

    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Google Cloud Logging
    """

    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))
	
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

    # Print it, writing it away to Google Cloud Logging
    print(random_joke)
