#ifndef LOG_INFO_H
#define LOG_INFO_H
#include <stdio.h>
#define LXTLOG(fmt, ...) \
    logInfo(__FILE__, __LINE__, fmt, ##__VA_ARGS__)
void logInfo(const char*file, int line, const char* fmt, ...);
#endif