%{
    #include<stdio.h>
    #include<string.h>
    int verb_count = 0;
    int adverb_count = 0;
    int adjective_count = 0;
    int noun_count = 0;
%}

%xverb_token
%xadverb_token
%xadjective_token
%xnoun_token

%%
"run"|"walk"|"swim"|"fly"|"eat"|"drink"|"sleep"|"play"|"work"
{
    verb_count++;
    BEGIN(verb_token);
}

"quickly"|"slowly"|"angrily"|"happily"|"carefully"|"loudly"|"well"|"badly"|"hard"|
{
    adverb_count++;
    BEGIN(adverb_token);
}

"happy"|"sad"|"angry"|"excited"|"excited"|"tired"|"strong"|"weak"|"big"|"small"|"fast"
{
    adjective_count++;
    BEGIN(adjective_token);
}

"dog"|"cat"|"bird"|"car"|"house"|"tree"|"flower"|"book"|"pencil"|"computer" 
{
    noun_count++;
    BEGIN(noun_count);
}


<verb_token>.|\n      { BEGIN(INITIAL); }
<adverb_token>.|\n    { BEGIN(INITIAL); }
<adjective_token>.|\n { BEGIN(INITIAL); }
<noun_token>.|\n      { BEGIN(INITIAL); }

%%
int yywrap(){}
int main(int argc,char **argv[])
{
    yylex();
    printf("Number of verbs: %d\n",verb_count);
    printf("Number of adverbs: %d\n",adverb_count);
    printf("Number of adjective: %d\n",adjective_count);
    printf("Number of noun: %d\n",noun_count);
    return 0;
}
