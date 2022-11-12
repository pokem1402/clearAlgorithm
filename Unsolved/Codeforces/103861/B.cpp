
#include <iostream>
#include <string>

using namespace std;

//  '\n' + '\0'
char buffer[5002];

// ary = Source string, start1/2 = start of substring 1/2, slength = length of substrings
int compare_substring(const char * s, const int start1, const int start2, const int slength){

    const unsigned char *s1 = (const unsigned char *) s + start1;
    const unsigned char *s2 = (const unsigned char *) s + start2;

    unsigned char c1 = 0, c2 = 0;

    for (int i = 0; !(c1 - c2) && (i < slength); i++)
    {
        c1 = (unsigned char)*s1++;
        c2 = (unsigned char)*s2++;
        if(c1 == '\0' || c2 == '\0')
            return -1;
    }

    return c1 - c2;
}

unsigned int get_init_length(char * s){

    unsigned int length = 0;
    do{
        if(*s == '\0')
            break;
        if(*s == '\n'){
            *s = '\0';
            break;
        }
        s++;
        length++;
    }while(true);

    return length;

}

int get_answer(const char * buffer, const int n){

    int answer = 0;
    int lc, lb;

    for (int start = 0; start <= n - 6; start++)
    {
        for (int la = 1; 3 * la <= n - 3 - start; la++)
        {
            if (!compare_substring(buffer, start, start+la, la))                 // A1 == A2?
            {
                for (int L = 2; L <= n - start - 3 * la - 1; L++)
                {
                    if (compare_substring(buffer, start, start + 2*la + L, la))  // A2 == A3 ?
                        continue;

                    lc = L - 1;
                    lb = 1;

                    while ((lb <= n - start - 3 * la - L) && (lc > 0))
                    {

                        if (!compare_substring(buffer, start+ 2*la, start + 3*la + L , lb)){  // B1 == B2 ?
                            answer++;
                            lc--;
                            lb++;
                        }
                        else
                            break;
                    }
                }
            }
        }
    }

    return answer;
}

int main(){

    int T, answer, n;
    scanf("%d\n", &T);


    for (int i=0; i<T; i++){
        
        // scanf("")
        fgets(buffer, sizeof(buffer), stdin);

        n = get_init_length(buffer);
        // getline(cin >> ws, S);                      // getline extract ws from previous cin buffer remained 
        answer = get_answer(buffer, n);
        // cout<< answer << "\n";
        printf("%d\n", answer);
    }
    return 0;
}