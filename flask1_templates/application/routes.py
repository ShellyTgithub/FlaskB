from application import app
from flask import render_template

# Section 1 above is used for importing Libraries that we will need.
#

# Section 2: HELPER FUNCTIONS e.g. DB connection code and methods

def get_date():
    """ Function to return (fake) date - TASK: Update this from your previous assignment. Add the code to pass this date to the home 	HTML template.
    """
    today = "Today"
    app.logger.info(f"In get_date function! Update so it returns the correct date!")
    return today

# Section 3: CREATE AND RUN THE MAIN APPLICATION



# Section 4: APPLICATION ROUTES (WEB PAGE DEFINITIONS)

@app.route('/')
def home():
    """Landing page. Note there is no HTML being written here - it is all kept in the templates/home.html file!
    """
    return render_template(
        'home.html',
        title="Using Templates Demo Site",
        description="Smarter page templates with Python, Flask & Jinja."
    )
