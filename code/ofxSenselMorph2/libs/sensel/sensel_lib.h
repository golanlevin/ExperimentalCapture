/******************************************************************************************
* SENSEL CONFIDENTIAL
*
* Copyright 2013-2017 Sensel, Inc
* All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains the property of Sensel, Inc.
* The intellectual and technical concepts contained herein are proprietary to Sensel, Inc.
* and may be covered by U.S. and Foreign Patents, patents in process, and are protected
* by trade secret or copyright law. Dissemination of this information or reproduction of
* this material is strictly forbidden unless prior written permission is obtained from
* Sensel, Inc.
******************************************************************************************/

#ifndef __SENSEL_LIB_H__
#define __SENSEL_LIB_H__

#ifdef _WIN32
#include <windows.h>
#define SENSEL_LIB __declspec(dllexport)
#else
#define SENSEL_LIB
#define WINAPI
#endif

#define SENSEL_LIB_VERSION_MAJOR 0
#define SENSEL_LIB_VERSION_MINOR 5

#define SENSEL_LIB_ERROR_NONE 0
#define SENSEL_LIB_ERROR_DATA_LENGTH 1
#define SENSEL_LIB_ERROR_FORCES 2
#define SENSEL_LIB_ERROR_LABELS 4
#define SENSEL_LIB_ERROR_INIT 8
#define SENSEL_LIB_ERROR_MALLOC 16

#ifdef __cplusplus
extern "C" {
#endif

	SENSEL_LIB int WINAPI senselDecompressInit(unsigned char* metadata, int metadata_size);

	SENSEL_LIB int WINAPI senselDecompressGetCols();

	SENSEL_LIB int WINAPI senselDecompressGetRows();

	SENSEL_LIB int WINAPI senselDecompressFrame(unsigned char* frame_data, int data_size, float* force_array, unsigned char* label_array);

#ifdef __cplusplus
}
#endif

#endif // __SENSEL_LIB_H__
