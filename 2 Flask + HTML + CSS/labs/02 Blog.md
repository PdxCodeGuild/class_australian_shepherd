

# Lab 3: Blog

Let's make the template of a blog with a title, top-nav, side-nav, and multiple posts. Use [flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) and [semantic elements](https://www.w3schools.com/html/html5_semantic_elements.asp) (header, nav, section, and footer). You can use a [custom font](https://fonts.google.com/), [fancy colors](https://htmlcolorcodes.com/color-names/), and make generate fake content using an [Ipsum](https://meettheipsums.com/).

Make sure you have a [responsive design](../docs/09%20-%20CSS%20Responsive%20Design.md) that offers different, legible layouts for phone, tablet, and desktop screen sizes. You can test this in the browser devtools. Don't forget to use cascading min-width media queries for a mobile first design, and remember to include the responsive meta tag in your HTML.

It should look professional, but this does not mean it needs to be complicated. A clean, simple, minimalist layout with custom color pallate, fonts, and subtle backgrounds or whitespace works great. For examples of simple yet attractive design, check out:  

http://www.geert.io/  
https://www.blog.google/  
http://www.nextportland.com/  
https://daringfireball.net/  

## Step 1

Install the Flask framework and build a route that returns a "Hello World!" message.

## Step 2

Create a list of at least four dictionaries for your blog posts. Your list of dictionaries should look like so:
```python
posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    }, {
    ...
    }
]
```
HINT: You can use the [Ipsum generator](https://meettheipsums.com/) of your choice to generate filler text to use for your blog posts.

## Step 3

Create the Flask template for your blog and make sure that in your Python code you pass your blog posts into your template. Use the Flask template to render the blog posts in your Python into a full webpage and make sure you add the other items required -- header, footer, top and/or side navigation.

HINT: You'll want to loop though each dictionary in your posts, and then render each value in the dictionary in its proper place in your template.

## Step 4

Create a static folder and a CSS file for your Flask website and make sure you `link` to it in your template. From there, create a responsive, mobile-first design for your blog with at least three screen sizes.
