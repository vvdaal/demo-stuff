Open the Google Cloud Console and go to Cloud Functions.

Click Create Function

function name: example-03-dad-jokes-via-bucket

Region: Whatever region is close to you

Trigger type: Cloud Storage

Event type: Finalise/Create

Click the "Browse" button after the bucket field.

Click the icon with a bucket and a + inside to create a new bucket.

Name the bucket "dadjokebucket"

Leave all other options default / as they're set.

Now select your newly created "dadjokebucket" bucket in the browser.

Click the "select" button at the bottom.

CLick the "save" button under the trigger fieldset.

Click "next"

Select runtime: Python 3.9

Entry point, enter: dad_joke_generator_background

Copy and paste the contents of the main.py file from this repository to the inline editor.

Click "Deploy"

After deployment is finished, when you now upload a file into your "dadjokebucket" bucket it will call the Cloud Function you just created.


You can access and upload things to the bucket by going to "Cloud Storage" in the Google Cloud Console.

You can access the Cloud Function(s) and see the logs by going to "Cloud Functions" in the Google Cloud Console.

