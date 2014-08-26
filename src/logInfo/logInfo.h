#ifndef LOG_INFO_H
#define LOG_INFO_H
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
void logInfo(const char*file, int line, const char* fmt, ...);
#define LXTLOG(fmt, ...) \
    logInfo(__FILE__, __LINE__, fmt,##__VA_ARGS__)

#endif