# Django-Todo-App
This webapp is a basic todo list for users to list the things that they need to do! I used Django to power the website, bootstrap and css to stylize it, and of course html. Note that this webapp is not active since its not production ready. This webapp was created to learn about django and web development.

# How it works
When you first visit the webapp you will be greeted with the homepage, shown below, where your Todo list resides. However, you will need register before adding anything to your Todo list in order to save your Todo list so that you can come back later to work on your list.

![Initial HomePage](https://i.imgur.com/zIWLYRv.png)

Below is the registration place where you register for an account. Like all websites, username and password validations are run to ensure that you meet all password requirements and you register with a unique username.

![Registration Page](https://i.imgur.com/8Rstkws.png)

Once you have registered an account you will be redirected to the login page which is shown below.

![Login Page](https://i.imgur.com/AKo5UXD.png)

Once logged in, you will be able to add tasks or todos to your Todlist by simply typing what you need to do in the text box and clicking add. When you have completed one of your tasks you can label it as completed by clicking on the task which will change the text color to red and cross a line through the text. Notice that when you logged in, the nav bar options change to reflect the options you have as a logged in user.

![HomePage once logged in](https://i.imgur.com/LKWUUHj.png)

You will also have the options to delete all completed tasks and delete all tasks.

![Delete Completed feature](https://i.imgur.com/5njGYwm.png) ![Delete All feature](https://i.imgur.com/78JW17j.png)

Finally, you can logout by clicking the "logout" option in the navbar which will redirect you to the logout option where you will have the option to login in cause you logged out by accident.

![Logout Page](https://i.imgur.com/JHTTmjV.png)

# Things that can be added:
- Password resets for users who have forgotten their password
- Invitation/Remind feature: Users would be able to invite/remind others about a todo such as an event they are attending.
