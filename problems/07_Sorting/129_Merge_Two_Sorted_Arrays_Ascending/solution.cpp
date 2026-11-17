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

bool isSquare(long long x) {
    if (x < 0) return false;
    long long r = (long long)llround(sqrt((long double)x));
    while (r * r < x) r++;
    while (r * r > x) r--;
    return r * r == x;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<double> a(n), b(m), res;
    for (auto &v : a) cin >> v;
    for (auto &v : b) cin >> v;
    res.reserve(n + m);
    merge(a.begin(), a.end(), b.begin(), b.end(), back_inserter(res));
    cout << fixed << setprecision(6);
    for (size_t i = 0; i < res.size(); i++) cout << (i ? " " : "") << res[i];
    cout << "\n";
}
