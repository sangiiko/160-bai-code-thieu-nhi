#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long x) {
    if (x < 2) return false;
    if (x == 2 || x == 3) return true;
    if (x % 2 == 0 || x % 3 == 0) return false;
    for (long long i = 5; i * i <= x; i += 6)
        if (x % i == 0 || x % (i + 2) == 0) return false;
    return true;
}

bool isPerfect(long long x) {
    return x == 6 || x == 28 || x == 496 || x == 8128 || x == 33550336;
}

bool isPalin(long long x) {
    if (x < 0) return false;
    long long orig = x, rev = 0;
    while (x > 0) { rev = rev * 10 + x % 10; x /= 10; }
    return orig == rev;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n; vector<long long> a(n), order;
    unordered_map<long long, int> freq;
    int mxf = 0;
    for (auto &v : a) {
        cin >> v;
        if (freq[v] == 0) order.push_back(v);
        freq[v]++;
        mxf = max(mxf, freq[v]);
    }
    vector<long long> res;
    for (auto v : order) if (freq[v] == mxf) res.push_back(v);
    for (size_t i = 0; i < res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << "\n";
}
