#include <bits/stdc++.h>

using namespace std;

// Complete the formingMagicSquare function below.
int formingMagicSquare(vector<vector<int>> s) {
  vector<vector<vector<int>>> mat{{8, 1, 6}, {3, 5, 7}, {4, 9, 2}};

  for (int j = 0; j < 3; j++) {
    for (int k = 0; k < 8; k++) {
      cost[k] += abs(s[i][j] - mat[k][i][j]);
    }
  }

  sort(cost.begin(), cost.end());
  return cost[0];
}

int main() {
  ofstream fout(getenv("OUTPUT_PATH"));

  vector<vector<int>> s(3);
  for (int i = 0; i < 3; i++) {
    s[i].resize(3);

    for (int j = 0; j < 3; j++) {
      cin >> s[i][j];
    }

    cin.ignore(numeric_limits<streamsize>::max(), '\n');
  }

  int result = formingMagicSquare(s);

  fout << result << "\n";

  fout.close();

  return 0;
}
