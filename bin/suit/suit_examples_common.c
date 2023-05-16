/*
 * Copyright (c) 2020-2023 SECOM CO., LTD. All Rights reserved.
 *
 * SPDX-License-Identifier: BSD-2-Clause
 */

#include <sys/stat.h>
#include <sys/types.h> // mkdir
#include "suit_examples_common.h"

size_t read_from_file(const char *file_path,
                      uint8_t *buf,
                      const size_t buf_len)
{
    size_t read_len = 0;
    FILE* fp = fopen(file_path, "rb");
    if (fp == NULL) {
        return 0;
    }
    read_len = fread(buf, 1, buf_len, fp);
    fclose(fp);
    return read_len;
}

#ifdef _WIN32
const char sep = '\\';
#else
const char sep = '/';
#endif
size_t write_to_file(const char *file_path,
                     const void *buf,
                     const size_t buf_len)
{
    size_t write_len = 0;
    char dir_name[SUIT_MAX_NAME_LENGTH];
    char *next_sep;
    next_sep = (char *)file_path - 1;

    while ((next_sep = strchr(next_sep + 1, sep)) != NULL) {
        const int dir_name_len = next_sep - file_path;
        memcpy(dir_name, file_path, dir_name_len);
        dir_name[dir_name_len] = '\0';
        mkdir(dir_name, 0775);
    }

    FILE* fp = fopen(file_path, "wb");
    if (fp == NULL) {
        return 0;
    }
    write_len = fwrite(buf, 1, buf_len, fp);
    fclose(fp);
    return write_len;
}
