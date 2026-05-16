% males
male(john).
male(michael).
male(david).
male(james).
male(robert).

% females
female(mary).
female(sarah).
female(linda).
female(emily).
female(lisa).

% parents
parent(john, michael).
parent(john, david).
parent(mary, michael).
parent(mary, david).

parent(michael, james).
parent(michael, emily).
parent(sarah, james).
parent(sarah, emily).

parent(david, robert).
parent(david, lisa).
parent(linda, robert).
parent(linda, lisa).

% relationships rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

child(X, Y) :- parent(Y, X).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
grandchild(X, Y) :- grandparent(Y, X).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

uncle(X, Y) :- parent(Z, Y), sibling(X, Z), male(X).
aunt(X, Y) :- parent(Z, Y), sibling(X, Z), female(X).

cousin(X, Y) :- parent(Z, X), parent(W, Y), sibling(Z, W).