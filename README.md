# [Where Do We Eat?](https://devpost.com/software/where-do-we-eat)

## Say goodbye to indecision and discover your perfect dining spot with friends! Vote on restaurants based on cuisine and price preferences, ensuring the top choices rise to the surface.

### Inspiration
It can be a challenge to decide where to eat, especially when you're going out with a group of friends who all have different preferences. It's even harder when everyone is indecisive! We realized that it would be nice to have a website that could suggest us restaurants based on everyone's collective opinion.

### What it does
*Where Do We Eat?* is a website that automatically lists the best nearby restaurants based on the preferences of different people in your group. You can start by creating a new session, which will give you a unique code that you can share with your friends. After the session is created, anyone with the code can join in. Everyone gets to select which cuisines they enjoy most, as well as a price range. Every time someone submits their preference, the list of suggested restaurants changes accordingly! The more people that like a certain cuisine, the more restaurants from that given cuisine will appear. Everyone can also upvote/downvote restaurants on the list, and this will adjust the ranking of the restaurants. Upvoted restaurants will rise up the list, while downvoted ones will go down (and sometimes be removed). A list of participants is also shown (so you know who has or has not joined in!).

### How we built it
We used Python and Flask for the backend, and React for the frontend. We used the Yelp API to get restaurant data.

### Challenges we ran into
- Learning how to use Flask was a challenge! None of us had experience linking the frontend to the backend, so there were a lot of concepts we had to learn.
- We faced a ton of bugs and errors; some were harder to fix than others.
- Developing the UI was tough since we didn't have much experience with it.
- Everyone worked on a different part of the project, and merging it all together was quite challenging at times.

### Accomplishments that we're proud of
- We made so much progress! We managed to complete the tasks we planned out at the start and now have a working website.
- We learned a lot (e.g. learning to work with Yelp API, Flask, and React) 

### What we learned
- It's important to get help when you're stuck. Working with teammates/mentors to solve an issue is often much faster than trying to solve it alone.
- Dividing tasks allows us to work more efficiently. All of us contributed a lot to the project in different ways.
- Using new technologies is daunting at first, but it gets a lot easier with practice. We started out struggling to work with Flask, but towards the end, we got quite comfortable with it.

### What's next for Where Do We Eat?
- More filters! It would be nice to have additional options, such as dietary restrictions.
