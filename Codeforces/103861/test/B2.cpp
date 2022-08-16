#include <vector>

using namespace std;

char buffer[5002];

struct Substring
{

    char digit;
    // the head idxs of the substring
    vector<int> idx;
    vector<Substring> child; 
};


struct Idx
{
    // the order among n size substrings
    // nstr_ord[n-1][i] : the i th substring among the n size substrings 
    vector<int> nsstr_ord; 
};

// ary = Source string, start1/2 = start of substring 1/2, slength = length of substrings
int compare_substring(const char *s, const int start1, const int start2, const int slength)
{

    const unsigned char *s1 = (const unsigned char *)s + start1;
    const unsigned char *s2 = (const unsigned char *)s + start2;

    unsigned char c1 = 0, c2 = 0;

    for (int i = 0; !(c1 - c2) && (i < slength); i++)
    {
        c1 = (unsigned char)*s1++;
        c2 = (unsigned char)*s2++;
        if (c1 == '\0' || c2 == '\0')
            return -1;
    }

    return c1 - c2;
}

unsigned int get_init_length(char *s)
{

    unsigned int length = 0;
    do
    {
        if (*s == '\0')
            break;
        if (*s == '\n')
        {
            *s = '\0';
            break;
        }
        s++;
        length++;
    } while (true);

    return length;
}

int get_answer(const char * buffer, const int n){

    int answer= 0;


    vector<Idx> buffer_idx;
    vector<Substring> Substrings;


    // initialize buffer_idx
    for (int idx= 0; idx <= n; idx++){

        Idx index;

        Substring ss;
        ss.digit = buffer[idx];

        // index.nsstr_ord.push_back

        buffer_idx.push_back(index);
    }




    return answer;
}


int main(){
    
    



    return 0;
}