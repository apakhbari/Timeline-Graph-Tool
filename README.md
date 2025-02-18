# Timeline-Graph-Tool

```
 _______  ___   __   __  _______  ___      ___   __    _  _______      _______  ______    _______  _______  __   __ 
|       ||   | |  |_|  ||       ||   |    |   | |  |  | ||       |    |       ||    _ |  |   _   ||       ||  | |  |
|_     _||   | |       ||    ___||   |    |   | |   |_| ||    ___|    |    ___||   | ||  |  |_|  ||    _  ||  |_|  |
  |   |  |   | |       ||   |___ |   |    |   | |       ||   |___     |   | __ |   |_||_ |       ||   |_| ||       |
  |   |  |   | |       ||    ___||   |___ |   | |  _    ||    ___|    |   ||  ||    __  ||       ||    ___||       |
  |   |  |   | | ||_|| ||   |___ |       ||   | | | |   ||   |___     |   |_| ||   |  | ||   _   ||   |    |   _   |
  |___|  |___| |_|   |_||_______||_______||___| |_|  |__||_______|    |_______||___|  |_||__| |__||___|    |__| |__|
```

run it using
```
sudo docker run -it timeline_graph_tool:1.0
```

My Prompt:
Help me with problem i have. I am looking for a tool that can make me create time series Graphs. So i tell it my starting point and ending point in time (for example 2015 - 2024) and then tell it i have been doing Job A from july 2016 to september of 2017 and job B from january of 2017 to March of 2018 and job C from October of 2019 untill 2024 and it creates an intuitive, easy to understand graph for me.
Main purpose of tool is to have starting point of different years as vertexes, and then a main edge which is connecting all (starting point of different years) vertexes together. Then create vertexes for starting point and ending point of different Jobs i have and create an edge  uniquely for each job, for example job A has a vertex for starting point in time in july 2016 and a vertex for ending point in september 2017 and this two vertexes are connected together using an edge.
The main thing here is that i don't want my edges to collide together, (So maybe my graph is flat?). save output to a jpg file.
I am giving you an image for reference.


# acknowledgment
## Contributors

APA 🖖🏻

## Links

```
  aaaaaaaaaaaaa  ppppp   ppppppppp     aaaaaaaaaaaaa   
  a::::::::::::a p::::ppp:::::::::p    a::::::::::::a  
  aaaaaaaaa:::::ap:::::::::::::::::p   aaaaaaaaa:::::a 
           a::::app::::::ppppp::::::p           a::::a 
    aaaaaaa:::::a p:::::p     p:::::p    aaaaaaa:::::a 
  aa::::::::::::a p:::::p     p:::::p  aa::::::::::::a 
 a::::aaaa::::::a p:::::p     p:::::p a::::aaaa::::::a 
a::::a    a:::::a p:::::p    p::::::pa::::a    a:::::a 
a::::a    a:::::a p:::::ppppp:::::::pa::::a    a:::::a 
a:::::aaaa::::::a p::::::::::::::::p a:::::aaaa::::::a 
 a::::::::::aa:::ap::::::::::::::pp   a::::::::::aa:::a
  aaaaaaaaaa  aaaap::::::pppppppp      aaaaaaaaaa  aaaa
                  p:::::p                              
                  p:::::p                              
                 p:::::::p                             
                 p:::::::p                             
                 p:::::::p                             
                 ppppppppp                             
```