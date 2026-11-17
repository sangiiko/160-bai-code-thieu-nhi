/*
 * Floating-point sequence/value checker with 1e-6 absolute/relative tolerance.
 * Also supports "EMPTY" sentinel output when applicable.
 */
#include "testlib.h"
#include <cmath>
#include <string>

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    const double EPS = 1e-6;

    if (ans.seekEof()) {
        quitf(_fail, "Jury answer is empty");
    }

    std::string firstAns = ans.readWord();
    if (firstAns == "EMPTY") {
        if (ouf.seekEof()) {
            quitf(_wa, "Expected EMPTY, got EOF");
        }
        std::string firstOut = ouf.readWord();
        if (firstOut != "EMPTY") {
            quitf(_wa, "Expected EMPTY, found '%s'", compress(firstOut).c_str());
        }
        if (!ouf.seekEof()) {
            quitf(_wa, "Extra output after EMPTY");
        }
        quitf(_ok, "EMPTY");
    }

    int count = 0;
    auto checkToken = [&](const std::string& ansTok) {
        count++;
        double expected = stringToDouble(ans, ansTok.c_str());
        if (ouf.seekEof()) {
            quitf(_wa, "Unexpected EOF at element %d (expected %.10f)", count, expected);
        }
        double actual = ouf.readDouble();
        if (!doubleCompare(expected, actual, EPS)) {
            quitf(_wa, "Element %d differs: expected %.10f, found %.10f", count, expected, actual);
        }
    };

    checkToken(firstAns);
    while (!ans.seekEof()) {
        std::string tok = ans.readWord();
        checkToken(tok);
    }

    if (!ouf.seekEof()) {
        quitf(_wa, "Extra information in contestant output");
    }

    quitf(_ok, "%d real value(s) matched within 1e-6 tolerance", count);
}
