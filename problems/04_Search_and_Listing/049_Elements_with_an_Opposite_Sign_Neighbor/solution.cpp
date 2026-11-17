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

bool isSquare(long long x) {
    if (x < 0) return false;
    long long r = (long long)llround(sqrt((long double)x));
    while (r * r < x) r++;
    while (r * r > x) r--;
    return r * r == x;
}

bool isPalin(long long x) {
    if (x < 0) return false;
    long long orig = x, rev = 0;
    while (x > 0) { rev = rev * 10 + x % 10; x /= 10; }
    return orig == rev;
}

int firstDigit(long long x) {
    x = llabs(x);
    while (x >= 10) x /= 10;
    return (int)x;
}

bool allOddDigits(long long x) {
    x = llabs(x);
    if (x == 0) return false;
    while (x > 0) {
        if ((x % 10) % 2 == 0) return false;
        x /= 10;
    }
    return true;
}

bool isPow3(long long x) {
    if (x < 1) return false;
    while (x % 3 == 0) x /= 3;
    return x == 1;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<double> a(n), res;
    for (auto &v : a) cin >> v;
    for (int i = 0; i < n; i++) {
        bool ok = (i > 0 && a[i] * a[i - 1] < 0) || (i + 1 < n && a[i] * a[i + 1] < 0);
        if (ok) res.push_back(a[i]);
    }

    if (res.empty()) cout << "EMPTY\n";
    else {
        cout << fixed << setprecision(6);
        for (size_t i = 0; i < res.size(); i++) cout << (i ? " " : "") << res[i];
        cout << "\n";
    }
}
