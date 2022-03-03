# FORMAL DEFINITION OF TINY BASIC

```
line ::= number statements CR
         statements CR
statements ::= statement
               statement : statements
statement ::= PRINT printlist
              INPUT varlist
              LET var = expression
              GOTO expression
              GOSUB expression
              RETURN
              IF expression relop expression THEN statement
              REM commentstring
              CLEAR
              RUN
              LIST
              LOAD "characterstring" 
              SAVE "characterstring"
              STOP
              END 
printlist ::=
              printitem
              printitem :
              printitem separator printlist
printitem ::= expression
              "characterstring"
varlist ::= var
            var , varlist
exprlist ::= expression
             expression , exprlist
expression ::= unsignedexpr
               + unsignedexpr
               - unsignedexpr
unsignedexpr ::= term
                 term + unsignedexpr
                 term - unsignedexpr
term ::= factor
         factor * term
         factor / term
factor ::= var
           number
           ( expression )
           functionpackage.json
function ::= RND ( expression )
number ::= digit
           digit number
separator ::= , ! ;
var ::= A ! B ! ... ! Y ! Z
digit ::= 0 ! 1 2 ! ... ! 9
relop ::= < ! > ! = ! <= ! >= ! <> ! ><
```

---

Дополнительные правила (реализация не требуется)

```
statement ::= ...
              PR printlist
              var = expression
              IF expression relop expression statement
              RUN exprlist
              LIST exprlist              
              ...
printlist ::=
              ...
              printitem :
function ::= ...
             USR ( exprlist )
```
