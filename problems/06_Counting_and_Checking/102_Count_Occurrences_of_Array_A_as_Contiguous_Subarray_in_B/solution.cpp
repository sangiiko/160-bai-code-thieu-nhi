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
    for (auto &v : a) cin >> v;
    for (auto &v : b) cin >> v;
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && a[i] != a[j]) j = pi[j - 1];
        if (a[i] == a[j]) j++;
        pi[i] = j;
    }
    int cnt = 0, j = 0;
    for (int i = 0; i < m; i++) {
        while (j > 0 && b[i] != a[j]) j = pi[j - 1];
        if (b[i] == a[j]) j++;
        if (j == n) { cnt++; j = pi[j - 1]; }
    }
    cout << cnt << "\n";
}
