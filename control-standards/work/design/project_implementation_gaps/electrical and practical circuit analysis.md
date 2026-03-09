0:00
Hey, how's it going everyone? This is the solid state workshop with essential and practical circuit analysis. This is
0:06
going to be a two-part series on circuit analysis. So, put on your thinking cap and let's
What is circuit analysis?
0:13
go. So, what exactly is circuit analysis anyway? Well, circuit analysis is a
0:20
toolkit for understanding and designing more complex circuits. So, if you want to get into the world of electronics or
0:27
you want to understand electronic circuits, well, you're going to need to understand the concepts brought to you
0:33
in circuit analysis first. And that's because circuit analysis is a layer of
0:40
abstraction. It is based off of other abstractions while other abstractions
0:45
are built off of it. So, you can look at this process chart here of how that
0:51
works. So you start off in physics and you learn about the electrons and protons and all the uh small low-level
1:01
things and then you move on to circuit analysis and learn how that works and then you move on to
1:06
electronics which is based off of circuit analysis and then you can move on to electronic systems which is based
1:14
off electronics. So in order to be successful in each area, you first need to understand the area that precedes it,
1:21
the layer of abstraction before it. All right, cool. What will be covered in this
What will be covered in this video?
1:29
video? Well, a whole range of topics. We're going to start from the very beginning with some simple circuits and
1:36
then we're going to move up into the world of more complex circuits. But along the way, we're going to discover
1:41
methods which simplify the complex circuits and make performing an analysis
1:47
on them easier. So here are the topics that we're going to talk about
1:52
today. We're going to start by talking about linear circuit elements and then
1:57
we're going to move on to Ohm's law and series and parallel circuits which you may have already seen before in a
2:04
physics class or something. Then we're going to talk about voltage and current dividers. Then move on to the big two.
2:11
Kershoff's current law and its associated nodal analysis and Kershoff's voltage law and its associated loop
2:18
analysis. And we're going to talk about some methods for analysis that are a
2:24
little more abstract but are definitely still really cool. And those include source transformation, the norin
2:31
equivalents, and finally superp position.
Linear Circuit Elements
2:37
Today we're going be dealing with linear circuit elements in all of our examples. And what are the linear circuit elements
2:43
that we might encounter? Well, we have the humble resistor with units ohm and
2:49
symbol omega. The capacitor with units farad and symbol f. The inductor with
2:56
units henry and symbol H. The voltage source with units volt and symbol V. and
3:05
the current source with units ampere or amps and symbol a. And now what makes a
3:12
linear circuit element linear? Well, say we were to write out a
3:19
relationship between current and voltage for any of these elements, more specifically resistors, capacitors, and
3:25
inductors. But say we were to write out current as a function of
3:31
voltage. We would find that the current through these devices, these
3:37
elements is going to be a function of voltage times some constant. And so that
3:44
makes it a linear um element because it there is a linear operator in
3:51
that relationship. In a nonlinear circuit element, the operator is
3:57
something like an exponential operator, e to the power of something. But we
4:03
won't be encountering nonlinear circuit elements today. So don't worry about those. And more specifically today,
4:11
we're going to be dealing with exclusively resistors, voltage sources,
4:16
and current sources. Before we go any further, let's discuss
Nodes, Branches, and Loops
4:22
the different parts of a circuit and the names we give to these parts. Here's a circuit that we'll use
4:28
as an example. And now the first part is called a node. And a node is a junction
4:36
of connecting wires. It's where circuit elements are joined together. So in this
4:42
case, we have four nodes because there are four points of connection in this circuit. We have a node connecting the
4:50
voltage source to a resistor. Here we have two resistors and a voltage source
4:55
connected together. And here we have a voltage source and a resistor connected together. We also include this big node
5:03
at the bottom. And every point on this big node
5:08
is at the same electric potential. And well, how could that be?
5:14
Well, there's nothing in between any of the points on the node here that could alter its potential such as a resistor
5:21
or a source. And if say we did add one of those things, well then this whole
5:27
thing is no longer a node. Maybe only this part would be a
5:32
node. Next part we have is called a branch. And so a branch is really just a
5:40
fancy name for any of the circuit elements between two nodes. So here are all our all our branches in
5:47
the circuit. It's really as easy as it sounds. It's the element between
5:54
nodes. I guess the difference between a branch and just a circuit element is that a branch is an element that is part
6:02
of a circuit by definition while a circuit element on its own can just be a
6:07
standalone thing that we can talk about by itself. All right. So finally let's talk
6:14
about loops. And a loop is a closed path that
6:19
begins and ends at the same node. And a loop can't pass through any node more
6:26
than once. So here we have three different loops in this circuit. We have a small
6:32
loop here. We have another small loop
6:38
here. And then we have one big loop that encompasses the entire circuit. And
6:43
these are all loops. So try to become familiar with these terms because I'll be using them
6:50
to describe points on a circuit. And um plus you get to sound smart when talking
6:55
to your friends. So um that's a plus. All right. So, Ohm's law, the most
Ohm’s Law
7:03
fundamentally basic and essential relationship in all of circuit analysis.
7:09
Now, before we talk about the actual equation, let's talk about the variables that it is consisted
7:15
of. So, we have V for voltage, I for current, and R for resistance. And now
7:23
remember voltage is an across variable meaning you take the voltage between two
7:29
points or across some element in the circuit and I or current is a through
7:36
variable meaning it's the current through an element and resistance is simply a
7:42
constant assigned to a particular resistor.
7:48
Now, Ohm's law says V = I _ R, I = V /
7:54
R, or R= V / I. So, it makes it possible for us to
8:02
solve for an unknown current, voltage, or resistance, granted that we already have
8:07
two of those elements of that equation.
8:13
So, if we have a circuit that looks like this with a voltage source of 30 volts and a resistance of 75 ohms, we
8:20
can determine the current that must flow through that resistor. And that's easy because in this case, I = 30 over 75 and
8:32
that equals 4 amps. Circuit elements can be connected in two
Series Circuits
8:39
basic fashions either in series or in parallel. So let's talk about series
8:44
first. In a series circuit, the elements in a circuit are connected one after
8:50
another. Meaning the front of one circuit element is attached to the back
8:55
of another element and the front of that element is attached to the back of
9:00
another element. That's what makes it a series circuit. In a series circuit, there's only one
9:07
path for current to flow. And that's because there's only one loop here.
9:13
Where else could the current possibly flow? And how could it possibly be different at different points in the
9:20
circuit? So, we could test for current here and it'll be the same as
9:26
current. The same value for current will be found here and the same value for current will be found here.
9:34
Now, if we have multiple resistors in our circuit, then we can
9:40
simplify multiple resistors down to one equivalent resistance. And we can do that using a very simple uh equation
9:48
that says R equivalent equals R1 + R2 plus all the way up to RN, which is the
9:56
nth resistor. So in our particular instance we have an 100 ohm resistor and a 50 ohm resistor
10:04
in series. So the equivalent resistance that would be formed between this point
10:11
and this point would be 150 ohms. And now that we know the
10:17
equivalent resistance basically we can rewrite these two resistors as one resistor. Then we can solve for the
10:24
current just as we did previously. So applying Ohm's law, we see that the
10:30
current is equal to 30 volts, the source voltage over the equivalent resistance
10:35
of 150 ohms. So dividing 30 by 150 gives
10:41
us2 amps. In a parallel circuit like this
Parallel Circuits
10:47
one, all resistors share a common voltage. And we can see that because the
10:52
30 volt source here is attached across both the 150 ohm and the 100 ohm
10:58
resistor simultaneously and in the same places. But the difference between
11:03
parallel and series is that the currents through each of these resistors can be different. And in this case they are
11:09
different because the values of the resistances are different. So there's going to be less current
11:16
flowing through the 150 ohm resistor than in the 100 ohm
11:22
resistor. And say we wanted to find the current up here, the green
11:28
current. How could we do that? Well, we can turn these two
11:34
resistors arranged in the parallel configuration into one equivalent
11:40
resistor like we did in series circuits. And we're going to use this
11:47
equation 1 / R equivalent equals 1 / R1 + 1 / R2 all the way up to 1 / R
11:57
N. And so in this case we find that the equivalent resistance that will replace
12:03
this circuit block right here is equal to 1 over 150 + 1 over 100
12:12
and then whatever answer you get there you just flip it. So this arrangement of resistors can be
12:20
replaced by 160 ohm resistor. And so therefore we can find what that green current would be.
12:27
And we're going just use Ohm's law. And you divide 30 volts by our equivalent
12:33
resistance of 60 ohms. And we find that the green current would be.5
12:38
amps. Now, say we wanted to find the currents through each of the resistors. How would we do that? Well, we would
12:46
simply divide the source voltage since both share the same source voltage by
12:54
the resistance. So for the pink current through the 150 ohm resistor that's
13:01
equal to 30 volts over 150 which equals2 and the blue current through the
13:09
100 ohm resistor is equal to 30 vol over 100
13:14
ohms and that equals.3 amps. So some takeaways from here.
13:21
Basically we can say that the green current flows into this node here. This
13:26
junction of components splits. Some of it goes down
13:32
one chute and some of it goes down another chute here. And then back at the bottom and then down at the bottom these
13:38
currents recombine back into the green current. And rinse and repeat.
Voltage Dividers
13:49
A voltage divider is a circuit that creates a voltage which is some fraction of its voltage source. So here is an
13:56
example of a voltage divider circuit. It is a series circuit where the output is
14:02
observed or taken across the second resistor. So in this case, that's that 10 ohm resistor. And it's a series
14:10
circuit because the 10V source and the 40 ohm resistor and the 10 ohm resistor
14:15
are all in series with each other. We can kind of ignore these wires or lines over here because when we're taking the
14:22
output, we're just observing the output. We're not really intruding upon the circuit. So it doesn't really contribute to the circuit, at least in the ideal
14:29
case. We'll see uh more about that later. But anyway in a series circuit
14:34
like this with multiple resistors and a voltage source or any source the voltage across each resistor
14:42
uh will be different uh as dictated by Ohm's law V equals IR. So where I the
14:48
current is the same for all of them uh but the resistance uh can will dictate
14:54
the voltage across each resistor. So if we want to find V out in
15:00
this case, we're going to first start with finding the equivalent resistance. So that's that's easy. That's 40 + 10.
15:07
So that's 50 ohms. And now we can find the current through these resistors. And that is 2
15:15
amps. Easy enough. And then to find V out, we can simply
15:22
multiply the current which is the same for both resistors because it's serious circuit and multiply it by the
15:29
resistance of R2. And in this case, that's 10 ohms. So you just do 2 _ 10
15:36
ohms and that'll give you the voltage across the 10 ohm resistor. Uh now
15:42
technically uh we can also take the voltage across the 40 ohm resistor and that would be 02 amps times 40 ohms
15:51
which would give us 8 volts. So as you can see uh 2 volts and 8 volts would add
15:56
up to 10 volts. So that makes sense I hope. All right
16:02
cool what we just did is all fine and dandy except it takes a couple of steps about
16:08
three to reach our answer. So we want to write a general equation that describes
16:13
the output of any two resistor voltage divider. So here is a general schematic
16:21
of a voltage divider. So we have a VS and we have an R1 and we have an
16:29
R2. And we also have a current that flows through the circuit. It's the same current everywhere in the circuit
16:34
because this is a series circuit. And we have a voltage output a V out
16:40
which is observed across R2. So let's put all these things into
16:47
mathematical equations. So R equivalent equals R1 + R2 because it's a
16:53
series circuit. And the current I is equal to
16:59
VS over R equivalent. And V out is equal to the current
17:06
through R2 times the resistance of
17:13
R2. And we know that the current is the same for everywhere in the circuit. So that current through R2 is simply just
17:21
I. And so now we can substitute in to our V out equation. We can substitute in
17:28
VS over R equivalent for I. And then we can rearrange and come to
17:36
the final equation of VS time R2 over R1 + R2. And that will
17:45
give you the voltage output the V out for any two resistor voltage divider
17:52
uh with any voltage source and any two resistors.
17:58
Now most generally we can write an equation that says V out= VS _ RX over R
18:06
equivalent. And what is RX? RX is the resistor you would like to find the
18:12
voltage across and R equivalent is again the
18:18
total resistance. So we can find the voltage across any of the resistors and
18:24
we can have any number of resistors. We can have three four five six resistors and all you have to do is put uh the
18:32
value of that resistor in the numerator and um over top of the equivalent resistance and multiply it times the
18:38
source voltage and you will get the voltage across that resistor
18:46
RX. In practice, the output of the voltage divider is going to be hooked up to something. We want V out to do
18:54
something for us. So in circuits, that means we're going to attach a load to it. But when we attach a load to it,
19:01
which is in this case a resistor, we fundamentally change the nature of the
19:07
voltage divider. H. So let's look at this circuit. This is the new circuit,
19:13
the new voltage divider with a load resistor RL attached across its output.
19:19
And RL takes the place of what was before an open circuit. And we're going to learn that attaching a load RL
19:27
reduces the divider's output voltage. And well, how could that be?
19:32
Well, let's look back to the original equation that says V out= VS _ R2 over
19:38
R1 + R2. And then if we to look back at the circuit, we would notice that R2 and RL
19:47
are in what configuration? Well, they're in parallel.
19:54
So what used to be just R2 is now really R2 parallel RL, the
20:03
equivalent resistance. So we can rewrite the V out equation to take this into account.
20:10
So the old R2 now becomes R2 parallel RL and we can
20:18
substitute that in anytime we see R2. And we know that based on our
20:24
knowledge of parallel resistors and parallel circuits in general that R2 parallel RL is going to be less than the
20:31
original value of R2. And why is that? Well, think here. If you have R2, which
20:38
is some value, and then you attach another
20:43
resistor in parallel with it, you're effectively creating another path for current to flow through. So the
20:50
equivalent resistance is going to be less because now there is another path for current to travel
20:57
through. All right? So if the equivalent resistance up here is less than the
21:04
original R2, that means that this voltage output is going to be less than the original voltage
21:12
output. Now if the load resistance RL is much greater than a resistance of R2,
21:20
then the output voltage only drops by a little bit. And why is that? Well, thinking
21:26
back to the equation for parallel resistors again, adding a big resistor in parallel with a comparatively small
21:33
resistor will only reduce the equivalent resistance by a small amount. So this
21:41
resistance will only be decreased by a small amount. So if this is only decreased by a small amount, then V out
21:48
is only a little bit smaller than the original V out. Another way to think about
21:55
this is that the current through RL, the
22:00
current through the load, the load current should be much should be much less than the current through the
22:06
divider, the current through R1 and R2.
22:11
So if we knew that our load was going to draw 10 milliamps here, then we should
22:18
ensure as a rule of thumb that the current through R1 and R2 is at least 10
22:26
or maybe even 100 times greater than the 10 milliamps flowing through RL. And
22:32
that's going to ensure that the voltage across RL is close to what we intended it to
22:39
be. Originally, I wasn't going to include a
Current Dividers
22:44
section on current dividers because most real world circuits
22:50
employ voltage dividers and not current dividers. And that's because most sources in the real world more closely
22:57
resemble voltage sources. However, understanding current dividers is still definitely a good
23:03
thing to know. So a current divider is a circuit that creates a current which is
23:10
some fraction of its current source. So it's kind of the opposite of a voltage
23:16
divider which creates a fraction of its voltage source. And this is what one looks like.
23:24
This is the general form the general schematic of a current divider. And a current divider is a parallel
23:31
circuit where the output current is observed in one of its branches. So in this case it's the current through the
23:38
branch consisting of RX the current I out going through this
23:44
branch. And so the first step to finding I out is to first find this value
23:53
RT. and RT is the equivalent resistance
23:58
of all the other branches excluding RX. So it's the equivalent
24:05
resistance of these two branches and not including the RX
24:12
branch. And if there's only one other branch other than RX, so say R2 wasn't
24:19
here, then it would simply be the value of R1. that would be the equivalent resistance. But since we have two
24:26
branches here, we would follow the formula for a parallel um circuit for parallel
24:33
resistances which is RT = 1 / R1 + 1 / R2 and then flipped.
24:42
Now to find I out you're going to follow this equation which says I out = _ RT
24:51
over RX + RT. Let's compare this to the voltage
24:58
divider equation. In the voltage divider equation, what was in the numerator? Can you remember? Right, it was the resistor
25:06
which we were concerned about. So R2 generally but in the current divider
25:14
it's the opposite. It's the equivalent resistance of everything except for the
25:20
resistor that we are interested in. And it the resistor that we're interested in this case is RX. And you'll notice that
25:28
RT is the equivalent resistance of R1 and R2 but not
25:35
RX. Interesting.
Kirchhoff’s Current Law (KCL)
25:48
So, here we are. The real meat and potatoes of circuit analysis. It's getting good. So, Kershoff's current law
25:55
or KCL for short says that all currents entering a node must equal all currents
26:00
exiting a node. Basically, what goes in must come out. And in mathematical
26:08
terms, the sum of all currents in a node equals zero. We can also express this as
26:14
a summation of I. And where J is a particular instance
26:19
of current just tells you what current we're talking about. And so here are some
26:26
illustrations to help you understand KCO. The yellow and the green currents
26:32
represent currents entering a node while the red, blue, and pink currents
26:38
represent currents exiting a node. And in the chart below, we can see that the
26:43
sum of all the currents entering the node equals the sum of the currents exiting the node. Regardless of what the
26:51
what the individual currents are, they all add up to the same current.
26:57
In practice, we write a KCL equation for a node in the form I1 plus I2 plus I3
27:05
just like we have in this equation here. And we set that all equal to zero as we
27:10
learned before because the sum of all currents in a node equals zero. And I1 and I2 and I3 are just all
27:19
the currents coming in and out of the node if you didn't catch on.
27:25
So we use the convention that a current entering a node is a positive I because
27:30
you can think of it as adding to a node and a current exiting a node is a
27:36
negative I because you can think of it as being subtracted from the node. So let's do a problem with
27:45
this. So we're given a circuit that looks like this and we're also given some currents
27:52
initially. So, we're given that there are there's 4 milliamps going to the right, 12 milliamps going up here and 2
28:00
milliamps going to the left. And we're also given the currents I1 and I2 as
28:06
arbitrarily going to the right, but we're not actually sure if they go to the left or right quite
28:11
yet. And so, we're also set up nodes. So, we're going to call this node right
28:18
here node A. and this node right here in the
28:23
middle, node B. And now we're asked find I1 and I2
28:32
using KCL. And the first thing we should ask ourselves
28:37
is do I need to find one current before I can find the other current?
28:43
So, if I want to find I1, we first need to find the current
28:50
I2. And if that doesn't make sense, hopefully it'll make sense in a minute or two. So, let's write the node
28:57
equation for node B first because that's
29:03
correlated with I2. So, the KCL at node B, what is that
29:10
going to be? Well, here's what it is, and we'll explain why. Well, we have a positive I2
29:18
entering the node, so we write positive I2. And we have a positive 12 milliamps
29:25
also entering the node. So, we write pos2. And we have 4 milliamps exiting
29:32
the node. So, we write minus 4 milliamps. And that's it. And then we
29:38
set that equal to zero. and then we can easily solve and find that I2 equ=8
29:44
milliamps and we'll talk about what a negative current means in a second. So
29:50
now let's move on to node A over here. So what's the KCL equation at node
29:57
A? Well, here it is and we'll talk about that. So we have a negative I1 coming
30:07
out of the node because it's exiting. It's a negative I1. And you have I2 also
30:14
exiting the node. And then we have a positive 2 milliamps coming up from the bottom here
30:20
into the node A. So we have a negative I1 minus an I2 plus 2 milliamps and set
30:28
that equal to zero. And we know that I2 is 8 milliamps. So we can simply plug
30:34
that right into I2. And we can then solve for I1. And we
30:42
find that I1 equals 10 milliamps. And so what did that 8
30:47
milliamps from before mean? The I2 equals8 milliamps. Well, in the
30:52
direction that we specified, so we just said that yeah, I2 is going to go to the right. It means
31:00
that it's actually it's actually a positive 8
31:06
milliamps going to the left. So all we have to do is if we get a negative current is we just say that the real
31:14
current is going in the opposite direction and is a positive current. So a negative current just
31:22
tells you to flip the direction of the current and make the value of the current positive.
Nodal Analysis
31:31
Building off of KCL is something called nodal analysis. And nodal analysis is a
31:36
process that uses KCL to determine node voltages. And so here's the basic setup
31:43
for nodal analysis. To use nodal analysis, we
31:49
first need to create a reference node. And so a reference node in our example
31:57
circuit diagram over here is the strip of wire in the bottom. That's our
32:03
reference node. Now, how do we choose which node we want to make a reference node in a
32:09
circuit? Well, rule of thumb is to pick the node in your circuit with the most
32:14
connections to it. That'll make your life a little easier. Now remember in a circuit a voltage is
32:21
defined as a difference in potential between two points. So if I was to say
32:27
that the voltage at some point is 5 volts. Well then I also have to specify
32:33
that it's 5 volts with respect to what other point? So I would have to give that
32:39
other point. So when we set up a reference node we're providing that other point in
32:45
the circuit. We're saying that all of our voltage meas measurements are referred or referenced to that reference
32:52
node. So to this node down here. So if we look at our example, what
32:58
is the voltage at this point right here? Well, it's Vx with reference to ground or with
33:06
respect to ground, any way you want to say it. And the voltage here is
33:12
Vy with respect to ground. All right, moving
33:18
on. And so we know that a current through resistor is described and governed by Ohm's law, which says the
33:27
difference in potential across a resistor over the resistance gives us
33:34
the current. So in this case, that's going to be Vx minus Vy over R. And why
33:44
is it vx minus v y? Well, because the current is going in the direction to the
33:50
right. Meaning that there would be a lower voltage at this point than there would be at this point vx because a
33:58
resistor creates a voltage drop. And now vx and vy are what we call
34:06
node voltages. And we might be interested in solving for those. And so to solve for
34:12
these we can write the KCL equation for each node in the circuit except for the
34:19
reference node here. We exclude the reference nodes in our equations. And so we can write out the
34:27
standard KCL equations like we did before in our previous examples. Except
34:33
now instead of writing I1 I2 I3 equals zero, we write in the form Vx - V Y / R
34:42
plus V Z minus V B whatever over R
34:49
whatever you want to whatever points there are in the circuit. So we we use this form vx - v y / r instead of just
34:59
i. All right. The moment we all been waiting for the nodal analysis sample
35:05
problem. Oh, wait. No, no one was waiting for it. All right. Anyway, here
35:11
is the sample nodal analysis problem that we're going to attempt here. Hopefully I don't get it wrong. Uh we're
35:17
going to try to find the voltage VO here, the V out, whatever you want to call it. And before we get started,
35:23
let's note a couple things about the circuit. The reference node is already set up for us, and it's this node down
35:29
here. How do we know that's the reference node? Because there's a ground symbol attached to it. That basically
35:34
signifies that it is the reference node. And then we have two nodes up top
35:39
here that we are interested in. Uh node one here and node two
35:46
here. And we also have uh two currents that we're interested in. And that's I1 which goes to the
35:52
right and I2 which also goes to the right. Those are set arbitrarily. I can have made them go to the left if I had
36:00
chosen to. All right, so let's get started and let's start at node one. Let's write out
36:05
the KCL equation at node one. What's that going to be? Well, we have three currents associated with node one and
36:12
those are I1, I2, and I. So let's write out the
36:20
equation for that. Since I1's going into the node, it's a positive I1. Since I2
36:26
is coming out of the node, it's a negative I2. And since is pointing into
36:32
the node, it is a positive is. And now
36:38
this equation here is just a standard KCL equation. We've done this before. But now to do nodal analysis, we want to
36:44
put it into the form of a difference in voltage across a resistor over the
36:50
resistance. And so which ones can we do that for? Well, we can do it for I1 cuz I1 is associated with the current
36:56
through R1 and I2 is associated with the current through R2. So we can write this out. We can
37:04
write those two out in that form. However, we can't write it out like that for is because is
37:12
does not have a resistor associated with it. So, here's what that new equation looks
37:17
like. And we have VS, which is the source voltage over here, minus V1,
37:24
which is the voltage at node one, over the resistance R1. And in a very similar
37:29
fashion, it's V1 minus V2 over
37:35
R2. And now why just for for instance why why is I2 defined as the voltage V1
37:43
minus V2 and not the other way around? Well because the current is going from
37:48
left to right. And then is we just tack on at the end here and set it all equal to
37:55
zero. And now we can just do some kind of re uh algebraic clever rearranging
38:02
and we can get it into a form like this where we have vub1 _ some
38:08
constant plus v2 _ some constant and usually these constants are the um r
38:15
constants for resistance and then we're going to set that equal to the other constants that
38:22
we know here. All right. So, just let that be for now. We have an equation with two
38:28
variables. So, in order to solve for both of those variables, we're going to need another equation so that we can get
38:34
two equations, two variables, and then solve using some method. So, let's move on to KCL at node 2. And the KCL node 2
38:44
is kind of weird, but it will hopefully make sense. So, KCL node 2 is I2 minus
38:51
I2 equals Z. And you might be saying, well, well, obvious that's that's weird. I don't know why you're writing that
38:57
out, but bear with me. So, let's because the because there's two currents
39:02
associated with node 2. We have the current flowing into I2 from here and the
39:09
current coming out of I2 down to the reference node. And those
39:15
currents are in magnitude the same, but we can define them differently. So, what
39:21
do I mean by that? Well, the current going through R2
39:26
here is technically V_sub_1 minus V2 over the resistance
39:33
R2. And because no current can flow anywhere else, that same current also
39:38
flows through R3. So that's why they're the same. But the current through R3 can be
39:44
defined as V2 minus 0 for ground over the
39:52
resistance value of R3. So that's where this comes from. So yes, they are the
39:57
same current, but we can define the current through each one of these resistors which are
40:03
participating in this KCL equation differently. All right. So now again we
40:09
can do some rearranging like we did before and land on an equation like this. So now we have two equations and
40:17
two variables and that means we can solve for it with some method of our
40:22
choosing for me. I'm going to put it in matrix
40:27
form. And so here's what the matrix form is for these two equations.
40:35
So we have a 2x2 matrix here which includes all of our um R variables and
40:42
here's our matrix for V1 and V2 which we're trying to solve for. And here are some of our our constants in this
40:49
matrix. And then however you want to solve for this is up to you. You can use system of equations, you can plug things
40:56
in. Whatever is most comfortable for you is what you should use. For me, I can pump this into my calculator pretty
41:02
easily. So that's probably what I'll do. So I would do the inverse of of uh this
41:08
matrix times this matrix and that should give me v_sub_1 and v2 pretty
41:14
easily. And so let's just uh before I get ahead of myself here, we can rewrite
41:20
this matrix with real numbers. So I've converted all the R1's and R2s and R3s into real numbers here. And I've
41:28
converted this expression into a real number over here. And so I can solve for
41:33
it. And so I find that V_sub_1 equals 14 volts and V2 equals 6
41:40
volts. And because V2 and V out here are the same point
41:46
electrically because they're on the same node, it means that V2 equals VO or V
41:52
out. And so V out equals 6 volts across here. Well, that's kind of
42:00
a lot of work. So, I'd be lying to tell you that this was the easiest way you could have done this problem. So, bear
42:06
with me and we'll now look at a an easier way to do
42:13
this. So, I just blew through that last example at like mock three and I don't
42:18
know if that made it seem easy or if I just confused you and hopefully I didn't confuse you, but the way we did that
42:25
problem was not very smart. We kind of went into it blindly in a brutish brute
42:32
force method. We just kind of collected as much data as we could and then prayed
42:38
that we could find an answer based off that data. So let's try to be a little smarter about it and we'll do that in
42:46
this method. Again, let's start with a KCL at node one. So the KCL node one is
42:53
going to be the same I1 minus I2 plus is. And you should know why we've have negatives and positives
43:00
there. And as we start expanding it out into the nodal analysis uh form the beginning it starts off the
43:08
same VS minus V1 over R1 which which corresponds to the current I1 here. But
43:14
now I2 we define as V1 over R2 + R3. Hm.
43:21
Why did we do that? Well, it's because we lumped together R2 and R3 as one
43:27
resistor because they are in series as we learned before. And we can disregard
43:33
this whole wire kind of flying off here because there's no current in that wire. It's not going anywhere. It's not doing
43:40
anything. So, you can completely disregard that wire and just call this a series connection of R2 and
43:47
R3. And now what is the voltage across R2 + R3? Well, it's the voltage at node
43:55
one up here, V1. So it's V1 with reference to ground is the voltage
44:02
across R2 + R3. So that's why we have that term there. And is simply just
44:09
tacked on the end like we did before because we have no other way of defining it. All right. Right. So now what we can
44:15
do is we can split up all our fractions and move things over to other sides of the equation
44:22
and we get all our V1s on one side of the equation and our constants on the
44:28
other side of the equation. And now we can plug in for R1, R2 and R3, VS and is
44:35
we can find V1 just like that. So we found the voltage at this node is 14
44:42
volts of course with respect to ground. And so now how can we find the
44:49
voltage at V2? If we have the voltage up here and we have these two resistors in
44:55
series. How could we do? Of course we're going to use the voltage divider equation because this is a voltage
45:02
divider. We have two resistors in series. we can pluck off the voltage across that second resistor by using the
45:09
voltage divider equation. So that is super simple and all we have to do is
45:15
say that V2 equals the the source voltage or so-called source voltage in
45:21
this case it's V1 here times the resistor of interest R3 over the
45:29
combination of R2 R3. So, V1 _ R3 over R2 + R3. And we simply solve for that.
45:39
And we find that V2 equ= 6 VT. And we know that V2 is the same thing as V
45:46
out. And now that those are the same answers that we got before and it took a
45:52
lot less work to get to the to get to those two answers. So use your head when you're doing these problems. Try to pick
45:58
out these circuit elements like not circuit elements, these circuit blocks like voltage dividers. Voltage dividers
46:05
come up everywhere. So look for those first. Look for things like that. It'll
46:11
make your life a whole lot easier. Kershoff's voltage law is the complement
Kirchhoff’s Voltage Law (KVL)
46:19
of his current law and it states that all voltage drops must equal all voltage
46:27
rises in a closed loop. And well, what does that
46:33
mean? So imagine that you're going to go skiing. You can imagine a
46:40
voltage rise as a ski lift that carries you to the top of a mountain. And as you
46:47
get higher on your journey to the top of the mountain, your
46:53
potential energy, like you know from physics, also increases. Your potential
46:59
increases. So that's a voltage rise. And then once you get to the top of the mountain, you're up at the top. Yay.
47:06
you're going to start skiing down. And skiing down a mount is like passing through resistors in a circuit. That's
47:14
one resistor right there. And then you get to this flat point. You can think of that as a node, even though that really wouldn't be
47:20
flat. Um, but just for the sake of this argument. And then the next hill is like
47:26
another resistor and then you hit some flat point and then the next hill is like another resistor.
47:33
Hm. Well, let's think back about skiing again. So, as you as you ski as you ski
47:39
down your first hill right here and you get to this flat point, you're at a
47:44
lower potential than you were before up here. So, you've experienced a potential
47:51
drop. And same thing goes for here. You're at a lower potential at this second flat section than you were at the
47:59
first flat section right here. So you experience another potential drop and
48:06
eventually you get to the bottom where you experience one more potential
48:12
drop. And so you notice that once you've reached the end here, you've reached the
48:18
same potential that you started at at the very beginning before you even started your ascent up the hill over
48:25
here. You're at the same potential potential of zero. And so if you're an electron in a
48:31
circuit and these are all resistors and this was a voltage source which kind of
48:38
energizes you then if you're if you're an electron you would after you finish your descent
48:45
you would get immediately back on the lift and start all over again because
48:51
it's an electric circuit and it keeps going. Right? All right. So maybe that was kind of a weird example. Here's the
48:57
circuit I was trying to model using the skiing analogy. So, we have the voltage source
49:03
here, which is the voltage rise. And then we have three resistors in series. And those would have been the
49:11
three little hills. And those are all voltage drops because uh if we have a
49:16
current going in this direction, then they're all going to be voltage drops. And then this will be a voltage rise
49:24
through the voltage source. So we said that the drops must equal the
49:34
rises right that is the sum of all voltages in a closed loop equals zero
49:41
that's another way of saying that and once again we can express this in a in
49:47
the summation notation that rhymed as the summation of all the V's equal to
49:54
zero and again J just tells you J just tells you what voltage we're talking about. So voltage V1, V2,
50:02
V3, whatever one we're talking about. And now before we wrote out an
50:08
equation for each node and its associated currents that was in KCL, but
50:13
now we're dealing with KVL. And so we're going to write out an equation for each loop and all the
50:21
voltages associated with that loop. So we write that out in the form V1 + V2
50:28
plus V3 and on and on up to VN and set
50:33
that equal to zero. And that's how we write an equation for a loop. And that
50:38
is a KVL equation. All right, just to clarify a
50:44
few things. Say we have like a single loop circuit like this one. The first thing we want to do is set up some
50:49
arbitrary loop current. In this case, it's called I right here. And usually, we set up I to go in
50:57
the clockwise direction. And if we had multiple loops in our circuit, they'd all go in the clockwise direction. And
51:02
that just helps to simplify the problem. So, set them all up in the clockwise
51:08
direction. And now if we were to go through a voltage
51:14
source from negative to positive as we would since we're going in the clockwise
51:20
direction then we are experiencing a voltage rise.
51:26
And interestingly enough a voltage rise in a KVL equation by convention is
51:32
actually a minus V H. It's kind of weird. So in the KVL equation this would
51:39
be minus V1. And now if we had a voltage source
51:49
say in the same place here except we had the positive and the negative switched
51:56
and we went through that voltage source from positive to negative then we
52:02
would have a voltage drop. And in a cave equation, a voltage drop is a positive
52:08
V. And then as we keep going along and we go through the uh we go through all
52:14
these resistors right here, all these resistors will have a voltage drop because they are
52:22
resistors and resistors always have voltage drops and that's a plus
52:27
fee. All right, let's do a problem. Okay, here's our example circuit and
52:35
we're asked to find VAB across this 2 ohm resistor using
52:41
KVL. So, the first thing that we should do is to find the current around the loop. So, the current that
52:49
goes around this loop and the current will be the same everywhere because everything is in series with each other.
52:57
So every point in the circuit will have the same current. So to do KVL we need to set up
53:04
our arbitrary loop current in the clockwise direction. So we call I that
53:10
loop current. And then we want to start at some point in the circuit and perform
53:17
KVL by going through each one of the elements in the loop and doing that
53:22
until we return back to that point where we started. So this for this circuit,
53:27
we're going to start at point B down here. And we're going to go through all the elements in the clockwise direction
53:35
and add up all of their voltages until we get back to
53:41
B. And here is what the KVL equation would look like. And we'll explain why.
53:47
So we start at B and we go clockwise. We're going to go through a voltage source from positive to negative. That
53:53
means it's a voltage drop. So you write a positive 15 in the
54:00
equation and then we get to this 3 ohm resistor right here and we don't really
54:06
know the voltage across it but we do know that there is a current I going through that resistor. So V equals IR as
54:13
per ohms law. So you can just simply write plus 3 _ I. Since it's a voltage
54:19
drop it's a positive 3 I. And then you go through
54:24
that and then you come to this 1 ohm resistor and it's also going to be a voltage drop because it's a resistor and
54:31
it's 1 ohm times the current I. So one I
54:36
and then you get up to this 6V source and you're going to go from negative to positive on your 6volt
54:44
source. So that's in fact a voltage rise. So you write a -6 in your KVL
54:52
equation. And then you come to the 3 ohm resistor and do like you did before and do 3 I +
54:58
3 I. And then you come to your 2 ohm resistor and do plus 2 I. And then you return back to your
55:06
starting point B. And once you've reached your starting point, you know you've completed the KVL equation. So
55:15
now what we can do is combine all our um like
55:21
terms and we can solve for our current.
55:26
And so we see here that the current I equals 1 amp. And what does negative 1
55:32
amp means? It means it's actually 1 amp in the opposite direction that we specified. So yeah, it is in fact in the
55:39
other direction. So now we want to find VAB. How can we find VAB? Well, of
55:47
course, very easily. We know that V equals
55:52
IIR. And so we just multiply the current
55:58
times the resistance in which AB is across. And AB is across this 2 ohm resistor
56:04
here. So we do V AB equals 1 amps.
56:11
um times 2 ohms and we get that VAB would be -2 volt from A to B which is
56:20
the same thing as a positive 2 volts from B to
Loop Analysis
56:28
A. So loop analysis with KVL, it's kind of the parallel to nodal analysis with
56:36
KCL. Loop analysis is a process that uses KVL to determine loop
56:42
currents. So here's the example circuit that we're going to look at. So if we have a circuit like this, the first
56:48
thing we want to do is to assign loop currents to all the independent loops.
56:53
And in this case, we have two independent loops. And they are these smaller subloops with inside the
56:59
circuit. Those are independent loops. And when you see a problem that should be solved with uh loop analysis, it'll
57:07
be pretty obvious what are the loops. There usually be like two or three of them, maybe four if you're lucky. Um so
57:15
what you want to do is is assign the loop currents to both of these. So we'll call them I1 and I2 and they'll both be
57:21
in the clockwise direction. And that's because that makes life easier. All
57:26
about making life easier here, you know. All right. So to solve for these loop
57:32
currents, we want to write a KVL equation for uh each of them and then
57:37
solve using system of equations or matrices or whatever floats our boat.
57:43
All right, so now a couple words of wisdom, even though I'm not that wise, but a couple words of wisdom about
57:50
solving these. If we're in loop one with current
57:57
I1, then say we're to go through this middle resistor here, what's the value
58:03
of the voltage across that resistor? Well, you would initially say, well,
58:08
it's it's R _ I1, right? Close. But
58:13
look, I2 is also passing through that resistor. We're not in I2, but I2 has to
58:20
be considered. So what is the voltage across this
58:26
resistor? Well, it's the resistance value R times I1, which is in the positive
58:33
direction because we're going in the positive direction of I, minus I2 because I2 is going in the
58:41
opposite direction of I1. So I1 is in
58:46
the positive direction. So we have a positive I1 minus I2 because it's going in the
58:52
opposite direction of I1. So R _ I1 minus I2 is the voltage
59:02
across this resistor. And now say we were in the I2 loop. It would be basically the
59:09
opposite. I2 is now in the positive direction because we're going around the
59:15
loop like this. And now I going in the opposite direction because I1 is going
59:21
down through the resistor and I2 is going up through that resistor. And we're going to say that I2 is in the
59:27
positive direction because that's the loop that we're in. So R _ I2 minus I1
59:33
for that particular loop. Hope that makes
59:38
sense. All right. All right. So, let's work on this circuit using loop analysis. We're asked to find the
59:44
current I1 through this 1k resistor. And we're going to set up
59:50
three different loop currents cuz we have three independent loops in this circuit. So, we're going to set up an
59:55
I1, an I2, and an I3 loop. And so, let's
1:00:02
start up in I1 and write the KVL equation for that. So, the KVL for I1,
1:00:08
here it is. And how did we get there? Well, say we started in the lower right hand corner of the I1 loop right here
1:00:16
and we went in the clockwise direction as per I1 is
1:00:21
in. What would we get? Well, we go through this voltage source from negative to positive. So therefore, we
1:00:28
have a -15 as per the convention. And then after we get to 15,
1:00:35
we come across this 2k resistor right here. And what is the voltage across this 2k
1:00:41
resistor? Well, it's going to be the current through the 2k resistor times 2k, the resistance of the
1:00:48
resistor. So, what is the current through that 2k resistor? Well,
1:00:54
it's obviously going to include I1 cuz we are in the I1 loop. But what other
1:00:59
current is associated with it? Well, also I2, right? Cuz I2 is going through
1:01:05
that 2k resistor also. Now, what direction are we in? Well, we're in the direction of I1. So, I1 is going to be
1:01:14
positive and I2 is going in the opposite direction of I1. So, it's going to be negative. So,
1:01:21
how would we write this? Well, just look up here. 2K _ the quantity I1 minus
1:01:29
I2. And so, I1 is going from right to left and I2 is going from left to right.
1:01:36
And so that's kind of justification for why we can write I1 minus I2. They're
1:01:41
going in opposite directions. All right. So after we're done with the 2K resistor, we keep going
1:01:47
up in our loop and nothing there, nothing there. And we come across the 1k
1:01:52
resistor. What is the voltage across the 1k resistor? Well, it's going to be the current through the 1k resistor
1:01:59
multiplied by its resistance. So what's the current through this 1k resistor?
1:02:04
Well, it's simply just I1. It is the only associated current with this 1k
1:02:10
resistor. So, the voltage is simply 1k times
1:02:15
I1. And then we keep going. We keep going. We keep going. And we get back to our original starting point. So, we know
1:02:23
we've finished. And so, we finish off our equation by setting it equal to
1:02:29
zero. And so now a good next step for us is to
1:02:34
to look at these resistance coefficients here of 2k and 1k and find the greatest
1:02:40
common factor between the two of them and then divide by that. So in this case we're going to divide by a
1:02:46
1k. So let's divide everything in this equation by 1k and and then simplify further. So
1:02:53
here's what we get. Now how did we go from a 15 over
1:02:59
1k5 over 1k to -15 milliamps? Well if
1:03:05
you remember if you divide something in volts which 15 is in5 is in by something
1:03:11
in kiloohms you will get something in milliamps. Maybe something good to
1:03:18
remember makes your life easier. Now 2k and 1k are going to cancel to just a
1:03:27
two and 1 k and 1k are going to cancel to a 1. And of course 0 divid 1k is
1:03:34
going to be zero. All right. So now we can simplify this a little more and come
1:03:39
across our final equation for the KVL for the loop I1.
1:03:48
So we have two variables and one equation. So we're going to need at least one more equation
1:03:55
to solve for both of those variables. So let's move on to the KVL for I2. And
1:04:03
we're going to follow a very similar process to find our KVL for I2. So let's start in the same place that we kind of
1:04:10
started in I1. We'll start in this lower right hand corner and we'll move
1:04:15
clockwise. So what's the equation going to be? So here it is. And how do we get there? So if we're in our loop and we
1:04:22
move clockwise, the first thing we come upon is the 2k resistor. What's the voltage across this 2k resistor? Well,
1:04:30
it's simply going to be again the current through that resistor times its resistance. So what's the current going
1:04:36
through that resistor? Well, it's only going to be I2. There's no other associated currents. Nothing else is
1:04:42
flowing through the 2k resistor. So the voltage is simply 2k _ I2 as we
1:04:48
have here. And then we keep going clockwise around the loop and we come across the second 2k resistor. And now
1:04:55
the voltage across this 2k resistor is going to be basically the opposite of what we found in the I1 loop when we
1:05:02
were in the I1 loop. So up here remember we found that the voltage across that same resistor was 2k _ I1 - I2 the
1:05:11
quantity of but now we're going to find that the voltage in this loop is going to be 2k _ I2 - I1 which is basically
1:05:20
the opposite and so why is that? Well, now remember that we're in the direction of
1:05:26
I2. I2 is our positive direction. So, it's going to be a positive I2. And
1:05:33
I1 opposes I2. It's in the opposite direction. So, we're going to have a negative I1 cuz I2 is going from left to
1:05:42
right and I1 is going from right to left. So, that's why we have positive
1:05:48
and a negative. All right. Right. So then after the 2k resistor, we hook a right
1:05:56
here and we meet up with our 4k resistor. So what's the voltage across
1:06:01
the 4k resistor going to be? Well, again, it's going to be the same thing. Its resistance times the current through
1:06:07
it. So we're in the loop I2. So that takes the
1:06:13
positive direction. I2 is in the positive direction. So I2 is positive again. And now we have
1:06:21
I3 also going through that 4k resistor. And I3 is in the opposite direction of I2. So we write a negative
1:06:28
I3. And after we're done with that resistor, we come back to where we
1:06:34
started. So we've know we know we've finished. Set our equation equal to zero. And let's do a similar process to
1:06:41
what we did in I1. So what are we going to do? Well, find the greatest common
1:06:46
factor of all the resistances, which in this case is going to be 2k, and divide everything by
1:06:54
2k. And so, a little more simplification, and we land upon something like
1:07:01
this. So, how do we get this 5 milliamps? How did that sneak in there? Well, look at our look at our i3 loop
1:07:08
over here. What is in our i3 loop? we have a current source, a 5 milliamp current
1:07:14
source. So whenever you have a current source in one of your independent loops, the value of the loop current I3
1:07:22
right here will automatically take on the value of the current source.
1:07:30
So actually in this case I3 is going to be a negative 5 milliamps. And why is
1:07:37
that? Well, you guessed it. is because the 5 milliamp source is going in the
1:07:43
counterclockwise direction and I3 is in the clockwise direction. So to account
1:07:48
for that, we make I3 a negative 5 milliamps cuz it's going in the opposite direction of I3
1:07:56
um of the 5 millia source. So that's why uh when we have an I3 right here, it's a
1:08:02
negative I3. We plug in a negative 5 milliamps and a negative and a negative make a positive and that's why we get
1:08:09
positive 5 milliamps right here. Set that equal to zero. And let's continue
1:08:15
our simplification process. And we come across our final equation for the KVL
1:08:22
for I2. And now we have two equations, two variables. We're good to go. Let's
1:08:27
solve for I1 and I2. And uh well actually right now we're just going to solve for I1 cuz that's the only thing
1:08:32
we're interested in. Okay. So we can use whatever method we like
1:08:39
the best. I'm going to use some simple system of equations and land upon I1
1:08:45
hopefully. All right. So we take the first equation from I1 right here and
1:08:52
we're going to multiply it by two so that the I2s right here go away.
1:09:00
I'm sorry. I mean multiply this by two so that the I2s go away.4 plus a
1:09:06
positive 4 I2 is going to be of course zero I2. And then just continue adding
1:09:11
everything here as you know how to do I'm sure. So we get 5 I1 = 20 milliamps.
1:09:17
So of course I equ= 4 milliamps. And that is our answer. So the current
1:09:23
through this 1k resistor is going to be 4 milliamps. And that's how you do it using loop
Source Transformation
1:09:31
analysis. All right, so we're on the home stretch now. And I promise that the rest of the video won't be too painful.
1:09:38
Uh so now let's talk about something called source transformation. And before we can do
1:09:44
that, let's get some definitions out of the way. So first thing is called a thean circuit. What's a thean circuit?
1:09:52
Well, the circuit is just a circuit that takes on this form. So that's a voltage source in series
1:09:58
with a resistor. And the second thing is a
1:10:05
Norton circuit. And a Norton circuit takes on this form. It's a current source in parallel with a
1:10:14
resistor. And so the slide is titled source transformation. So what's that? Well, source
1:10:21
transformation is a method that allows us to easily convert between these two
1:10:26
types of circuits. So that means if I have a theant circuit, I can create a Norton circuit which will behave
1:10:33
identically in a circuit. So what's the conversion process? Well, the first part is super
1:10:40
easy. The resistor for both of them is the same. So Raven and R Norton are the
1:10:47
same value. So from now on we can just refer to the resistance as R cuz they're
1:10:53
the same. And so if I have a Norton circuit
1:10:59
you can find the equivalent thean voltage by using Ohm's law and multiplying the Norton current I know by
1:11:08
the resistance and that would give you the equivalent thean voltage. And if you have a Thean
1:11:14
circuit, you can find the equivalent Norton and current by dividing Vevenan by R. And it's literally that easy. And
1:11:21
that's how you can do source transformation. Turning a Thean circuit like this into a Nerton circuit like
1:11:28
this and vice versa. It can really help you simplify down circuits and make them
1:11:34
easier for you to analyze using the methods that we've already
Thevenin’s and Norton’s Theorems
1:11:40
learned. So Mr. Thean and Mr. Norton both created theorems that say very
1:11:47
similar things. Basically they say you can take any blackbox circuit consisting
1:11:54
of voltage sources, current sources and resistors and can convert them into a
1:12:00
thean circuit or a Norton circuit. And a a black box is basically just some
1:12:07
system or some circuit where you don't really care about the actual components inside of it. You may know the
1:12:13
components and you may know the schematic for the blackbox circuit, but you don't really care about them because
1:12:19
all you care about is how the blackbox interacts with the outside world. What
1:12:25
are its inputs and outputs like? So you can reduce a super complex
1:12:32
circuit to just one source and one resistor. And that's all you need to describe the behavior of one of these
1:12:40
circuits. And uh as we just learned about source transformation, you can convert this blackbox circuit into say a
1:12:48
thean equivalent circuit. And then once you have it in the form of avvenan equivalent circuit, you can easily
1:12:53
convert it to a Norton equivalent circuit. And of course you can do it the other way around. You can you can
1:12:59
convert first to a Norton equivalent circuit and then you can convert to a thean equivalent circuit. So it's really
1:13:05
up to you to find a the Norton equivalent
1:13:10
circuit. One of the things we need to find is the value of resistor R. And so for what we're doing, we're
1:13:18
going to be presented with some multi-element circuit and we're going to be asked to reduce it down to its
1:13:24
equivalent. So how do we find R? The first thing we want to do is to detach
1:13:30
the load resistor if there's one present. And how do you identify the load resistor? Well, it's the resistor
1:13:37
the output voltage is being taken across or the output current is going
1:13:45
through. Next thing to do is to set all sources equal to zero. That means you're
1:13:50
going to shortcircuit all the voltage sources and you're going to open circuit the current sources. And why does this
1:13:57
set them equal to zero? Remember that a voltage is a difference in potential between two points in a
1:14:04
circuit. And that's what a voltage source creates, a difference in potential. And so if you were to connect
1:14:10
those two points together as you do in a short circuit, there's no longer any
1:14:15
potential difference. Therefore, the voltage is zero. And in a current source by
1:14:22
opencircuiting it, you prevent the possibility of any current flowing. So
1:14:27
therefore, there is zero current. And so that's how you set sources equal to zero. And that's
1:14:34
why. And lastly, you want to find the equivalent resistance of this new circuit looking in quote unquote looking
1:14:41
in from the two output terminals. And you can use your knowledge of series and parallel resistors and combinations of
1:14:48
series and parallel to simplify down to just one
1:14:54
resistor. Let's just hone in on the equivalent circuits for now. We'll get to Norton equivalent circuits a little
Thevenin Equivalent Circuits
1:15:01
later, but for now we need to find the second part of our equivalent circuit.
1:15:06
We've already found R. Now we need to find V thean. So what are we going to
1:15:12
do? Well, here's our known circuit just for example. And the resistor in purple
1:15:17
over here res represents the load resistor. So what's the first step? The first thing I want to do is to detach
1:15:24
the load resistor. Again, as we've done before in the previous step, finding R.
1:15:30
And the second step is to find the open circuit voltage VOC across the circuit's
1:15:37
output terminals. So it's really as simple as that. Now that process can be pretty complicated because you might
1:15:43
have to use um nodal loop voltage divider source transformation any of those processes to find VOCC. But that's
1:15:52
really all you have to do. You just have to detach the load resistor and then find what the voltage across the output
1:15:57
terminals would be. And this includes all the sources. Um of course uh the sources are not set equal to zero when
1:16:04
you're finding Vanin. As usual, let's do an example to really
1:16:12
understand what we just learned. So, we have a circuit and we're asked find VAB,
1:16:18
the voltage across these two output terminals using Thean's theorem. So,
1:16:24
what's the first thing that we're going to do? Well, let's find RVan or just R, whatever one you want to call
1:16:29
it. So, here's how we find RVan. We've in this new circuit over here, what have
1:16:36
we done? Well, we've removed the load resistor of 6k. And that's the load resistor because
1:16:42
AB is across it. And then we've shortcircuited our 3V
1:16:49
voltage source. And we've opencircuited our 2 milliamp current source. And now all we have to do is
1:16:56
find the equivalent resistance of this new circuit looking in from these terminals. So we get an equivalent
1:17:03
resistance of 3 koohms. Easy. Now the next part is going be a little more difficult, but it's going to be finding
1:17:09
Vanin. So what are we going to do? Well, here's a circuit we're going to work on. We've moved this circuit down here, and
1:17:18
we've removed the 6 kiloohm load resistor. And I've labeled
1:17:23
this as node one, and the voltage at node one being V1. So, there's a bunch
1:17:29
of different ways you could you could do this uh to solve for VOCC, but here's the way I'm going to do
1:17:35
it. Let's do the KCL at node one. So, we have 2 milliamps going into the node,
1:17:42
and we can't have a current here because uh this end is disconnected. So, we can
1:17:47
only have a current through the 2k and the 1k um like so.
1:17:53
So the KCL is simply going to be 2k into the node and then out of the node comes
1:17:59
a current of V1 since that's the voltage here over the equivalent resistance of
1:18:05
2k + 1k which is 3k and then um and set
1:18:10
that equal to zero cuz those are the only two currents and then we can simplify and we
1:18:16
get that the voltage at v1 is 6 volts. So basically you can think of it as a um
1:18:22
6V current s uh voltage source uh between here and
1:18:28
here. So now how can we find VOCC? Uh let's try a KVL. And we can do a KVL on
1:18:34
this loop right here. Even though VOCC um is totally an open circuit, you can
1:18:41
still do a KVL on it. Uh you can you can create a loop that includes that
1:18:46
voltage. So, here's how the loop um turns out. And how do we get a negative 6 volts?
1:18:53
Well, remember if this is technically a voltage source between here and here, you're going to go through the negative
1:18:59
to the positive here of that voltage source that. So, that would be -6
1:19:04
volts. And then you get a -3 volts going through the voltage source here. And
1:19:10
then you get a positive VOC going through the voltage source. And then you've returned back to where you
1:19:15
started. So that's how we get that KVL and then you can
1:19:22
simplify and add and you get that Vanin which is the same thing as VOCC equals 9
1:19:29
volt. But we're not done cuz we just found VOCC and or we found Vean and we found
1:19:36
RVan but now we need to find VAB which is the voltage across this 6k resistor
1:19:42
right here. So let's let's move on to the right over here. And this is our
1:19:49
circuit now including the load resistor because we can't just disregard that load resistor. It's still part of the
1:19:55
circuit. Here's our equivalent our um thean equivalent circuit includes the 9V
1:20:01
source right here and the 3k resistor in series. And then we add in the 6k load
1:20:10
resistor. So, we're asked to find the voltage across that 6k load resistor. And well, how can we do that? Well, it
1:20:17
should be obvious by now. We're going to use a voltage divider. And that's real easy cuz all you have to do is multiply
1:20:23
that source voltage of 9 volts by the by the R2 over R1 + R2 combination. And
1:20:31
that's going to be a VAB of 6 volts.
1:20:36
So, as you can see, kind of a lot less work than doing it in a more traditional
1:20:41
manner, but we still get to the same result and we can probably do it
Norton Equivalent Circuits
1:20:47
quicker. Norton equivalent circuits. So, to find I Norton, which is the parallel
1:20:53
to Vevean, we follow a very similar process with some small changes.
1:21:00
So we have a known circuit and again the first step we're going to do is to detach the load resistor just as we did
1:21:08
before. And now the second step is to shortcircuit the output terminals. So we
1:21:14
didn't do this before. Before we had an open circuit, but now we're going to short circuit the output terminals.
1:21:19
Meaning we take a piece of wire and directly connect those two terminals together.
1:21:25
And the third step is to find the short circuit current ISC
1:21:32
through the shorted output. So the current through that piece of wire that
1:21:37
we just put in there. Whereas before we found the open circuit voltage between
1:21:43
those two terminals. Now we're finding the shortcircuit current. And now you can use again any
1:21:50
form analysis to find that shortcircuit current. nodal loop voltage divider. Whatever is the quickest and the easiest
1:21:57
or whatever you understand the best. Let's do the same problem we did
1:22:04
before using theorem and now let's use Norton's theorem. So here's the circuit from before and we're asked to find VAB
1:22:12
and now we're going to use Norton's theorem to find VAB. How is the process going to be similar and how is it going
1:22:18
to be different? Well, the first part finding R Norton or Ravenan, the same thing is going to be identical. So, we
1:22:25
just short circuit our voltage sources, open circuit our current sources, and remove the load resistor and find the
1:22:31
equivalent resistance. And that's what we did here, 3 koohms, the same as before. And now we have to find I
1:22:39
Norton. So, how do we do that? Well, I redrew the circuit down here, except now
1:22:44
I removed the 6 koohm load resistor and I've shortcircuited the output. Next
1:22:50
thing I'm going to do is just for me visualizing, I've moved the voltage source over there
1:22:58
just so I could see a little better. You don't have to do that personal taste. And now what do we have here?
1:23:05
Well, we have a current source in parallel with a resistor. What can we do
1:23:12
with a current source in parallel with a resistor that we just learned? Of course, we can do source transformation on it and
1:23:21
make it a voltage source in series with a resistor. And that's what we did here.
1:23:26
So, we had a 2 milliamp current source in parallel with a 3k resistor. To find the Vevean of that, you just have to
1:23:34
multiply 2 milliamps _ 3K and you get 6 V. And now you put that 3k resistor and
1:23:42
you put it in series with that new 6V voltage source. And now we have a one
1:23:49
loop circuit with two voltage sources and one resistor. What could be easier?
1:23:54
And what we want to find is the current through that loop. because the current in that loop is going to be ISC and
1:24:01
that's what we're interested in. So let's do the KVL on that circuit. So
1:24:08
let's start up here on the top on the upper right and we go through
1:24:14
the 3V source. So that's going to be a -3. Come around here, go through the 6V
1:24:20
source and that's going to be a -6. And we come across this resistor. And what's the voltage across this resistor?
1:24:27
You guessed it, it's 3k times the current ISC. And we set that equal to zero because we know we're finished. And
1:24:34
so we can reduce and simplify and we get that ISC equals 3 milliamp. So that is
1:24:42
our short circuit current 3 milliamps and that's also equal to I Norton. So
1:24:49
now let's rewrite our circuit in its Norton form. And now we can solve for
1:24:55
VAB. So here it is. We have our 3 milliamp source which we just determined
1:25:01
was 3 milliamps in parallel with the 3k
1:25:06
resistor. And now again as we did before, we're going to tack on that 6k
1:25:12
load resistor right here cuz that has to be included in our analysis to find
1:25:20
VAB. And now how can we find the voltage across AB? Real easy. find the
1:25:25
equivalent resistance of the 3k and the 6k in parallel which turns out to be 2k and then do v= i and that is going to
1:25:35
be 3 milliamps _ the 2 koohm resistor uh the equivalent um resistance between 3k
1:25:42
and 6k which is 2k so 2k _ 3 milliamps and we get 6 volts across
1:25:49
AB just as we got before using theorem and now we've just used Norton's theorem
1:25:55
term to find the same answer. So, it's really up to you which one do you like better. Um, and use whatever one makes
1:26:03
more sense for for you. All right, so there's light at the
Superposition Theorem
1:26:10
end of the tunnel now. Um, thank you for sticking with me. We're almost done. The last topic for today is superposition
1:26:16
theorem. And it's really a clever theorem. So in a circuit you can think about voltage sources and current
1:26:23
sources as driving forces each which contribute to the circuit in some way.
1:26:30
So superposition basically says you can consider the circuit one source at a
1:26:36
time. Find each sourc's contribution to the circuit and then add up all those
1:26:43
contributions at the end and that will be the actual contribution.
1:26:48
So here's the general process for doing that. Superposition says that a circuit with multiple sources can be solved by
1:26:54
this process. First thing we want to do, set all sources equal to zero except for the one that we're considering. And we
1:27:02
know how to set all sources equal to zero. Then you want to solve for the
1:27:07
necessary currents and voltages. Depends on the problem of course using only that one source which is actually going to be
1:27:15
relatively easy. And then you want to repeat step
1:27:21
two with the next source and then the next source and however many sources you
1:27:28
have. And then at the end you want to quote superimpose the solutions onto each other. Basically the sum of all the
1:27:37
solutions. Now you're going to have a bunch of different equations with seemingly the same variable. it's going
1:27:44
to be like, you know, I1 and I2 or whatever. But you need to differentiate between
1:27:50
um the variables from the different equations because they're not the same. So, what you want to use is the prime
1:27:57
symbol to differentiate variables with the same name. So, here's the general process. We have a circuit looks like
1:28:03
this, one of these double loop circuits, classic, right? And uh here's what we're going to do.
1:28:10
we're going to to uh take out one source. So in this in this uh case right here, we've taken out this voltage
1:28:16
source and we're going to solve for I1 single prime and I2 single prime. And
1:28:25
then we've in in the right circuit over here, we've taken out this voltage
1:28:30
source and we solve for I1 prime and I2P
1:28:35
prime. And then at the end, the big finale to actually find the real value
1:28:41
of I1, all you do is add up I1 single prime plus I1 double prime and you get
1:28:48
the actual value for I1. Same thing for I2. So that's the process. Now, of
1:28:54
course, let's do one last example. Last hurah. All right, last problem for the
1:29:02
day. Let's try to find VO, the voltage across this 6k resistor
1:29:09
using superp position. So what's the first thing that we're going to do? Well, we're going to draw the circuit
1:29:15
with one of the sources removed. And the first source we're going to remove is the 12vt source. So that's going to get
1:29:22
shortcircuited. So that's what happens here. And now you're probably wondering, whoa, where did the uh where did this
1:29:28
where did these two 6k resistors go? Remember now if I shortcircuit this 12vt
1:29:33
source what am I also shortcircuiting? I'm also shortcircuiting these two 6k resistors.
1:29:40
So they are also shortcircuited. So they go away and you just replace um this
1:29:46
entire circuit block right here with one short circuit which is what you see right
1:29:52
here. And now we're interested in solving for VO single prime right there.
1:29:59
What have I done to help us out a little bit? I put in a current I1. And so, what type of circuit are we
1:30:06
looking at right here? Well, we're looking at a classic current divider.
1:30:11
And how are we looking at a current divider? Because we have a current source and these two branches right
1:30:19
here, they're in parallel. So, that's a classic example of a current divider. So if you can think back to the equation of
1:30:25
a current divider, we're going to find that I1 is defined like
1:30:32
this. And it's equal to everything that we're not interested over the total resistance
1:30:39
times the current source. And that's what we have here. So we're interested in the current I1, which is going
1:30:44
through that one 6K resistor. So what we put up top is the the two 6k resistors
1:30:51
in series. is that's the equivalent resistance of that branch and then you put it over the equivalent total and
1:30:56
that's 6k + 6k + 6k and then multiply that by the value of the current source
1:31:02
and you get the current I1
1:31:07
lovely so simplify that down you find that I1 equals 4
1:31:12
milliamps now how do we find VO single prime well easy V equals IR but now you
1:31:20
just have to take into fact uh into account that I1 is flowing uh from negative to positive of VO
1:31:29
single prime so that we basically just flip the voltage so it's a -4 volt -4 _
1:31:37
6 = -4 vol. So that's VO single prime.
1:31:43
Now we have to find VO double prime. And so what's how you going to do that?
1:31:48
Well, we're going to take the original circuit and instead of deleting the
1:31:53
voltage source, now we're going to delete the current source. So, let's draw that out. So, it's going to look
1:31:59
like that. So, we have an open circuit where the current source used to be. And now
1:32:06
we call this voltage VOP prime. And I've grayed out these two 6k resistors. I
1:32:12
mean, these these two 6k resistors really have some bad luck. Uh why' I gray those out? Well, if I have a a
1:32:18
single loop here, you have to if you really notice right here, you have a
1:32:24
single loop right here. What happens in this loop uh has no bearing on what
1:32:30
happens in this loop. So, we're just going to disregard whatever happens in that loop. Treat this as a single loop.
1:32:38
And if I want to find the voltage across this 6k resistor, what can I do? Well, I
1:32:44
can do a number of things. I can do K I can do KVL uh or probably someone else.
1:32:50
But if right now I'm going to use voltage divider. I'm really into using my dividers right now. So how do I use
1:32:56
voltage divider? Well, I just do my source voltage of 12 volts times
1:33:03
the resistor that I'm interested in, which is this 6k resistor. But it would be the same actually for any of them
1:33:10
over my equivalent resistance of all the resistors. So that's 6K + 6K + 6K. And
1:33:17
that'll give me the voltage across that 6K resistor, the voltage VO
1:33:24
double prime. And that equals 4 vol. So
1:33:29
I've just calculated that VO single prime= -4 volt and VOP prime equals 4 V.
1:33:38
How do I find out the real value of VO? Real easy. All you have to do is add the
1:33:45
two together. VO single prime plus VP prime equals VO. And so, of course, that
1:33:52
is going to equal -20 volts. Real easy.
1:33:59
And it was pretty quick. All right, great
Ending Remarks
1:34:05
work. Here are my ending remarks for this video. First thing, the key to
1:34:10
solving circuit problems quickly and correctly is practice. By far the most
1:34:15
important thing you can do is keep practicing. Second thing, each technique
1:34:20
that we've learned today is not terribly difficult on its own. The challenging part is really identifying which
1:34:27
technique or combination of techniques is appropriate for a given circuit. So
1:34:33
someone can ask you solve for this current using this technique and it'll
1:34:39
probably be pretty easy because you're going to know exactly what you have to do. But if someone just says solve for
1:34:44
this current and they don't tell you what technique to use, that's where the challenge lies. And it's really important to be able to identify which
1:34:51
technique makes the most sense. Third thing, experiment with
1:34:58
circuits on your own. Can't stress this enough. play around with circuits and see how changing things in a circuit
1:35:04
will affect it. And uh you can purchase the components that we used in this
1:35:10
video, even though we didn't use real components. We just put them up on a screen, but we can you can purchase the real components
1:35:17
um from distributors like Mouser and Digi Key. And they're pretty
1:35:23
inexpensive, probably only a couple cents each for those resistors. And you can create a voltage source using
1:35:29
batteries or if you have a power supply that's even better. Uh and you can uh
1:35:36
see how changing things around will affect the circuit. In a similar way,
1:35:41
you can use simulation software like LT Spice which is free and you can download from linear technologies website to
1:35:48
verify your findings and to learn more about circuit behavior. So, if you have homework to do or if
1:35:55
you're just analyzing some circuit and you want to make sure you did it right, you can put it in LT Spice and check if
1:36:01
your answers match. And of course, you can always play around and see how changing values will change your
1:36:07
circuit. All right? So, I really encourage you to do those uh those things and keep practicing and I'm sure
1:36:15
you'll be great at circuit analysis.
1:36:20
As always, thanks for watching. I know my videos are long and if you sat through this whole thing, thanks so
1:36:27
much. Um, but I I hope it was helpful for you. I'd love to hear your feedback
1:36:33
if you have any. What would you like to see uh more of? What did you not enjoy
1:36:39
so much? I'd like to hear that, too. And uh if you liked it, give it a thumbs up. And if you want to see more videos,
1:36:46
definitely subscribe to my channel. All right, guys. Have a great day.

