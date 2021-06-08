<p>Idea:<br>
Simulation of evolution in a three-tier ecosystem by randomly assigning genetic traits to the initial population.<br></p>
<p>
Structure of ecosystem:<br>
The ecosystem consists of producers (autotrophic) (plants), primary consumers (rabbits), and secondary consumers (foxes)<br>
The sources of food for the rabbits include grasslands and forests. The sources of water for the foxes and rabbits include lakes and ponds.<br>
The plants (in forest and grasslands) regenerate themselves slowly (sunlight) and the water in lakes and ponds regenerate through rainfall.<br>
</p>
<p>
Genetics:<br>
Each Animal has Genetics G defined by the 7-tuple (M, S, Hs, Hr, Tr, P, V) where:<br>
  <ul>
  <li>M = mating requirement</li>
  <li>S = size of steps the animal takes</li>
  <li>Hs = hunting skill (only for fox)</li>
  <li>Hr = resistance to hunger</li>
  <li>Tr = resistance to thirst</li>
  <li>P = fear of predator (only for rabbit)</li>
  <li>V = vision radius</li></ul></p>

<p>
Definition 1: Animal<br>
We define an animal as a six-tuple (A, H, T, M, p, G) where:<br>
       <ul>
       <li>A = age</li>
       <li>H = hunger</li>
       <li>T = thirst</li>
       <li>M = urge to mate</li>
       <li>p = position in the food chain</li>
       <li>G = genetics (traits)</li></ul><br>
    Here, only p and G remains constant for a particular animal</p>
 <p>   
 Definition 2: Rabbit<br>
 We define a rabbit as an animal with p = 2</p>
 <p>
 Defintion 3: Fox<br>
 We define a fox as an animal with p = 1</p>
 <p>
 Defintion 4: Landform<br>
 We define a landfrom as the triplet (L, F, W) where:<br>
        <ul>
        <li>L = set of locations</li>
        <li>F = current food availability</li>
        <li>W = current water availabilty</li></ul></p>
 <p>
  Landforms are of types:<br>
        <ul>
        <li>Grassland</li> 
        <li>Forest</li>
        <li>Lake</li>
        <li>Pond</li>
        <li>Quagmire</li>
        <li>Rugged Land</li></ul>
        
<p>
Mechanism of variation:<br>
The initial population is given randomly generated characteristics (genetics). As the animals mate, the offspring gets a mean of all the 
genetic traits of the parents. Thus, only the fittest may survive and genetics may therby evolve (eliminating the weaker species)</p>

<p>
Procedure:
We can implement more variation (or more randomly generated traits) in the initial population. Tweaking the randomness even a minute amount can produce drastically 
different results (as seen by the graphs plotted by stats.py). We can study and the variation of the genetics each generation and see if the "fittest" do survive</p>


 
 
 
 
 
 
 
 
 
 
 
