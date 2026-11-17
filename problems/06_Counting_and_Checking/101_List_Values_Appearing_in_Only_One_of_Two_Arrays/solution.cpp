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
    int n, m; cin >> n >> m;
    vector<long long> a(n), b(m);
    unordered_set<long long> sa, sb, printed;
    for (auto &v : a) { cin >> v; sa.insert(v); }
    for (auto &v : b) { cin >> v; sb.insert(v); }
    vector<long long> res;
    for (auto v : a) if (!sb.count(v) && printed.insert(v).second) res.push_back(v);
    for (auto v : b) if (!sa.count(v) && printed.insert(v).second) res.push_back(v);
    if (res.empty()) cout << "EMPTY\n";
    else {
        for (size_t i = 0; i < res.size(); i++) cout << (i ? " " : "") << res[i];
        cout << "\n";
    }
}
