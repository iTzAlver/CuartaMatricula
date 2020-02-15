#include <bits/stdc++.h>

#define long long ll
using namespace std;

vector<string> split_string(string);

// Complete the lilysHomework function below.
int lilysHomework(vector<int> arr) {
    
    int contador=0;
    int ui,ordi;

    map<string,int> posunarr;
    vector<int> unorderarr;

    for(int i=0;i<arr.size();i++){
        unorderarr.push_back(arr[i]);
    }
    sort(arr.begin(),arr.end(),greater<int>());
    
    for(int i=0;i<arr.size();i++){
        posunarr[to_string(unorderarr[i])]=i;
    }

    for(int i=0;i<arr.size();i++){
        if(unorderarr[i] != arr[i]){

            ui = unorderarr[i];
            ordi = arr[i];

            //Swap
            unorderarr[ui]^=unorderarr[posunarr[to_string(ordi)]];
            unorderarr[posunarr[to_string(ordi)]]^=unorderarr[ui];
            unorderarr[ui]^=unorderarr[posunarr[to_string(ordi)]];
            //Fin swap
            
            
            posunarr[to_string(ui)]=posunarr[to_string(ordi)];
            posunarr[to_string(ordi)] = i;
            contador+=1;
        }

    }
    
    return contador;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int result = lilysHomework(arr);

    fout << result << "\n";

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
