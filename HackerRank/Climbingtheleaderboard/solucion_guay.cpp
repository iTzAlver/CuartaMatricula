#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the climbingLeaderboard function below.
vector<int> climbingLeaderboard(vector<int> scores, vector<int> alice) {
    //He cambiado cosas,he usado la idea de remover los duplicados,inicialmente lo hice
    //con un diccionario pero no hace falta. Intentaré hacerlo con las funciones lower_bound
    //y upper_bound,que queda mas corto todavia
    int ns=scores.size();
    vector<int> puntuaciones(ns);
    vector<int> lista_soluciones;
    int j = 0;
    for (int i=0; i<ns-1; i++){ 
        if (scores[i] != scores[i+1]){
            puntuaciones[j++] = scores[i];}
    } 
    puntuaciones[j++] = scores[ns-1]; 

    int b,k=0;
    ns=j;
    for(auto i: alice){
        for(b=puntuaciones.size()/2;b>=1;b/=2){
            while((k+b < ns) and i<= puntuaciones[k+b]){k+=b;}
        }
        (i< puntuaciones[k+b])?k=k+2:k=k+1;
        lista_soluciones.push_back((k));
        k=0;
    }
    return lista_soluciones;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int scores_count;
    cin >> scores_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string scores_temp_temp;
    getline(cin, scores_temp_temp);

    vector<string> scores_temp = split_string(scores_temp_temp);

    vector<int> scores(scores_count);

    for (int i = 0; i < scores_count; i++) {
        int scores_item = stoi(scores_temp[i]);

        scores[i] = scores_item;
    }

    int alice_count;
    cin >> alice_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string alice_temp_temp;
    getline(cin, alice_temp_temp);

    vector<string> alice_temp = split_string(alice_temp_temp);

    vector<int> alice(alice_count);

    for (int i = 0; i < alice_count; i++) {
        int alice_item = stoi(alice_temp[i]);

        alice[i] = alice_item;
    }

    vector<int> result = climbingLeaderboard(scores, alice);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

