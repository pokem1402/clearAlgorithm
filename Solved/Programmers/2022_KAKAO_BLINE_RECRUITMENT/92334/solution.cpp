#include <string>
#include <vector>

using namespace std;

bool rpt_mtx[1000][1000];
int reported[1000];

void sort(vector<string> id_list, vector<int> &order, int max)
{

    vector<vector<int>> buckets;

    for (int i = 0; i < id_list.size(); i++)
    {
        order.push_back(i);
    }

    for (char i = 'a'; i <= 'z' + 1; i++)
    { // zero for null
        vector<int> alphabet;
        buckets.push_back(alphabet);
    }

    for (int i = max - 1; i >= 0; i--)
    {
        for (auto x : order)
        {
            if (id_list[x].size() > i)
            { // in range
                char alphabet = id_list[x][i];
                buckets[alphabet - 'a' + 1].push_back(x);
            }
            else
            { // out of range
                buckets[0].push_back(x);
            }
        }

        int count = 0;
        for (auto &bucket : buckets)
        {
            while (bucket.size())
            {
                order[count++] = *bucket.begin();
                bucket.erase(bucket.begin());
            }
        }
    }
}

int get_length_longest_word(vector<string> id_list)
{

    int n = id_list.size();

    int max = 0;

    for (auto x : id_list)
    {
        if (max < x.size())
            max = x.size();
    }
    return max;
}

vector<string> split(string s, char delim)
{

    vector<string> substrings;

    int position = s.find(delim);

    substrings.push_back(s.substr(0, position));
    substrings.push_back(s.substr(position + 1, s.length() - 1));
    return substrings;
}

int find(string id, const vector<string> &id_list, const vector<int> &order)
{

    for (const auto &x : order)
    {

        if (id_list[x].length() != id.length())
            continue;

        int i = 0;
        while ((id_list[x][i] == id[i]) && i < id.length())
            i++;

        if (i == id.length())
            return x;
    }
    return -1;
}

vector<int> solution(vector<string> id_list, vector<string> report, int k)
{

    vector<int> answer, order;

    int max, n;

    n = id_list.size();
    max = get_length_longest_word(id_list);

    // id_list sorting by radix
    sort(id_list, order, max);

    for (int i = 0; i < n; i++)
        answer.push_back(0);

    // get
    for (auto rep_s : report)
    {

        vector<string> rep = split(rep_s, ' ');

        int aIdx = find(rep[0], id_list, order);
        int bIdx = find(rep[1], id_list, order);

        if (!rpt_mtx[aIdx][bIdx])
        {
            rpt_mtx[aIdx][bIdx] = true;
            reported[bIdx]++;
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (reported[i] >= k)
        {
            for (int j = 0; j < n; j++)
            {
                if (rpt_mtx[j][i])
                    answer[j]++;
            }
        }
    }

    return answer;
}