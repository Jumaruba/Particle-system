# Particle-system
A particle system with collision avoidance made with artificial intelligence - still in development


## Movement 

The movement is created by randomizing the acceleration, the force. 

Take a read at [link](https://www.sohamkamani.com/blog/2017/09/10/random-line-generation/) 

## First part

The first part consists of the application of the graphical interface for the particle system.  
Every time a particle collides with another it turns black.

![particle system](https://github.com/Jumaruba/Particle-system/blob/master/Images/Anota%C3%A7%C3%A3o%202020-01-24%20170733.png)

## Second part

The second part consists of applying of the NEAT (genetic algorithm) to avoid collision between particles.  
How ever, the model is not applied to all particles. It's applied in just one particle.  
Every time a population is extinguished a new population is born with genes of the best elements from the previous population.  
The second part is still in development.  