Search in video
Intro
0:00
This video is just the basics of electronic components, what they look like and what they actually do - and how they work in fact
0:07
So let's start with one of the most common, the one that I just picked up there the resistor
0:12
So this is a one thousand Ohm resistor I can tell that from the color bands on it, and we'll look at that later on how the color bands are interpreted
0:19
However the function of a resistor if I use the water analogy because the water analogy is very good
Resistors
0:26
If you have a pipe With water flowing through it and part of that pipe is narrowed down to a section
0:34
Then that will restrict the flow of water through that pipe Say for instance the main water pipe coming into the house. If you put a very thin
0:41
Pipe in line with that, even a fairly short one then it would really Restrict the flow of water coming in because the water would want to flow through quite quickly
0:49
But it would be forced in through this narrow channel and the resistance Posed by that narrow channel would limit the water flow in the same way that a resistor
0:59
Does exactly the same to electricity it limits the flow of electricity? the flow of Current and
1:06
In this case with the water analogy the pressure of the water
1:14
equals the voltage and it's quite interesting that the chinese sometimes refer to the voltage as pressure and it is that's exactly what it is and
1:22
the flow of the water equals the current
1:30
So the higher the flow the higher the current Now the construction of a resistor is usually in the case of these ones
1:37
this is a carbon film resistor and You get metal film, Carbon film, wire wound but one of the most common is just carbon film or the metal film and they have
1:46
a little ceramic Tube which is coated with either the metallized coating or a carbon coating up to a
1:56
Specific thickness and the thicker the carbon coating on it and the the type of the composition they're putting on it
2:03
the more conductive it will be but then they can fine-tune that they actually cut a spiral round it and
2:09
that creates a long thin path of the carbon and That increases the value of the resistance and once they've done that they put a metal cap in the end
2:20
with the leads coming off and they dip it in a sort of....
2:25
I suppose it's a lacquer really and Typically with the carbon film resistors which are my favourite, they're one of the easiest to read it'll be this sort of beige coloured
2:35
I'm not sure. What would you call that color? I've never really thought about that Beige let's call it beige it's sort of rich beige and the metal film
2:43
Resistors, which I don't like because they're usually blue and they're really hard to read. The blue color makes the color bands....
2:51
It's very.... it makes it easy to mix colors like orange and brown because they've got such a dark background
2:58
But I'll go into those colors afterwards, so that's the function of a resistor I'm not going to go into too much at the moment because at the end of the video
3:04
I'll cover things like ohm's law, but I don't want to bore the pants off you so let's move on to capacitors.
3:13
Oh - I should I should continue and say about the resistors the function of resistor is
3:19
To limit the current flow so say for instance you had An led you wanted an led to light from a battery if you connected the led straight across the battery it would burn the led out
3:29
in most instances but if you put a resistor in series with the
3:35
let's just draw as a physical Led and you hook across the plus 12 volts and
3:42
zero Volts Then by choosing the resistor value you can actually limit the current to the correct value of the led they're also used for things like
3:52
time delays you might have a Resistor charging up a capacitor
3:57
you know it trickles the current into it until the voltage reaches a certain level and then that could be used as a timing function, and you also get variable resistors where effectively it's a
4:09
Carbon track Connected at both ends are only really you only need to use a connector one end and with a wiper
4:19
that actually wipes around that track so you know depending on its position that will vary the resistance, so
4:25
Let's move on to capacitor now Because they're quite interesting so a capacitor in its most basic form is a layer of insulating material with a
Capacitor
4:36
conductive surface on each side and The best way to describe a capacitor in the water flow theory is a chamber
4:45
with a diaphragm in it that stops the water flowing directly through and
4:54
That diaphragm can flex a certain amount in either direction So say for instance, you've connected it across a battery
5:02
The positive charge would flow in at this side, and it would cause it to flex over to the negative side
5:08
It doesn't actually physically work like this but this is a good way to describe it and if you reverse the polarity then that charge that amount that filled up would then be pushed out the other side and
5:20
it would flex the other way and this allows capacitors to be used to basically hold a charge of electricity or
5:27
in the case of the AC capacitors that you often see me using these in my led lamps that
5:34
diaphragm it means that on the AC on each half wave when the polarity swaps that will let through a small amount of energy the electrons will flow back and
5:43
forth through it, but not just pass right through like a short circuit So to describe a capacitor to actually show you what a capacitor does let's make one. So I've got a bit of a
5:54
cardboard here. This is a standard six by four photo a piece of photo material and
6:01
I've got two bits of metalized films, so let's say stick the metalized film on either side, so
6:06
We've got a metal electrode, and I'm sticking it onto the insulator the dielectric and
6:13
This is old aluminium tape I think that don't seem to stick very well But that's alright. It will do what we need to do and
6:22
Then the other side of this I'll stick the other bit of tape, and that's the other electrode
6:28
and This is the physical construction. That's used throughout all capacitors
6:34
They're all pretty much like this, but not using cardboard and aluminium foil So let's get that pretty much as close to the other one alignment as possible
6:47
and the actual the two factors determine the capacitance here are the area of metallization that's in parallel with other one and
6:57
How thick the insulator is is in between them you think you know this cards. It's you know it's very thin so it's going to be quite a
7:05
You know it's going to be a Modestly high-value capacitance, but that's not true This is not going to be a high value of capacitance at all so let's put this round
7:13
let's be optimistic and say 200 Nano Farad and I'll connect it one side and the other side and
7:23
The capacitance is actually... Oops! I'm not making contact I'm connecting on to the adhesive side here my capacitor measures
7:33
One point. Oh that's terrible isn't it it's one point eight Nano farad. It's not very high at all and
7:39
if I was to cut this in half, so the actual to prove that the area of the
7:46
foil affects the capacitance if I get a pair of scissors Scissors, and I cut this in half right now
7:54
So it's one point eight three if I cut that in half It's halved the capacitance. It's now point eight, and if I cut that again in half, it'll go down to about point four
8:07
Which it has so that's basically how the capacitor works. It's basically an insulator the two metal plates on either side and
8:15
the area of the metallization and the thinness of the
8:20
separator is what Determines the capacitance and
8:25
to get the value of capacitance up the it means that in reality for components like this little hundred keep in mind that I managed
8:34
what was that just a couple of nano farad this one is rated 100 Nano farad and
8:39
If you look at things like this one this is an electrolytic capacitor which is rated
8:44
470 Micro Farad, which is a massive capacitance and to achieve that ... let's get the notepad back in again
Multilayer capacitors
8:56
To achieve the higher capacitance they often make the capacitors multi-layer, so this is something
9:02
I just printed out, I designed on the computer as a printed circuit board design sort of layout
9:08
But I just did it as a sort of graphic and if you can imagine that the blue is layers of insulation
9:14
in the ceramic capacitors and these are metallized sort of plates then by
9:20
alternating the pole sort of creating a comb of them with insulators and then putting a
9:28
Metallization down the end to connect them all together you can create Quite a large capacitance in a small area just by making a multi-story capacitor
9:35
so to speak and That's still the layers of insulation in these it's still going to be super thin you'd need a microscope probably to see all the layers
9:46
where you are going for a High voltage capacitor the size has to go up these are also 100 Nano farad. So you look at this one. It's 109 fire
9:55
It's really small, but it's a low voltage one when you're increasing the voltage you have to increase the thickness of the dielectric the insulation between them and
10:03
To make this type of capacitor these are metallized film capacitors and it's a film that's metallized
10:11
on one side and they take two strips of it, and they basically sandwich them together and
10:20
the plastic aspect of it is the insulator and the metallization is the electrode and
10:26
to fit a lot in a small area they then actually just spiral the take a big long strip and they spiral it round into a small area, and that's what creates the sort of larger area and
10:39
The thickness of the plastic film itself will Determine the voltage rating
10:44
This is a ceramic disc capacitor usually quite low values. It's usually one of the simplest and it usually is just a disc of
10:52
Ceramic with a conductive layer on both sides and then an electrode that just comes across and comes off
10:58
and then it's dipped in insulation, but you think that even this one this one is rated 10 nano farad
11:04
and it's rated [1000] volts, but To get that 10 nano farad the installation must be really really thin in the inside. I've never actually opened one of these up
11:14
Let's open one of them up right now and take a look. Ohh. Not the thing to do with your snips
11:22
That is so it really is wafer thin in there. It's so thin that most of the thickness of that is the protective coating
11:30
That is super thin in there. I don't know if you can even see that it just looks like a line
11:37
So electrolytic capacitors are one of the more exciting capacitors, and I don't mean that in a good way
11:43
the electrolytic capacitors to achieve such a high capacitance they contain a liquid electrolyte and
11:52
they have a a very thin foil inside and
11:57
the foil to create an extremely thin insulator they form an oxide layer on the aluminum foil in there and
12:06
That means it really is like Micron thick which means that they can get a very high capacitance in a small area, but to couple
12:12
onto that surface. They have to use a liquid [electrolyte] which then because ... if you looked at the
12:17
Foil it would look all pitted and mottled with that oxide coating so to get a good coupling
12:23
They use a liquid that just fills in those gaps and that's one of the downsides of well one of many of the downsides of the electrolytic capacitors because traditionally and
12:34
all the old say for instance, all the old video games from the 80s Tend to suffer problems after a while with what's called drying of the electrolytics, so they still measure the correct capacitance
12:47
but their equivalent of resistance the resistance to current flow through them changes it increases and
12:54
What that means is that They stop doing their job properly. When you get the large values like this. They're usually used to
13:04
smooth ripple so say for instance you had the output from the mains was rectified and you had a big peaky, Sort of like the
13:12
The AC full wave rectified AC waveform. Which is like the two sides of a sine wave
13:17
then by putting this across that it then just reduces it to a very slight ripple and a nice smooth DC voltage and
13:25
as that Capacitor dries out over time that ripple will get bigger, and it ultimately starts causing problems when it dips down
13:34
So low that the electronics can't sustain normal operation, and that's when you have to change capacitors
13:41
However, that's a more of an issue with Modern electronics because whereas in the old days the capacitors only had to
13:48
deal with a 100 Hertz or 120 Hertz, just mains frequency rectified
13:54
Nowadays the capacitors have to deal with the output from switch mode power supplies which is like thousands of Hertz tens of thousands of hertz and it means that they actually heat up and
14:04
they Dissipate more energy. They're just put under a lot more stress, and if you look at the top of this one
14:11
you'll see this little cross on it, and that's a safety vent because When these fail what actually happens is that oxide coating is
14:20
Can be perforated and that's really common if you accidentally connect them in reverse because it relies in the polarity to keep that
14:28
Oxide coating intact when you connect them in reverse that fails, and then suddenly you've basically got this
14:35
Liquid filled thing just connected across the power supply with no current limiting it just basically it turns into a sort of resistor and it boils
14:43
the electrolyte and when that happens the top will either sort of if you looked at it from the side bulge up and
14:51
but if it goes too far that x that's etched on to the Top will
14:56
split open and it will vent out the top and the other option there if it doesn't do that is sometimes it blows the whole can off and
15:04
it just makes a mess it gives out a vapor of the electrolyte, which is slightly caustic and it
15:12
Can unravel the foil across the room it can go off with enough Force to actually cause injury if it hits you
15:18
So you have to be kind of careful with electrolytic capacitors? so erm...
15:25
What have we covered? Let's look at diodes now
Diodes
15:31
Diodes come in various flavors. They are used for various functions you get signal diodes rectifier diodes and light emitting diodes
15:39
The function of a diode is to allow current to flow in One direction, but not the other
15:45
So the symbol for a diode. oh, I didn't mention the symbol for a capacitor was
15:52
that basically representing the two metal plates with an air gap in between and in the case the electrolytic the
16:00
That has the positive and negative are marked with
16:05
The positive being the sort of just the empty box and the negative being the filled box just for the polarity reference
16:12
However moving on to the diodes the symbol for a diode is very easy. It's very
16:17
self-explanatory In the water equivalents thing it would be a pipe with a one-way valve in it
16:23
So the water could only floor one way in this case you have the anode of the diode and the cathode spelt with a "K"
16:29
I'm not sure why they do that there must be some reason. I've never really investigated that too much but
16:36
Current will flow positive from the anode it will flow through the diode to the negative
16:41
but if you try reversing the polarity very little current if any will flow through that diode in reverse and
16:47
The main values you have to consider with diodes are the current you want to flow through them say for instance
16:54
This is a one amp diode. That's rated to handle one amp flowing through something like a
17:00
1N4148 signal diode it's not designed for anything major. It's just designed for say
17:08
rectifying small electrical signals, so it's only rated about 100 milliamps or so if that
17:13
and The other Factor is the peak inverse voltage that's what voltage it will block coming in the wrong direction so supposing if you did connect
17:22
Well this one is a 1N4007 It's rated 1000 volts so that means that it will block 1000 volts going the wrong Direction
17:29
But if you were to exceed that dramatically it will avalanche and it will start conducting the opposite Direction
17:35
So you have to choose the correct diode for the job. This is a silicon diode which typically has a when it's forward passing current in the correct direction positive to negative
17:47
it will typically have a voltage drop of about point 6 volts and Sometimes you know it depends on the voltage rating actually sometimes go up to one volt and it also depends on the current flowing through it
17:57
you get Schottky diodes which have a much lower forward voltage of between 0.2 to 0.5 volts and in
18:04
Cases of rectification that lower voltage actually makes them much more efficient the light emitting diode our
18:11
Favorite type of Diode really is a diode junction That is optimized. It behaves like a normal diode, but when it's forward biased when the currents flowing through it,
18:23
it emits light and the very first leds were actually
18:29
Here are some here, they look just like the 1N4148 diodes these are actually leds they look just like ordinary glass diodes, but these are really vintage leds and
18:39
when you pass current through In the correct direction a little red dot glows inside them
18:46
it's very very dim but they were purely for printed circuit board indicators these days of course leds are used for illumination and have
18:54
evolved greatly but one of the things you have to note with LEDs is they don't have a very high - because they're purely
19:04
Optimized for emitting light they don't have a high reverse blocking voltage it's usually just about five volts
19:09
So if you were to connect the polarity wrong in this and exceed about five volts then in the case of the
19:15
white, blue, green leds that may damage them but with red ones they may end up just conducting but not lighting in the wrong direction
19:22
but not suffer damage and
19:27
so [em] let's say the other diodes zener diodes a
19:33
zener Diode is a diode used for voltage regulation or
19:39
Voltage to provide a voltage reference. It will act like a normal diode if you pass current through in the normal direction
19:45
And it drops roughly about 0.6 volts, but you get them say for instance You want a 5 volt supply you get a 5 volt zener and when you
19:54
apply a reverse current positive flowing down to negative. It will actually
20:00
start conducting fairly Precisely at 5 volts So if you limit the current through the resistor That limits the current flow then the voltage will just sit round about 5 volts, and that's often used to provide
20:11
Very simple power supplies and regulation in circuitry
20:17
Let me think what's next. I think we may actually be going in the direction of the resistors again and.... Oh, let's look at transistors
20:27
The world of transistors is huge. There are so many different types of transistors you get the small transistors you get the big transistors
Transistors
20:35
One of the most common ones I tend to use for small projects is just a little
20:40
BC547 and the equivalent in America may roughly be a 2N3904
20:49
and for simplicity I'm just going to show the basic NPN silicon transistor one of the oldest fashioned type transistors about and
20:56
the symbol for it is this You get three pins
21:02
and if you ever want to find out what the pinout for your Transistor is if you're not sure just go on google and the number in - like 2N3904
21:11
Google it look for images, and you'll find pictures of the transistor with the actual pin
21:18
Designations usually just printed under them it just makes it very easy to find data like that, so it's got three pins
21:26
it's got the base pin. It's got the collector pin and the emitter pin in the case of an NPN transistor. It's
21:33
usually switching something down to the ground rail the negative rail or the zero volt rail and
21:43
it's used as an amplifier or switch. Supposing for instance you had a small tungsten lamp and you had say a
21:52
a five volt supply. If you wanted to control that lamp if you want to turn the lamp on and off?
21:58
But you only had very limited current available you can use a transistor and as soon as you exceed about 0.6 volts
22:05
Because it's silicon again. That's the standard silicon junction voltage Above the ground Rail here the zero volts and a
22:14
Modest current the Transistor typically has a value called a gain It's got a voltage rating a gain rating and a power dissipation rating there are lots of other ratings
22:23
But really let's keep it simple and say you know because in most instances when you're using transistor It's going to be an NPN and it's going to be like this
22:31
So say for instance you've got a gain of a hundred and that lamp's going to pass 100 milliamps to light fully
22:39
Then you want to pass at least one milliamp Into the base here and that will then be multiplied by the gain of the transistor
22:49
And it will switch the lamp so it's basically it's like a relay but it's got no moving parts And it's a little electronic switch. You know, it's just a really handy little thing
22:58
and you can also use them in other formats like for voltage or current regulation things like that, but
23:05
Just knowing the basic Operation that you know as soon as the the base has X-amount of current going in at roughly about 0.6
23:13
Volts above the emitter here then the collector current will flow that's all you really need to know it's just to get started
23:21
other types and resistors are things like the This one pictured here is a mosfet, and they're optimized for
23:31
Switching really high loads, and that one is you know I chose the STP36NF06L
23:37
for my rGB controllers because one of the nicest things about it is that it can handle a lot of current and it's on state resistance is so low that
23:48
It doesn't impede the flow of current when it's turned on To such a level that's there
23:54
It doesn't really get very warm you can pass you can use it to switch quite a modest current without having to worry even about
24:00
applying the Heatsink to because traditional transistors would
24:05
have a slight voltage drop across them and that would result in the heat dissipating, so Mosfets are much better for that they also have an extremely sensitive input
24:14
But they generally require much higher voltage on their gate as they call it too actually
24:19
Turn on but the current flow is virtually zero there. That's required to turn these on. It's a sort of
24:24
capacitive effect, so They're quite amazing things you also get a hybrid that
24:31
The Mosfets are not as robust as the traditional
24:37
Let's see bipolar transistor like this one So you get a hybrid called an IGBT
24:43
insulated Gate Bipolar Transistor, which is almost like a Traditional transistor with low gain but with one of these transistors on the front of it
24:52
So it's very easy to turn it on and it Can switch massive currents and it's a really robust transistor, but you can find all that online if you actually look for it
25:01
This is just a basically guide, so let's now look into things like Ohm's law. Ohm's law
Ohms Law
25:09
Which is just a couple of formulas - really easy and the best way to remember them is with a triangle
25:20
"V" equals "I" times "R" where "I" let's Draw that out a wee bit wider and put what they actually are voltage
25:32
Equals current, which is "I" times resistance which is ohms?
25:43
He said drawing right out the triangle. Okay? That's all right and
25:48
an application of this would be Supposing you had a 12 volt supply and you had three LEDs
26:02
so there's the three LEDs and each one is dropping about two volts each and
26:09
You want to choose a resistor that is going to limit the current So that's zero volts over there. You want to choose a resistor
26:16
it's going to limit the current through these leds to ten milliamps, so Across the leds you've got six volts dropped
26:24
across the resistor because it's 12 volts supply you get a six across the
26:30
LEDs and you're going to have six across the resistor to drop So to work out the choice of the resistor value in Ohms
26:40
You would R equals V over I
26:46
Sorry, I should mention here V equals IxR but the reason I've drawn a triangle voltage equals current times resistance
26:52
But if you want to reverse that formula resistance equals voltage divided by current and current equals voltage
26:59
divided by resistance that's why I've drawn in the triangle here, so Voltage equals current times resistance and for the other ones you divide the one above it
27:09
Much as you'd write it. If you're actually doing a Mathematical formula "R" equals "V" over "I" and "I" equals "V" over "R"
27:17
It's just an easy way to remember how they relate to each other So to calculate the resistor equals voltage to be dropped over the current so it's six volts to be dropped six volts
27:29
Divided by the current you want which is 0.01 amp which is ten milliamps
27:35
so if you bring the calculator in for that I Don't need to use the calculator But I will use the calculator for this six volts divided by 0.01 (ten milliamps) equals
Ohms Calculator
27:48
600 Ohms Six hundred Ohms now that's not a standard resistor value the six hundred Ohms.
27:57
You would have to use the nearest standard value which might be 560 ohms or
28:03
680 Ohms and The other way this form that can be used is... if you are
28:11
trying to measure how much current is flowing through some existing leds say four instance, you're measuring some led tape and
28:17
You might find that actually putting an ammeter in series with it - because a voltage drop across the resistor in series with the leds is
28:23
So low you might find an ammeter actually skews the reading a bit so say for instance
28:30
you've got a 12 Volt supply and It's feeding more leds, but you don't know the voltage across leds, and you don't know the current through them
28:44
But there's a resistor and you do know the value of the resistor
28:50
So if that's say for instance a 330 ohm resistor
28:55
330 Ohm resistor and you measure the voltage across that while the LEDs are running and you measure 5 volts and
29:03
To calculate how much current is flowing through that whole circuit You would use the formula
29:10
"I" equals "V" over "R". So that's the voltage dropped across the resistor
29:16
Divided by the value of the resistor, which is 330 Ohms
29:23
equals so that's a 5 volts divided by the 330 Ohm resistor value
29:30
Equals point zero one five so the answer is its drawing about 15 milliamps.
29:36
The 50mA is passing through that whole circuit, so it's useful be able to do it that way. Now with resistors
29:42
there are a couple of variables with them you can choose the
29:48
resistance value say for instance this is a 1 kilohm (1000 ohm) and You can also choose the power rating because if you use too small a resistor
29:56
It can actually go up in smoke. Would you like me to demonstrate that? I think you would like me to demonstrate that.
Resistor Demonstration
30:02
Let's use this Handily placed 10 Ohm resistor. I've got here. Which is just trying to escape, it must know what's about to happen to it.
30:09
So this has a 10 ohm resistor. It's color code is Brown Black Black 1 0 and a
30:15
No zeros at the end, so I'm going to connect it across 12 volts and when I do that
30:20
it's going to grossly exceed its power rating. A current of about 1 amp is going to flow through it which means it's going to dissipate about 12 watts while it's only rated
30:28
quarter watt so it's going to be the best part of 50 times its rating so let's see what happens.
30:34
It's smoking Glowing and it just burst into flames and failed. OK, would you like to see that again?
30:43
Yes, you would So let's get another 10 ohm resistor here
30:51
Hook it up, and we'll see it burst into flames again
30:57
Lots of smoke and my workshop is now absolutely stinking
31:02
So yes, so you have to choose the correct power rating for resistors. How'd you work that out? That's where another formula comes in - very simple triangle again
31:13
"P" power equals current times the voltage
31:20
so say for instance let's choose an example of this
31:26
Interesting 10 watt red, LED which has a voltage when it's operating of about nine volts and
31:32
Requires about 1 amp, which you know to give it the power rating of the led itself That's the nine volts times 1 amp is nine watts.
31:39
so to calculate if we were to actually put a resistor at 12 volt supply again and
31:45
choose our resistor to limit the Current through this to the 1 amp
31:52
So let's see here's the I'll just draw a huge big LED I'm not going to draw what's in it -
31:57
there's a three by three array, but the voltage across that is about nine volts, so we get three volts to drop across the resistor and
32:05
if we go back to the original formula R equals V over I We've got three volts divided by the one amp. We need so that's going to be about 3 Ohms
32:14
But to actually work out the power rating of it We have to multiply power equals the current through the resistor times the voltage across it, so this has got three volts across it at
32:24
one amp so it's going to dissipate three watts, but we'd actually better choosing a higher power resistor
32:30
And it's not a terribly efficiently way to drive the LED, but it works. It's very very simple and
32:36
I'd probably choose a 5 watt resistor because you want it to stay cool. You often see resistors that have just been pushed too far on printed circuit boards. You know they've been
32:45
Designed and they've said I need a 1 watt resistor they use a 1 watt resistor and instead of the nice color code
32:51
It's basically the whole thing is just brown and the circuit board shows heat round it as well. So it's good to dissipate - get rid of that heat.
32:59
The colour codes This is the color code for resistors
Resistor Colour Code
33:05
now a resistor has markings on it - in the case of
33:11
This one here this 1000 Ohm resistor. It's got one band here. Which is brown
33:19
It's got a black band actually let's let write it like that
33:25
black And it's got another band which is red and then at the end. It's got a band which is gold
33:36
The gold band at the end indicates the tolerance but what's really important for us is the first three bands and this
33:42
The one of them the gold one indicates the tolerance in this case, it's 5% tolerance, and it just means that
33:50
It's going to be within 5% of the - if you measured the resistance of this it's a thousand ohms It's going to be you know within 5% of 1000 Ohms
34:01
The color code itself is worked out like this -
34:06
The first line is the first number - the first band is the first number so in the case of Brown it means 1 so that's one
34:15
The black means zero and the red means two but the third code is actually a multiplier
34:21
So in the case the red one it means there's two zeros two zeros equals 1000 Ohms. If you had a forty seven ohm resistor
34:32
It would be yellow for the four violet for the Seven
34:38
and then because there are no zeros after that it would be a black band. Yellow violet black would be forty seven ohms.
34:45
If it's going to be a much lower value like four point seven Ohms, you'll get
34:50
Basically a divider either gold or silver where the first two digits if it's followed by a gold band it will be a
34:57
first digit point second digit and so for instance four point seven would be a
35:04
Yellow Violet gold and it would be four point seven or for even lower values you
35:12
Can't see if I really come across silver often it's zero point and then the first two bands so that would be in the case of the
35:21
four and seven the yellow and violet it would be 0.47 Ohms very small value.
35:28
So there are ways to remember this the one I was taught with is:- Billy Brown Revives On Your Gin But Values Good Whisky.
35:36
That's basically the colors in sequence the first letter of the colors
35:42
Starting at zero and going up to nine and this is one of these things that It seems a bit daunting when you have to remember a color code like this
35:49
But the more you do it the easier it gets and there are really rude ones. I mean
35:55
it's helpful when the first word Is actually the color because the first two?
36:01
Letters are "B" unfortunately, so Billy Brown the brown indicated the brown color
36:07
but you also get the really rude one Black Boys Ride Our Young Girls, But Virgins Go Without.
36:14
Which is strangely the rude ones are the easiest ones to remember? I mean, I would try and be politically correct and say you must only use really polite ones
36:23
But to be honest the ruder ones. I mean by all means you guys If you're familiar with the color code, and you have one that you like to remember things by no matter
36:33
How rude it is within reason put it in the comments down below? But the ruder ones are just the easiest to remember and once you've you know
36:41
After you've been using resistors and doing you know reading the color codes for a while You'll just end up you'll just look at a resistor and go 1K (1000 ohms) just look at it
36:50
And just instantly know the value It's how it is. The same color code is sometimes used on older capacitors, and it's still used on
36:58
inductors which look very much like resistors and so That's just a summary. I mean, I'm not going to go into too much detail because it would get boring very very quickly
37:08
But this is just the basics of what you need to know how to work out the power rating of a resistor if you're driving quite a heavy load with it. In most instances of standard quarter watt resistor is fine and
37:21
How to choose the resistance value to limit current to whatever you want through leds and things that.
37:26
So fundamentally, that's it Just hopefully that's sort of helped
37:32
And I've not over complicated it as I sometimes do, and that's put some of the jigsaw pieces together.
37:38
Because as you understand it and as you build stuff with electronics and to be honest the best way to learn electronics is buy kits
37:45
Build them, blow them up. Have little incidents, try and fix them Maybe fix them successfully, and that way you'll just suddenly - everything will just fall into place
37:53
and You'll suddenly realize that Without even noticing it that you suddenly know how all these components work and what they do and how to select them
38:01
It's just a natural thing that evolves over time.
