# Find Fibonacci by Value

## Created with ❤️

### Technical Decisions made:

- First implemented the base cases of fibonacci which were 0 and 1, returning their respective numbers.
- Two variables were used with a temporary variable to switch the value in each iteration.
- Decided not to add a base case for 1 as the second variable starts with value 1 and the for wouldn't change the value.
- Avoided use of recursivity as it would be slower
- Integated the fibonacci function into an API using flask with the endpoint /fibonacci

### Optimization

The code as it is right now is O(n) and uses three variables. The only optimization I would think is to use "x" or "n" somehow inside the loop instead of using the temp variable. As of right now I don't see any optimization whatsover

### Engineering Thinking

What I do every time I have to solve a problem, I first gather all the information I need to start tackling the problem at hand. After I know what I'm facing, I start making tests to check if what I'm doing is what is required for the solution. To finish it off, I optimize the solution in any way I can.

## Happy Coding! :computer:
