# Password Generator

Let's create a simple password generator using Flask.
1. Setup a route for `localhost:5000/generate/<int:num_of_characters>`
   -  This route will generate a password of length specified in the route.
   -  This can just be lowercase letters for now
2. Allow for query params to alter the overall password
   - `uppercase=True` should allow for uppercase characters
   - `digits=True` should allow for numbers
   - `special=True` should allow for special characters
   - One, all, or none of these query params may be entered so be sure to account for all possibilities
