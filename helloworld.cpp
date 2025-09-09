#include <stdio.h>
#include <dave/version.h>

int main() {
    printf("version: %d\n", discord::dave::MaxSupportedProtocolVersion());
    return 0;
}
