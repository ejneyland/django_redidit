# REDIDIT, reddit .. redid
Reddit-esque thread/comment posting platform

Joint project: Ethan & Christian

- Develop using Python on a Django framework

- Connect App up to a database for storing posts and comments

- Connect to third-party cloud storage for image uploads

To-Do:
- create method to allow user to create new User and enter in their information
- create method to allow user to update User details
- create method to allow user to create Post
- create method to allow user to edit Post
  - post must display a last-modified date/time
  - restrict which fields can be modified (i.e. cannot edit date published or user)
- create Comment class
  - comments can be made on a Post,
  - but no comments on comments (for now)
  - one Post has several independent Comment instances
  - like/dislike function and out
