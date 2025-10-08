% Facts
fact(rainy).
fact(cloudy).

% Rules
rule([rainy, cloudy], wet_grass).
rule([wet_grass], slippery).

% Forward chaining
forward :-
    rule(Conds, Fact),
    all_true(Conds),
    \+ fact(Fact),
    assert(fact(Fact)),
    write('Derived: '), write(Fact), nl,
    forward.
forward.

% Check if all conditions are true
all_true([]).
all_true([H|T]) :- fact(H), all_true(T).

% Run
start :-
    write('Initial facts: '), nl,
    list_facts,
    forward,
    write('Final facts: '), nl,
    list_facts.

% List all facts
list_facts :- fact(F), write(F), nl, fail.
list_facts.
