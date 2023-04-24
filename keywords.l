%{
    #inlude<stdio.h>
    #include<stdlib.h>
    int keywords = 0;
    int identifiers = 0;
    int operators = 0;

%}

%%
if|else|while|do|for|int|printf|return|main  { keywords++; }
[a-zA-Z][a-zA-Z0-9]*                         { identifiers++; }
\+|\-|\*|\/|\%|\=|\!=                        { operators++; }
.                                            ;

%%
int yywrap(void){
    return 1;
}
int main(int argc,char** argv){
    if (argc>1){
        FILE *file;
        file = fopen(argv[1], "r");
        if(!file){
            fprintf(stderr, "Could not open %s\n",argv[1]);
            exit(1);
        }
        yyin = file;   
    }
    yylex();
    printf("Keywords :%d\nIdentifiers: %d\nOperators: %d\n",keywords.identifiers,operators);
    return 0;
}
