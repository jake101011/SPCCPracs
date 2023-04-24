%{
    int vow_count=0;
    int const_count=0;

%}

%%
[aeiouAEIOU] {vow_count++;}
[a-zA-Z] {const_count++;}
%%
int yywrap(){}
int main()
{
    printf("Enter the string of vowels and consonants:");
    yylex();
    printf("No of vowels are: %d\n"vow_count);
    printf("No of consonants are: %d\n" ,const_count);
    return 0;
}
