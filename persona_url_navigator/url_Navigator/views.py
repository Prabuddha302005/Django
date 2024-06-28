from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def personalUrl(request):
    return HttpResponse(
'''

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Personal Url Navigator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>

<!-- As a heading -->
<nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <span class="navbar-brand mb-0 h1">Url Navigator</span>
  </div>
</nav>

 <a href="https://www.youtube.com/"><h1>youtube</h1></a>
    <a href="https://www.udemy.com"><h1>Udemy</h1></a>
    <a href="https://stackoverflow.com/"><h1>StackOverflow</h1></a>
    <a href="https://chatgpt.com/"><h1>ChatGpt</h1></a>
    <a href="https://github.com/"><h1>Github</h1></a>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>

   
                       
                        
'''
)
