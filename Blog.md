# Python Web programming

## Technologies used - Flask, Jinja2, HTML

- Flask
	- Flask is a simple, easy-to-use microframework for Python that can help build scalable and secure web applications. 
	- A Web Application Framework or a simply a Web Framework represents a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management, and so on.

- Jinja2
	- jinja2 is a popular template engine for Python.A web template system combines a template with a specific data source to render a dynamic web page.
	- It allows us to use python variables in HTML code.
		```
		<html>
			<head>
				<title>{{ title }}</title>
			</head>
			<body>
				<h1>Hello {{ username }}</h1>
			</body>
		</html> 
		```

## Advantages of using Flask

- Flask is a lightweight web application framework designed to get results fast and leave room to make the app more detailed in the future. 
- Due to its lightweight nature, the project's code always consists only of what you put in it, with no unnecessary code responsible for features you don’t use.

## Useful resources

- Run the demo site by opening the folder in Terminal and entering `flask run`
- [Getting Started with Flask](https://www.digitalocean.com/community/tutorials/getting-started-with-flask-a-python-microframework)
- If you use the fish shell instead of bash, you will need to install [virtualfish](https://virtualfish.readthedocs.io/en/latest/install.html#) to create virtual environments.