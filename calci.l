%{
#include "y.tab.h"
#include<math.h>
extern double vbltable[26]; %}

%%
[0-9]+  {   yylval.dval=atof(yytext);
            return NUMBER;
        }
[\t]    ;
[a-z]   {
            yylval.vblno=yytext[0] - 'a';
            return NAME;
        }
"$"     {   return 0;}\n |
            return yytext[0];
            
%%

int yywrap(void) 
{
    return 0;
}

int main(void)
{
    yyparse();
    return 0; 
}

int yyerror(void)
{
    printf("error");
    exit(1);
}