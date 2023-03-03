#include <stdio.h>

int main() {
    int num;
    while (scanf("%d", &num) != EOF) {
        int e = (num >> 24) & 0xFF; // 取高8位
        int b = (num >> 8) & 0xFFFF; // 取中间16位，去掉e和v
        int v = num & 0xFF; // 取低8位
        b = (b << 8) | e; // b 左移8位，并加上 e
        int result = (b << 8) | v; // b 左移8位，并加上 v
        printf("%d\n", result);
    }
    return 0;
}