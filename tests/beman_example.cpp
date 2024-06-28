#include <example.hpp>
#include <scn/scan.h>

#include <iostream>
#include <vector>

int main()
{
    std::string source{
        "1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 111 222 333 444 555 666 "
        "777 888 999"};
    std::vector<int> integers;
    auto input = scn::ranges::subrange{source};

    while (auto result = scn::scan<int>(input, "{}")) {
        integers.push_back(result->value());
        input = result->range();
    }

    for (auto i : integers) {
      std::cout << i << "\n";
    }
    return 0;
}
