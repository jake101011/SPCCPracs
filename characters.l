%{
    #include<stdio.h>
    int word_count = 0;
    int char_count = 0;
    int line_count = 0;
%}

%%
[A-Za-z] + {word_count++; char_count +=strlen(yytext);}
. { char_count++;}
\n { line_count++; }

%%
int main(){
    yylex();
    printf("Word count:%d\n",word_count);
    printf("Character count:%d\n",char_count);
    printf("Line count:%d\n",line_count);
    return 0;
}
int yywrap(){
    return 1;
}
